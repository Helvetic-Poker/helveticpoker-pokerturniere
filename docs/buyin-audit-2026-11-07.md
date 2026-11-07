# Buy-in.info-Abgleich – 07.11.2026

## Ergebnis

- Buy-in.info-Hauptkalender: 100 sichtbare Zeilen insgesamt; 85 Zeilen im Zukunftsfenster 07.–13.11.2026. Davon 2 Cash Games und 1 Hinweis auf einen geschlossenen Spieltag ausgeschlossen: **82 Turnierlistings**.
- Zwölf zugängliche Veranstalteransichten (auf 07.11.–31.12.2026 begrenzt): **318 Turnierlistings**.
- Rohe Listing-Vorkommen der Hauptansicht plus zwölf Veranstalteransichten: **400**.
- Überschneidungen zwischen den Ansichten: **74**.
- Eindeutige Turniere in diesen primären Ansichten: **326**. Acht davon sind nur in der Hauptansicht sichtbar (Airfield 2, STATION 2, Kartenfreunde Wynental 1, HSOP 3).
- Die separate Another-Poker-Übersicht wurde zur Konfliktauflösung herangezogen, aber nicht nochmals als zusätzliche Listing-Zeilen gezählt.

## Veranstalteransichten

| Veranstalter | Turnierlistings 07.11.–31.12. | Letzter sichtbarer Termin |
|---|---:|---|
| FOIF DRÜ EFFRETIKON | 96 | 31.12.2026 |
| 24Poker | 28 | 06.12.2026 |
| AZ Poker Club Bern | 25 | 27.12.2026 |
| Capital Poker Club Bern | 15 | 27.12.2026 |
| House of Cards Luzern | 16 | 30.12.2026 |
| Munot Poker Schaffhausen | 13 | 28.11.2026 |
| Another Poker Basel | 39 | 03.12.2026 |
| Prestige Poker Dietlikon | 14 | 16.11.2026 |
| Grand Casino Luzern | 29 | 20.12.2026 |
| Pöstli Poker | 21 | 03.12.2026 |
| Sports Zugerland | 14 | 28.12.2026 |
| RPR/Roger's Pokerroom | 8 | 29.12.2026 |
| **Summe** | **318** | |

Die Capital-Filteransicht (/calendar?forganizer=493) ist als älterer Indexstand gekennzeichnet; ein jüngerer Detailseiten-Schnipsel enthält zusätzliche „Weitere Turniere“-Zeilen. Diese sekundären Zeilen wurden nicht verwendet, um die aktuelle Filteransicht zu überschreiben. Bereits vorhandene Capital-Datensätze wurden deshalb nicht allein wegen ihrer Abwesenheit in der älteren Filteransicht gelöscht.

## Änderungen auf main

### 16 fehlende Grand-Casino-Luzern-Turniere ergänzt

Die aktuelle Buy-in.info-Veranstalteransicht für Grand Casino Luzern listet für Dezember 29 Turniere im Zukunftsfenster. 13 davon waren bereits im Bestand, 16 fehlten und wurden in `data/09.json` ergänzt:

- 10.12. 19:30 – Afterwork – CHF 100 + 20
- 11.12. 18:30 – Sat. für PCSM Main Event – CHF 125 + 25
- 12.12. 15:00 – Warm Up to PCSM – CHF 200 + 40
- 12.12. 18:30 – Sat. für PCSM Main Event – CHF 125 + 25
- 13.12. 15:00 – Super Sat. für PCSM Main Event – CHF 220 + 40
- 16.12. 13:00 – PCSM Season Ranking Freeroll – Freeroll
- 16.12. 13:05 – Flip & Go – CHF 110 + 0
- 16.12. 13:15 – Sat. für PCSM Main Event – CHF 125 + 25
- 17.12. 13:05 – Flip & Go – CHF 110 + 0
- 17.12. 13:15 – Sat. für PCSM Main Event – CHF 125 + 25
- 17.12. 15:00 – PCSM Day 1B – CHF 800 + 80
- 18.12. 13:00 – PCSM Day 1C – CHF 800 + 80
- 18.12. 16:00 – Flip & Go – CHF 110 + 0
- 18.12. 18:00 – PCSM Day 1D – CHF 800 + 80
- 19.12. 15:00 – PCSM Tag 2 – CHF 800 + 80
- 20.12. 13:00 – PCSM Finale – CHF 800 + 80

Die Buy-in.info-Filteransicht nennt keine Variante für diese Einträge; deshalb ist `variant: TBA` gesetzt. Die offizielle PCSM-Seite bestätigt die Championship Week vom 16.–20.12.2026, weist aber darauf hin, dass Details zu Struktur/Startzeiten/Buy-ins noch veröffentlicht werden. Für bereits konkret auf Buy-in.info gelistete Daten wurde Buy-in.info als Mindestquelle verwendet.

### Drei bestehende Datensätze korrigiert

1. Another Poker Basel, 09.11., 18:40: Titel/Buy-in auf „Satellite 350 Master Freezeout“, CHF 30 + 10 geändert. Quellenkonflikt: Hauptkalender und separate Veranstalterübersicht nennen diesen Eintrag; der Filter `?forganizer=226` nennt stattdessen „Hyper Turbo Satelitte - 1 Ticket garantiert“, CHF 24 + 6. Gemäss Vorrangregel wurden Hauptkalender und Veranstalterübersicht gewählt; Variante bleibt TBA.
2. Airfield, 14.11. „Bounty Hero“: Veranstalter auf „Airfield Pokerclub Interlaken“ und Buy-in auf CHF 50 + 50 + 30 korrigiert (vorheriger Bestand: Pokerhelden/Airfield, CHF 70 + 30 + 25).
3. Airfield, 15.11. „Satelitte BOPM Main Event“: Veranstalterbezeichnung auf „Airfield Pokerclub Interlaken“ korrigiert.

### Keine Dublettenbereinigung

Es wurden in diesem Lauf keine neuen semantischen Dubletten gefunden und keine bestehenden Datensätze gelöscht.

## Datenqualität nach Änderung

- Gesamtbestand: **780** Datensätze.
- Zukunftsbestand 07.11.–31.12.2026: **400** Datensätze.
- Dateien: data/01.json bis data/09.json; Anzahlen: 15, 15, 15, 15, 15, 14, 15, 11, 665.
- JSON-Syntax: 9/9 gültig.
- Doppelte IDs: 0.
- Doppelte Slugs: 0.
- Semantische Dublettengruppen (Datum/Zeit/Veranstalter/Titel): 0.
- Fehlende Pflichtfelder: 0.
- Cash Games im Turnierdatenbestand: 0.

## Nicht vollständig erreichbare Zeiträume / Blocker

Die Hauptkalenderansicht endet im auslesbaren Ausschnitt am 13.11.2026. Versuche mit `?page=2`, `?offset=100`, `?start=100`, `?date=2026-11-14` und `?datum-ab=2026-11-14` lieferten keine vollständige Folgeseite.

Die erreichbaren Veranstalteransichten enden unterschiedlich:

- FOIF DRÜ: bis 31.12. (im Zielzeitraum vollständig sichtbar).
- 24Poker: bis 06.12.; 07.–31.12. nicht auslesbar.
- AZ Poker Club: bis 27.12.; 28.–31.12. nicht auslesbar.
- Capital Poker Club: bis 27.12.; 28.–31.12. nicht auslesbar; Filterindex älter als die Hauptansicht.
- House of Cards: bis 30.12.; 31.12. nicht auslesbar.
- Munot Poker: bis 28.11.; 29.11.–31.12. nicht auslesbar.
- Another Poker: bis 03.12.; 04.–31.12. nicht auslesbar.
- Prestige Poker: bis 16.11.; 17.11.–31.12. nicht auslesbar.
- Grand Casino Luzern: bis 20.12.; 21.–31.12. nicht auslesbar.
- Pöstli Poker: bis 03.12.; 04.–31.12. nicht auslesbar.
- Sports Zugerland: bis 28.12.; 29.–31.12. nicht auslesbar.
- RPR/Roger's Pokerroom: bis 29.12.; 30.–31.12. nicht auslesbar.
- STATION, Airfield und Kartenfreunde Wynental: keine vollständige separate aktuelle Veranstalteransicht im Abruf; nur Hauptkalender-/Suchindex-Einträge.
- HSOP: keine vollständige separate aktuelle Buy-in.info-Ansicht; Hauptkalenderlistings und offizielle Veranstalterquelle vorhanden.

Es wurde in den heute geprüften Quellen keine eindeutig bestätigte offizielle Absage gefunden.

## Verwendete Quellen

- https://buy-in.info/calendar
- https://buy-in.info/tournaments/520 (FOIF DRÜ)
- https://buy-in.info/tournaments/132 (24Poker)
- https://buy-in.info/tournaments/564 (AZ Poker Club)
- https://buy-in.info/calendar?forganizer=493 (Capital Poker Club; älterer Filterindex)
- https://buy-in.info/calendar?forganizer=570 (House of Cards)
- https://buy-in.info/calendar?forganizer=558 (Munot Poker)
- https://buy-in.info/calendar?forganizer=226 (Another Poker Filter; Titelkonflikt)
- https://buy-in.info/tournaments/226 (Another Poker Veranstalterübersicht; Titelkonflikt)
- https://buy-in.info/calendar?forganizer=189 (Prestige Poker)
- https://buy-in.info/calendar?forganizer=458 (Grand Casino Luzern)
- https://buy-in.info/tournaments/554 (Pöstli Poker)
- https://buy-in.info/tournaments/553 (Sports Zugerland)
- https://buy-in.info/tournaments/540 (RPR/Roger's Pokerroom)
- https://www.grandcasinoluzern.ch/spielen/poker-circle/poker-circle-swiss-masters
