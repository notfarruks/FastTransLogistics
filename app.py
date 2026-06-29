"""
Fast & Smart Logistics — Flask marketing site.

Trilingual (AZ / RU / EN), server-side rendered with Jinja2, plain CSS.
Language is chosen via ?lang=xx and persisted in a cookie.
Ready to deploy to Railway (see Procfile).
"""
import os

from flask import (
    Flask,
    Response,
    g,
    make_response,
    redirect,
    render_template,
    request,
    url_for,
)

from content import (
    LANGUAGES,
    TRANSLATIONS,
    PARTNERS,
    COUNTRIES,
    SERVICES,
    COMPANY,
    TESTIMONIALS,
    FAQ,
)

app = Flask(__name__)

DEFAULT_LANG = "az"


def current_lang():
    """Resolve active language: query param > cookie > default."""
    lang = request.args.get("lang")
    if lang in LANGUAGES:
        return lang
    cookie_lang = request.cookies.get("lang")
    if cookie_lang in LANGUAGES:
        return cookie_lang
    return DEFAULT_LANG


@app.before_request
def set_language():
    g.lang = current_lang()


@app.after_request
def persist_language(response):
    """If the user explicitly switched language, remember it."""
    chosen = request.args.get("lang")
    if chosen in LANGUAGES:
        response.set_cookie("lang", chosen, max_age=60 * 60 * 24 * 365)
    return response


@app.context_processor
def inject_globals():
    """Make translation helpers available in every template."""
    t = TRANSLATIONS[g.lang]
    return {
        "lang": g.lang,
        "languages": LANGUAGES,
        "t": t,
        "company": COMPANY,
        "seo_countries": [c["name"] for c in COUNTRIES[g.lang]],
        # convenience for the language switcher: keep current page, swap lang
        "switch_lang_url": lambda code: url_for(request.endpoint, lang=code)
        if request.endpoint
        else "/?lang=" + code,
    }


@app.route("/")
def home():
    return render_template(
        "home.html",
        page="home",
        services=SERVICES[g.lang],
        countries=COUNTRIES[g.lang],
        partners=PARTNERS,
        testimonials=TESTIMONIALS[g.lang],
        faq=FAQ[g.lang],
    )


@app.route("/services")
def services():
    return render_template(
        "services.html",
        page="services",
        services=SERVICES[g.lang],
    )


@app.route("/coverage")
def coverage():
    return render_template(
        "coverage.html",
        page="coverage",
        countries=COUNTRIES[g.lang],
        faq=FAQ[g.lang],
    )


@app.route("/partners")
def partners():
    return render_template(
        "partners.html",
        page="partners",
        partners=PARTNERS,
    )


@app.route("/contact", methods=["GET", "POST"])
def contact():
    sent = False
    if request.method == "POST":
        data = {
            "name": request.form.get("name", "").strip(),
            "email": request.form.get("email", "").strip(),
            "origin": request.form.get("origin", "").strip(),
            "destination": request.form.get("destination", "").strip(),
            "message": request.form.get("message", "").strip(),
        }
        # Log-only for now. Visible in Railway logs.
        # To send real email, add a provider (Resend/SendGrid) here.
        app.logger.info("New contact inquiry: %s", data)
        print("New contact inquiry:", data, flush=True)
        sent = True

    return render_template("contact.html", page="contact", sent=sent)


@app.route("/robots.txt")
def robots():
    body = "\n".join(
        [
            "User-agent: *",
            "Allow: /",
            f"Sitemap: {request.url_root}sitemap.xml",
            "",
        ]
    )
    return Response(body, mimetype="text/plain")


@app.route("/sitemap.xml")
def sitemap():
    base = request.url_root.rstrip("/")
    pages = ["home", "services", "coverage", "partners", "contact"]
    xmlns = (
        'xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
        'xmlns:xhtml="http://www.w3.org/1999/xhtml"'
    )
    rows = [f'<?xml version="1.0" encoding="UTF-8"?>', f"<urlset {xmlns}>"]
    for ep in pages:
        path = url_for(ep)
        for code in LANGUAGES:
            loc = f"{base}{path}?lang={code}"
            rows.append("  <url>")
            rows.append(f"    <loc>{loc}</loc>")
            for alt in LANGUAGES:
                rows.append(
                    f'    <xhtml:link rel="alternate" hreflang="{alt}" '
                    f'href="{base}{path}?lang={alt}"/>'
                )
            rows.append(
                f'    <xhtml:link rel="alternate" hreflang="x-default" '
                f'href="{base}{path}"/>'
            )
            rows.append("  </url>")
    rows.append("</urlset>")
    return Response("\n".join(rows), mimetype="application/xml")


@app.route("/healthz")
def healthz():
    return {"status": "ok"}, 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=True)
