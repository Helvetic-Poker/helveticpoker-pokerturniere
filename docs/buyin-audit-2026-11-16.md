# Buy-in.info-Tagesabgleich – 16.11.2026

## Ergebnis

- Buy-in.info-Ansichtszeilen: **413**
- Davon tatsächliche Turnierlistings: **409**
- Überschneidungen zwischen Hauptkalender und Veranstalterübersichten: **86**
- Eindeutige Turniere in den erreichbaren Ansichten: **323**
- Fehlende Turniere ergänzt: **0**
- Bestehende Angaben korrigiert: **9 Startzeiten**
- Dubletten bereinigt: **0**
- Offizielle Absagen neu bestätigt: **0**

Eine vollständige Abdeckung bis 31.12.2026 wird nicht behauptet: Die Hauptkalender-Paginierung über die ersten 100 sichtbaren Zeilen hinaus war in dieser Prüfung nicht vollständig auslesbar.

## Quellenumfang und Zählung

### Hauptkalender

Die aktuelle Hauptkalenderansicht `https://buy-in.info/calendar` zeigt 100 Zeilen, vom 16.11.2026 bis zu den ersten zwei sichtbaren Einträgen am 25.11.2026.

- 96 Turnierlistings
- 2 Cash Games (ausgeschlossen)
- 2 geschlossene Prestige-Platzhalter (ausgeschlossen)

Alle 96 Turnierlistings wurden über alle neun `data/*.json`-Dateien abgeglichen; alle sind vorhanden.

### Veranstalterübersichten

Zwölf aktuell erreichbare Buy-in.info-Veranstalterübersichten wurden vollständig ausgelesen:

| Veranstalter | Listing-Zeilen |
|---|---:|
| 24Poker | 19 |
| FOIF DRÜ EFFRETIKON | 80 |
| AZ Poker Club Bern | 27 |
| Capital Poker Club Bern | 28 |
| House of Cards Luzern | 14 |
| Munot Poker Schaffhausen | 8 |
| Another Poker Basel | 29 |
| Prestige Poker Dietlikon | 15 |
| Grand Casino Luzern | 41 |
| Pöstli Poker | 33 |
| Sports Zugerland | 12 |
| RPR/Roger's Pokerroom | 7 |
| **Summe** | **313** |

Die 313 Veranstalterlistings und 96 Hauptkalenderlistings ergeben 409 Ansichts-Vorkommen. 86 davon überschneiden sich zwischen Hauptkalender und Veranstalterseiten; damit ergeben sich **323 eindeutige Turniere**. Alle 323 sind im Datenbestand enthalten.

### Zusätzliche gefilterte Ansichten

Suchindex-Ansichten zu den Organizer-Filtern 226 (Another Poker), 458 (Grand Casino Luzern), 493 (Capital Poker Club) und 558 (Munot Poker) wurden ergänzend geprüft. Für House of Cards war eine ältere gefilterte Ansicht verfügbar; für die Abdeckung wurde die aktuelle Veranstalterübersicht bevorzugt. Direkte Web-Abrufe mehrerer Filter-URLs waren nicht zuverlässig möglich.

## Neun quellenbestätigte Startzeiten korrigiert

Die aktuelle Buy-in.info-Hauptkalenderansicht nennt für diese konkreten Datumszeilen ausdrücklich folgende Zeiten. Vorher stand in Helvetic Poker jeweils `TBA`.

| Datum | Veranstalter | Turnier | Neu |
|---|---|---|---:|
| 23.11.2026 | Prestige Poker Dietlikon | 125K Extra Monday | 19:00 |
| 23.11.2026 | Pöstli Poker | Pokemon | 19:30 |
| 23.11.2026 | FOIF DRÜ EFFRETIKON | Easy Monday NEW BOUNTY-TURNIER | 19:30 |
| 23.11.2026 | Sports Zugerland | Swiss Poker Trophy | 19:30 |
| 24.11.2026 | 24Poker | Haidy's PLO Warm Up - 2 Gtd !! | 17:30 |
| 24.11.2026 | RPR/Roger's Pokerroom | Dienstagturnier mit Halbjahrespot SHOT-CLOCK | 18:30 |
| 24.11.2026 | FOIF DRÜ EFFRETIKON | 200er FREEZEOUT | 18:30 |
| 24.11.2026 | 24Poker | 24-Big Tuesday Poker 130er | 19:00 |
| 24.11.2026 | AZ Poker Club Bern | Dienstag Special ReBuy Monster Stack | 19:00 |

Für alle neun Datensätze wurden `last_checked` auf `2026-11-16` gesetzt und ein datums- und zeitbezogener Quellenvermerk zur aktuellen Hauptkalenderansicht ergänzt. Titel, Datum, Buy-in und übrige Turnierfelder blieben unverändert. Es wurden keine Uhrzeiten aus wöchentlichen Mustern übernommen.

## Ergänzende offizielle Quellen und Konflikte

- Der offizielle AZ-Turnierkalender bestätigt die bereits vorhandenen AZ Sunday Freezout-Termine am 22.11., 06.12. und 27.12. jeweils um 15:00 Uhr: https://azpoker.club/tournament/
- Grand Casino Basel bestätigt das Sparkling Tournament am 05.12.2026 um 12:00 Uhr im Rahmen des Basler Poker Festivals: https://grandcasinobasel.com/event/basler-poker-festival-3/
- Grand Casino Luzern bestätigt den PCSM-/Autumn-Special-Stop vom 26.–29.11.2026: https://www.grandcasinoluzern.ch/spielen/poker-circle/poker-circle-swiss-masters
- Die aktuelle Buy-in.info-Clubübersicht des Grand Casino Luzern listet am 16. und 17.12. jeweils zwei getrennte „Sat. für PCSM Main Event“: 13:15 Uhr für CHF 125 und 19:00 Uhr für CHF 180. Das sind unterschiedliche Veranstaltungen, keine Dubletten.
- Beim Capital Poker Club Bern nennt die aktuelle Veranstalterübersicht den CPC THE GRAND am 27.12.2026. Eine ältere „Weitere Turniere“-Tabelle enthält den 26.12.; gewählt wurde die aktuelle Veranstalterübersicht mit 27.12.

Es wurde keine neue offizielle Absage festgestellt. Es wurde kein neuer, konkret datierter zusätzlicher Anbietertermin entdeckt, der noch nicht im Datenbestand war.

## Datenqualität über alle neun Turnierdateien

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
| data/09.json | 755 |
| **Gesamt** | **869** |

- JSON-Syntax: 9/9 gültig
- Pflichtfelder laut `scripts/check-event-data.py` (Titel, Datum, Stadt, Veranstalter): keine fehlenden Werte
- Ungültige Datumsformate: 0
- Doppelte IDs: 0
- Doppelte Slugs: 0
- Semantische Dubletten bei Vergleich von Datum, Zeit, Veranstalter, Titel und Buy-in: 0
- Turnierdatensätze vom 16.11. bis 31.12.2026: 367

Der bestehende Qualitätsprüfer meldet zwei `possible_duplicates` für die PCSM-Satelliten am 16. und 17.12. Der Prüfschlüssel ignoriert Startzeit und Buy-in; die Clubübersicht weist die jeweiligen Paare jedoch ausdrücklich mit unterschiedlichen Zeiten (13:15/19:00) und Buy-ins (CHF 125/180) aus. Die beiden Warnungen sind deshalb **keine tatsächlichen Dubletten**. Der Workflow ist erfolgreich durchgelaufen; das Prüfschema wurde nicht verändert.

## GitHub-Commit und Workflows

Datencommit auf `main`:

- https://github.com/Helvetic-Poker/helveticpoker-pokerturniere/commit/fe8ff2fcd7d92a6d4596bd28df43a79397f01561
- Commit-Nachricht: `Correct nine tournament start times from current Buy-in.info calendar (2026-11-16)`

Workflows für diesen Commit:

- Tournament data quality report: https://github.com/Helvetic-Poker/helveticpoker-pokerturniere/actions/runs/43824129667 — **success**
- Generate and deploy tournament pages: https://github.com/Helvetic-Poker/helveticpoker-pokerturniere/actions/runs/43824129669 — **success**

## Tatsächlich heruntergeladenes Pages-Artefakt

- Artefakt: https://github.com/Helvetic-Poker/helveticpoker-pokerturniere/actions/runs/43824129669/artifacts/14206036246
- Artefakt-ID: `14206036246`
- ZIP-Grösse: 1'781'172 Bytes
- SHA-256: `2a87321ab99d66b4997a5f370090f0c6da82422462a3c5f26d3507648f3b8557`
- Enthalten: 9 Turnier-JSON-Dateien, 2 Cash-Game-JSON-Dateien, 869 Turnierdetailseiten, 20 Veranstalterseiten, 942 HTML-Dateien und eine Sitemap mit 938 URLs.
- Alle neun Turnier-JSON-Dateien stimmen bytegenau (Git-Blob-SHA) mit den Dateien auf `main` überein.
- 869/869 Turnierdetailseiten vorhanden; Datum, Startzeit und Buy-in stimmen für alle 869 Seiten mit den JSON-Daten überein.
- 20/20 Veranstalterseiten-Zähler stimmen mit den aus den JSON-Dateien berechneten kommenden Events überein; die Zähler summieren sich auf 368 (einschliesslich eines Termins 2027).

Alle neun korrigierten Turnierdetailseiten sind im Artefakt vorhanden und wurden mit Datum, Startzeit und Buy-in geprüft.

## Live-Verifikation und Cache-Abweichung

Die neun korrigierten Detailseiten wurden live geöffnet bzw. über die aktuelle Sports-Zugerland-Veranstalterseite aufgerufen. Alle neun zeigen die korrigierten Werte.

Der Web-/Crawler-Abruf von Homepage und AZ-Veranstalterseite liefert dagegen noch einen älteren Snapshot: Die Homepage zeigt weiterhin den 15.11. als nächsten Termin und ältere Veranstalterzähler; die AZ-Seite zeigt 20 kommende Turniere statt 27 im Artefakt. Das ist eine Cache-/Crawler-Abweichung. Das heruntergeladene Artefakt und die direkt geöffneten Detailseiten sind aktuell.

## Verbleibende Blocker – keine Vollständigkeitsbehauptung

1. **Hauptkalender-Paginierung:** Die Hauptansicht endet nach 100 Zeilen am 25.11. (dort sind nur die ersten zwei Zeilen sichtbar). Die Schaltfläche zum Nachladen weiterer Zeilen konnte über den Webabruf nicht bedient werden. Versuche mit `?page=2`, `?offset=100`, `?start=100`, Datumsparametern und direkten Organizer-Filtern lieferten keine vollständige zweite Seite.
2. **Organizer-Enddaten:** Die aktuell sichtbaren Veranstalterübersichten enden unterschiedlich früh: 24Poker 06.12.; FOIF DRÜ 31.12.; AZ 27.12.; Capital 27.12.; House of Cards 30.12.; Munot 28.11.; Another Poker 03.12.; Prestige 24.11.; Grand Casino Luzern 20.12.; Pöstli 28.12.; Sports Zugerland 28.12.; RPR 29.12. Diese Enddaten beschreiben die letzte sichtbare Listung, nicht den Beweis, dass danach keine weiteren Turniere geplant oder veröffentlicht werden.
3. **Keine vollständige aktuelle Buy-in.info-Veranstalterübersicht in diesem Abruf:** Airfield, HSOP, STATION, 72 Offsuite, Pokerhelden/Airfield, DC Poker Club, Open Valais Poker und Kartenfreunde Wynental. Einzelne aktuelle Kalenderzeilen oder offizielle datierte Quellen sind vorhanden; sie ersetzen keine vollständige Monatsübersicht.
4. **Restliche Kalenderabdeckung:** Der Zeitraum 26.11.–31.12. kann deshalb nicht als vollständig aus Buy-in.info-Hauptkalender und allen Veranstalterseiten extrahiert bestätigt werden.

**Fazit:** Die 323 eindeutigen Turniere der heute erreichbaren Haupt- und Veranstalteransichten sind vorhanden. Neun Startzeiten wurden direkt nach datierten Hauptkalenderzeilen korrigiert. Datenprüfung und Deployment waren erfolgreich; das tatsächliche Artefakt ist geprüft. Die nicht erreichbare Hauptkalender-Paginierung und die genannten Veranstalter-/Monatslücken bleiben offen.
