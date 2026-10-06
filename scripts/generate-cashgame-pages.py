from pathlib import Path
import json, html
ROOT=Path('.')
DATA=ROOT/'data/cashgames.json'
OUT=ROOT/'cashgames/index.html'
BASE='https://cashgame.helveticpoker.ch'
data=json.loads(DATA.read_text(encoding='utf-8')) if DATA.exists() else []
confirmed=[x for x in data if x.get('status')=='confirmed']
paused=[x for x in data if x.get('status')=='paused']
rows=[]
for x in data:
    if x.get('status') not in {'confirmed','paused'}: continue
    title=f"{x.get('provider')} · {x.get('variant')} {x.get('stakes')}" if x.get('variant')!='' else x.get('provider')
    rows.append(f'<article class="card"><h3>{html.escape(title)}</h3><div class="meta">{html.escape(x.get("city",""))} · {html.escape(x.get("canton",""))} · {html.escape(x.get("schedule",""))}</div><span class="status">{html.escape(x.get("status",""))}</span><a class="source" href="{html.escape(x.get("source_url",""))}" target="_blank" rel="noopener">Offizielle Quelle →</a></article>')
page=f'''<!doctype html><html lang="de-CH"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Cash Games Schweiz | Helvetic Poker</title><meta name="description" content="Aktuelle Cash Games in Schweizer Casinos: Varianten, Limits, Buy-ins und Spielzeiten."><link rel="canonical" href="{BASE}/"><style>body{{margin:0;background:#f3f5f7;color:#13263a;font-family:Arial,sans-serif}}main{{max-width:1100px;margin:auto;padding:30px 18px}}header{{background:#0c1b27;color:#fff;padding:16px 20px}}h1{{font-size:48px;margin:0 0 10px}}.hero,.card{{background:#fff;border:1px solid #dfe5ea;border-radius:15px;padding:22px}}.hero{{margin-bottom:15px}}.cards{{display:grid;grid-template-columns:repeat(2,1fr);gap:9px}}.card h2,.card h3{{margin:0 0 6px}}.meta{{color:#6f7c8b;font-size:12px;margin-bottom:8px}}.status{{font-size:11px;font-weight:700}}.source{{display:block;color:#e21b35;margin-top:9px;font-size:11px;font-weight:700}}@media(max-width:700px){{h1{{font-size:34px}}.cards{{grid-template-columns:1fr}}}}</style></head><body><header>Helvetic Poker · Cash Games Schweiz</header><main><section class="hero"><h1>Cash Games Schweiz</h1><p>Aktuelle Cash Games in Schweizer Casinos.</p><p><strong>{len(confirmed)}</strong> bestätigte Angebote · <strong>{len(paused)}</strong> pausierte Angebote</p></section><section class="cards">{"".join(rows)}</section></main></body></html>'''
OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(page,encoding='utf-8')
print(f'Generated cashgame preview with {len(data)} records.')
