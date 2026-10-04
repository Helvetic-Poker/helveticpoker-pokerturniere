import html, json, re
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

BASE_URL = "https://pokerturniere.helveticpoker.ch"
ROOT = Path(".")
DATA_DIR = ROOT / "data"
TODAY = datetime.now(ZoneInfo("Europe/Zurich")).date()

def esc(v): return html.escape(str(v or ""), quote=True)

def slugify(v):
    v=str(v or "").strip().lower().replace("ä","ae").replace("ö","oe").replace("ü","ue").replace("ß","ss")
    return re.sub(r"[^a-z0-9]+","-",v).strip("-")

def event_slug(e):
    return e.get("slug") or slugify("-".join(str(x) for x in [e.get("title"),e.get("city"),e.get("date_start"),e.get("id")] if x))

def load():
    out=[]
    for p in sorted(DATA_DIR.glob("*.json")):
        try: data=json.loads(p.read_text(encoding="utf-8"))
        except Exception: continue
        if isinstance(data,list): out.extend(data)
        elif isinstance(data,dict):
            out.extend(data.get("events") if isinstance(data.get("events"),list) else [data])
    return out

events=load()

def d(v):
    try: return date.fromisoformat(str(v))
    except Exception: return date.max

upcoming=[e for e in events if d(e.get("date_start"))>=TODAY]

def buy(e):
    v=e.get("buy_in")
    if isinstance(v,(int,float)) and v>0: return v
    return None

def label(e):
    x=str(e.get("buy_in_label") or "").strip()
    if x: return x.replace("Buy-in ","",1)
    v=buy(e)
    return f"CHF {v:,.0f}".replace(",", "'") if v else "Buy-in siehe Veranstalter"

def sort_key(e): return (e.get("date_start") or "9999-99-99",e.get("time") or "99:99",e.get("title") or "")

def row(e):
    return f'''<article class="event"><a href="/turniere/{esc(event_slug(e))}/"><div class="date"><strong>{esc(e.get("date_start",""))}</strong><span>{esc(e.get("time","—"))} Uhr</span></div><div><h2>{esc(e.get("title") or "Pokerturnier")}</h2><p>{esc(e.get("city") or "")}{(" · " + esc(e.get("organizer") or "")) if e.get("organizer") else ""}</p><div class="tags"><span>{esc(e.get("variant") or "")}</span><span>{esc(label(e))}</span></div></div><b>Details →</b></a></article>'''

def write(slug,title,desc,items):
    items=sorted(items,key=sort_key)
    url=f"{BASE_URL}/{slug}/"
    graph={"@context":"https://schema.org","@graph":[
        {"@type":"CollectionPage","@id":url+"#webpage","url":url,"name":title,"description":desc,
         "isPartOf":{"@type":"WebSite","name":"Helvetic Poker – Pokerturniere Schweiz","url":BASE_URL+"/"},
         "mainEntity":{"@type":"ItemList","name":title,"numberOfItems":len(items),"itemListElement":[
             {"@type":"ListItem","position":i+1,"name":e.get("title") or "Pokerturnier","url":f"{BASE_URL}/turniere/{event_slug(e)}/"}
             for i,e in enumerate(items[:100])
         ]}},
        {"@type":"BreadcrumbList","itemListElement":[
            {"@type":"ListItem","position":1,"name":"Pokerturniere Schweiz","item":BASE_URL+"/"},
            {"@type":"ListItem","position":2,"name":title,"item":url}
        ]}
    ]}
    page=f'''<!doctype html><html lang="de-CH"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title><meta name="description" content="{esc(desc)}"><meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1"><link rel="canonical" href="{esc(url)}">
<meta property="og:type" content="website"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{esc(url)}"><meta property="og:site_name" content="Helvetic Poker">
<script type="application/ld+json">{json.dumps(graph,ensure_ascii=False)}</script>
<style>*{{box-sizing:border-box}}body{{margin:0;background:#f4f6f8;color:#13263a;font-family:Arial,Helvetica,sans-serif}}a{{color:inherit}}header{{background:#0c1b27;border-top:4px solid #e21b35}}.nav{{max-width:1120px;margin:auto;padding:14px 18px;display:flex;justify-content:space-between;align-items:center}}.logo{{width:220px;max-height:58px;object-fit:contain;object-position:left}}.links{{display:flex;gap:18px;font-size:13px;font-weight:700;color:#fff}}.links a{{text-decoration:none}}main{{max-width:1120px;margin:auto;padding:26px 18px 55px}}.crumb{{font-size:13px;color:#687580;margin-bottom:14px}}.hero{{background:#fff;border:1px solid #dfe5ea;border-radius:16px;padding:30px;box-shadow:0 8px 24px #10223810}}h1{{margin:0;font-size:clamp(34px,5vw,52px);line-height:1.05}}.lead{{color:#5e6b78;font-size:17px;max-width:850px;margin:14px 0 0}}.stats{{display:flex;gap:8px;margin-top:18px;flex-wrap:wrap}}.stat{{padding:9px 12px;border:1px solid #e0e5ea;border-radius:10px;background:#fafbfc}}.stat strong{{display:block;font-size:19px}}.stat span{{font-size:11px;color:#6c7884}}.list{{display:grid;gap:8px;margin-top:16px}}.event{{background:#fff;border:1px solid #dfe5ea;border-radius:14px;overflow:hidden}}.event a{{display:grid;grid-template-columns:140px 1fr auto;align-items:center;gap:16px;padding:14px;text-decoration:none}}.date{{border-left:4px solid #e21b35;padding-left:11px}}.date strong{{display:block;font-size:15px}}.date span{{font-size:11px;color:#6b7782}}.event h2{{font-size:16px;margin:0 0 4px}}.event p{{font-size:12px;color:#687580;margin:0 0 7px}}.tags{{display:flex;gap:6px;flex-wrap:wrap}}.tags span{{font-size:10px;background:#f0f2f5;border-radius:999px;padding:4px 8px;font-weight:700}}.event b{{background:#e21b35;color:#fff;border-radius:8px;padding:9px 11px;font-size:11px;white-space:nowrap}}@media(max-width:700px){{.links{{display:none}}main{{padding:20px 10px}}.hero{{padding:24px 20px}}.event a{{grid-template-columns:1fr}}.event b{{justify-self:start}}}}
</style></head><body><header><div class="nav"><a href="/"><img class="logo" src="/assets/helvetic-poker-logo.png" alt="Helvetic Poker"></a><nav class="links"><a href="/">Kalender</a><a href="/stadt/">Städte</a><a href="/kanton/">Kantone</a><a href="/veranstalter/">Veranstalter</a></nav></div></header><main><div class="crumb"><a href="/">Pokerturniere Schweiz</a> › {esc(title)}</div><section class="hero"><h1>{esc(title)}</h1><p class="lead">{esc(desc)}</p><div class="stats"><div class="stat"><strong>{len(items)}</strong><span>kommende Turniere</span></div><div class="stat"><strong>{len({e.get("city") for e in items if e.get("city")})}</strong><span>Städte</span></div><div class="stat"><strong>{len({e.get("organizer") for e in items if e.get("organizer")})}</strong><span>Veranstalter</span></div></div></section><section class="list">{"".join(row(e) for e in items[:100])}</section></main></body></html>'''
    out=ROOT/slug; out.mkdir(parents=True,exist_ok=True); (out/"index.html").write_text(page,encoding="utf-8")
    return url

targets=[
("pokerturniere-bis-50-chf","Pokerturniere bis CHF 50 in der Schweiz","Pokerturniere bis CHF 50: aktuelle Schweizer Turniere mit kleinen Buy-ins, Terminen, Orten und Veranstaltern.",lambda e:(buy(e) is not None and buy(e)<=50) or bool(e.get("is_freeroll"))),
("pokerturniere-bis-100-chf","Pokerturniere bis CHF 100 in der Schweiz","Pokerturniere bis CHF 100: aktuelle Schweizer Turniere mit Buy-ins bis CHF 100, Terminen, Orten und Veranstaltern.",lambda e:(buy(e) is not None and buy(e)<=100) or bool(e.get("is_freeroll"))),
("freeroll-pokerturniere","Freeroll Pokerturniere in der Schweiz","Freeroll Pokerturniere in der Schweiz: aktuelle kostenlose Turniere, Termine, Orte und Veranstalter.",lambda e:bool(e.get("is_freeroll"))),
("nlh-pokerturniere","NLH Pokerturniere in der Schweiz","NLH Pokerturniere in der Schweiz: aktuelle No-Limit-Hold'em-Turniere mit Terminen, Buy-ins und Spielorten.",lambda e:(e.get("variant") or "").strip().upper()=="NLH"),
("plo-pokerturniere","PLO Pokerturniere in der Schweiz","PLO Pokerturniere in der Schweiz: aktuelle Pot-Limit-Omaha-Turniere mit Terminen, Buy-ins und Spielorten.",lambda e:(e.get("variant") or "").strip().upper() in {"PLO","PLO8"})
]
urls=[]
for slug,title,desc,predicate in targets:
    items=[e for e in upcoming if predicate(e)]
    if len(items)>=2: urls.append(write(slug,title,desc,items))
(ROOT/".generated-category-urls.txt").write_text("\n".join(urls)+("\n" if urls else ""),encoding="utf-8")
print(f"Generated {len(urls)} intent-based SEO category pages.")
