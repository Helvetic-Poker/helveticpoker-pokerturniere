# Buy-in.info-Abgleich – 2026-11-04

## Umfang und Zählweise

- Hauptkalender: 100 sichtbare Zeilen für 04.–13.11.2026; 97 Turnierlistings, 2 Cash Games und 1 Hinweis auf einen geschlossenen Spieltag.
- Zusätzlich geprüfte Buy-in.info-Veranstalteransichten (zukünftige Zeilen): FOIF DRÜ 100, 24Poker 30, AZ Poker Club 28, Capital Poker Club 35, House of Cards 17, Munot 16, Another Poker 40, Prestige 14 (davon 13 Turniere und 1 Schliessungshinweis), Grand Casino Luzern 15 (davon 13 Turniere und 2 Cash Games), Pöstli 23, Sports Zugerland 15, RPR 8.
- Zusammen: 441 sichtbare Zeilen/Vorkommen über alle Ansichten, davon 435 Turnier-Listing-Vorkommen. Nach Abgleich von Datum, Titel, Veranstalter, Ort und Zeit ergeben sich 344 unterschiedliche Turniere in den konkret zugänglichen Ansichten; 91 Vorkommen sind Überschneidungen zwischen Hauptkalender und Veranstalteransichten.
- Eine Zeile vom 13.11.2026 ist bereits enthalten: Buy-in.info nennt „Airfield Pokerclub Interlaken“, die offizielle Pokerhelden-Seite bestätigt dasselbe „Pokerseries Cup Season 2“; Veranstalterlabel im Datensatz wurde auf die Buy-in-Bezeichnung normalisiert.

## Validierte Datenänderungen

- Vier explizit im FOIF-Organisatorenkalender gelistete Feiertagsturniere ergänzt: 24.12. Freeroll und Happy Thursday; 25.12. Crazy Friday und Time Challenge. Die Quelle nennt Datum, Titel und Buy-in, aber keine Startzeit/Variante; deshalb TBA statt Übernahme eines Wochenmusters.
- FOIF am 01.12. korrigiert: Buy-in.info listet „200er FREEZEOUT“, CHF 200+40; der alte Datensatz „300er FREEZEOUT“, CHF 300+45 wurde korrigiert.
- Fünf Easy-Monday-Termine (23.11., 30.11., 07.12., 14.12., 21.12.) entfernt: nicht im aktuellen Buy-in-Organisatorenkalender aufgeführt und keine datierte offizielle Bestätigung gefunden; ein generischer Wochenplan reicht nicht.
- Fünf AP-Championship-Datensätze (Day 1 A–D und Final Day) entfernt: sie fehlen im aktuellen Another-Poker-Kalenderfilter; die offizielle Turnierseite verweist für aktuelle Turniere auf Buy-in.info. Der ältere Organisatoren-Überblick enthält noch den Final Day, aber der neuere Kalenderfilter nicht. Keine offizielle Absage behauptet; die Termine gelten als nicht mehr aktuell bestätigt.
- Startzeiten auf TBA gesetzt, wo die zugängliche Quelle kein konkretes Datum/Zeit-Paar liefert: FOIF ab 14.11. (Organizerliste nennt Datum/Titel/Buy-in, nicht Zeit), 24Poker 14.11.–06.12. (Organizerliste ohne Zeiten), Prestige Monthly Omaha Freezeout am 16.11. (Listing ohne Zeit).
- Sports Zugerland 19:30 beibehalten: die offizielle FAQ nennt ausdrücklich den Beginn der Swiss Poker Trophy um 19:30; die konkreten Daten sind einzeln auf Buy-in.info gelistet.
- AZ Championship Serie 4: Buy-in.info-Werte beibehalten (07.11. CHF 120+20+20; 14./21./28.11. und 05.12. CHF 120+20), obwohl die Check-Raise-Ansicht CHF 100+40 zeigt. Konflikt in den Datensätzen dokumentiert; Buy-in.info ist Primärquelle.
- Capital Poker Club, Ranking Final 22.11.: aktuelle Buy-in-Organisatorenübersicht führt Freeroll; eine ältere gecachte Kalenderfilteransicht zeigte CHF 100+30. Aktuelle Organisatorenübersicht gewählt und Konflikt dokumentiert.

## Quellen

- Hauptkalender: https://buy-in.info/calendar
- FOIF: https://buy-in.info/tournaments/520
- 24Poker: https://buy-in.info/tournaments/132
- AZ Poker Club: https://buy-in.info/tournaments/564
- Capital Poker Club: https://buy-in.info/tournaments/493
- House of Cards: https://buy-in.info/tournaments/570
- Munot: https://buy-in.info/tournaments/558
- Another Poker: https://buy-in.info/calendar?forganizer=226
- Prestige: https://buy-in.info/tournaments/189
- Grand Casino Luzern: https://buy-in.info/tournaments/458
- Pöstli: https://buy-in.info/tournaments/554
- Sports Zugerland: https://buy-in.info/tournaments/553
- RPR: https://buy-in.info/tournaments/540
- Offizielle Sports-Zugerland-Zeitangabe: https://sports-zugerland.ch/sport/poker/
- Offizielle Pokerhelden-Turnierübersicht: https://www.pokerhelden.ch/turniere
- Offizielle HSOP-Turnierübersicht: https://www.hsop.ch/turnierkalender

## Blocker / nicht vollständig auslesbar

- Die Hauptkalender-Pagination nach dem sichtbaren Ausschnitt bis 13.11.2026 liefert keinen nutzbaren Folgeseiten-Link. Versuche mit `?page=2`, `?p=2`, `?offset=100`, `?start=100`, `?date=2026-11-14` und `?datum-ab=2026-11-14` ergaben keine vollständige Folgeseite.
- Die zugänglichen Veranstalterlisten enden unterschiedlich: Prestige 16.11., Munot 28.11., Another 03.12., 24Poker 06.12., Grand Casino 16.12., Pöstli 03.12., RPR 29.12., Sports 28.12., AZ/Capital 27.12., House of Cards 30.12., FOIF 31.12. Diese Listen ersetzen keine vollständige Prüfung aller übrigen Monate/Filter.
- Für HSOP, Pokerhelden/72 Offsuite und STATION war keine vollständige aktuelle Buy-in.info-Organisatorenansicht bis 31.12. erreichbar; offizielle Veranstalterseiten wurden ergänzend geprüft.
- Daher keine Behauptung vollständiger Abdeckung bis 31.12.2026.

## Qualitätsprüfung

- Alle neun `data/*.json`-Dateien werden nach dem Commit erneut validiert.
- Cash Games bleiben ausgeschlossen; keine semantischen Dubletten werden absichtlich eingeführt.
