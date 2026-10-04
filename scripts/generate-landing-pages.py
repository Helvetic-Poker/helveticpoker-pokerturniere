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

def row(e):
    d = e.get('date_start') or ''
    try:
        y, m, day = d.split('-')
        d = f'{day}.{m}.{y}'
    except Exception:
        pass
    meta = ' · '.join(
        x for x in [
            d,
            e.get('time') or '',
            e.get('city') or '',
            ('Buy-in ' + e.get('buy_in_label')) if e.get('buy_in_label') else ''
        ] if x
    )
    return f'<li><a href="/turniere/{esc(event_slug(e))}/"><strong>{esc(e.get("title") or "Pokerturnier")}</strong><span>{esc(meta)}</span></a></li>'

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
*{{box-sizing:border-box}}
body{{margin:0;font-family:Arial,sans-serif;color:#151515;background:#f4f4f4;line-height:1.55}}
a{{color:inherit}}
header{{background:#fff;border-bottom:1px solid #ddd}}
.head,main{{max-width:980px;margin:auto;padding:18px 20px}}
.head{{display:flex;justify-content:space-between;gap:20px}}
.head a{{text-decoration:none;color:#555;font-weight:700}}
.card{{background:#fff;border:1px solid #ddd;border-radius:22px;overflow:hidden;box-shadow:0 15px 45px #00000010}}
.top{{height:5px;background:linear-gradient(90deg,#c8102e 0%,#c8102e 68%,#c9a227 100%)}}
.intro{{padding:34px 48px 22px}}
h1{{margin:0;font-size:clamp(32px,5vw,52px);line-height:1.08}}
.intro p{{color:#666;font-size:17px;max-width:760px}}
.count{{display:inline-block;background:#f6ecee;color:#a30d25;border-radius:999px;padding:7px 12px;font-size:12px;font-weight:800}}
.list{{padding:8px 48px 45px}}
ul{{list-style:none;padding:0;margin:0;border-top:1px solid #e5e5e5}}
li{{border-bottom:1px solid #e5e5e5}}
li a{{display:flex;justify-content:space-between;gap:20px;padding:16px 2px;text-decoration:none}}
li strong{{font-size:16px}}
li span{{color:#777;font-size:13px;text-align:right}}
li a:hover strong{{color:#c8102e}}
@media(max-width:640px){{
.head,main{{padding:15px 12px}}
.intro,.list{{padding-left:22px;padding-right:22px}}
li a{{display:block}}
li span{{display:block;text-align:left;margin-top:5px}}
}}
</style>
</head>
<body>
<header><div class="head"><strong>Helvetic Poker · Pokerturniere Schweiz</strong><a href="/">← Zum Kalender</a></div></header>
<main>
<article class="card">
<div class="top"></div>
<section class="intro">
<h1>{esc(title)}</h1>
<p>{esc(desc)}</p>
<div class="count">{len(upcoming)} kommende Turniere erfasst</div>
</section>
<section class="list">
<h2>Kommende Pokerturniere</h2>
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
