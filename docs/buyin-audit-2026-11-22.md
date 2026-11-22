# Buy-in.info-Abgleich – 22.11.2026

## Ergebnis

- Fehlende aktuelle Buy-in.info-Turniere in den heute erreichbaren Ansichten ergänzt: **0**
- Bestehende Datensätze quellenbasiert korrigiert: **20 Veranstaltungen**
- Korrigierte Feldwerte: **24**
- Dubletten entfernt: **0**
- Vollständige Kalenderabdeckung bis 31.12.2026: **nicht bestätigt**

Die Änderungen wurden direkt auf `main` vorgenommen. Die aktuelle direkte Veranstalterübersicht hat bei Quellenkonflikten Vorrang vor älteren Detailseiten bzw. gecachten Suchtreffern.

## Buy-in.info-Prüfumfang

Geprüft wurden die Hauptkalenderansicht, zwölf direkte Veranstalter-/Clubübersichten, die STATION-Detailtabelle sowie datumsbezogene Suchindex-Ausschnitte für 26.–29.11.2026.

### Ansichtszeilen

| Ansicht | Rohzeilen | Cash Games | geschlossene Platzhalter | gültige Turnierlistings |
|---|---:|---:|---:|---:|
| Hauptkalender, 22.11.–erste Zeile 28.11. | 73 | 1 | 1 | 71 |
| 12 Veranstalter-/Clubübersichten | 286 | 8 | 5 | 273 |
| STATION, Airfield und HSOP – ergänzende Detail-/Suchansichten | 17 | 0 | 0 | 17 |
| **Gesamt** | **376** | **9** | **6** | **361** |

Die 71 gültigen Hauptkalender-Zeilen überschneiden sich mit den Veranstalter-/Detailansichten. Daraus ergeben sich:

- Gültige Listing-Vorkommen: **361**
- Überschneidungen: **71**
- Eindeutige aktuelle Turniere: **290**
- Im Datenbestand vorhanden: **290/290**

Die 100 sichtbaren Hauptkalenderzeilen reichen insgesamt vom 20.11. bis zum ersten Eintrag am 28.11.2026. Davon liegen 73 Zeilen im Zielzeitraum ab 22.11. Die datumsbezogenen Suchindex-Snippets für 28.–29.11. wurden zur Feldkontrolle verwendet, aber nicht als zusätzliche vollständige Ansichtsseiten gezählt, um Doppelzählung zu vermeiden.

### Veranstalterübersichten – gültige zukünftige Listings

| Veranstalter | Listings |
|---|---:|
| 24Poker | 13 |
| Capital Poker Club Bern | 23 |
| House of Cards Luzern | 12 |
| Munot Poker Schaffhausen | 21 |
| Prestige Poker Dietlikon | 15 |
| Another Poker Basel | 21 |
| Pöstli Poker | 28 |
| Grand Casino Luzern | 40 |
| FOIF DRÜ Effretikon | 67 |
| AZ Poker Club Bern | 17 |
| Sports Zugerland | 10 |
| RPR/Roger's Pokerroom | 6 |
| **Zwölf Übersichten** | **273** |

Ergänzende aktuelle Buy-in.info-Detail-/Suchansichten:
- STATION Poker Club: 5
- Airfield Pokerclub Interlaken: 7
- HSOP Helvetic Series of Poker: 5

Die 8 zusätzlichen Legacy-Datensätze bei AZ (5) und Another Poker (3) sind nicht mehr in den aktuellen direkten Veranstalterübersichten enthalten. Sie wurden nicht gelöscht, da keine datierte offizielle Absage bestätigt wurde. Sie werden nicht als aktuelle Listings gezählt und bleiben mit den bestehenden Quellenkonflikt-Hinweisen dokumentiert.

## Validierte Korrekturen

### Acht Startzeiten ergänzt

Aus der aktuellen Buy-in.info-Hauptkalenderansicht:

| Datum | Veranstalter | Turnier | Start |
|---|---|---|---:|
| 28.11.2026 | 24Poker | 24-300er Kingpin Freezeout | 16:00 |
| 29.11.2026 | 24Poker | Kristinas Super Stack 150K | 15:00 |
| 28.11.2026 | FOIF DRÜ | Saturday Night 150K | 19:30 |
| 28.11.2026 | FOIF DRÜ | Time Challenge | 22:30 |
| 29.11.2026 | FOIF DRÜ | Freeroll | 14:30 |
| 29.11.2026 | FOIF DRÜ | SundayChill Deepstack | 16:00 |
| 29.11.2026 | FOIF DRÜ | Time Challenge | 18:30 |
| 29.11.2026 | Pöstli Poker | Omaha Time | 15:00 |

Alle acht Uhrzeiten stehen in konkreten datierten Kalenderlistings. Keine wurde aus einem Wochenmuster übernommen.

### Airfield – sieben Buy-in.info-Listings angeglichen

Die aktuelle Hauptkalenderansicht führt alle sieben BOPM-Termine unter **Airfield Pokerclub Interlaken**. Vier Datensätze wurden von der älteren Bezeichnung „Pokerhelden / Airfield Poker Club“ auf die aktuelle Buy-in.info-Veranstalterbezeichnung umgestellt. Vier Titel wurden an den aktuellen Hauptkalender angeglichen:

- BOPM Mainevent Flight 1A
- BOPM Mainevent Flight 1B
- BOPM Mainevent FINAL
- BOPM Closer

Die übrigen drei BOPM-Titel waren bereits korrekt. Die Veranstaltungsorteinträge „Airfield Poker Club“ bleiben erhalten.

### Zwei HSOP-Titel angeglichen

- 27.11.: „10. HSOP OPEN 1A“
- 28.11.: „10. HSOP OPEN 1B“

Die aktuelle Hauptkalenderansicht verwendet diese Titel ohne das Wort „Flight“.

### Drei AZ-Buy-ins korrigiert

Die aktuelle direkte Veranstalterübersicht https://buy-in.info/tournaments/564 listet die AZ-Championship-Termine am 28.11., 05.12. und 12.12. jeweils mit **CHF 100+20+20**.

Die numerischen `buy_in`-Werte wurden auf 100 gesetzt und die Labels auf „CHF 100 + 20 + 20“ korrigiert. Ältere Detailseiten und einzelne gecachte Filter-Suchtreffer zeigen teils CHF 120+20. Die aktuelle direkte Veranstalterübersicht hat Vorrang. Für den 12.12. nennt sie keine Startzeit; TBA bleibt bestehen.

## Ergänzende offizielle Quellen

Das offizielle Grand Casino Luzern bestätigt den Poker Circle Swiss Masters Autumn Special vom 26.–29.11.2026 sowie die Championship Week im Dezember:
- https://www.grandcasinoluzern.ch/spielen/poker-circle/poker-circle-swiss-masters
- https://www.grandcasinoluzern.ch/events

Die konkreten Buy-ins und Startzeiten der einzelnen Veranstaltungen wurden weiterhin anhand der aktuellen Buy-in.info-Listungen geführt. Keine zusätzlichen datierten Veranstaltungen wurden allein aus einem allgemeinen Serienzeitraum erzeugt.

## Datenqualität – alle neun Dateien

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
| data/09.json | 807 |
| **Gesamt** | **921** |

Prüfungen:
- JSON-Syntax: 9/9 gültig
- Doppelte IDs: 0
- Doppelte Slugs: 0
- Semantische Dubletten: 0
- Fehlende Pflichtfelder: 0
- Ungültige Datumsformate: 0
- Ungültige Zeitformate: 0
- Zukünftige Datensätze ohne Quellenhinweis: 0
- Cash Games in den Turnierdateien: 0
- Datensätze 22.11.–31.12.2026: 343

## Commits

- data/08.json – Airfield-Angaben: https://github.com/Helvetic-Poker/helveticpoker-pokerturniere/commit/45be9dd2dc1394bbae2daa819e9add495893edf8
- data/09.json – Zeiten und AZ-Buy-ins: https://github.com/Helvetic-Poker/helveticpoker-pokerturniere/commit/3f67d6fc2a89599a4f65b93dd81868c21f9e7d11

## Blocker / nicht vollständig auslesbare Bereiche

Die direkte Hauptkalenderansicht enthält 100 Zeilen und endet beim ersten Eintrag am 28.11.2026 um 13:00 Uhr. Folgende Versuche waren über den Webabruf nicht erreichbar:

- `?page=2`
- `?p=2`
- `?offset=100`
- `?start=100`
- `?date=2026-11-29`
- `?from=2026-11-29`
- `?fdate=2026-11-29`
- `?dateFrom=2026-11-29`
- `?startDate=2026-11-29`

Die aktuelle Hauptkalender-Pagination nach dem 28.11. und damit eine vollständige globale Dezemberansicht bleiben nicht auslesbar. Die Suchindex-Ausschnitte für 28.–29.11. sind hilfreich, ersetzen aber keine vollständigen Monatsseiten.

Letzte direkt sichtbare zukünftige Listung je Veranstalterübersicht:
- 24Poker: 06.12.
- Another Poker: 25.12.
- AZ Poker Club: 27.12.
- Capital Poker Club: 27.12.
- FOIF DRÜ: 31.12.
- Grand Casino Luzern: 20.12.
- House of Cards: 30.12.
- Munot Poker: 30.12.; 31.12. ist als geschlossen markiert.
- Pöstli Poker: 28.12.
- Prestige Poker: 01.12. ist als geschlossen markiert.
- RPR: 29.12.
- Sports Zugerland: 28.12.
- STATION-Detailtabelle: 30.11.
- HSOP und Airfield: aktuelle datierte Hauptkalenderlistings bis 29.11.; keine vollständige aktuelle Veranstalter-Monatsübersicht.

Diese letzten sichtbaren Termine sind keine Garantie, dass danach keine weiteren Turniere veröffentlicht werden. Eine vollständige Abdeckung bis 31.12.2026 wird ausdrücklich nicht behauptet.
