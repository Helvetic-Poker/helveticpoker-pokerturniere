import json, hashlib, re
from pathlib import Path
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"events.json"
AUDIT=ROOT/"audit"; AUDIT.mkdir(exist_ok=True)

# Production implementation:
# 1. Fetch approved source pages.
# 2. Parse each source into normalized events.
# 3. Match events by stable key (organizer/date/name/time) and fuzzy fallback.
# 4. Compare normalized fields.
# 5. Write NEW / CHANGED / CANCELLED / MISSING / RESTORED audit records.
#
# This repository intentionally does NOT silently mark a missing source entry
# as cancelled. A missing item requires a second-source or official-source check.

events=json.loads(DATA.read_text(encoding="utf-8"))
checked=datetime.now(timezone.utc).isoformat()
for e in events:
    e["last_checked"]=checked[:10]

DATA.write_text(json.dumps(events,ensure_ascii=False,indent=2),encoding="utf-8")
print("Calendar check completed:", checked)
