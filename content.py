# -*- coding: utf-8 -*-
"""
All site content lives here so app.py stays small and the copy is easy to edit.
Three languages: Azerbaijani (az), Russian (ru), English (en).
"""

LANGUAGES = {
    "az": "AZ",
    "ru": "RU",
    "en": "EN",
}

# --- Company facts (mostly language-independent) ---
COMPANY = {
    "name": "Fast & Smart Logistics",
    "phone": "+994 50 227 55 15",
    "phone_href": "+99450227551",
    "email": "seo@fast-smart.az",
    "cert_series": "BDV № 11004",
    "tin": "1806550591",
    "valid_from": "04.03.2024",
    "valid_until": "04.03.2031",
}

# Partner / client list — shown as tiles. Swap to <img> once real logos exist.
PARTNERS = [
    "Azertexnolayn",
    "Sirab",
    "Prime Cotton",
    "Kazbegi",
    "Sumqayıt Technologies Park",
    "Azəralüminium",
    "Azersun",
    "Zəyəm Technologies Park",
    "mr.fix",
    "Aral Group",
    "Ganja Sharab",
    "Gilan Seramik",
    "Agrarco",
    "Monopak",
]

# Countries served, per language (flag emoji + localized name).
COUNTRIES = {
    "az": [
        {"flag": "🇦🇿", "name": "Azərbaycan"},
        {"flag": "🇬🇪", "name": "Gürcüstan"},
        {"flag": "🇷🇺", "name": "Rusiya"},
        {"flag": "🇹🇷", "name": "Türkiyə"},
        {"flag": "🇧🇾", "name": "Belarus"},
        {"flag": "🇪🇺", "name": "Avropa"},
        {"flag": "🇷🇸", "name": "Balkan ölkələri"},
        {"flag": "🇨🇳", "name": "Çin"},
    ],
    "ru": [
        {"flag": "🇦🇿", "name": "Азербайджан"},
        {"flag": "🇬🇪", "name": "Грузия"},
        {"flag": "🇷🇺", "name": "Россия"},
        {"flag": "🇹🇷", "name": "Турция"},
        {"flag": "🇧🇾", "name": "Беларусь"},
        {"flag": "🇪🇺", "name": "Европа"},
        {"flag": "🇷🇸", "name": "Балканские страны"},
        {"flag": "🇨🇳", "name": "Китай"},
    ],
    "en": [
        {"flag": "🇦🇿", "name": "Azerbaijan"},
        {"flag": "🇬🇪", "name": "Georgia"},
        {"flag": "🇷🇺", "name": "Russia"},
        {"flag": "🇹🇷", "name": "Turkey"},
        {"flag": "🇧🇾", "name": "Belarus"},
        {"flag": "🇪🇺", "name": "Europe"},
        {"flag": "🇷🇸", "name": "Balkan countries"},
        {"flag": "🇨🇳", "name": "China"},
    ],
}

# Services, per language.
SERVICES = {
    "az": [
        {
            "icon": "📦",
            "title": "Standart yüklərin daşınması",
            "desc": "Quru yolu ilə standart yüklərin təhlükəsiz və vaxtında çatdırılması — birbaşa istənilən nöqtəyə.",
        },
        {
            "icon": "❄️",
            "title": "Temperatura nəzarət edilən daşımalar",
            "desc": "Soyuducu nəqliyyat ilə temperatura həssas yüklərin nəzarət altında daşınması.",
        },
        {
            "icon": "🌍",
            "title": "Beynəlxalq logistika",
            "desc": "Azərbaycan, Gürcüstan, Rusiya, Avropa, Türkiyə və digər ölkələr arasında tam logistika həlləri.",
        },
        {
            "icon": "🛡️",
            "title": "Beynəlxalq tələblərə uyğunluq",
            "desc": "Bütün beynəlxalq daşıma tələblərinə və sənədləşməyə tam uyğunluq.",
        },
    ],
    "ru": [
        {
            "icon": "📦",
            "title": "Перевозка стандартных грузов",
            "desc": "Безопасная и своевременная доставка стандартных грузов автомобильным транспортом — напрямую в любую точку.",
        },
        {
            "icon": "❄️",
            "title": "Температурный режим",
            "desc": "Перевозка температурно-чувствительных грузов в рефрижераторах под полным контролем.",
        },
        {
            "icon": "🌍",
            "title": "Международная логистика",
            "desc": "Полные логистические решения между Азербайджаном, Грузией, Россией, Европой, Турцией и другими странами.",
        },
        {
            "icon": "🛡️",
            "title": "Соответствие требованиям",
            "desc": "Полное соответствие всем международным требованиям к перевозкам и документации.",
        },
    ],
    "en": [
        {
            "icon": "📦",
            "title": "Standard cargo transport",
            "desc": "Safe, on-time delivery of standard freight by road — straight to any destination you need.",
        },
        {
            "icon": "❄️",
            "title": "Temperature-controlled transport",
            "desc": "Refrigerated transport for temperature-sensitive cargo, kept under full control end to end.",
        },
        {
            "icon": "🌍",
            "title": "International logistics",
            "desc": "Complete logistics solutions across Azerbaijan, Georgia, Russia, Europe, Turkey and beyond.",
        },
        {
            "icon": "🛡️",
            "title": "Full compliance",
            "desc": "Full compliance with all international transport requirements and documentation.",
        },
    ],
}

# --- UI strings, per language ---
TRANSLATIONS = {
    # ============================ AZERBAIJANI ============================
    "az": {
        "meta_desc": "Fast & Smart Logistics — Azərbaycan, Gürcüstan, Rusiya, Avropa, Türkiyə və digər ölkələrə beynəlxalq quru yük daşımaları.",
        "nav_home": "Ana səhifə",
        "nav_services": "Xidmətlər",
        "nav_coverage": "Əhatə dairəsi",
        "nav_partners": "Tərəfdaşlar",
        "nav_contact": "Əlaqə",
        "cta_nav": "Təklif al",

        "hero_title": "Yükləriniz üçün sürətli və ağıllı logistika",
        "hero_subtitle": "Məhsullarınızı istənilən vaxtda birbaşa istənilən nöqtəyə quru yolu ilə təhlükəsiz daşıyırıq. Azərbaycan, Gürcüstan, Rusiya, Avropa, Türkiyə və daha çox.",
        "hero_cta_primary": "Təklif al",
        "hero_cta_secondary": "Xidmətlərə bax",
        "hero_badge": "Lisenziyalı daşıyıcı",
        "hero_cert": "Buraxılış vəsiqəsi · Seriya {series}",

        "stats_staff": "mütəxəssis işçi",
        "stats_trucks": "yükdaşıyıcı avtomobil",
        "stats_garage": "qaraj sahəsi",
        "stats_offices": "ofis (AZ + GE)",

        "about_title": "Biz kimik",
        "about_text": "Fast & Smart Logistics — beynəlxalq nəqliyyat və logistika şirkətidir. Azərbaycan, Gürcüstan, Rusiya, Avropa, Balkan ölkələri, Belarus, Çin və Türkiyə kimi ölkələrə yüklərin daşınması ilə məşğuluq. Şirkətimiz dünya bazarında fəaliyyətini davamlı olaraq genişləndirir.",

        "why_title": "Niyə biz",
        "why_items": [
            {"icon": "⚡", "title": "Sürətli çatdırılma", "text": "Yüklərin müntəzəm və vaxtında daşınması."},
            {"icon": "✅", "title": "Beynəlxalq tələblərə uyğunluq", "text": "Bütün beynəlxalq standartlara tam riayət."},
            {"icon": "🤝", "title": "Əməkdaşlıq üçün əla şərait", "text": "Hər iki istiqamətdə əlverişli şərtlər."},
            {"icon": "🔁", "title": "Müntəzəm daşımalar", "text": "Malların daimi və etibarlı daşınması."},
        ],

        "services_title": "Xidmətlərimiz",
        "services_intro": "Standart və temperatura nəzarət edilən yüklər üçün tam logistika həlləri.",

        "coverage_title": "Əhatə dairəmiz",
        "coverage_intro": "Şirkətimiz dünya bazarında fəaliyyətini genişləndirir — hər iki istiqamətdə daşımalar.",
        "coverage_directions": "Hər iki istiqamət",

        "partners_title": "Müştərilərimiz və tərəfdaşlarımız",
        "partners_intro": "Aparıcı Azərbaycan brendləri bizə etibar edir.",

        "cta_title": "Səmərəli əməkdaşlıq üçün hazırıq",
        "cta_text": "Biz həmişə yeni imkanlar axtarırıq. Yükünüz üçün təklif alın.",
        "cta_button": "Bizimlə əlaqə saxlayın",

        "contact_title": "Əlaqə",
        "contact_intro": "Yükünüzün təfərrüatlarını göndərin — sizə qısa zamanda təklif verəcəyik.",
        "form_name": "Adınız",
        "form_email": "E-poçt",
        "form_origin": "Haradan",
        "form_destination": "Haraya",
        "form_message": "Yük haqqında məlumat",
        "form_submit": "Göndər",
        "form_success": "Təşəkkür edirik! Müraciətiniz qəbul olundu, tezliklə sizinlə əlaqə saxlayacağıq.",
        "contact_phone_label": "Telefon",
        "contact_email_label": "E-poçt",
        "contact_address_label": "Ünvan",
        "contact_address": "Qafqaz Business Center, Bakı, Azərbaycan",

        "footer_about": "Beynəlxalq quru yük daşımaları üzrə logistika şirkəti.",
        "footer_links": "Keçidlər",
        "footer_contact": "Əlaqə",
        "footer_rights": "Bütün hüquqlar qorunur.",
        "footer_cert": "VÖEN {tin} · Buraxılış vəsiqəsi {series} (etibarlıdır {until} tarixinədək)",
    },

    # ============================== RUSSIAN ==============================
    "ru": {
        "meta_desc": "Fast & Smart Logistics — международные автомобильные грузоперевозки в Азербайджан, Грузию, Россию, Европу, Турцию и другие страны.",
        "nav_home": "Главная",
        "nav_services": "Услуги",
        "nav_coverage": "География",
        "nav_partners": "Партнёры",
        "nav_contact": "Контакты",
        "cta_nav": "Получить расчёт",

        "hero_title": "Быстрая и умная логистика для ваших грузов",
        "hero_subtitle": "Безопасно доставляем ваши товары автомобильным транспортом напрямую в любую точку и в любое время. Азербайджан, Грузия, Россия, Европа, Турция и не только.",
        "hero_cta_primary": "Получить расчёт",
        "hero_cta_secondary": "Наши услуги",
        "hero_badge": "Лицензированный перевозчик",
        "hero_cert": "Разрешение · Серия {series}",

        "stats_staff": "специалистов",
        "stats_trucks": "грузовых автомобилей",
        "stats_garage": "гаражная площадь",
        "stats_offices": "офиса (AZ + GE)",

        "about_title": "О компании",
        "about_text": "Fast & Smart Logistics — международная транспортно-логистическая компания. Мы осуществляем перевозку грузов в Азербайджан, Грузию, Россию, страны Европы и Балкан, Беларусь, Китай и Турцию. Компания постоянно расширяет своё присутствие на мировом рынке.",

        "why_title": "Почему мы",
        "why_items": [
            {"icon": "⚡", "title": "Быстрая доставка", "text": "Регулярная и своевременная перевозка грузов."},
            {"icon": "✅", "title": "Соответствие требованиям", "text": "Полное соблюдение всех международных стандартов."},
            {"icon": "🤝", "title": "Отличные условия", "text": "Выгодные условия в обоих направлениях."},
            {"icon": "🔁", "title": "Регулярные рейсы", "text": "Постоянная и надёжная перевозка товаров."},
        ],

        "services_title": "Наши услуги",
        "services_intro": "Полные логистические решения для стандартных и температурных грузов.",

        "coverage_title": "География перевозок",
        "coverage_intro": "Компания расширяет деятельность на мировом рынке — перевозки в обоих направлениях.",
        "coverage_directions": "Оба направления",

        "partners_title": "Наши клиенты и партнёры",
        "partners_intro": "Нам доверяют ведущие азербайджанские бренды.",

        "cta_title": "Готовы к эффективному сотрудничеству",
        "cta_text": "Мы всегда ищем новые возможности. Получите расчёт для вашего груза.",
        "cta_button": "Связаться с нами",

        "contact_title": "Контакты",
        "contact_intro": "Отправьте детали груза — мы быстро подготовим для вас расчёт.",
        "form_name": "Ваше имя",
        "form_email": "Эл. почта",
        "form_origin": "Откуда",
        "form_destination": "Куда",
        "form_message": "Информация о грузе",
        "form_submit": "Отправить",
        "form_success": "Спасибо! Ваша заявка принята, мы скоро свяжемся с вами.",
        "contact_phone_label": "Телефон",
        "contact_email_label": "Эл. почта",
        "contact_address_label": "Адрес",
        "contact_address": "Qafqaz Business Center, Баку, Азербайджан",

        "footer_about": "Логистическая компания международных автомобильных грузоперевозок.",
        "footer_links": "Ссылки",
        "footer_contact": "Контакты",
        "footer_rights": "Все права защищены.",
        "footer_cert": "ИНН {tin} · Разрешение {series} (действует до {until})",
    },

    # ============================== ENGLISH ==============================
    "en": {
        "meta_desc": "Fast & Smart Logistics — international road freight to Azerbaijan, Georgia, Russia, Europe, Turkey and more.",
        "nav_home": "Home",
        "nav_services": "Services",
        "nav_coverage": "Coverage",
        "nav_partners": "Partners",
        "nav_contact": "Contact",
        "cta_nav": "Get a quote",

        "hero_title": "Fast & smart logistics for your cargo",
        "hero_subtitle": "We move your goods safely by road, straight to any destination, any time. Azerbaijan, Georgia, Russia, Europe, Turkey and beyond.",
        "hero_cta_primary": "Get a quote",
        "hero_cta_secondary": "See services",
        "hero_badge": "Licensed carrier",
        "hero_cert": "Access certificate · Series {series}",

        "stats_staff": "specialists",
        "stats_trucks": "freight vehicles",
        "stats_garage": "garage space",
        "stats_offices": "offices (AZ + GE)",

        "about_title": "Who we are",
        "about_text": "Fast & Smart Logistics is an international transport and logistics company. We carry freight to Azerbaijan, Georgia, Russia, Europe, the Balkans, Belarus, China and Turkey. The company is continuously expanding its presence in the global market.",

        "why_title": "Why us",
        "why_items": [
            {"icon": "⚡", "title": "Fast delivery", "text": "Regular, on-time movement of your cargo."},
            {"icon": "✅", "title": "International compliance", "text": "Full adherence to all international standards."},
            {"icon": "🤝", "title": "Great terms", "text": "Favorable conditions in both directions."},
            {"icon": "🔁", "title": "Regular routes", "text": "Consistent and reliable transport of goods."},
        ],

        "services_title": "Our services",
        "services_intro": "Complete logistics solutions for standard and temperature-controlled cargo.",

        "coverage_title": "Where we operate",
        "coverage_intro": "We're expanding across the global market — freight in both directions.",
        "coverage_directions": "Both directions",

        "partners_title": "Our clients & partners",
        "partners_intro": "Trusted by leading Azerbaijani brands.",

        "cta_title": "Ready for effective cooperation",
        "cta_text": "We're always looking for new opportunities. Get a quote for your cargo.",
        "cta_button": "Get in touch",

        "contact_title": "Contact us",
        "contact_intro": "Send your cargo details and we'll get a quote back to you quickly.",
        "form_name": "Your name",
        "form_email": "Email",
        "form_origin": "From",
        "form_destination": "To",
        "form_message": "Cargo details",
        "form_submit": "Send",
        "form_success": "Thank you! Your inquiry has been received — we'll be in touch shortly.",
        "contact_phone_label": "Phone",
        "contact_email_label": "Email",
        "contact_address_label": "Address",
        "contact_address": "Qafqaz Business Center, Baku, Azerbaijan",

        "footer_about": "International road freight logistics company.",
        "footer_links": "Links",
        "footer_contact": "Contact",
        "footer_rights": "All rights reserved.",
        "footer_cert": "TIN {tin} · Access certificate {series} (valid until {until})",
    },
}
