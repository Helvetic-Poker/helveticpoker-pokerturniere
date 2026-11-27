# Tagesaudit – Buy-in.info-Abgleich vom 27.11.2026

## Ergebnis
- Quelle: https://buy-in.info/calendar
- Aktuelle Hauptkalender-Suchergebnisse am 27.11.2026: konkrete Listings vom 27.11. bis mindestens 04.12.2026.
- Zusätzlich direkte datierte Veranstalterfilter: Prestige (https://buy-in.info/calendar?forganizer=189), Grand Casino Luzern (https://buy-in.info/calendar?forganizer=458), Another Poker Basel (https://buy-in.info/calendar?forganizer=226).
- Hauptkalender-Suchergebnisse enthalten die datierten Einträge 27.–30.11. sowie 01.–04.12.; die Organizerfilter für Another Poker reichen in der abgerufenen Ansicht bis 25.12., Prestige mindestens bis 10.12. und Grand Casino Luzern bis 10.12.
- Keine vollständige paginierte Kalenderextraktion für alle Monate bis 31.12. gelang. Daher keine Vollständigkeitsbehauptung und keine künstliche Gesamtzahl über nicht deduplizierte Ansichten.

## Änderungen auf main
Zwei fehlende konkrete Buy-in.info-Turniere ergänzt:
1. HSOP Helvetic Series of Poker – HSOP GRAUBÜNDEN, 01.12.2026, 19:00, CHF 95+25.
   Quelle: aktuelle Hauptkalenderansicht https://www.buy-in.info/calendar, geprüft 27.11.2026.
2. Another Poker Basel – Hyper Turbo Satelitte - 1 Ticket garantiert, 02.12.2026, 18:40, CHF 24+6, Satellite.
   Quelle: datierte Veranstalterfilteransicht https://buy-in.info/calendar?forganizer=226, geprüft 27.11.2026.

Drei bestehende TBA-Startzeiten anhand konkreter datierter Hauptkalenderzeilen korrigiert:
- 24Poker – 24-Big Tuesday Poker 130er, 01.12., 19:00.
- AZ Poker Club Bern – Dienstag Special ReBuy Monster Stack, 01.12., 19:00.
- AZ Poker Club Bern – Monster Stack 100K, 20 min Level, 02.12., 19:00.

Keine Uhrzeit wurde aus einem Wochenmuster abgeleitet. Cash Games wurden ausgeschlossen. Es wurden keine Dubletten entfernt. Der ältere Another-Poker-Eintrag Master Freezeout am 28.11. bleibt als dokumentierter Quellenkonflikt bestehen, da er in der aktuellen Organizeransicht nicht auftaucht, aber keine datierte offizielle Absage vorliegt.

## Abgleich und Blocker
- Aktuelle Hauptkalender-Suchergebnisse liefern konkrete Zeilen für 27.–30.11. sowie 01.–04.12.; die erste sichtbare HTML-Hauptansicht ist nicht die vollständige Kalenderpagination.
- Prestige-Organizerfilter liefert konkrete Einträge vom 27.11. bis mindestens 10.12.
- Grand-Casino-Luzern-Organizerfilter liefert konkrete Einträge vom 27.11. bis mindestens 10.12.; Cash Games ausgeschlossen.
- Another-Poker-Organizerfilter liefert konkrete Einträge vom 30.11. bis mindestens 25.12.
- Für 05.–31.12. sind damit nicht alle Veranstalter und nicht alle Monatsansichten vollständig abgedeckt. Insbesondere FOIF, Munot, Capital, AZ, Pöstli, 24Poker, House of Cards, Sports Zugerland, RPR, STATION, HSOP, Airfield, DC, RDC, OVP, 72 Offsuite und Grand Casino Basel konnten nicht als vollständiger aktueller Dezemberexport dedupliziert werden.
- Hauptkalender-Folgeseiten und vollständige Datumsfilter bleiben ein technischer Blocker.

## Datenqualität nach Änderung
- Alle neun Dateien data/01.json bis data/09.json erneut abgerufen und JSON-geparst.
- Datei-Zählung: data/01.json: 15; data/02.json: 15; data/03.json: 15; data/04.json: 15; data/05.json: 15; data/06.json: 14; data/07.json: 15; data/08.json: 10; data/09.json: 846.
- Gesamt: 960 Turnierdatensätze.
- 27.11.–31.12.2026: 320 Datensätze.
- Doppelte IDs: 0.
- Doppelte Slugs: 0.
- Cash Games in Turnierdateien: 0 (separate Cash-Game-Dateien bleiben unberührt).
- Deduplizierung: keine ID-/Slug-Dubletten gefunden; keine Datensätze gelöscht.

## Deployment
- Datencommit: 87053ab58bcfbc8c08a43948a5d5c9a46250f8bb.
- Nachfolgende GitHub-Actions-Qualitätsprüfung und Pages-Deployment müssen nach Abschluss kontrolliert werden.
- Ein neues Artefakt ist zum Zeitpunkt der Audit-Erstellung noch nicht verifiziert.
- Live-Seiten müssen nach dem Build separat geprüft werden; alte Cache-Antworten sind vom Artefakt zu unterscheiden.

## Repository
https://github.com/Helvetic-Poker/helveticpoker-pokerturniere
