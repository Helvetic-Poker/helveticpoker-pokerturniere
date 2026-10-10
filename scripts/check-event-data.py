#!/usr/bin/env python3
"""Read-only quality report for the public poker tournament JSON data."""
import json
import re
from collections import Counter
from datetime import date
from pathlib import Path

DATA_DIR = Path("data")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
REQUIRED = ("title", "date_start", "city", "organizer")
issues = Counter()
events = []
source_files = 0

for path in sorted(DATA_DIR.glob("*.json")):
    source_files += 1
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR {path}: JSON konnte nicht gelesen werden ({exc})")
        issues["invalid_json"] += 1
        continue

    if isinstance(payload, list):
        rows = payload
    elif isinstance(payload, dict):
        rows = payload.get("events", [payload])
        if not isinstance(rows, list):
            print(f"ERROR {path}: 'events' ist keine Liste")
            issues["invalid_events_container"] += 1
            continue
    else:
        print(f"ERROR {path}: oberste JSON-Struktur muss Liste oder Objekt sein")
        issues["invalid_root"] += 1
        continue

    for index, event in enumerate(rows, start=1):
        if not isinstance(event, dict):
            print(f"ERROR {path} Eintrag {index}: kein Objekt")
            issues["invalid_event"] += 1
            continue
        event["_quality_source"] = f"{path}:{index}"
        events.append(event)
        for field in REQUIRED:
            if not str(event.get(field) or "").strip():
                print(f"WARN {path} Eintrag {index}: Pflichtfeld '{field}' fehlt")
                issues[f"missing_{field}"] += 1
        raw_date = str(event.get("date_start") or "").strip()
        if raw_date:
            if not DATE_RE.match(raw_date):
                print(f"WARN {path} Eintrag {index}: Datum nicht im Format YYYY-MM-DD: {raw_date}")
                issues["invalid_date_format"] += 1
            else:
                try:
                    date.fromisoformat(raw_date)
                except ValueError:
                    print(f"WARN {path} Eintrag {index}: ungültiges Kalenderdatum: {raw_date}")
                    issues["invalid_date"] += 1

# Flag likely duplicates without deleting or changing any public data.
seen = {}
for event in events:
    key = (
        str(event.get("title") or "").strip().casefold(),
        str(event.get("date_start") or "").strip(),
        str(event.get("city") or "").strip().casefold(),
        str(event.get("organizer") or "").strip().casefold(),
    )
    if all(key):
        if key in seen:
            print(f"WARN möglicher Doppel-Eintrag: {seen[key]} und {event['_quality_source']} ({key[0]}, {key[1]}, {key[2]})")
            issues["possible_duplicates"] += 1
        else:
            seen[key] = event["_quality_source"]

print()
print(f"Datenqualitätsbericht: {source_files} JSON-Dateien, {len(events)} Einträge geprüft")
if issues:
    for name, count in sorted(issues.items()):
        print(f"- {name}: {count}")
    print("Hinweis: Dieser Bericht verändert keine Daten und blockiert die Veröffentlichung nicht.")
else:
    print("Keine Auffälligkeiten nach den geprüften Basisregeln gefunden.")
