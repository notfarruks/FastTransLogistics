# Fast & Smart Logistics — website

Trilingual (AZ / RU / EN) marketing site for **Fast & Smart Logistics**, an
international road-freight company based in Baku, Azerbaijan.

Built with **Flask + Jinja2 + vanilla CSS** — no build step, no Node. Designed
to deploy to **Railway** with zero config.

## Stack
- Flask 3 (Python 3.12), server-side rendered Jinja2 templates
- Vanilla CSS with design tokens (dark "tech-logistics" theme)
- gunicorn in production
- Railway hosting (Nixpacks auto-detect)

## Structure
```
FastTransLogistics/
├── app.py            # Flask routes + language handling
├── content.py        # All copy in AZ / RU / EN + company facts
├── requirements.txt
├── Procfile          # gunicorn start command
├── runtime.txt       # Python version pin
├── templates/        # base.html + 5 pages + _logo/_cta partials
└── static/
    ├── css/styles.css
    ├── js/main.js    # mobile nav toggle
    └── img/favicon.svg
```

## Run locally
```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py                       # http://localhost:8080
```

## Deploy to Railway
1. Push this folder to GitHub (files must be at the repo root).
2. railway.app → New Project → Deploy from GitHub repo → select the repo.
3. Railway installs deps and runs `gunicorn app:app` from the `Procfile`.
4. Settings → Networking → Generate Domain to get a public URL.

## Languages
Switch with the AZ/RU/EN pill in the nav. The choice is read from `?lang=xx`
and remembered in a cookie for a year. Default is Azerbaijani. All text lives in
`content.py` — edit there to change copy.

## Contact form
The `/contact` form is **log-only** for now: submissions print to the server
log (visible in Railway logs). To send real email, add a provider (Resend /
SendGrid / Postmark) inside the `contact()` POST branch in `app.py`.

## Editing the design
Colors, fonts, radius and spacing are CSS variables at the top of
`static/css/styles.css`. Change them once and the whole site re-skins.

## Partner logos
Partners are currently styled text tiles. Drop real logo PNG/SVGs into
`static/img/` and swap the `.partner-tile` text for `<img>` tags in
`templates/partners.html` and `templates/home.html`.
