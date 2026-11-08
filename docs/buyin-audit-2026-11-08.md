# Verbindlicher Buy-in.info-Abgleich – 08.11.2026

## Ergebnis und Abdeckungsgrenze

Der Datenbestand wurde auf `main` aktualisiert. Der Abgleich ist **nicht vollständig**: Die Hauptkalender-Pagination endet im abrufbaren Stand am 16.11.2026; mehrere Veranstalteransichten enden früher als der 31.12.2026.

## Buy-in.info: gezählte Ansichten

| Ansicht | Rohe Zeilen | Turnierlistings | Letzter sichtbarer Termin |
|---|---:|---:|---|
| Hauptkalender | 100 | 97 | 16.11.2026 |
| FOIF DRÜ EFFRETIKON | 94 | 94 | 31.12.2026 |
| Pöstli Poker | 20 | 20 | 03.12.2026 |
| Munot Poker Schaffhausen | 12 | 12 | 28.11.2026 |
| Capital Poker Club Bern | 32 | 32 | 27.12.2026 |
| Grand Casino Luzern | 43 | 41 | 20.12.2026 |
| Another Poker Basel | 38 | 38 | 03.12.2026 |
| 24Poker | 25 | 25 | 06.12.2026 |
| Prestige Poker Dietlikon | 16 | 15 | 17.11.2026 |
| House of Cards Luzern | 16 | 16 | 30.12.2026 |
| Sports Zugerland | 14 | 14 | 28.12.2026 |
| RPR/Roger's Pokerroom | 8 | 8 | 29.12.2026 |
| **Summe** | **418** | **412** | |

Ausgeschlossen: 2 Cash Games in der Hauptansicht, 1 geschlossener Spieltag in der Hauptansicht, 2 Cash Games im Grand-Casino-Luzern-Filter und 1 geschlossener Spieltag im Prestige-Filter.

Nach Abgleich der Überschneidungen: **82 wiederholte Listing-Vorkommen** und **330 eindeutige Turniere** in Hauptkalender und den elf aktuellen Veranstalteransichten.

Überschneidungen zur Hauptansicht: FOIF 18, Pöstli 7, Munot 4, Capital 5, Grand Casino Luzern 2, Another Poker 17, 24Poker 8, Prestige 15, House of Cards 3, Sports Zugerland 2, RPR 1.

### Sekundäre AZ-Detailtabelle

Die Buy-in.info-Detailseite mit der Tabelle „Weitere Turniere“ für AZ Poker Club Bern enthält 20 ausdrücklich datierte Einträge bis 16.12.2026. Sechs überschneiden sich mit der Hauptansicht; 14 zusätzliche Termine wurden als sekundäre Buy-in-Quelle berücksichtigt. Die Tabelle nennt keine Startzeiten. Die 14 Termine wurden deshalb mit `TBA` gespeichert. Vier ältere Datensätze für 18.12., 23.12., 25.12. und 27.12. wurden entfernt, da sie weder in dieser datierten Tabelle noch in einer datierten offiziellen Quelle belegt waren.

Die AZ-Detailtabelle wird separat ausgewiesen und nicht in die primäre 330er-Vereinigungsmenge eingerechnet. Einschliesslich dieser Sekundärtabelle ergeben sich 432 Listing-Vorkommen und 344 eindeutige Turniere.

## Änderungen

### Fehlende Buy-in.info-Turniere ergänzt

**15 fehlende Einträge ergänzt:**
- 12 Grand-Casino-Luzern-Turniere aus dem aktuellen Filter vom 16.–20.12.2026: zusätzliche PCSM-Satellites, Crazy Pineapple, PCSM Showdown Freeroll, Bounty Hunter, Freezeout, PCSM Cup Day 1A/1B/Final Day, Ladies Event, Omaha-Satellite und Omaha.
- 3 Prestige-Einträge aus Hauptkalender und aktuellem Veranstalterkalender: Sunday Deep am 15.11. um 15:00, Sunday 50er am 15.11. um 19:00 und 125K Extra Monday am 16.11. um 19:00.

### Quellenstrenge und Korrekturen

- 12 Startzeiten vom 14.–16.11. aus der aktuellen Hauptkalenderansicht ausdrücklich übernommen.
- 33 nicht datiert belegte Startzeiten auf `TBA` gesetzt: AZ 14, Sports Zugerland 12, RPR 7. Generische Wochenprogramme und Drittanbieter-Zeitangaben wurden nicht als offizielle datierte Bestätigung verwendet.
- Für die fünf zukünftigen „Top Structure 2026“-Einträge Variante und Turnierart auf `TBA` gesetzt, weil die zugängliche Quelle diese Angaben nicht nennt.
- Capital Poker Club Bern, Ranking Final am 22.11.: Buy-in auf Freeroll korrigiert. Die aktuelle Veranstalterübersicht nennt Freeroll; ein älterer Kalenderfilter zeigt noch CHF 100+30. Die aktuelle Veranstalterübersicht hat Vorrang.
- Another Poker Basel, 14.11.: aktueller Hauptkalender und aktueller Veranstalterfilter stimmen inzwischen auf „Master Freezeout“, CHF 300+50 überein. Ein älterer Cache-Snapshot mit „300er Progressive Freezeout“ / CHF 200+100+50 wurde als veraltet dokumentiert.

### Dubletten und unbelegte Einträge

- 2 generische Grand-Casino-Luzern-Platzhalter entfernt, weil sie durch einzeln datierte Autumn-Special- bzw. PCSM-Turniere abgedeckt sind.
- 4 AZ-Termine ohne aktuellen datierten Buy-in- oder offiziellen Beleg entfernt: 18.12., 23.12., 25.12. und 27.12.2026.
- Keine doppelten IDs, Slugs oder semantischen Eventgruppen verbleiben.

### Ergänzende offizielle Quelle: Grand Casino Basel

Die offizielle Eventseite des Grand Casino Basel bestätigt das Basler Poker Festival vom 03.–06.12.2026 am Ort Metro im Grand Casino Basel. Das offizielle Fivebet-Programm enthält 11 datierte Programmstufen mit konkreten Zeiten und – soweit angegeben – Buy-ins. Diese 11 Stufen wurden ergänzend aufgenommen, obwohl sie in den heute zugänglichen Buy-in.info-Ansichten nicht als Einzelturniere gefunden wurden; sie zählen daher **nicht** zu den 330 Buy-in.info-Turnieren.

Für BOARDING Final Day (04.12., 13:00) und TAKE OFF Final Day (06.12., 14:00) nennt das Programm keinen separaten Buy-in. Beide Einträge führen deshalb `buy_in_label: TBA` und keinen erfundenen Betrag. Die zugehörigen Flight-Tage sind separat aufgeführt.

## Datenqualität

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
| data/09.json | 688 |
| **Gesamt** | **802** |

406 Datensätze liegen zwischen 08.11. und 31.12.2026; ein weiterer Datensatz liegt danach in 2027.

Prüfung aller neun Dateien:
- JSON-Syntax: 9/9 gültig
- doppelte IDs: 0
- doppelte Slugs: 0
- semantische Dubletten: 0
- fehlende erforderliche Felder: 0
- leere Startzeitfelder: 0
- Cash Games im Turnierbestand: 0

## Commits, Workflows und Artefakt

Datenänderungen:
- 12 explizite Hauptkalenderzeiten und 9 Grand-Casino-Basel-Programmtermine: https://github.com/Helvetic-Poker/helveticpoker-pokerturniere/commit/fb192cc6d4d1dc7ad1109bba684275d28fc6aab0
- AZ-Startzeit auf TBA: https://github.com/Helvetic-Poker/helveticpoker-pokerturniere/commit/a391161dd8b99980d5bd0c349d0576bc6c2d0b64
- Grand-Casino-Luzern-Platzhalter entfernt und AZ-Zeit korrigiert: https://github.com/Helvetic-Poker/helveticpoker-pokerturniere/commit/7556bb9e80b99a63312e2aef50f61011d258ca5c
- Fehlende GCL-/Prestige-Turniere, TBA-Korrekturen und Quellenkonflikte: https://github.com/Helvetic-Poker/helveticpoker-pokerturniere/commit/d959341bc37308d71a21b6f82a31a56b1bed2c07

Für den letzten Datencommit:
- Datenqualitäts-Workflow: https://github.com/Helvetic-Poker/helveticpoker-pokerturniere/actions/runs/42460839402
- Pages-Deployment: https://github.com/Helvetic-Poker/helveticpoker-pokerturniere/actions/runs/42460839476
- Pages-Artefakt: https://github.com/Helvetic-Poker/helveticpoker-pokerturniere/actions/runs/42460839476/artifacts/13608524940
- Artefakt-SHA256: `7829017cdb4f3de7c1fe5b493d73c4aa6c7f18b0c8ff241782298f000c8168ae`

Das heruntergeladene Artefakt enthält 9 Turnier-JSON-Dateien, 802 Turnierdetailseiten und 20 Veranstalterseiten. Alle neun JSON-Dateien stimmen bytegenau über ihre Git-Blob-SHAs mit `main` überein. Alle 26 in diesem Lauf neu hinzugefügten Detailseiten sind vorhanden und in der Sitemap. Alle 20 Veranstalterseiten-Zähler stimmen mit den im Artefakt enthaltenen zukünftigen Datensätzen überein. Kartenfreunde Wynental hat einen Turniereintrag, aber keine eigene Veranstalterseite.

## Live-Prüfung und Cache-Abweichung

Die Live-Startseite zeigt die neuen Top-Veranstalter-Zähler (u. a. Grand Casino Luzern 41, Another Poker 38, Capital Poker Club 32, 24Poker 25 und AZ 20) und die Termine vom 08.11.2026. Gleichzeitig meldet der dynamische Block „Heute“ noch 0 Turniere, obwohl die statische Liste heutige Termine enthält.

Die direkt verlinkte Grand-Casino-Luzern-Veranstalterseite zeigt noch 31 statt 41 Termine und enthält die inzwischen entfernten generischen Platzhalter. Die Veranstalter-Indexseite trägt noch den Aktualisierungsstand 28.10.2026 und kennt Grand Casino Basel nicht. Das ist eine nachweisbare Live-/Cache-Abweichung zum erfolgreich erzeugten Artefakt; die neuen Grand-Casino-Basel- und Detailseiten konnten über den Web-Abruf nicht direkt geöffnet werden.

## Nicht erreichbare Quellen und Zeiträume

- Hauptkalender: sichtbare 100 Zeilen enden am 16.11.2026. `?page=2`, `?offset=100`, `?start=100`, `?date=2026-11-17` und `?datum-ab=2026-11-17` lieferten keine nutzbare Folgeseite.
- 24Poker: 07.–31.12. nicht sichtbar.
- Prestige: 18.11.–31.12. nicht sichtbar.
- Munot: 29.11.–31.12. nicht sichtbar.
- House of Cards: 31.12. nicht sichtbar.
- Capital Poker Club: 28.–31.12. nicht sichtbar.
- Grand Casino Luzern: 21.–31.12. nicht sichtbar.
- Another Poker: 04.–31.12. nicht sichtbar.
- Pöstli Poker: 04.–31.12. nicht sichtbar.
- Sports Zugerland: 29.–31.12. nicht sichtbar.
- RPR: 30.–31.12. nicht sichtbar.
- AZ Poker Club: keine aktuelle Veranstalterübersicht; sekundäre Detailtabelle endet am 16.12., 17.–31.12. nicht bestätigt.
- HSOP, STATION Poker Club, Airfield Pokerclub Interlaken und Kartenfreunde Wynental: keine vollständige aktuelle Buy-in.info-Veranstalteransicht; nur einzelne Hauptkalenderzeilen bzw. ergänzende offizielle Quellen verfügbar.

Es wurde keine vollständige Abdeckung bis 31.12.2026 bestätigt. Keine Termine wurden aus wöchentlichen Mustern hochgerechnet.


### Zusätzlicher Capital-Quellenkonflikt

Die Veranstalterseite Capital Poker Club Bern enthält im sekundären Abschnitt „Weitere Turniere“ einen CPC-THE-GRAND-Termin am 26.12.2026. Dieser Termin fehlt in der aktuellen bevorstehenden Veranstalterübersicht und im aktuellen Kalenderfilter, der den 27.12. als letzten sichtbaren Termin führt. Gemäss Quellenpriorität wurde der 26.12.-Eintrag nicht übernommen; er bleibt als ungeklärter Detailtabellen-Konflikt dokumentiert.
