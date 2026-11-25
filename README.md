# Pokerturniere Schweiz – Helvetic Poker

Zentraler Kalender der Schweizer Pokerszene.

## Aktueller Stand
- Datenstand: 25.11.2026
- Zeitraum im Datenbestand: Oktober 2026 bis mindestens Dezember 2026
- **958 Turnierdatensätze** in 9 Turnierdateien unter `data/` (zusätzlich 2 separate Cash-Game-Dateien)
- **347 Datensätze** vom 25.11.2026 bis 31.12.2026
- Letzter Buy-in.info-Abgleich: 25.11.2026 – [Tagesaudit](docs/buyin-audit-2026-11-25.md); 91 eindeutige Turnierzeilen in der sichtbaren Hauptkalenderansicht plus vier zusätzliche, zuvor fehlende Veranstalterlistings; keine Vollständigkeitsbehauptung
- 4 fehlende Turniere aus Another Poker und Capital Poker Club ergänzt; keine bestehenden Felder korrigiert und keine Dubletten entfernt
- Direktlinks zu den jeweiligen Veranstaltern
- Filter: Heute, Morgen, Wochenende, Monat, Region, Buy-in, Variante, Turnierart, Veranstalter und Suche
- Mobile-first Darstellung

## Quellenabgleich 25.11.2026 – Buy-in.info
- Hauptkalender: 100 sichtbare Zeilen; sieben vom 24.11. sind vergangen. Vom 25.11. bis zum letzten sichtbaren Eintrag am 01.12. sind 93 Zeilen sichtbar; zwei Cash Games ausgeschlossen ergeben 91 gültige Turnierlistings. Alle 91 sind im Datenbestand vorhanden.
- Zwölf aktuelle Veranstalter-/Clubübersichten wurden zusätzlich geöffnet. Dabei wurden vier zuvor fehlende Termine entdeckt und ergänzt: Another Poker Time Poker Tournament PL Omaha 4 Card am 06.12.; Capital Poker Club X-MAS Special am 23.12.; Capital Special ULTIMATE BIG Mystery Bounty am 26.12.; Capital CPC THE GRAND Freezeout am 26.12. Fehlende Startzeiten bleiben TBA.
- Datenbestand: 958 Turnierdatensätze; 347 liegen vom 25.11. bis 31.12.2026. Alle neun JSON-Dateien sind valide; doppelte IDs, Slugs und semantische Events: 0.
- Die Hauptkalender-Paginierung nach den ersten 100 Zeilen und mehrere spätere Anbieter-/Monatsansichten bleiben unvollständig. Eine vollständige Abdeckung bis 31.12.2026 wird ausdrücklich nicht behauptet.
- Details: [Tagesaudit 25.11.2026](docs/buyin-audit-2026-11-25.md).

## Quellenabgleich 24.11.2026 – Buy-in.info
- Hauptkalender: 100 sichtbare Zeilen, davon 89 ab 24.11. bis zum ersten Eintrag am 01.12.2026. Zwölf aktuelle Veranstalterübersichten: 298 Ansichtszeilen. Insgesamt 387 Ansichtszeilen; nach Ausschluss von 10 Cash-Game-Zeilen und 5 geschlossenen Platzhaltern bleiben 372 Turnier-Listing-Vorkommen. 73 Überschneidungen ergeben **299 eindeutige aktuelle Buy-in.info-Turniere** in den erreichbaren Ansichten; alle 299 sind im Datenbestand.
- 30 fehlende Termine ergänzt (29 24Poker, 1 Prestige); 11 bestehende Datensätze quellenbasiert korrigiert (10 Startzeiten, 1 Buy-in-Label, 1 Titel). Der HSOP-Titel vom 24.11. folgt der aktuellen Buy-in.info-Hauptkalenderansicht; die abweichende offizielle HSOP-Bezeichnung ist im Audit dokumentiert. Keine Dubletten entfernt.
- Die Hauptkalender-Paginierung nach der ersten 100-Zeilen-Ansicht und mehrere Veranstalterfilter bleiben blockiert oder liefern alte Snapshots. Eine vollständige Abdeckung bis 31.12.2026 wird ausdrücklich nicht behauptet.
- Datenqualität, GitHub Actions, Pages-Artefakt und Live-Cache-Abweichungen: [Tagesaudit 24.11.2026](docs/buyin-audit-2026-11-24.md).

## Quellenabgleich 19.11.2026 – Buy-in.info und offizielle Veranstalterquellen
- Die aktuelle Buy-in.info-Hauptkalenderansicht enthält 100 Zeilen; ab 19.11. bis zum ersten Eintrag am 27.11. sind 92 Ansichtszeilen sichtbar. Davon sind 89 Turnierlistings, zwei Cash Games und ein geschlossener Prestige-Platzhalter.
- Zusätzlich wurden zwölf direkte Veranstalterübersichten sowie die STATION-Detailtabelle geprüft. Zusammen ergeben diese 296 Ansichtszeilen (12 Cash Games und ein geschlossener Prestige-Platzhalter ausgeschlossen). Zusammen mit dem Hauptkalender: **388 Ansichtszeilen**; nach Ausschluss von 14 Cash-Game-Zeilen und zwei geschlossenen Platzhaltern bleiben **372 Turnier-Listing-Vorkommen**. **83 Überschneidungen** ergeben **289 eindeutige Buy-in.info-Turniere** in den heute erreichbaren Ansichten. Alle 289 sind im Datenbestand; keine Vollständigkeitsbehauptung.
- Die Pöstli-Übersicht ist heute wieder direkt erreichbar und listet 31 konkrete Termine bis 28.12.2026. Auch RPR und STATION sind mit aktuellen datierten Übersichten erreichbar.
- Keine fehlenden Buy-in.info-Turniere in den erreichbaren Ansichten ergänzt. **14 zusätzliche datierte Veranstaltertermine** wurden ergänzend aufgenommen: zehn OVP-Turniere (01.–26.12.) aus der offiziellen OVP-Seite und deren Check-Raise-Registrierungen sowie vier RDC-Poker-Club-Turniere (21.11.–02.12.) aus datierten Veranstalterregistrierungen. Diese 14 Zusatztermine werden ausdrücklich nicht als Buy-in.info-Listings gezählt.
- Sechs bestehende Eventdatensätze wurden in Feldern korrigiert: drei OVP-Main-Event-Titel auf die aktuellen Registrierungsbezeichnungen, der AZ-Titel am 06.12. auf die aktuelle Buy-in.info-Organizerbezeichnung sowie zwei AZ-Championship-Startzeiten am 28.11. und 05.12. auf die datierte Check-Raise-Zeit 19:00. Die Buy-in-Konflikte bei AZ wurden zugunsten der aktuellen Buy-in.info-Angaben dokumentiert.
- Fünf frühere AZ-„Top Structure“-Termine (27.11., 04.12., 11.12., 18.12., 25.12.) und das Another-Poker-Satellite vom 23.11. fehlen in den aktuellen Buy-in.info-Haupt-/Organizeransichten. Sie wurden nicht blind gelöscht: frühere explizite Buy-in-Listungen bleiben mit Konflikthinweis erhalten, bis eine datierte Absage oder Bestätigung vorliegt. Sie werden nicht als aktuell sichtbare Listings gezählt.
- Konflikte: Check-Raise listet am 20.11. bei AZ „Amazing Friday Structure“ (CHF 200+30), während Buy-in.info im Hauptkalender „Top Structure 2026“ (CHF 300+40) führt; gewählt wird Buy-in.info. Für AZ Championship Serie 4 zeigt Check-Raise CHF 100+40, Buy-in.info aktuell CHF 120+20; Buy-in.info bleibt für den Buy-in maßgeblich. Am 06.12. nennt Buy-in.info „AZ 3nd ANNIVERSARY JUBILE, Hold'em“, die offizielle AZ-Seite „AZ Sunday Freezout“; der Buy-in-Titel folgt Buy-in.info, Zeit/Freezeout der datierten offiziellen AZ-Seite.
- Datenbestand nach Ergänzungen: 890 Datensätze, davon 357 vom 19.11. bis 31.12.2026. Alle neun JSON-Dateien werden nach dem Commit erneut auf Syntax, IDs, Slugs, semantische Dubletten, Pflichtfelder, Datum/Zeit und Cash Games geprüft.
- Die Hauptkalender-Pagination bleibt blockiert: die sichtbare Ansicht endet nach 100 Zeilen mit dem ersten Eintrag am 27.11.2026. Versuche mit `?page=2`, `?offset=100`, `?start=100`, Datumsparametern und direkten Organizerfiltern lieferten keine vollständige Folgeseite. Offene spätere Veranstalterzeiträume sind im Tagesaudit dokumentiert; vollständige Abdeckung bis 31.12.2026 wird nicht behauptet.

Details: [Tagesaudit 19.11.2026](docs/buyin-audit-2026-11-19.md).

**Deployment 19.11.2026:** Datencommit [cbe311c](https://github.com/Helvetic-Poker/helveticpoker-pokerturniere/commit/cbe311c0dfe3ee058f6195dbf5fbf3af233f638e), Quellenkorrektur [90fe1fa](https://github.com/Helvetic-Poker/helveticpoker-pokerturniere/commit/90fe1fab3c0c1188bfd4df9b1d880229f2e21864); Qualitätsworkflow [44484777956](https://github.com/Helvetic-Poker/helveticpoker-pokerturniere/actions/runs/44484777956) und Pages-Deploy [44484777983](https://github.com/Helvetic-Poker/helveticpoker-pokerturniere/actions/runs/44484777983) erfolgreich. Das heruntergeladene [Pages-Artefakt 14510326128](https://github.com/Helvetic-Poker/helveticpoker-pokerturniere/actions/runs/44484777983/artifacts/14510326128) enthält 890 Turnierseiten, 21 Veranstalterseiten und 9 bytegenau mit main übereinstimmende Turnier-JSON-Dateien. Live-Caches sind teilweise älter; Details stehen im Tagesaudit.

## Quellenabgleich 15.11.2026 – Buy-in.info und offizielle Veranstalterquellen
- Hauptkalender: 100 sichtbare Zeilen vom 15.11. bis 23.11.2026 (97 Turnierlistings, zwei Cash Games, ein geschlossener Prestige-Platzhalter).
- Zwölf aktuelle Veranstalterübersichten: 306 Zeilen (304 Turnierlistings plus zwei geschlossene Prestige-Platzhalter). Zusammen mit dem Hauptkalender: **406 Ansichtszeilen**; nach Ausschluss von zwei Cash Games und drei geschlossenen Platzhaltern bleiben **401 Turnier-Listing-Vorkommen**. **85 Überschneidungen** ergeben **316 eindeutige Buy-in.info-Turniere** in den erreichbaren Ansichten. Alle 316 sind im Datenbestand; keine Vollständigkeitsbehauptung.
- Zwei im Hauptkalender sichtbare, in der AZ-Veranstalterübersicht fehlende Turniere ergänzt (17.11. Dienstag Special ReBuy Monster Stack, 19:00, CHF 50+15; 19.11. AZ Win The Button!! Monster Stack, 19:00, CHF 70+20). Elf bestehende Startzeiten anhand expliziter Hauptkalenderzeilen korrigiert.
- Zwei Airfield-Datensätze beim Veranstalternamen normalisiert; Heads-up-Titel/Variante korrigiert. Der Titel des offiziellen 26.11.-Satellites wurde angepasst. Vier Munot-Quellenhinweise sowie weitere Airfield-/72-Offsuite-Provenienzen wurden aktualisiert.
- Die offizielle Pokerhelden-Turnierübersicht listet 19 datierte Termine bis 19.12.2026, darunter drei Überschneidungen mit dem Buy-in-Hauptkalender und 16 zusätzliche offizielle Einträge. Alle 19 waren nach dem Abgleich bereits im Datenbestand: die drei Airfield-Ergänzungen BOPM Opener (26.11.), Flight 1B (28.11.) und Main Event Final (29.11.) lagen in `data/08.json`; zwei 72-Offsuite-Termine lagen in `data/09.json`. Sie wurden deshalb nicht doppelt angelegt.
- Die alte Buy-in.info-Detailseite 112555 ist ein Termin vom 16.01.2026; ihre „Weitere Turniere“-Tabelle endet am 07.11.2026. Sie ist kein aktueller Airfield-Kalender und wird nicht als Nachweis für spätere Termine verwendet. Für 20./21.11. gelten die aktuellen Buy-in-Hauptkalenderzeilen; die offizielle Pokerhelden-Übersicht bestätigt sie.
- Datenbestand: 862 Datensätze, davon 378 vom 15.11.–31.12.2026 und 420 vom 12.11.–31.12.2026. Neun JSON-Dateien valide; keine doppelten IDs/Slugs/semantischen Events, keine fehlenden Pflichtfelder, ungültigen Daten/Zeiten oder Cash Games.
- Fehlende Turniere ergänzt: 2 (Buy-in-Hauptkalender). Bestehende Datensätze korrigiert: 14 (elf Startzeiten, zwei Veranstalternamen, zwei Titel und eine Variante; einzelne Datensätze enthalten mehrere Feldkorrekturen). Dubletten entfernt: 0. Quellen-/Prüfhinweise aktualisiert: 23 bestehende Datensätze.
- Die Hauptkalender-Pagination bleibt blockiert: die sichtbare Ansicht endet nach 100 Zeilen am 23.11.2026 und zeigt eine „…“-Schaltfläche. Versuche mit `?page=2`, `?offset=100` und `?start=100` sowie direkte Organizer-Filter-URLs sind über den Webabruf nicht zuverlässig zugänglich. Die offenen Veranstalterzeiträume sind im Tagesaudit dokumentiert. Vollständige Abdeckung bis 31.12.2026 wird ausdrücklich nicht behauptet.

Details: [Tagesaudit 15.11.2026](docs/buyin-audit-2026-11-15.md).

- Datencommit: [9534b84](https://github.com/Helvetic-Poker/helveticpoker-pokerturniere/commit/9534b84a04d13bb16d9d9df10cb9afcdfe098711). Datenqualität [Run 43689930371](https://github.com/Helvetic-Poker/helveticpoker-pokerturniere/actions/runs/43689930371) und Pages-Deploy [Run 43689930358](https://github.com/Helvetic-Poker/helveticpoker-pokerturniere/actions/runs/43689930358) beide SUCCESS. Das heruntergeladene Pages-Artefakt [ID 14152240679](https://github.com/Helvetic-Poker/helveticpoker-pokerturniere/actions/runs/43689930358/artifacts/14152240679) enthält 9 Turnier-JSON-Dateien, 862 Detailseiten, 20 Veranstalterseiten plus Verzeichnisindex und 931 Sitemap-URLs; alle neun JSON-Blobs stimmen bytegenau mit dem Datencommit überein.
- Artefakt-ZIP: 1'763'476 Bytes, SHA-256 `64af8d46cfa472ca5f2fb07b2d7f8e0de6a5935f97bea2491346e731933575ca`; alle 9 Daten-JSON-Blobs stimmen bytegenau mit `main` beim Datencommit überein.
- Live: AZ-Veranstalterseite und beide neuen AZ-Detailseiten sowie BOPM-Detailseiten sind direkt erreichbar und stimmen mit dem Artefakt überein. Homepage und Pokerhelden-Listenansicht zeigen teilweise ältere Crawl-/Cache-Snapshots (14.11. bzw. alter 26.12.-Jahresranking-Termin); die Artefakt- und Detailseitenprüfung ist davon getrennt. [Tagesaudit 15.11.2026](docs/buyin-audit-2026-11-15.md).

## Quellenabgleich 14.11.2026 – Buy-in.info und Veranstalterquellen
- Die aktuelle Buy-in.info-Hauptkalenderansicht enthält 100 sichtbare Zeilen vom 13.11. bis 21.11.2026. Ab 14.11. sind 85 Zeilen im Prüfzeitraum.
- Zwölf aktuelle Veranstalterübersichten enthalten zusammen 331 Zeilen; davon liegen 318 ab 14.11. im Prüfzeitraum. Die zusätzliche STATION-Detailtabelle enthält 10 konkret datierte Termine.
- Zusammen: 413 Ansichtszeilen im Zeitraum ab 14.11.; nach Ausschluss von zwei Cash-Game-Ansichtszeilen und drei geschlossenen Prestige-Platzhaltern bleiben 408 Turnier-Listing-Vorkommen. 76 Wiederholungen zwischen Ansichten ergeben 332 eindeutige Turniere in den heute erreichbaren Ansichten. Alle 332 sind im Datenbestand enthalten; das ist keine Vollständigkeitsbehauptung für den gesamten Kalender.
- 13 bestehende Datensätze korrigiert: drei AZ-Titel auf die aktuelle Schreibweise „AZ Sunday Freezout 30`000 max pot“, zehn STATION-Varianten auf Hold'em. Bei sechs STATION-Terminen wurden zuvor fehlende Startzeiten anhand der datierten aktuellen Veranstalterseiten ergänzt.
- Acht zusätzliche, datierte Veranstaltertermine ergänzt (sieben OVP, ein RPR TimePoker). Diese sind ausdrücklich Zusatzquellen und werden nicht als Buy-in.info-Listings gezählt.
- Der Bestand umfasst nun 860 Turnierdatensätze, davon 390 vom 14.11. bis 31.12.2026. Alle neun Turnier-JSON-Dateien sind gültig; doppelte IDs/Slugs/semantische Events, fehlende Pflichtfelder und ungültige Datums-/Zeitformate: 0.
- Die Hauptkalender-Pagination bleibt blockiert; die erste Ansicht endet am 21.11.2026. Mehrere Veranstalterseiten enden vor dem 31.12.2026. Eine vollständige Abdeckung bis 31.12. wird ausdrücklich nicht behauptet. Details: [Tagesaudit 14.11.2026](docs/buyin-audit-2026-11-14.md).

## Datenprinzip
- Buy-in.info ist die verbindliche Mindestquelle für Schweizer Turnierlistings.
- Konkrete Daten werden nur aus ausdrücklich datierten Kalender- oder Veranstalterquellen übernommen; Wochenmuster werden nicht hochgerechnet.
- Fehlende Startzeiten, Varianten oder Turnierarten bleiben `TBA`, solange keine datierte Quelle sie bestätigt.
- Cash Games werden nicht in den Turnierdatenbestand übernommen.
- Bei widersprüchlichen Buy-in.info-Ansichten hat die aktuelle Hauptkalender-/Veranstalterübersicht Vorrang; Abweichungen werden dokumentiert.

## Quellenabgleich 11.11.2026
- Die direkt geöffnete Hauptkalenderansicht zeigte 100 sichtbare Zeilen; 33 lagen vor dem 11.11.2026, 2 waren Cash Games. Für den Prüfzeitraum ab 11.11. blieben 65 Turnierlistings in dieser Ansicht.
- Zwölf aktuelle Veranstalterübersichten enthielten zusammen 320 ausdrücklich datierte Turnierlistings ab 11.11.2026.
- Zwischen diesen vollständigen Ansichten gab es 61 Überschneidungen: 385 Listing-Vorkommen ergeben 324 eindeutige Turniere. Zwei weitere HSOP-Termine (16./17.11.) wurden nur in aktuellen Suchindex-Snippets sichtbar und separat bestätigt; damit sind 326 eindeutige Turniere in allen heute erreichbaren Ansichten erfasst.
- Ein fehlendes RPR-TimePOKER-++-Turnier am 11.11.2026 wurde ergänzt; Another-Poker-Buy-ins/Titel, HSOP-Haupttitel, sieben FOIF-Titel, 15 House-of-Cards-Titel und ein GCL-Titel wurden nach aktueller Quelle korrigiert.
- 16 ausdrücklich in der aktuellen Hauptkalenderansicht sichtbare Startzeiten wurden von TBA auf die datierten Uhrzeiten gesetzt.
- Alle neun JSON-Dateien wurden erneut auf Syntax, doppelte IDs/Slugs, semantische Dubletten, Pflichtfelder, Uhrzeitformate und Cash Games geprüft.
- Die Hauptkalender-Pagination hinter der sichtbaren ersten Ansicht bleibt nicht vollständig auslesbar. Für HSOP, Airfield und weitere nicht separat gefilterte Anbieter ist der Zeitraum nach dem sichtbaren Hauptkalender-Ausschnitt nicht vollständig verifizierbar. Es wird keine vollständige Buy-in.info-Abdeckung bis 31.12.2026 behauptet.

Der tägliche Quellenabgleich wird fortgeführt. Ein erfolgreicher JSON-/Pages-Build ersetzt nicht die Prüfung der tatsächlich erreichbaren Buy-in.info-Monate und der öffentlichen Live-Auslieferung.

## Quellenabgleich 12.11.2026 – Pöstli-Nachtrag
- Die aktuelle Buy-in.info-Pöstli-Veranstalterübersicht wurde erneut erfolgreich abgerufen und enthält 36 konkrete Turniertermine vom 12.11. bis 28.12.2026.
- 19 zuvor fehlende Dezembertermine wurden in `data/09.json` ergänzt; fehlende Startzeiten bleiben TBA.
- Der Bestand umfasst nun 852 Datensätze, davon 410 vom 12.11. bis 31.12.2026.
- Hauptkalender-Pagination und mehrere weitere Veranstalterzeiträume bleiben eingeschränkt; eine vollständige Buy-in.info-Abdeckung bis 31.12.2026 wird nicht behauptet. Details: [Tagesaudit 12.11.2026](docs/buyin-audit-2026-11-12.md).


## Quellenabgleich 13.11.2026 – Prestige-Nachtrag und Hauptkalenderzeiten
- Die aktuelle Buy-in.info-Hauptkalenderansicht enthält 100 sichtbare Zeilen vom 13.11. bis 21.11.2026 (18:40). Davon sind 97 Turnierlistings, zwei Cash Games und ein als „Dienstag PP geschlossen“ gelisteter Prestige-Schliesstag.
- Zusätzlich wurden zwölf aktuelle Veranstalterübersichten sowie die STATION-Detailtabelle „Weitere Turniere“ geprüft. Zusammen mit dem Hauptkalender ergeben die erreichbaren Ansichten 441 Zeilen; sieben Cash-Game-/Schliesstag-Zeilen sind keine Turnierlistings. Nach 88 Überschneidungen ergeben sich 346 eindeutige Buy-in.info-Turniere in den erreichbaren Ansichten. Diese Zahl ist keine Vollständigkeitsbehauptung für den gesamten Kalender.
- In der aktuellen Prestige-Übersicht (https://buy-in.info/tournaments/189) fehlten sechs konkret gelistete Termine am 21.–23.11.2026. Alle sechs wurden in data/09.json ergänzt; vier Zeiten sind explizit im Titel enthalten, zwei nicht veröffentlichte Zeiten bleiben TBA.
- Vier bestehende Startzeiten vom 20.11.2026 wurden anhand der aktuellen Hauptkalenderzeilen korrigiert: 24Poker 19:00, FOIF Crazy Friday 19:30, Pöstli Progressiv-Bounty 20:00, FOIF Time Challenge 22:30. Der HSOP-Titel wurde auf die aktuelle Schreibweise „FREEZEOUT TURNIER“ korrigiert.
- 22 bisher fehlende Provenienznotizen für zukünftige Datensätze ergänzt: 18 mit datierten Buy-in.info-Ansichten und vier mit datierter offizieller HSOP-Quelle (diese vier werden nicht als bestätigte Buy-in.info-Listings gezählt). Keine Startzeit wurde aus einem Wochenmuster abgeleitet. Variante/Turnierart bleiben TBA, wenn sie nicht ausdrücklich aus dem konkreten Titel oder einer datierten Quelle hervorgehen.
- Der Bestand umfasst nun 852 Datensätze, davon 397 vom 13.11. bis 31.12.2026 und 410 vom 12.11. bis 31.12.2026.
- Datenqualität über alle neun Turnierdateien: keine doppelten IDs/Slugs/semantischen Events, keine fehlenden Pflichtfelder, keine ungültigen Datums-/Zeitformate, keine Cash Games in den Turnierdateien.
- Hauptkalender-Pagination bleibt blockiert: die sichtbare Ansicht endet nach 100 Zeilen; Versuche mit ?page=2, ?offset=100, ?start=100, Datums- und forganizer-Parametern konnten nicht zuverlässig als vollständige Folgeseiten abgerufen werden. Die offenen Veranstalterzeiträume sind im Tagesaudit 13.11.2026 aufgeführt.

Details: [Tagesaudit 13.11.2026](docs/buyin-audit-2026-11-13.md).


### Datenqualitätszahlen nach Filter-/Official-Source-Crosscheck (Stand 13.11.2026)
- 852 Datensätze insgesamt; 397 vom 13.11. bis 31.12.2026.
- Im Prüfzeitraum: 148 Startzeiten TBA, 129 Varianten TBA, 66 Turnierarten TBA, 2 Buy-in-Angaben TBA; alle TBA-Werte sind bewusst nicht mit unbelegten Angaben aufgefüllt.
- 0 zukünftige Datensätze ohne source_note; 9/9 Turnier-JSON-Dateien gültig; 0 doppelte IDs, Slugs oder semantische Events.


### Artefaktprüfung 13.11.2026

Der Pages-Deploy-Run [43399143080](https://github.com/Helvetic-Poker/helveticpoker-pokerturniere/actions/runs/43399143080) war erfolgreich. Das tatsächliche Artefakt (ID 14023593376) enthält 9 Turnier-JSON-Dateien mit 852 Datensätzen, 852 Turnierdetailseiten, 20 Veranstalterseiten und 921 Sitemap-URLs. Alle neun Turnier-JSON-Dateien stimmen bytegenau mit den Git-Blobs auf `main` überein. Der separate Qualitätsworkflow [43396767371](https://github.com/Helvetic-Poker/helveticpoker-pokerturniere/actions/runs/43396767371) war ebenfalls erfolgreich. Details und bekannte Kalenderblocker stehen im [Tagesaudit 13.11.2026](docs/buyin-audit-2026-11-13.md).


### Nachprüfung 14.11.2026, 08:35
- Die zwölf aktuellen Buy-in.info-Veranstalterübersichten wurden erneut direkt geöffnet: 331 Zeilen insgesamt, davon 318 ab 14.11. bis 31.12.; dazu 10 STATION-Detailzeilen und 85 Zeilen der aktuellen Hauptkalender-Suchansicht im Zeitraum. Nach Ausschluss von zwei Cash Games und drei geschlossenen Prestige-Platzhaltern ergeben sich 408 Listing-Vorkommen, 76 Überschneidungen und 332 eindeutige Turniere; alle 332 sind im Bestand enthalten.
- Ein widersprüchlicher Quellenhinweis zum Another-Poker-„Big Fish“ vom 14.11. wurde bereinigt. Hauptkalender und Veranstalterübersicht bestätigen CHF 50+20; die Turnierfelder waren bereits korrekt.
- Der zusätzliche „CPC THE GRAND“-Eintrag im sekundären Capital-Block ist durch die aktuelle Suchansicht als 26.12.2027 bestätigt und wurde nicht in den 2026-Bestand übernommen. Der GCL-PCSM-Day-1A-Eintrag 15.12. steht ebenfalls nur im sekundären Block; die aktuelle Hauptübersicht bestätigt 16.12.2026.
- Keine fehlenden Turniere ergänzt, keine Turnierfelder geändert, keine Dubletten entfernt. Details und Blocker: [Nachprüfung im Tagesaudit](docs/buyin-audit-2026-11-14.md).

- Fünf Pöstli-Startzeiten (14., 15., 16., 19. und 20.11.) wurden am 14.11. erneut in der aktuellen Hauptkalender-Suchansicht bestätigt; die bereits vorhandenen Uhrzeiten wurden mit datierten Quellenhinweisen versehen.

### Deployment- und Live-Prüfung 14.11.2026, 08:43
- Datenqualitätsworkflow [43572358508](https://github.com/Helvetic-Poker/helveticpoker-pokerturniere/actions/runs/43572358508) und Pages-Deployment [43572358527](https://github.com/Helvetic-Poker/helveticpoker-pokerturniere/actions/runs/43572358527): beide SUCCESS.
- Das tatsächlich heruntergeladene Pages-Artefakt [14103944534](https://github.com/Helvetic-Poker/helveticpoker-pokerturniere/actions/runs/43572358527/artifacts/14103944534) enthält 860 Turnierseiten, 20 Veranstalterseiten und alle neun Turnier-JSON-Dateien bytegenau wie der Datencommit `ac612a2d47bb7b19693d33201aa7e25ebf3fa8e6`; 860/860 Detailseiten und 20/20 Veranstalterzähler geprüft.
- Die Live-Veranstalterseiten Pöstli (34 kommende) und Another Poker (31 kommende) sowie die Detailseiten Pöstli Omaha PL und Another Big Fish stimmen mit dem Artefakt überein. Die Live-Homepage-Suchansicht zeigt noch einen älteren Snapshot (13.11. als nächsten Termin; alte Veranstalterzähler) und wird als Cache-Abweichung behandelt.


## Nachprüfung 15.11.2026 – sieben zusätzliche AZ-Listings

- Der erneute Abgleich der aktuellen [AZ-Veranstalterübersicht](https://buy-in.info/tournaments/564) fand sieben konkrete Turniertermine, die im ersten Tagespass noch nicht im Datenbestand waren: 24.11., 26.11., 01.12., 03.12., 08.12., 10.12. und 12.12.2026. Alle sieben wurden mit den ausdrücklich gelisteten Buy-ins ergänzt; nicht veröffentlichte Startzeiten bleiben TBA.
- Die aktuelle AZ-Übersicht nennt für den 08.12. CHF 50+20; der ältere 03.11.-Detaildatensatz mit CHF 50+15 wurde nicht übertragen.
- Sechs bestehende „Monster Stack 100K, 20 min Level“-Datensätze wurden nach der gleichnamigen Buy-in.info-Detailbeschreibung von Hold'em NL mit Re-Buy als Turnierart „Rebuy“ korrigiert.
- Der aktuelle Cross-View-Abgleich umfasst 425 sichtbare Zeilen (Hauptkalender, zwölf Veranstalterübersichten und STATION-Detailtabelle), 419 Turnierlistings im Prüfzeitraum, 93 Überschneidungen und 326 eindeutige Turniere. Alle 326 sind im Datenbestand enthalten.
- Datenbestand: 869 Datensätze in neun Turnier-JSON-Dateien; 385 Datensätze vom 15.11. bis 31.12.2026. Keine doppelten IDs/Slugs/semantischen Events, keine ungültigen JSON-/Datums-/Zeitfelder, keine Cash Games in den Turnierdateien.
- [Datencommit](https://github.com/Helvetic-Poker/helveticpoker-pokerturniere/commit/813149fc14ee417d0dfecec98a84ef35f19e04d9); [Qualitätsworkflow](https://github.com/Helvetic-Poker/helveticpoker-pokerturniere/actions/runs/43691206498) und [Pages-Deploy](https://github.com/Helvetic-Poker/helveticpoker-pokerturniere/actions/runs/43691206506) SUCCESS.
- Das heruntergeladene [Pages-Artefakt 14152556167](https://github.com/Helvetic-Poker/helveticpoker-pokerturniere/actions/runs/43691206506/artifacts/14152556167) enthält 869 Turnierdetailseiten, 20 Veranstalterseiten und 938 Sitemap-URLs; alle neun Turnier-JSON-Dateien stimmen bytegenau mit dem Datencommit überein.
- Der Live-Webabruf zeigt weiterhin den alten Stand (AZ 20 statt 27 kommende Turniere; Homepage mit 14.11. als nächstem Termin). Die sieben neuen Detailseiten sind im Artefakt und in der Sitemap vorhanden, aber im Live-Webabruf nicht abrufbar. Cache-/Live-Abweichung ausdrücklich offen.
- Hauptkalender-Pagination hinter 23.11. und mehrere Veranstaltermonate bleiben nicht vollständig erreichbar; eine vollständige Abdeckung bis 31.12.2026 wird nicht behauptet.

Details: [Tagesaudit 15.11.2026 – Nachprüfung](docs/buyin-audit-2026-11-15-followup.md).


## Tagesabgleich 20.11.2026 – Buy-in.info
- 385 Ansichtszeilen geprüft (14 Cash Games und zwei geschlossene Platzhalter ausgeschlossen), 369 Listing-Vorkommen, 87 Überschneidungen und 282 eindeutige aktuelle Turniere.
- Drei fehlende Another-Poker-Basel-Termine (11.12., 18.12., 25.12.) ergänzt; zwölf bestehende Datensätze korrigiert (neun Startzeiten, drei Titel). Keine Dubletten bereinigt.
- Neun ältere, in aktuellen Haupt-/Veranstalteransichten nicht mehr gelistete Events bleiben mit dokumentiertem Quellenkonflikt erhalten und werden nicht als aktuelle Listings gezählt.
- 893 Datensätze in neun JSON-Dateien; JSON, IDs, Slugs und semantische Dubletten über alle Dateien geprüft.
- [Qualitätsworkflow](https://github.com/Helvetic-Poker/helveticpoker-pokerturniere/actions/runs/44694292980) und [Pages-Deploy](https://github.com/Helvetic-Poker/helveticpoker-pokerturniere/actions/runs/44694293006) SUCCESS. Das heruntergeladene [Pages-Artefakt 14609901853](https://github.com/Helvetic-Poker/helveticpoker-pokerturniere/actions/runs/44694293006/artifacts/14609901853) enthält 893 Detailseiten, 21 Veranstalterseiten und 965 Sitemap-URLs.
- Die Hauptkalender-Paginierung und mehrere Veranstaltermonate bleiben offen; eine vollständige Abdeckung bis 31.12.2026 wird nicht behauptet.

Details: [Tagesaudit 20.11.2026](docs/buyin-audit-2026-11-20.md).
