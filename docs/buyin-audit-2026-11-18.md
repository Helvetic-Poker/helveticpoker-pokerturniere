# Buy-in.info-Abgleich – 18. November 2026

## Ergebnis und Umfang

Der Abgleich erfolgte gegen die aktuelle Hauptkalenderansicht und die heute erreichbaren Veranstalterübersichten. Die Hauptkalenderansicht liefert 100 sichtbare Zeilen vom 18.11.2026 bis zum ersten Eintrag am 27.11.2026. Darin sind 2 Cash-Game-Zeilen und 1 geschlossener Platzhalter; verbleiben 97 Turnierlistings.

Elf Veranstalterübersichten waren heute in einer aktuellen Ansicht auslesbar. Ihre Ansichtszeilen:

| Veranstalter | Zeilen |
|---|---:|
| Another Poker Basel | 29 |
| AZ Poker Club Bern | 26 |
| Munot Poker Schaffhausen | 8 |
| FOIF DRÜ Effretikon | 74 |
| Capital Poker Club Bern | 26 |
| House of Cards Luzern | 13 |
| 24Poker | 15 |
| RPR/Roger's Pokerroom | 6 |
| Sports Zugerland | 11 |
| Prestige Poker Dietlikon | 12 |
| Grand Casino Luzern | 42 |
| **Summe** | **262** |

Die 262 Zeilen enthalten 2 Cash Games und 1 geschlossenen Platzhalter; 259 davon sind Turnierlistings. Die Pöstli-Veranstalterübersicht `https://buy-in.info/tournaments/554` lief heute wiederholt in einen Timeout. Ihre Zeilen werden deshalb nicht als aktuell vollständig ausgelesen gezählt; sieben Pöstli-Turniere sind in der sichtbaren Hauptkalenderansicht enthalten.

| Zählung | Ergebnis |
|---|---:|
| Hauptkalender-Ansichtszeilen | 100 |
| Veranstalter-Ansichtszeilen (11 erreichbare Seiten) | 262 |
| **Ansichtszeilen gesamt** | **362** |
| Cash-Game-Zeilen (in beiden Ansichten) | 4 |
| Geschlossene Platzhalter (in beiden Ansichten) | 2 |
| **Gültige Listing-Vorkommen** | **356** |
| Überschneidungen Hauptkalender ↔ erreichbare Veranstalterseiten | 80 |
| **Eindeutige Turniere in den heute vollständig vergleichbaren Ansichten** | **276** |

Alle 276 eindeutigen, heute in den auslesbaren Ansichten bestätigten Turniere sind im Datenbestand vorhanden. Die Zahl ist ausdrücklich keine Vollabdeckung des Buy-in.info-Gesamtkalenders, da insbesondere die Pöstli-Seite und die Hauptkalender-Folgeseiten nicht vollständig erreichbar waren.

## Änderungen in `data/09.json`

Keine neuen Datensätze waren aus den heute vollständig vergleichbaren Ansichten hinzuzufügen. Sieben bestehende Datensätze wurden anhand der datierten Hauptkalenderzeilen korrigiert:

1. FOIF DRÜ, 26.11.2026, Freeroll: TBA → 18:00.
2. FOIF DRÜ, 26.11.2026, Happy Thursday: TBA → 19:30.
3. Sports Zugerland, 26.11.2026, Swiss Poker Trophy: TBA → 19:30.
4. Pöstli Poker, 26.11.2026, Donschti Gämbler: TBA → 20:15.
5. AZ Poker Club, 26.11.2026, AZ Win The Button!! Monster Stack: TBA → 19:00.
6. Munot Poker, 21.11.2026: Titel von „NEW MEGA DEEP STACK 30K POT“ auf „GEBURI SPECIAL ANDY 200 BOUNTY“ korrigiert; Variante TBA, Turnierart Bounty. Die heutige Hauptkalender- und Veranstalterübersicht stimmen in dieser Bezeichnung überein.
7. Pokerhelden/Airfield, 26.11.2026: Titel auf die aktuelle Hauptkalender-Bezeichnung „Satelitte BOPM Main Event“ korrigiert; 21:00 und CHF 20+5 bleiben bestehen.

Alle fünf Uhrzeiten stammen aus ausdrücklich datierten Zeilen der aktuellen Hauptkalenderansicht, nicht aus einem Wochenmuster. Die Startzeit von Pöstli und die weiteren Felder wurden nicht aus generischen Veranstalterprogrammen abgeleitet.

### Nicht mehr gelisteter Another-Poker-Termin

Der Datensatz „Hyper Turbo Satelitte - 1 Ticket garantiert“, 23.11.2026, CHF 24+6, war in einer früheren Kalenderansicht enthalten, fehlt aber heute sowohl in der Hauptkalenderansicht als auch in der aktuellen Another-Poker-Veranstalterübersicht. Eine datierte offizielle Absage war nicht auffindbar; die offizielle Website war im Webabruf nicht erreichbar. Der Eintrag wurde deshalb nicht blind gelöscht oder als abgesagt markiert, sondern mit dem Quellenkonflikt dokumentiert und nicht zu den heutigen aktuellen Listings gezählt.

Dubletten wurden nicht bereinigt, weil bei der heutigen Prüfung keine tatsächlichen Dubletten festgestellt wurden.

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
| data/09.json | 762 |
| **Gesamt** | **876** |

Nach den Änderungen: JSON-Syntax 9/9 valide; 876 eindeutige IDs; 876 eindeutige Slugs; 0 semantische Dubletten nach Titel/Datum/Zeit/Ort/Veranstalter/Buy-in; 0 fehlende Felder title/date_start/city/organizer; 0 ungültige Datums- oder Zeitformate; 0 Cash Games in den neun Turnierdateien.

## Quellen und Abdeckungsblocker

- Hauptkalender: https://buy-in.info/calendar – heute 100 sichtbare Zeilen, Schluss am ersten Eintrag vom 27.11.2026; keine vollständige Dezemberansicht.
- Die Versuche `?page=2`, `?offset=100`, `?start=100`, `?date=2026-11-18`, `?datefrom=2026-11-18` und `?from=2026-11-18` ließen sich im Webabruf nicht laden. Die Suchindexansichten und Organizer-Filter liefern Teilmengen, aber keine vollständige zweite Kalenderseite.
- Pöstli Poker: `https://buy-in.info/tournaments/554` wiederholt Timeout; der verfügbare Suchindex-Snapshot ist drei Wochen alt und wird nicht als aktuelle vollständige Abdeckung gewertet. Der aktuelle Hauptkalender bestätigt Pöstli-Termine vom 19.11. bis 26.11.; der weitere Zeitraum bis 31.12. bleibt in dieser Prüfung offen.
- Letzte sichtbare Termine der heute erreichbaren Veranstalterübersichten: Another Poker 06.12.; AZ Poker Club 27.12.; Munot 28.11.; FOIF DRÜ 31.12.; Capital Poker Club 27.12.; House of Cards 30.12.; 24Poker 06.12.; RPR 29.12.; Sports Zugerland 28.12.; Prestige Poker 24.11.; Grand Casino Luzern 20.12. Diese Enddaten bezeichnen die letzte heute sichtbare Zeile, nicht den Beweis, dass danach keine weiteren Turniere existieren.
- Die aktuelle Main-Calendar-Sicht und die elf auslesbaren Veranstalterseiten decken den Zeitraum 18.11.–31.12. daher nicht vollständig ab. Keine Hochrechnung aus Wochenmustern wurde verwendet.

## Verwendete Buy-in.info-Quellen

- Hauptkalender: https://buy-in.info/calendar
- Another Poker Basel: https://buy-in.info/tournaments/226
- AZ Poker Club Bern: https://buy-in.info/tournaments/564
- Munot Poker Schaffhausen: https://buy-in.info/tournaments/558
- FOIF DRÜ Effretikon: https://buy-in.info/tournaments/520
- Capital Poker Club Bern: https://buy-in.info/tournaments/493
- House of Cards Luzern: https://buy-in.info/tournaments/570
- 24Poker: https://buy-in.info/tournaments/132
- RPR/Roger's Pokerroom: https://buy-in.info/tournaments/540
- Sports Zugerland: https://buy-in.info/tournaments/553
- Prestige Poker Dietlikon: https://buy-in.info/tournaments/189
- Grand Casino Luzern: https://buy-in.info/club/458
- Pöstli Poker (heute nicht vollständig abrufbar): https://buy-in.info/tournaments/554

Audit-Zeitpunkt: 18.11.2026.
