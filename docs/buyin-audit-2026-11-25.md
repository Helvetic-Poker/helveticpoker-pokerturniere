# Tagesaudit – Buy-in.info-Abgleich vom 25.11.2026

## Ergebnis

- Der aktuelle Buy-in.info-Hauptkalender wurde am 25.11.2026 erneut abgerufen: https://buy-in.info/calendar
- Sichtbare Hauptkalenderzeilen: **100**.
- Davon vergangen (24.11.): **7**.
- Ab 25.11. bis zum letzten sichtbaren Eintrag am 01.12.: **93 Zeilen**.
- Cash Games in diesem Zeitraum ausgeschlossen: **2** (27.11. und 28.11., Grand Casino Luzern).
- Gültige Turnierzeilen der sichtbaren Hauptansicht: **91**.
- Doppelte Turnierzeilen innerhalb dieser Hauptansicht: **0**.
- Alle **91** gültigen sichtbaren Hauptkalender-Turniere sind im Datenbestand über alle neun data/*.json-Dateien vorhanden.
- Neue Turniere ergänzt: **0**.
- Bestehende Datensätze korrigiert: **0**.
- Dubletten bereinigt: **0**.
- Es gab keinen quellenbasierten Grund für eine Datenänderung. Daher wurde kein Turnierdatensatz verändert.

## Kontrollierte aktuelle Hauptkalenderzeilen

Die Hauptansicht listet am 25.11. neun Turniere. Diese sind vorhanden:
- Another Poker Basel – Hyper Turbo Satelitte - 1 Ticket garantiert, 18:40, CHF 24+6.
- AZ Poker Club Bern – Monster Stack 100K, 20 min Level, 19:00, CHF 70+20.
- Capital Poker Club Bern – NEW Mittwoch Deepstack / 20Min Level, 19:00, CHF 70+20.
- Munot Poker Schaffhausen – NEW COOL WEDNESDAY, 19:00, CHF 75+25.
- House of Cards Luzern – House of Cards - Lucky Wednesday, 19:00, CHF 60+20.
- Prestige Poker Dietlikon – 75er- Turnier, 19:00, CHF 75+25.
- Another Poker Basel – Classic Wednesday- On Top 1 GCL Ticket 340, 19:00, CHF 100+30.
- Another Poker Basel – Time Poker Turnier PL Omaha, 19:30, CHF 100+30.
- Pöstli Poker – Mittwuch Spez, 20:15, CHF 45+15.

Die datierten Zeilen vom 26.11. bis 01.12. wurden ebenfalls gegen den Datenbestand geprüft. Die im Hauptkalender sichtbaren Turniere sind vorhanden. Dazu gehören unter anderem Grand Casino Luzern Autumn Special, Munot NEW 100ER THURSDAY, Capital Poker Club 3 Jahre CPC - TEAM Poker Special, STATION SUPER BOMB POT EDITION ADD-ON, Prestige Progressive Bounty, Another Poker Small Fish, Sports Zugerland Swiss Poker Trophy, Pöstli Donschti Gämbler sowie die konkret gelisteten Flights und Wochenendturniere.

Quellen:
- Aktuelle Hauptkalenderansicht, Zeilen 4–103: https://buy-in.info/calendar
- Ergänzender aktueller Kalenderabruf: https://buy-in.info/calendar
- Aktuelle Grand-Casino-Veranstalter-/Clubübersicht: https://buy-in.info/club/458
- Aktuelle Sports-Zugerland-Veranstalterübersicht: https://buy-in.info/tournaments/553

## Quellen- und Abgleichregeln

- Es wurden keine Daten aus einem Wochenmuster abgeleitet.
- Keine fehlende Uhrzeit wurde durch eine Uhrzeit eines anderen Veranstaltungstags ersetzt.
- Cash Games wurden nicht in die Turnierabdeckung aufgenommen.
- Frühere Quellenkonflikte und nicht mehr in aktuellen Übersichten sichtbare historische Datensätze wurden nicht ohne bestätigte offizielle Absage gelöscht.
- Die aktuelle Buy-in.info-Hauptkalenderansicht hat Vorrang vor älteren „Weitere Turniere“-Tabellen auf Detailseiten.

## Datenbestand und Qualitätsprüfung

Alle neun Turnierdateien wurden direkt vom aktuellen main-Branch gelesen und erfolgreich als JSON geparst.

| Datei | Datensätze |
|---|---:|
| data/01.json | 15 |
| data/02.json | 15 |
| data/03.json | 15 |
| data/04.json | 15 |
| data/05.json | 15 |
| data/06.json | 14 |
| data/07.json | 15 |
| data/08.json | 10 |
| data/09.json | 840 |
| **Gesamt** | **954** |

Prüfergebnisse:
- JSON-Syntax: 9/9 gültig.
- Doppelte IDs: 0.
- Doppelte Slugs: 0.
- Semantische Dubletten über Datum, Veranstalter, Titel, Zeit und Buy-in: 0.
- Fehlende Pflichtfelder bei den sichtbaren zukünftigen Listings: 0.
- Cash Games in den Turnierdateien: 0.
- Die sichtbaren Hauptkalender-Turniere ab 25.11. sind sämtlich abgedeckt.

## Grenzen der heutigen Extraktion

Die Hauptkalenderansicht zeigt nur 100 Zeilen und endet heute beim 01.12.2026 um 18:30 Uhr. Die Folgeseiten bzw. Datumsfilter konnten in diesem Abruf nicht als vollständige weitere Hauptkalenderseite extrahiert werden.

Die heutigen 91 Turnierzeilen sind daher **nur die gültigen Einträge der sichtbaren Hauptkalenderansicht**, keine Gesamtzahl aller aktuellen Buy-in.info-Turniere. Die zwölf Veranstalterübersichten wurden heute nicht vollständig neu extrahiert und dedupliziert. Insbesondere bleiben die Hauptkalender-Folgeseite ab 01.12. sowie die vollständigen späteren Dezemberlisten einzelner Anbieter offen. Die heutigen Ansichtszeilen dürfen deshalb nicht als vollständige Abdeckung bis 31.12. interpretiert werden.

## Fazit

Für die heute vollständig sichtbare Hauptkalenderansicht sind alle 91 gültigen Turniere ab 25.11. im Helvetic-Datenbestand vorhanden. Es waren keine Datenänderungen erforderlich. Die neun JSON-Dateien sind gültig und der aktuelle Bestand enthält 954 Turnierdatensätze. Die Paginierung nach den ersten 100 Kalenderzeilen und die vollständige erneute Deduplizierung sämtlicher Veranstalteransichten bleiben offen. Eine vollständige Abdeckung bis 31.12.2026 wird ausdrücklich nicht behauptet.
