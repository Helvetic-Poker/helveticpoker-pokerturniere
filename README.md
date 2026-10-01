# HELVETIC POKER – POKERTURNIERE SCHWEIZ – FINAL MVP

Dieses Paket ist die fertige MVP-Basis für den Kalender.

## Hauptdateien
- `index.html` – öffentliche Kalenderoberfläche
- `events.json` – Eventdaten
- `events/<slug>/index.html` – individuelle Eventseiten
- `WIX_EMBED_SNIPPET.html` – Wix Harmony Einbettung
- `DEPLOYMENT.md` – Einbau-/Hosting-Anleitung
- `scripts/update_calendar.py` – tägliches Update-Grundgerüst
- `.github/workflows/update.yml` – täglicher GitHub-Actions-Job

## Datenqualität
Die Seed-Daten wurden aus der bisherigen Recherche übernommen. Sie sind nicht pauschal als offiziell bestätigt zu betrachten. Der Kalender zeigt den Prüfstatus transparent an.

## Architektur
Quelle → Normalisierung → Matching → Change Detection → events.json → Frontend → Wix Embed

## Produktionsregel
Offizielle Veranstalterquelle hat Vorrang vor sekundären Kalendern. Ein verschwundener Eintrag wird nie automatisch als abgesagt behandelt.
