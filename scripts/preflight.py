import json,re,sys
from pathlib import Path
from urllib.parse import urlparse
ROOT=Path(__file__).resolve().parents[1]; events=json.loads((ROOT/'events.json').read_text(encoding='utf-8')); errors=[]; slugs=set()
req=['id','date_start','date_end','title','city','region','organizer','venue','venue_type','variant','event_type','currency','is_freeroll','buy_in_label','status','last_checked','organizer_url','slug']
for e in events:
  for k in req:
    if k not in e: errors.append(f"{e.get('id','?')}: missing {k}")
  s=e.get('slug','')
  if s in slugs: errors.append(f'duplicate slug: {s}')
  slugs.add(s)
  if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',s): errors.append(f'unsafe slug: {s}')
  if e.get('status')!='verified': errors.append(f'non-verified public event: {e.get("id")}')
  if not (ROOT/'events'/s/'index.html').is_file(): errors.append(f'missing event page: {s}')
  u=urlparse(e.get('organizer_url',''))
  if u.scheme!='https' or not u.netloc: errors.append(f'invalid organizer URL: {e.get("id")}')
if not (ROOT/'404.html').is_file(): errors.append('missing 404.html')
if errors:
 print('\n'.join('ERROR: '+x for x in errors));sys.exit(1)
print(f'PASS: {len(events)} public events; {len(slugs)} unique slugs; all event pages present.')
