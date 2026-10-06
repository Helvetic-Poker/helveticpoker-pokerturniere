import html, json, re
from datetime import date, timedelta, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

BASE_URL = "https://pokerturniere.helveticpoker.ch"
ROOT = Path(".")
DATA_DIR = ROOT / "data"
TZ = ZoneInfo("Europe/Zurich")

CANTON_NAMES = {
    "AG":"Aargau","AR":"Appenzell Ausserrhoden","AI":"Appenzell Innerrhoden",
    "BL":"Basel-Landschaft","BS":"Basel-Stadt","BE":"Bern","FR":"Freiburg",
    "GE":"Genf","GL":"Glarus","GR":"Graubünden","JU":"Jura","LU":"Luzern",
    "NE":"Neuenburg","NW":"Nidwalden","OW":"Obwalden","SG":"St. Gallen",
    "SH":"Schaffhausen","SZ":"Schwyz","SO":"Solothurn","TG":"Thurgau",
    "TI":"Tessin","UR":"Uri","VD":"Waadt","VS":"Wallis","ZG":"Zug","ZH":"Zürich"
}

def esc(value):
    return html.escape(str(value or ""), quote=True)

def slugify(value):
    value = str(value or "").strip().lower()
    value = value.replace("ä","ae").replace("ö","oe").replace("ü","ue").replace("ß","ss")
    return re.sub(r"[^a-z0-9]+","-", value).strip("-")

def event_slug(event):
    return event.get("slug") or slugify("-".join(
        str(x) for x in [
            event.get("title"), event.get("city"),
            event.get("date_start"), event.get("id")
        ] if x
    ))

def load_events():
    events = []
    for path in sorted(DATA_DIR.glob("*.json")):
        if path.name.startswith("cashgames"):
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        if isinstance(data, list):
            events.extend(data)
        elif isinstance(data, dict):
            values = data.get("events")
            if isinstance(values, list):
                events.extend(values)
            else:
                events.append(data)
    return events

events = load_events()
today = datetime.now(TZ).date()

def parse_date(value):
    try:
        return date.fromisoformat(str(value))
    except Exception:
        return None

def date_label(value):
    d = parse_date(value)
    if not d:
        return value or ""
    return d.strftime("%d.%m.%Y")

def weekday_label(d):
    return ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"][d.weekday()]

def event_sort(event):
    return (event.get("date_start") or "9999-99-99", event.get("time") or "99:99", event.get("title") or "")

def buy_label(event):
    label = str(event.get("buy_in_label") or "").strip()
    if label:
        return label.replace("Buy-in ", "", 1)
    value = event.get("buy_in")
    if isinstance(value, (int, float)) and value > 0:
        return f"CHF {value:,.0f}".replace(",", "'")
    return "Buy-in siehe Veranstalter"

def page_url(slug):
    return f"{BASE_URL}/{slug}/"

# Only create links to collection pages that the main landing generator also publishes.
upcoming = [e for e in events if (parse_date(e.get("date_start")) or date.max) >= today]
city_counts = {}
organizer_counts = {}
canton_counts = {}
for e in upcoming:
    city = str(e.get("city") or "").strip()
    organizer = str(e.get("organizer") or "").strip()
    canton = CANTON_NAMES.get(str(e.get("canton") or "").strip().upper(), "")
    if city:
        city_counts[city] = city_counts.get(city, 0) + 1
    if organizer:
        organizer_counts[organizer] = organizer_counts.get(organizer, 0) + 1
    if canton:
        canton_counts[canton] = canton_counts.get(canton, 0) + 1

def collection_links(event):
    links = []
    city = str(event.get("city") or "").strip()
    organizer = str(event.get("organizer") or "").strip()
    canton = CANTON_NAMES.get(str(event.get("canton") or "").strip().upper(), "")
    if city in city_counts and city_counts[city] >= 2:
        links.append((f"Pokerturniere in {city}", f"/stadt/{slugify(city)}/"))
    if canton in canton_counts and canton_counts[canton] >= 2:
        links.append((f"Pokerturniere im Kanton {canton}", f"/kanton/{slugify(canton)}/"))
    if organizer in organizer_counts and organizer_counts[organizer] >= 2:
        links.append((f"Turniere von {organizer}", f"/veranstalter/{slugify(organizer)}/"))
    return links

def event_row(event):
    title = event.get("title") or "Pokerturnier"
    city = event.get("city") or ""
    venue = event.get("venue") or ""
    variant = event.get("variant") or ""
    time = event.get("time") or "—"
    slug = event_slug(event)
    tags = " ".join(
        f'<span class="tag">{esc(x)}</span>'
        for x in [variant, buy_label(event)]
        if x
    )
    return f"""
<article class="event">
  <a href="/turniere/{esc(slug)}/">
    <div class="date"><strong>{esc(date_label(event.get("date_start")))}</strong><span>{esc(time)} Uhr</span></div>
    <div class="main"><h2>{esc(title)}</h2><p>{esc(venue)}{(" · " + esc(city)) if city else ""}</p><div class="tags">{tags}</div></div>
    <div class="cta">Turnier ansehen →</div>
  </a>
</article>"""

def write_page(slug, label, title, description, items, range_text):
    url = page_url(slug)
    has_content = bool(items)
    robots = "index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1" if has_content else "noindex,follow"
    item_json = [
        {
            "@type": "ListItem",
            "position": i + 1,
            "name": event.get("title") or "Pokerturnier",
            "url": f"{BASE_URL}/turniere/{event_slug(event)}/"
        }
        for i, event in enumerate(items[:100])
    ]
    graph = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "CollectionPage",
                "@id": url + "#webpage",
                "url": url,
                "name": title,
                "description": description,
                "isPartOf": {
                    "@type": "WebSite",
                    "name": "Helvetic Poker – Pokerturniere Schweiz",
                    "url": BASE_URL + "/"
                },
                "mainEntity": {
                    "@type": "ItemList",
                    "name": label,
                    "numberOfItems": len(items),
                    "itemListElement": item_json
                }
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type":"ListItem","position":1,"name":"Pokerturniere Schweiz","item":BASE_URL + "/"},
                    {"@type":"ListItem","position":2,"name":label,"item":url}
                ]
            }
        ]
    }
    links = []
    seen = set()
    for event in items:
        for text, href in collection_links(event):
            if href not in seen:
                seen.add(href)
                links.append((text, href))
    related_html = "".join(
        f'<a href="{esc(href)}">{esc(text)}</a>' for text, href in links[:18]
    )
    rows = "".join(event_row(e) for e in items[:100])
    empty = f'<div class="empty">Für diesen Zeitraum sind aktuell keine Pokerturniere erfasst. <a href="/">Alle kommenden Turniere anzeigen →</a></div>' if not items else ""
    page = f"""<!doctype html>
<html lang="de-CH">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{esc(url)}">
<meta property="og:type" content="website">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{esc(url)}">
<meta property="og:site_name" content="Helvetic Poker">
<script type="application/ld+json">{json.dumps(graph, ensure_ascii=False)}</script>
<style>
*{{box-sizing:border-box}}
body{{margin:0;background:#f4f6f8;color:#13263a;font-family:Arial,Helvetica,sans-serif;line-height:1.45}}
a{{color:inherit}}
header{{background:#0c1b27;color:#fff;border-top:4px solid #e21b35}}
.nav{{max-width:1180px;margin:auto;padding:16px 22px;display:flex;align-items:center;justify-content:space-between;gap:20px}}
.logo{{width:235px;max-height:62px;object-fit:contain;object-position:left center}}
.navlinks{{display:flex;gap:18px;font-size:14px;font-weight:700}}
.navlinks a{{text-decoration:none}}
main{{max-width:1120px;margin:auto;padding:28px 18px 60px}}
.breadcrumb{{font-size:13px;color:#667482;margin-bottom:16px}}
.hero,.event,.related{{background:#fff;border:1px solid #dfe5ea;border-radius:16px}}
.hero{{padding:30px 30px 24px;box-shadow:0 8px 24px #10223810}}
h1{{margin:0;font-size:clamp(34px,5vw,52px);line-height:1.05;letter-spacing:-1px}}
.lead{{font-size:17px;color:#5d6a77;max-width:850px;margin:15px 0 7px}}
.range{{font-size:13px;color:#7b8793}}
.stats{{display:flex;gap:9px;flex-wrap:wrap;margin-top:18px}}
.stat{{border:1px solid #e1e6eb;border-radius:10px;padding:9px 12px;background:#fafbfc}}
.stat strong{{display:block;font-size:19px}} .stat span{{font-size:11px;color:#6d7884}}
.related{{margin-top:14px;padding:17px 20px}}
.related h2{{font-size:17px;margin:0 0 10px}} .related-links{{display:flex;gap:8px;flex-wrap:wrap}}
.related-links a{{padding:8px 11px;border:1px solid #dfe5ea;border-radius:999px;text-decoration:none;font-size:12px;font-weight:700}}
.related-links a:hover{{border-color:#e21b35;color:#e21b35}}
.list{{margin-top:18px;display:grid;gap:8px}}
.event{{overflow:hidden}} .event>a{{display:grid;grid-template-columns:145px 1fr auto;align-items:center;gap:18px;padding:15px 17px;text-decoration:none}}
.date{{border-left:4px solid #e21b35;padding-left:12px}} .date strong{{display:block;font-size:17px}} .date span{{font-size:12px;color:#6b7783}}
.main h2{{margin:0;font-size:17px;line-height:1.25}} .main p{{margin:4px 0 7px;color:#667482;font-size:12px}}
.tags{{display:flex;gap:6px;flex-wrap:wrap}} .tag{{background:#f0f2f5;border-radius:999px;padding:4px 8px;font-size:10px;font-weight:700;color:#53616f}}
.cta{{background:#e21b35;color:#fff;border-radius:8px;padding:9px 12px;font-size:12px;font-weight:700;white-space:nowrap}}
.empty{{background:#fff;border:1px dashed #cbd4dc;border-radius:14px;padding:28px;text-align:center;color:#65727e}}
footer{{max-width:1120px;margin:auto;padding:0 18px 35px;color:#7a8590;font-size:11px}}
@media(max-width:720px){{.nav{{padding:12px 14px}}.logo{{width:190px}}.navlinks{{display:none}}main{{padding:20px 10px 45px}}.hero{{padding:24px 20px}}h1{{font-size:36px}}.lead{{font-size:15px}}.event>a{{grid-template-columns:1fr;gap:8px}}.cta{{justify-self:start}}}}
</style>
</head>
<body>
<header><div class="nav">
<a href="/" aria-label="Helvetic Poker – Pokerturniere Schweiz"><img class="logo" src="/assets/helvetic-poker-logo.png" alt="Helvetic Poker"></a>
<nav class="navlinks" aria-label="Hauptnavigation"><a href="/">Kalender</a><a href="/stadt/">Städte</a><a href="/kanton/">Kantone</a><a href="/veranstalter/">Veranstalter</a></nav>
</div></header>
<main>
<div class="breadcrumb"><a href="/">Pokerturniere Schweiz</a> › {esc(label)}</div>
<section class="hero">
<h1>{esc(label)}</h1>
<p class="lead">{esc(description)}</p>
<div class="range">{esc(range_text)}</div>
<div class="stats">
<div class="stat"><strong>{len(items)}</strong><span>Turniere</span></div>
<div class="stat"><strong>{len({(e.get("city") or "") for e in items if e.get("city")})}</strong><span>Städte</span></div>
<div class="stat"><strong>{len({(e.get("organizer") or "") for e in items if e.get("organizer")})}</strong><span>Veranstalter</span></div>
</div>
</section>
{f'<section class="related"><h2>Weitere Pokerturnier-Übersichten</h2><div class="related-links">{related_html}</div></section>' if related_html else ''}
<section class="list">{rows or empty}</section>
</main>
<footer>Helvetic Poker · Pokerturniere Schweiz · Aktualisiert {today.strftime("%d.%m.%Y")}</footer>
</body>
</html>"""
    out = ROOT / slug
    out.mkdir(parents=True, exist_ok=True)
    (out / "index.html").write_text(page, encoding="utf-8")
    return url if has_content else None

tomorrow = today + timedelta(days=1)
week_end = today + timedelta(days=(6 - today.weekday()))
if today.weekday() == 6:
    weekend_start, weekend_end = today, today
elif today.weekday() == 5:
    weekend_start, weekend_end = today, today + timedelta(days=1)
else:
    days_to_saturday = 5 - today.weekday()
    weekend_start, weekend_end = today + timedelta(days=days_to_saturday), today + timedelta(days=days_to_saturday + 1)

def between(start, end):
    return sorted(
        [e for e in events if start <= (parse_date(e.get("date_start")) or date.max) <= end],
        key=event_sort
    )

targets = [
    (
        "pokerturniere-heute",
        f"Pokerturniere heute in der Schweiz – {today.strftime('%d.%m.%Y')}",
        f"Pokerturniere heute in der Schweiz: aktuelle Termine, Startzeiten, Buy-ins, Orte und Veranstalter für {today.strftime('%d.%m.%Y')}.",
        between(today, today),
        f"Termine für heute, {weekday_label(today) + ', ' + today.strftime('%d.%m.%Y')}"
    ),
    (
        "pokerturniere-morgen",
        f"Pokerturniere morgen in der Schweiz – {tomorrow.strftime('%d.%m.%Y')}",
        f"Pokerturniere morgen in der Schweiz: aktuelle Termine, Startzeiten, Buy-ins, Orte und Veranstalter für {tomorrow.strftime('%d.%m.%Y')}.",
        between(tomorrow, tomorrow),
        f"Termine für morgen, {weekday_label(tomorrow) + ', ' + tomorrow.strftime('%d.%m.%Y')}"
    ),
    (
        "pokerturniere-diese-woche",
        "Pokerturniere diese Woche in der Schweiz",
        "Pokerturniere diese Woche in der Schweiz: aktuelle Termine, Startzeiten, Buy-ins, Orte und Veranstalter für die laufende Woche.",
        between(today, week_end),
        f"Diese Woche: {today.strftime('%d.%m.')} bis {week_end.strftime('%d.%m.%Y')}"
    ),
    (
        "pokerturniere-wochenende",
        "Pokerturniere am Wochenende in der Schweiz",
        "Pokerturniere am Wochenende in der Schweiz: kommende Termine am Samstag und Sonntag mit Startzeiten, Buy-ins, Orten und Veranstaltern.",
        between(weekend_start, weekend_end),
        f"Wochenende: {weekend_start.strftime('%d.%m.')} bis {weekend_end.strftime('%d.%m.%Y')}"
    ),
]

generated = []
for slug, title, description, items, range_text in targets:
    url = write_page(slug, title, title, description, items, range_text)
    if url:
        generated.append(url)

(ROOT / ".generated-time-urls.txt").write_text(
    "\n".join(generated) + ("\n" if generated else ""),
    encoding="utf-8"
)

print(f"Generated {len(generated)} time-based SEO pages with live tournament data.")
