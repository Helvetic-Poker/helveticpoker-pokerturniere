import html, json, re
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(".")
DATA_DIR = ROOT / "data"
INDEX = ROOT / "index.html"

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
    return re.sub(r"[^a-z0-9]+","-",value).strip("-")

events = []
for path in sorted(DATA_DIR.glob("*.json")):
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        continue
    if isinstance(data, list):
        events.extend(data)
    elif isinstance(data, dict):
        events.extend(data.get("events", [data]) if isinstance(data.get("events", [data]), list) else [data])

today = datetime.now(ZoneInfo("Europe/Zurich")).strftime("%Y-%m-%d")
upcoming = [e for e in events if (e.get("date_start") or "") >= today]

def grouped(field):
    groups = {}
    for e in upcoming:
        value = (e.get(field) or "").strip()
        if value:
            groups.setdefault(value, 0)
            groups[value] += 1
    return sorted(groups.items(), key=lambda x: (-x[1], x[0].lower()))

cities_all = grouped("city")
priority_cities = ["Bern", "St. Gallen", "Luzern", "Basel", "Gisikon", "Oberentfelden", "Wilderswil", "Glarus", "Zürich", "Dietlikon", "Effretikon", "Düdingen"]
city_map = dict(cities_all)
cities = [(name, city_map[name]) for name in priority_cities if name in city_map]
cities += [(name, count) for name, count in cities_all if name not in {x[0] for x in cities}][:max(0, 12 - len(cities))]
organizers = grouped("organizer")
cantons = {}
for e in upcoming:
    code = (e.get("canton") or "").strip().upper()
    name = CANTON_NAMES.get(code) or (e.get("region") or "").strip()
    if name:
        cantons[name] = cantons.get(name, 0) + 1
cantons = sorted(cantons.items(), key=lambda x: (-x[1], x[0].lower()))

def cards(kind, items, limit=None):
    items = [(name, count) for name, count in items if count >= 2]
    if limit:
        items = items[:limit]
    return "".join(
        f'<a class="seo-hub-card" href="/{kind}/{esc(slugify(name))}/">'
        f'<span>{esc(name)}</span><small>{count} kommende Turniere</small></a>'
        for name, count in items
    )

hub = f'''<section class="seo-hub" aria-labelledby="seo-hub-title">
  <div class="seo-hub-head">
    <div>
      <h2 id="seo-hub-title">Pokerturniere in der Schweiz nach Ort &amp; Veranstalter</h2>
      <p>Finde kommende Pokerturniere nach Stadt, Kanton oder Veranstalter. <a href="/pokerturniere-schweiz/">So funktioniert der Kalender →</a></p>
    </div>
  </div>
  <div class="seo-hub-grid">\n    <div class="seo-hub-group seo-hub-group-wide">\n      <div class="seo-hub-group-head"><h3>Direkt zu den aktuellen Terminen</h3></div>\n      <div class="seo-hub-cards">\n        <a class="seo-hub-card" href="/pokerturniere-heute/"><span>Heute</span><small>Turniere heute</small></a>\n        <a class="seo-hub-card" href="/pokerturniere-morgen/"><span>Morgen</span><small>Turniere morgen</small></a>\n        <a class="seo-hub-card" href="/pokerturniere-diese-woche/"><span>Diese Woche</span><small>Laufende Woche</small></a>\n        <a class="seo-hub-card" href="/pokerturniere-wochenende/"><span>Wochenende</span><small>Samstag &amp; Sonntag</small></a>\n      </div>\n    </div>
    <div class="seo-hub-group seo-hub-group-wide">\n      <div class="seo-hub-group-head"><h3>Nach Buy-in &amp; Spielart</h3></div>\n      <div class="seo-hub-cards">\n        <a class="seo-hub-card" href="/pokerturniere-bis-50-chf/"><span>Bis CHF 50</span><small>Kleine Buy-ins</small></a>\n        <a class="seo-hub-card" href="/pokerturniere-bis-100-chf/"><span>Bis CHF 100</span><small>Buy-in bis CHF 100</small></a>\n        <a class="seo-hub-card" href="/freeroll-pokerturniere/"><span>Freerolls</span><small>Kostenlose Turniere</small></a>\n        <a class="seo-hub-card" href="/nlh-pokerturniere/"><span>NLH</span><small>No-Limit Holdem</small></a>\n        <a class="seo-hub-card" href="/plo-pokerturniere/"><span>PLO</span><small>Pot-Limit Omaha</small></a>\n      </div>\n    </div>\n    <div class="seo-hub-group">
      <div class="seo-hub-group-head"><h3>Beliebte Städte</h3><a href="/stadt/">Alle Städte →</a></div>
      <div class="seo-hub-cards">{cards("stadt", cities, 12)}</div>
    </div>
    <div class="seo-hub-group">
      <div class="seo-hub-group-head"><h3>Kantone</h3><a href="/kanton/">Alle Kantone →</a></div>
      <div class="seo-hub-cards">{cards("kanton", cantons)}</div>
    </div>
    <div class="seo-hub-group seo-hub-group-wide">
      <div class="seo-hub-group-head"><h3>Top Veranstalter</h3><a href="/veranstalter/">Alle Veranstalter →</a></div>
      <div class="seo-hub-cards">{cards("veranstalter", organizers, 12)}</div>
    </div>
  </div>
</section>'''

text = INDEX.read_text(encoding="utf-8")
start = "<!-- SEO_HUB_START -->"
end = "<!-- SEO_HUB_END -->"
if start not in text or end not in text:
    raise SystemExit("SEO hub markers missing in index.html")
before = text.split(start,1)[0]
after = text.split(end,1)[1]
text = before + start + "\n" + hub + "\n" + end + after
INDEX.write_text(text, encoding="utf-8")
print(f"Homepage hub generated: {len(cities)} cities, {len(cantons)} cantons, {len(organizers)} organizers.")
