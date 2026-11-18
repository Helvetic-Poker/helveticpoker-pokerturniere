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

## GitHub Actions, Pages-Artefakt und Live-Prüfung

- Datenqualitätsworkflow: [Run 44259891744](https://github.com/Helvetic-Poker/helveticpoker-pokerturniere/actions/runs/44259891744) – SUCCESS. Das Workflow-Log meldet 9 Turnier-JSON-Dateien und 876 Einträge, keine Auffälligkeiten nach den Basisregeln.
- Pages-Deployment: [Run 44259891800](https://github.com/Helvetic-Poker/helveticpoker-pokerturniere/actions/runs/44259891800) – SUCCESS. Checkout, Pages-Setup, Seitengenerierung, Artefakt-Upload und Deployment sind jeweils erfolgreich.
- Tatsächlich heruntergeladenes Artefakt: [github-pages, Artefakt 14406863319](https://github.com/Helvetic-Poker/helveticpoker-pokerturniere/actions/runs/44259891800/artifacts/14406863319). ZIP-Größe 1.797.009 Byte; SHA-256 `6c560b0154b035df6e12d2e9c4662eaeaab6d00fdb3e12ca0879df9d8481fb42`.
- Das ZIP enthält `artifact.tar`; nach Entpacken: 9 Turnier-JSON-Dateien mit 876 Datensätzen, 876 Turnierdetailseiten und 949 HTML-Dateien insgesamt. Die zwei separaten Cash-Game-JSON-Dateien enthalten 28 Cash-Game-Datensätze und werden nicht zu Turnieren gezählt.
- Alle neun Turnier-JSON-Dateien im Artefakt wurden über ihre Git-Blob-SHAs mit dem Commit-Inhalt verglichen und stimmen bytegenau überein.
- Die Veranstalterübersicht im Artefakt enthält 20 Veranstalterkarten. Die Zähler stimmen mit den generierten Veranstalterlinks überein: 24Poker 15, 72 Offsuite 2, AZ Poker Club 26, Airfield Pokerclub 2, Another Poker 30, Capital Poker Club 26, DC Poker Club 11, FOIF DRÜ 74, Grand Casino Basel 11, Grand Casino Luzern 40, HSOP 6, House of Cards 13, Munot 8, Open Valais 8, Pokerhelden/Airfield 15, Prestige 11, Pöstli 31, RPR 7, STATION 7, Sports Zugerland 11.
- Die sieben korrigierten Detailseiten sind im Artefakt vorhanden; Datum, Startzeit und Buy-in stimmen. Insbesondere die fünf korrigierten 26.11.-Startzeiten sind im HTML korrekt gerendert.
- Live-Prüfung: Die öffentliche Veranstalterübersicht https://pokerturniere.helveticpoker.ch/veranstalter/ zeigt den Stand 18.11.2026 und 20 Veranstalterkarten mit den Artefaktzählern. Sechs der sieben korrigierten Detailseiten waren im Webabruf direkt lesbar und stimmen mit dem Artefakt überein. Die Sports-Zugerland-Detailseite lieferte beim Webabruf einen Abruffehler; sie ist im heruntergeladenen Artefakt korrekt vorhanden.
- Cache-Abweichung: Die Live-Startseite https://pokerturniere.helveticpoker.ch/ zeigt im Webabruf noch einen älteren Snapshot mit 17.11.-Terminen und abweichenden Veranstalterzählern (u.a. FOIF DRÜ 75, AZ 27, DC 12, 24Poker 17). Das ist nicht der aktuelle Deployment-Artefaktstand. Die Veranstalterübersicht und die direkt geöffneten Detailseiten sind aktuell; die Startseite wird als Cache-Abweichung dokumentiert.

Datencommit: [4fa1ffe](https://github.com/Helvetic-Poker/helveticpoker-pokerturniere/commit/4fa1ffe60d0b59ad41e2222f95ffd2fae291c060). Diese Deployment-Ergänzung ist ein reiner Audit-Dokumentationsnachtrag; die geprüften Daten und das bereits erfolgreiche Deployment bleiben unverändert.

