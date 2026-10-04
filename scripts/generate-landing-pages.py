import html, json, re
from datetime import datetime
from pathlib import Path
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
    return 'Noch nicht veröffentlicht'

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

    if kind == 'stadt':
        title = f'Pokerturniere in {name}'
        desc = f'Kommende Pokerturniere in {name}: Termine, Startzeiten, Buy-ins, Spielarten und Veranstaltungsorte.'
        parent_name = 'Städte'
    elif kind == 'kanton':
        title = f'Pokerturniere im Kanton {name}'
        desc = f'Kommende Pokerturniere im Kanton {name}: Termine, Startzeiten, Buy-ins, Spielarten und Veranstaltungsorte.'
        parent_name = 'Kantone'
    else:
        title = f'Pokerturniere von {name}'
        desc = f'Kommende Pokerturniere von {name}: Termine, Startzeiten, Buy-ins und Spielarten im Schweizer Pokerkalender.'
        parent_name = 'Veranstalter'

    rows = ''.join(row(e) for e in upcoming[:60])

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
<style>
*{box-sizing:border-box}
body{margin:0;font-family:Arial,sans-serif;color:#151515;background:#f5f5f5;line-height:1.45}
a{color:inherit}
header{background:#fff;border-bottom:1px solid #e1e1e1}
.head{max-width:1180px;margin:auto;padding:14px 24px;display:flex;align-items:center;justify-content:space-between;gap:24px}
.logo{display:block;width:205px;height:auto;max-height:58px;object-fit:contain;object-position:left center}
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
h1{margin:0;font-size:clamp(36px,5vw,58px);line-height:1.03;letter-spacing:-1.5px}
.intro p{color:#626262;font-size:18px;max-width:820px;margin:18px 0 22px}
.badges{display:flex;flex-wrap:wrap;gap:10px}
.badge{display:inline-flex;align-items:center;gap:8px;background:#f3f3f6;border-radius:12px;padding:10px 15px;font-size:15px;font-weight:800}
.badge.primary{background:#fae8eb;color:#b20f2b}
.list{padding:0 28px 36px}
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
.details{justify-self:end;background:#c8102e;color:#fff;border-radius:9px;padding:12px 17px;font-weight:800;white-space:nowrap}
.details span{font-size:18px;margin-left:5px}
@media(max-width:1000px){
.nav{gap:15px}.nav a:nth-child(2),.nav a:nth-child(3){display:none}
.event-card>a{grid-template-columns:82px minmax(190px,1.5fr) 110px 150px 140px 105px;gap:12px}
}
@media(max-width:760px){
.head{padding:12px 15px}.logo{width:175px}.nav a{display:none!important}.all-btn{display:block!important}
main{padding:22px 12px 40px}.intro{padding:28px 22px 22px}h1{font-size:38px;letter-spacing:-.8px}
.intro p{font-size:16px}.list{padding:0 12px 25px}.list-head{display:block}h2{font-size:25px;margin-bottom:14px}
.event-card>a{grid-template-columns:64px minmax(0,1fr);gap:12px;padding:10px}
.date-box{height:62px}
.event-info{grid-column:2}
.event-info strong{font-size:15px}.event-info small{white-space:normal}
.time-info,.location-info,.buy-info{border-top:1px solid #eee;padding-top:9px}
.details{grid-column:2;justify-self:start;padding:9px 14px;margin-top:2px}
.event-title{font-size:17px}
}
</style>
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
<h1>{esc(title)}</h1>
<p>{esc(desc)}</p>
<div class="badges">
<span class="badge primary">◫ &nbsp;{len(upcoming)} kommende Turniere</span>
<span class="badge">⌖ &nbsp;{esc(name)}</span>
</div>
</section>
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
