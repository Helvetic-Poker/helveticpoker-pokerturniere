import html, json, re
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse
from zoneinfo import ZoneInfo

BASE_URL = 'https://pokerturniere.helveticpoker.ch'
ROOT = Path('.')
DATA_DIR = ROOT / 'data'

CANTON_NAMES = {
    'AG': 'Aargau', 'AR': 'Appenzell Ausserrhoden', 'AI': 'Appenzell Innerrhoden',
    'BL': 'Basel-Landschaft', 'BS': 'Basel-Stadt', 'BE': 'Bern', 'FR': 'Freiburg',
    'GE': 'Genf', 'GL': 'Glarus', 'GR': 'Graubünden', 'JU': 'Jura', 'LU': 'Luzern',
    'NE': 'Neuenburg', 'NW': 'Nidwalden', 'OW': 'Obwalden', 'SG': 'St. Gallen',
    'SH': 'Schaffhausen', 'SZ': 'Schwyz', 'SO': 'Solothurn', 'TG': 'Thurgau',
    'TI': 'Tessin', 'UR': 'Uri', 'VD': 'Waadt', 'VS': 'Wallis', 'ZG': 'Zug',
    'ZH': 'Zürich'
}

def esc(value):
    return html.escape(str(value or ''), quote=True)

def slugify(value):
    value = str(value or '').strip().lower()
    value = value.replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue').replace('ß', 'ss')
    value = re.sub(r'[^a-z0-9]+', '-', value)
    return value.strip('-')

def event_slug(event):
    return event.get('slug') or slugify('-'.join(str(x) for x in [event.get('title'), event.get('city'), event.get('date_start'), event.get('id')] if x))

events = []
for path in sorted(DATA_DIR.glob('*.json')):
    try:
        data = json.loads(path.read_text(encoding='utf-8'))
    except Exception:
        continue
    if isinstance(data, list):
        events.extend(data)
    elif isinstance(data, dict):
        events.extend(data.get('events', [data]) if isinstance(data.get('events', [data]), list) else [data])

today = datetime.now(ZoneInfo('Europe/Zurich')).strftime('%Y-%m-%d')

def upcoming_count_by(field):
    counts = {}
    for event in events:
        if (event.get('date_start') or '') < today:
            continue
        value = str(event.get(field) or '').strip()
        if value:
            counts[value] = counts.get(value, 0) + 1
    return counts

landing_city_counts = upcoming_count_by('city')
landing_organizer_counts = upcoming_count_by('organizer')
landing_cities = {name for name, count in landing_city_counts.items() if count >= 2}
landing_organizers = {name for name, count in landing_organizer_counts.items() if count >= 2}

def sort_event(e):
    return (e.get('date_start') or '9999-99-99', e.get('time') or '99:99', e.get('title') or '')

def format_date(e):
    start = e.get('date_start') or ''
    end = e.get('date_end') or ''
    try:
        y, m, day = start.split('-')
        start_fmt = f'{day}.{m}.{y}'
        if end and end != start:
            y2, m2, day2 = end.split('-')
            end_fmt = f'{day2}.{m2}.{y2}'
            return f'{start_fmt}–{end_fmt}'
        return start_fmt
    except Exception:
        return start

def format_date_parts(e):
    d = e.get('date_start') or ''
    try:
        y, m, day = d.split('-')
        months = ['', 'JAN', 'FEB', 'MÄR', 'APR', 'MAI', 'JUN', 'JUL', 'AUG', 'SEP', 'OKT', 'NOV', 'DEZ']
        weekdays = ['Mo', 'Di', 'Mi', 'Do', 'Fr', 'Sa', 'So']
        dt = datetime(int(y), int(m), int(day))
        return months[int(m)], day, weekdays[dt.weekday()]
    except Exception:
        return '', '', ''

def format_buy_in(e):
    label = str(e.get('buy_in_label') or '').strip()
    value = e.get('buy_in')
    if isinstance(value, (int, float)) and value > 0:
        if label and 'CHF' in label:
            return label.replace('Buy-in ', '', 1).strip()
        return f'CHF {value:,.0f}'.replace(',', "'")
    if label and label.lower() not in {'buy-in siehe veranstalter', 'siehe veranstalter'}:
        return label.replace('Buy-in ', '', 1).strip()
    return 'Noch offen'

def row(e):
    month, day, weekday = format_date_parts(e)
    variant = e.get('variant') or ''
    event_type = e.get('event_type') or ''
    tags = ''.join(
        f'<span class="tag">{esc(x)}</span>'
        for x in [variant, event_type if event_type not in {'Regular', ''} else '']
        if x
    )
    title = esc(e.get('title') or 'Pokerturnier')
    time = esc(e.get('time') or '—')
    city = esc(e.get('city') or '—')
    venue = esc(e.get('venue') or '')
    buy_in = esc(format_buy_in(e))
    date_full = esc(format_date(e))
    return f'''<li class="event-card">
<a href="/turniere/{esc(event_slug(e))}/">
<div class="date-box"><span>{esc(month)}</span><strong>{esc(day)}</strong><small>{esc(weekday)}</small></div>
<div class="event-main">
<strong class="event-title">{title}</strong>
<div class="tags">{tags}</div>
</div>
<div class="event-info time-info"><span class="icon">◷</span><div><strong>{time}</strong><small>Startzeit</small></div></div>
<div class="event-info location-info"><span class="icon">⌖</span><div><strong>{city}</strong><small>{venue or date_full}</small></div></div>
<div class="event-info buy-info"><span class="icon">◉</span><div><strong>{buy_in}</strong><small>Buy-in</small></div></div>
<span class="details">Details <span>→</span></span>
</a>
</li>'''

groups = {'stadt': {}, 'kanton': {}, 'veranstalter': {}}
for e in events:
    city = (e.get('city') or '').strip()
    organizer = (e.get('organizer') or '').strip()
    canton_code = (e.get('canton') or '').strip().upper()
    canton_name = CANTON_NAMES.get(canton_code) or (e.get('region') or '').strip()

    if city:
        groups['stadt'].setdefault(city, []).append(e)
    if canton_name:
        groups['kanton'].setdefault(canton_name, []).append(e)
    if organizer:
        groups['veranstalter'].setdefault(organizer, []).append(e)

def write_index_page(kind, values):
    labels = {'stadt': 'Städte', 'kanton': 'Kantone', 'veranstalter': 'Veranstalter'}
    singular = {'stadt': 'Stadt', 'kanton': 'Kanton', 'veranstalter': 'Veranstalter'}
    parent = labels[kind]
    entries = []
    for name, items in sorted(values.items()):
        upcoming = sorted([e for e in items if (e.get('date_start') or '') >= today], key=sort_event)
        if len(upcoming) < 2:
            continue
        entries.append((name, upcoming))

    url = f'{BASE_URL}/{kind}/'
    title = f'Pokerturniere Schweiz nach {singular[kind].lower()}'
    desc = f'Kommende Pokerturniere in der Schweiz nach {singular[kind].lower()}: aktuelle Termine, Orte und Veranstalter.'
    cards = ''.join(
        f'<a class="index-card" href="/{kind}/{esc(slugify(name))}/">'
        f'<strong>{esc(name)}</strong><span>{len(upcoming)} kommende Turniere</span><b>→</b></a>'
        for name, upcoming in entries
    )

    page = f'''<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)} | Helvetic Poker</title>
<meta name="description" content="{esc(desc)}">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
<link rel="canonical" href="{esc(url)}">
<meta property="og:type" content="website">
<meta property="og:title" content="{esc(title)} | Helvetic Poker">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{esc(url)}">
<meta property="og:site_name" content="Helvetic Poker">
<script type="application/ld+json">{json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Pokerturniere Schweiz","item":f"{BASE_URL}/"},{"@type":"ListItem","position":2,"name":title,"item":url}]}, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps({"@context":"https://schema.org","@type":"ItemList","name":title,"itemListElement":[{"@type":"ListItem","position":i+1,"name":name,"url":f"{BASE_URL}/{kind}/{slugify(name)}/"} for i,(name,_) in enumerate(entries)]}, ensure_ascii=False)}</script>
<style>
*{{box-sizing:border-box}}body{{margin:0;font-family:Arial,sans-serif;color:#151515;background:#f5f5f5}}a{{color:inherit}}
header{{background:#fff;border-bottom:1px solid #e1e1e1}}.head{{max-width:1180px;margin:auto;padding:14px 24px;display:flex;align-items:center;justify-content:space-between;gap:24px}}
.logo{{display:block;width:310px;max-height:88px;object-fit:contain;object-position:left center}}.nav{{display:flex;align-items:center;gap:28px;font-size:15px;font-weight:700}}.nav a{{text-decoration:none}}.all-btn{{background:#c8102e;color:#fff!important;padding:11px 18px;border-radius:9px}}
main{{max-width:1180px;margin:auto;padding:34px 24px 60px}}.breadcrumb{{font-size:14px;color:#666;margin-bottom:28px}}.card{{background:#fff;border:1px solid #dedede;border-radius:20px;overflow:hidden;box-shadow:0 12px 35px #0000000b}}
.top{{height:5px;background:linear-gradient(90deg,#c8102e 0%,#c8102e 68%,#c9a227 100%)}}.intro{{padding:38px 42px 28px}}h1{{margin:0;font-size:clamp(36px,5vw,58px);line-height:1.03;letter-spacing:-1.5px}}.intro p{{color:#626262;font-size:18px;max-width:820px;margin:18px 0 0}}.data-note{{font-size:12px!important;color:#8a8a8a!important;margin-top:10px!important}}
.grid{{padding:0 28px 38px;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}}.index-card{{display:grid;grid-template-columns:1fr auto;gap:6px 14px;padding:20px;border:1px solid #dedede;border-radius:15px;text-decoration:none;background:#fff}}.index-card:hover{{box-shadow:0 8px 24px #00000012;transform:translateY(-1px)}}.index-card strong{{font-size:18px}}.index-card span{{color:#777;font-size:13px}}.index-card b{{grid-column:2;grid-row:1 / span 2;align-self:center;color:#c8102e;font-size:22px}}
@media(max-width:760px){{.head{{padding:12px 15px}}.logo{{width:245px;max-height:72px}}.nav a{{display:none}}.all-btn{{display:block!important}}main{{padding:22px 12px 40px}}.intro{{padding:28px 22px 22px}}.grid{{grid-template-columns:1fr;padding:0 12px 25px}}}}
</style>
</head>
<body>
<header><div class="head"><a href="/" aria-label="Helvetic Poker – Pokerturniere Schweiz"><img class="logo" src="/assets/helvetic-poker-logo.png" alt="Helvetic Poker"></a>
<nav class="nav" aria-label="Hauptnavigation"><a href="/">Turniere</a><a href="/stadt/">Städte</a><a href="/kanton/">Kantone</a><a href="/veranstalter/">Veranstalter</a><a href="/">Kalender</a><a class="all-btn" href="/">Alle Turniere</a></nav></div></header>
<main><div class="breadcrumb"><a href="/">⌂</a> &nbsp;›&nbsp; {esc(parent)}</div>
<article class="card"><div class="top"></div><section class="intro"><h1>{esc(title)}</h1><p>{esc(desc)}</p><p class="data-note">Aktualisierte Übersicht · {esc(today)}</p></section><section class="grid">{cards}</section></article></main>
</body></html>'''
    out = ROOT / kind
    out.mkdir(parents=True, exist_ok=True)
    (out / 'index.html').write_text(page, encoding='utf-8')
    return url

provider_logos = {
    "24Poker": "https://zejcddvqhcbbmrufqsli.supabase.co/storage/v1/object/public/club-logos/6b50286d-2f09-47d4-a018-8c326b0ecef7/1774464947679-24poker.png",
    "AZ Poker Club Bern": "https://zejcddvqhcbbmrufqsli.supabase.co/storage/v1/object/public/club-logos/1170cdc9-4cb0-4ac0-902f-19c369fa99b4/1774464942453-azpokerclub.jpg",
    "Airfield Pokerclub Interlaken": "https://zejcddvqhcbbmrufqsli.supabase.co/storage/v1/object/public/club-logos/3a6035b2-ab43-4807-b3a5-28185be8f40b/1774465014142-pokerhelden.jpg",
    "Pokerhelden / Airfield Poker Club": "https://zejcddvqhcbbmrufqsli.supabase.co/storage/v1/object/public/club-logos/3a6035b2-ab43-4807-b3a5-28185be8f40b/1774465014142-pokerhelden.jpg",
    "Another Poker Basel": "https://zejcddvqhcbbmrufqsli.supabase.co/storage/v1/object/public/club-logos/c04768c0-8968-455e-acb3-38a42b79c3ee/1774464902622-anotherpoker.png",
    "Capital Poker Club Bern": "https://zejcddvqhcbbmrufqsli.supabase.co/storage/v1/object/public/club-logos/415712c9-af88-4b1e-a4a0-5ebc87de4470/1774464996304-capitalpokerclub.png",
    "FOIF DRÜ EFFRETIKON": "https://zejcddvqhcbbmrufqsli.supabase.co/storage/v1/object/public/club-logos/d5555268-b285-4c9f-8c62-8a53811cc8da/1774464838755-foifdrue.png",
    "FullEdge Pokerclub Pratteln BL": "https://zejcddvqhcbbmrufqsli.supabase.co/storage/v1/object/public/club-logos/e1315bad-abde-460a-9ee0-6a2bda3e13fb/1774464850053-fulledge.jpg",
    "House of Cards Luzern": "https://zejcddvqhcbbmrufqsli.supabase.co/storage/v1/object/public/club-logos/e20c02d3-49e6-4dfb-b2c2-4b20f29eadad/1774464785696-houseofcards.jpg",
    "HSOP Helvetic Series of Poker": "https://zejcddvqhcbbmrufqsli.supabase.co/storage/v1/object/public/club-logos/711a2b69-fae1-4b0b-afca-e83c36e2d9c1/1774464992979-hsop.jpg",
    "Munot Poker Schaffhausen": "https://zejcddvqhcbbmrufqsli.supabase.co/storage/v1/object/public/club-logos/6ce78667-c164-4a86-8874-e95496cb0bf5/1774464745546-munotpoker.png",
    "Prestige Poker Dietlikon": "https://zejcddvqhcbbmrufqsli.supabase.co/storage/v1/object/public/club-logos/6870a596-1d3e-466f-af92-5dc034a1d727/1774464799361-prestigepoker.jpg",
    "STATION Poker Club": "https://zejcddvqhcbbmrufqsli.supabase.co/storage/v1/object/public/club-logos/7a6418b7-dfb0-4519-aab5-e857f421a6d7/1774464732962-stationpokerclub.jpg",
    "Poker Club St. Gallen": "/assets/logos/poker-club-st-gallen.png",
    "Swiss Casino St. Gallen": "https://static.wixstatic.com/media/98a788_df2ae3f8c7e34e1ab9eba87e99a6f506~mv2.png/v1/fill/w_1024%2Ch_768%2Cal_c/Logo_SwissCasino4_3%20%282%29.png",
    "Grand Casino Luzern": "https://luzernerfest.ch/images/sponsoren/casino-luzern.png",
    "sports ZUGERLAND": "https://media.jobs.ch/media/f07dacd6-410e-4b8f-ae42-d713278866bc",
    "Fridli Poker": "/assets/logos/fridli-poker.jpg",
}

def write_page(kind, name, items):
    upcoming = sorted(
        [e for e in items if (e.get('date_start') or '') >= today],
        key=sort_event
    )

    # Avoid thin doorway-style landing pages. Only publish useful collections.
    if len(upcoming) < 2:
        return None

    slug = slugify(name)
    url = f'{BASE_URL}/{kind}/{slug}/'

    # Logos are only appropriate for organizer landing pages.
    # City and canton pages aggregate multiple providers and therefore stay neutral.
    logo_url = ''
    if kind == 'veranstalter':
        logo_url = provider_logos.get(name) or ''
        if not logo_url:
            for event in upcoming:
                provider_logo = str(event.get('provider_logo') or '').strip()
                if provider_logo:
                    logo_url = provider_logo
                    break

    if kind == 'stadt':
        title = f'Pokerturniere in {name}'
        desc = f'Kommende Pokerturniere in {name}: aktuelle Termine, Startzeiten, Buy-ins, Spielarten und Veranstaltungsorte im Schweizer Pokerkalender.'
        parent_name = 'Städte'
    elif kind == 'kanton':
        title = f'Pokerturniere im Kanton {name}'
        desc = f'Kommende Pokerturniere im Kanton {name}: aktuelle Termine, Startzeiten, Buy-ins, Spielarten und Veranstaltungsorte im Schweizer Pokerkalender.'
        parent_name = 'Kantone'
    else:
        title = f'Pokerturniere von {name}'
        desc = f'Kommende Pokerturniere von {name}: aktuelle Termine, Startzeiten, Buy-ins und Spielarten im Schweizer Pokerkalender.'
        parent_name = 'Veranstalter'

    rows = ''.join(row(e) for e in upcoming[:60])

    cities = sorted({str(e.get('city') or '').strip() for e in upcoming if str(e.get('city') or '').strip()})
    organizers = sorted({str(e.get('organizer') or '').strip() for e in upcoming if str(e.get('organizer') or '').strip()})
    variants = sorted({str(e.get('variant') or '').strip() for e in upcoming if str(e.get('variant') or '').strip()})
    venues = sorted({str(e.get('venue') or '').strip() for e in upcoming if str(e.get('venue') or '').strip()})
    dates = sorted({e.get('date_start') for e in upcoming if e.get('date_start')})
    buy_in_values = [e.get('buy_in') for e in upcoming if isinstance(e.get('buy_in'), (int, float)) and e.get('buy_in') > 0]
    top_variants = sorted(((variant, sum(1 for e in upcoming if (e.get('variant') or '').strip() == variant)) for variant in variants), key=lambda x: (-x[1], x[0].lower()))[:4]
    top_cities = sorted(((city, sum(1 for e in upcoming if (e.get('city') or '').strip() == city)) for city in cities), key=lambda x: (-x[1], x[0].lower()))[:4]
    stat_items = [
        ('Turniere', str(len(upcoming))),
        ('Orte', str(len(cities))),
        ('Veranstalter', str(len(organizers))),
        ('Spielarten', str(len(variants))),
    ]
    if kind == 'stadt':
        stat_items = [('Turniere', str(len(upcoming))), ('Veranstalter', str(len(organizers))), ('Spielarten', str(len(variants))), ('Spielorte', str(len(venues)))]
    elif kind == 'kanton':
        stat_items = [('Turniere', str(len(upcoming))), ('Städte', str(len(cities))), ('Veranstalter', str(len(organizers))), ('Spielarten', str(len(variants)))]
    elif kind == 'veranstalter':
        stat_items = [('Turniere', str(len(upcoming))), ('Städte', str(len(cities))), ('Spielarten', str(len(variants))), ('Spielorte', str(len(venues)))]

    stat_html = ''.join(
        f'<div class="stat"><strong>{esc(value)}</strong><span>{esc(label)}</span></div>'
        for label, value in stat_items
    )

    extra_title = {
        'stadt': f'Pokerturniere & Spielorte in {name}',
        'kanton': f'Pokerturniere & Städte im Kanton {name}',
        'veranstalter': f'{name}: Turniere & Spielorte'
    }[kind]
    extra_text = {
        'stadt': f'In {name} sind aktuell {len(upcoming)} kommende Pokerturniere erfasst. Die Termine zeigen dir auf einen Blick Veranstalter, Spielarten und Spielorte.',
        'kanton': f'Im Kanton {name} sind aktuell {len(upcoming)} kommende Pokerturniere erfasst. Die Übersicht verbindet die verfügbaren Termine mit Städten, Veranstaltern und Spielarten.',
        'veranstalter': f'Bei {name} sind aktuell {len(upcoming)} kommende Pokerturniere erfasst. Hier findest du die nächsten Termine sowie die dazugehörigen Städte, Spielarten und Spielorte.'
    }[kind]

    if buy_in_values:
        buy_in_summary = f" Die erfassten Buy-ins reichen von CHF {min(buy_in_values):,.0f} bis CHF {max(buy_in_values):,.0f}.".replace(',', "'")
    else:
        buy_in_summary = ""

    if kind == 'stadt':
        detail_text = f'In {name} findest du aktuell {len(upcoming)} kommende Pokerturniere.'
        if top_variants:
            detail_text += f' Vertreten sind unter anderem {", ".join(v for v, _ in top_variants)}.'
        detail_text += buy_in_summary
    elif kind == 'kanton':
        detail_text = f'Im Kanton {name} sind aktuell {len(upcoming)} kommende Pokerturniere erfasst.'
        if top_cities:
            detail_text += f' Die nächsten Termine verteilen sich unter anderem auf {", ".join(city for city, _ in top_cities)}.'
        detail_text += buy_in_summary
    else:
        detail_text = f'Für {name} sind aktuell {len(upcoming)} kommende Pokerturniere erfasst.'
        if top_cities:
            detail_text += f' Die Termine finden unter anderem in {", ".join(city for city, _ in top_cities)} statt.'
        detail_text += buy_in_summary

    related_html = ''
    if kind in {'kanton', 'veranstalter'}:
        for city, _ in top_cities:
            if city in landing_cities:
                related_html += f'<a class="related-chip" href="/stadt/{slugify(city)}/">Stadt: {esc(city)} →</a>'
    if kind == 'stadt' and canton_name:
        if canton_name in landing_cantons:
            related_html += f'<a class="related-chip" href="/kanton/{slugify(canton_name)}/">Kanton: {esc(canton_name)} →</a>'
    for variant, _ in top_variants:
        variant_key = variant.upper()
        if variant_key == 'NLH':
            related_html += '<a class="related-chip" href="/nlh-pokerturniere/">NLH Pokerturniere →</a>'
        elif variant_key in {'PLO', 'PLO8'}:
            related_html += '<a class="related-chip" href="/plo-pokerturniere/">PLO Pokerturniere →</a>'
    if buy_in_values:
        if min(buy_in_values) <= 50:
            related_html += '<a class="related-chip" href="/pokerturniere-bis-50-chf/">Pokerturniere bis CHF 50 →</a>'
        elif min(buy_in_values) <= 100:
            related_html += '<a class="related-chip" href="/pokerturniere-bis-100-chf/">Pokerturniere bis CHF 100 →</a>'

    collection_json = {
        '@context': 'https://schema.org',
        '@type': 'CollectionPage',
        'name': title,
        'url': url,
        'isPartOf': {
            '@type': 'WebSite',
            'name': 'Helvetic Poker – Pokerturniere Schweiz',
            'url': f'{BASE_URL}/'
        },
        'mainEntity': {
            '@type': 'ItemList',
            'name': title,
            'numberOfItems': len(upcoming),
            'itemListElement': [
                {
                    '@type': 'ListItem',
                    'position': i + 1,
                    'name': e.get('title') or 'Pokerturnier',
                    'url': f'{BASE_URL}/turniere/{event_slug(e)}/'
                }
                for i, e in enumerate(upcoming[:60])
            ]
        }
    }
    if kind == 'veranstalter':
        organizer_source_url = next((str(e.get('organizer_url') or '').strip() for e in upcoming if str(e.get('organizer_url') or '').strip()), '')
        collection_json['mainEntity'] = {
            '@type': 'Organization',
            '@id': url + '#organization',
            'name': name,
            'url': organizer_source_url or url
        }

    breadcrumb_json = {
        '@context': 'https://schema.org',
        '@type': 'BreadcrumbList',
        'itemListElement': [
            {
                '@type': 'ListItem',
                'position': 1,
                'name': 'Pokerturniere Schweiz',
                'item': f'{BASE_URL}/'
            },
            {
                '@type': 'ListItem',
                'position': 2,
                'name': parent_name,
                'item': f'{BASE_URL}/{kind}/'
            },
            {
                '@type': 'ListItem',
                'position': 3,
                'name': title,
                'item': url
            }
        ]
    }

    style = '''*{box-sizing:border-box}
body{margin:0;font-family:Arial,sans-serif;color:#151515;background:#f5f5f5;line-height:1.45}
a{color:inherit}
header{background:#fff;border-bottom:1px solid #e1e1e1}
.head{max-width:1180px;margin:auto;padding:14px 24px;display:flex;align-items:center;justify-content:space-between;gap:24px}
.logo{display:block;width:310px;height:auto;max-height:88px;object-fit:contain;object-position:left center}
.nav{display:flex;align-items:center;gap:28px;font-size:15px;font-weight:700;color:#333}
.nav a{text-decoration:none}
.nav a:hover{color:#c8102e}
.all-btn{background:#c8102e;color:#fff!important;padding:11px 18px;border-radius:9px}
main{max-width:1180px;margin:0 auto;padding:34px 24px 60px}
.breadcrumb{font-size:14px;color:#666;margin:0 0 28px}
.breadcrumb a{text-decoration:none;color:#555}
.card{background:#fff;border:1px solid #dedede;border-radius:20px;overflow:hidden;box-shadow:0 12px 35px #0000000b}
.top{height:5px;background:linear-gradient(90deg,#c8102e 0%,#c8102e 68%,#c9a227 100%)}
.intro{padding:38px 42px 28px}
.brand{display:flex;align-items:center;gap:18px;margin-bottom:20px}.brand img{width:72px;height:72px;object-fit:contain;border:1px solid #e2e5e8;border-radius:14px;padding:8px;background:#fff}.brand-label{font-size:13px;color:#777;font-weight:700;text-transform:uppercase;letter-spacing:.08em}
h1{margin:0;font-size:clamp(36px,5vw,58px);line-height:1.03;letter-spacing:-1.5px}
.intro p{color:#626262;font-size:18px;max-width:820px;margin:18px 0 22px}
.badges{display:flex;flex-wrap:wrap;gap:10px}
.badge{display:inline-flex;align-items:center;gap:8px;background:#f3f3f6;border-radius:12px;padding:10px 15px;font-size:15px;font-weight:800}
.badge.primary{background:#fae8eb;color:#b20f2b}
.stats-grid{padding:0 28px 22px;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px}.stat{padding:16px 18px;border:1px solid #dedede;border-radius:14px;background:#fafbfc}.stat strong{display:block;font-size:24px;line-height:1.1}.stat span{display:block;margin-top:5px;color:#777;font-size:12px}.context{padding:0 28px 28px}.context h2{font-size:24px;margin:0 0 7px}.context p{margin:0;color:#666;font-size:15px;max-width:900px}.related{padding:0 28px 30px}.related h2{font-size:22px;margin:0 0 12px}.related-links{display:flex;flex-wrap:wrap;gap:8px}.related-chip{display:inline-flex;padding:9px 12px;border:1px solid #dedede;border-radius:999px;text-decoration:none;font-size:13px;font-weight:700;background:#fafbfc}.related-chip:hover{border-color:#f0aab5;color:#c8102e}.list{padding:0 28px 36px}
.list-head{display:flex;align-items:end;justify-content:space-between;gap:20px;margin:8px 0 16px}
h2{font-size:30px;line-height:1.15;margin:0}
ul{list-style:none;padding:0;margin:0;display:grid;gap:8px}
.event-card{border:1px solid #dedede;border-radius:15px;background:#fff;overflow:hidden;transition:box-shadow .15s,transform .15s}
.event-card:hover{box-shadow:0 8px 24px #00000012;transform:translateY(-1px)}
.event-card>a{display:grid;grid-template-columns:92px minmax(230px,1.7fr) 130px 190px 155px 120px;align-items:center;gap:18px;padding:9px 14px;text-decoration:none}
.date-box{height:64px;border-left:4px solid #c8102e;border-radius:9px;background:#fff0f2;display:flex;flex-direction:column;align-items:center;justify-content:center;line-height:1}
.date-box span{font-size:12px;color:#c8102e;font-weight:800}
.date-box strong{font-size:25px;color:#c8102e;margin:3px 0}
.date-box small{font-size:12px;color:#c8102e;font-weight:700}
.event-title{font-size:18px;line-height:1.2;display:block}
.tags{display:flex;gap:7px;margin-top:8px;flex-wrap:wrap}
.tag{font-size:11px;background:#eef0f8;color:#273252;border-radius:999px;padding:4px 9px;font-weight:800}
.event-info{display:flex;align-items:center;gap:10px;min-width:0}
.event-info .icon{font-size:25px;color:#c8102e;line-height:1}
.event-info strong{display:block;font-size:16px;line-height:1.15;white-space:nowrap}
.event-info small{display:block;color:#777;font-size:12px;margin-top:4px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.buy-info .icon{color:#c28d00}
.buy-info .event-info strong{white-space:normal;overflow-wrap:anywhere}
.details{justify-self:end;background:#c8102e;color:#fff;border-radius:9px;padding:12px 17px;font-weight:800;white-space:nowrap}
.details span{font-size:18px;margin-left:5px}
@media(max-width:1000px){
.nav{gap:15px}.nav a:nth-child(2),.nav a:nth-child(3){display:none}
.event-card>a{grid-template-columns:82px minmax(190px,1.5fr) 110px 150px 140px 105px;gap:12px}
}
@media(max-width:760px){
.head{padding:12px 15px}.logo{width:245px;max-height:72px}.nav a{display:none!important}.all-btn{display:block!important}.brand img{width:60px;height:60px}.brand{gap:14px}
main{padding:22px 12px 40px}.intro{padding:28px 22px 22px}h1{font-size:38px;letter-spacing:-.8px}
.intro p{font-size:16px}.list{padding:0 12px 25px}.list-head{display:block}h2{font-size:25px;margin-bottom:14px}
.stats-grid{grid-template-columns:repeat(2,minmax(0,1fr));padding:0 12px 18px}.context{padding:0 12px 22px}.context h2{font-size:21px}.event-card>a{grid-template-columns:64px minmax(0,1fr);gap:12px;padding:10px}
.date-box{height:62px}
.event-info{grid-column:2}
.event-info strong{font-size:15px}.event-info small{white-space:normal}
.time-info,.location-info,.buy-info{border-top:1px solid #eee;padding-top:9px}
.details{grid-column:2;justify-self:start;padding:9px 14px;margin-top:2px}
.event-title{font-size:17px}
}
'''

    page = f'''<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)} | Helvetic Poker</title>
<meta name="description" content="{esc(desc)}">
<meta name="robots" content="index,follow">
<link rel="canonical" href="{esc(url)}">
<script type="application/ld+json">{json.dumps(breadcrumb_json, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(collection_json, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps({"@context":"https://schema.org","@type":"ItemList","name":title,"itemListElement":[{"@type":"ListItem","position":i+1,"name":e.get("title") or "Pokerturnier","url":f"{BASE_URL}/turniere/{event_slug(e)}/"} for i,e in enumerate(upcoming[:60])]}, ensure_ascii=False)}</script>
<style>{style}</style>
</head>
<body>
<header><div class="head">
<a href="/" aria-label="Helvetic Poker – Pokerturniere Schweiz"><img class="logo" src="/assets/helvetic-poker-logo.png" alt="Helvetic Poker"></a>
<nav class="nav" aria-label="Hauptnavigation">
<a href="/">Turniere</a>
<a href="/stadt/">Städte</a>
<a href="/kanton/">Kantone</a>
<a href="/veranstalter/">Veranstalter</a>
<a href="/">Kalender</a>
<a class="all-btn" href="/">Alle Turniere</a>
</nav>
</div></header>
<main>
<div class="breadcrumb"><a href="/">⌂</a> &nbsp;›&nbsp; <a href="/{kind}/">{esc(parent_name)}</a> &nbsp;›&nbsp; {esc(name)}</div>
<article class="card">
<div class="top"></div>
<section class="intro">
{f'<div class="brand"><img src="{esc(logo_url)}" alt="Logo von {esc(name)}" loading="lazy" referrerpolicy="no-referrer"><span class="brand-label">Veranstalter</span></div>' if logo_url else ''}
<h1>{esc(title)}</h1>
<p>{esc(desc)}</p>
<div class="badges">
<span class="badge primary">◫ &nbsp;{len(upcoming)} kommende Turniere</span>
<span class="badge">⌖ &nbsp;{esc(name)}</span>
</div>
</section>
<section class="stats-grid">{stat_html}</section>
<section class="context">
<h2>{esc(extra_title)}</h2>
<p>{esc(extra_text)} {esc(detail_text)}</p>
</section>
{f'<section class="related"><h2>Weitere Übersichten</h2><div class="related-links">{related_html}</div></section>' if related_html else ''}
<section class="list">
<div class="list-head"><h2>{len(upcoming)} kommende Pokerturniere{(" in " + esc(name)) if kind == "stadt" else ""}</h2></div>
<ul>{rows}</ul>
</section>
</article>
</main>
</body>
</html>'''

    out = ROOT / kind / slug
    out.mkdir(parents=True, exist_ok=True)
    (out / 'index.html').write_text(page, encoding='utf-8')
    return url

sitemap = set()
generated = 0

for kind, values in groups.items():
    write_index_page(kind, values)
    for name, items in sorted(values.items()):

        url = write_page(kind, name, items)
        if url:
            sitemap.add(url)
            generated += 1

landing_urls = sorted(sitemap)
(ROOT / '.generated-landing-urls.txt').write_text(
    '\n'.join(landing_urls) + ('\n' if landing_urls else ''),
    encoding='utf-8'
)

print(f'Generated {generated} useful SEO landing pages.')
print(f'Added {len(landing_urls)} landing URLs.')
