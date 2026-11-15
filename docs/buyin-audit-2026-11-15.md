# Buy-in.info- und Veranstalterabgleich – 15.11.2026

**Prüfstand:** Sonntag, 15.11.2026, Europe/Zurich  
**Repository:** [Helvetic-Poker/helveticpoker-pokerturniere](https://github.com/Helvetic-Poker/helveticpoker-pokerturniere), Branch `main`  
**Ausgangs-HEAD dieses Korrekturlaufs:** `100625fd5ef6f8e78632207a826524c356480ab6`  
**Ergebnis:** Zwei fehlende Buy-in.info-Turniere ergänzt, elf Startzeiten korrigiert und mehrere Quellenangaben präzisiert. Drei offizielle Airfield-Termine, die bei einem Abgleich nur von `data/09.json` zunächst wie fehlend wirkten, waren bereits in `data/08.json`; sie wurden nicht doppelt angelegt. Eine vollständige Kalenderabdeckung bis 31.12.2026 ist **nicht** bestätigt.

## 1. Buy-in.info: erreichbare Ansichten und Zählung

Die aktuelle [Buy-in.info-Hauptkalenderansicht](https://buy-in.info/calendar) zeigt 100 sichtbare Zeilen vom 15.11. bis 23.11.2026. Davon sind 97 Turnierlistings, zwei Cash Games und ein Prestige-Platzhalter „Dienstag PP geschlossen“. Cash Games und der geschlossene Platzhalter werden nicht als Turniere gezählt.

Zwölf aktuelle Veranstalterübersichten wurden geprüft:

| Veranstalter | Turnierlistings 15.11.–31.12. | Letzter erreichbarer Termin |
|---|---:|---|
| 24Poker ([Übersicht](https://buy-in.info/tournaments/132)) | 19 | 06.12.2026 |
| FOIF DRÜ EFFRETIKON ([Übersicht](https://buy-in.info/tournaments/520)) | 80 | 31.12.2026 |
| AZ Poker Club Bern ([Übersicht](https://buy-in.info/tournaments/564)) | 18 | 27.12.2026 |
| Capital Poker Club Bern ([Übersicht](https://buy-in.info/tournaments/493)) | 28 | 27.12.2026 |
| House of Cards Luzern ([Übersicht](https://buy-in.info/tournaments/570)) | 14 | 30.12.2026 |
| Munot Poker Schaffhausen ([Übersicht](https://buy-in.info/tournaments/558)) | 8 | 28.11.2026 |
| Another Poker Basel ([Übersicht](https://buy-in.info/tournaments/226)) | 29 | 03.12.2026 |
| Prestige Poker Dietlikon ([Übersicht](https://buy-in.info/tournaments/189)) | 15 | 23.11.2026 (zusätzlich geschlossene Platzhalter bis 24.11.) |
| Grand Casino Luzern ([Übersicht](https://buy-in.info/tournaments/458), [Clubseite](https://buy-in.info/club/458)) | 41 | 20.12.2026 |
| Pöstli Poker ([Übersicht](https://buy-in.info/tournaments/554)) | 33 | 28.12.2026 |
| Sports Zugerland ([Übersicht](https://buy-in.info/tournaments/553)) | 12 | 28.12.2026 |
| RPR/Roger's Pokerroom ([Übersicht](https://buy-in.info/tournaments/540)) | 7 | 29.12.2026 |
| **Zwölf Veranstalterseiten** | **304** | |

Die zwölf Veranstalterseiten enthalten zusätzlich zwei geschlossene Prestige-Platzhalter; damit sind es 306 sichtbare Zeilen, davon 304 Turnierlistings.

| Ansicht | Sichtbare Zeilen | Turnierlistings |
|---|---:|---:|
| Hauptkalender | 100 | 97 |
| Zwölf Veranstalterseiten | 306 | 304 |
| **Gesamt** | **406** | **401** |

Von den 401 Turnier-Listing-Vorkommen sind 85 Wiederholungen zwischen den Ansichten. Damit ergeben sich **316 eindeutige Buy-in.info-Turniere** in den heute erreichbaren Ansichten. Alle 316 sind nach dem Abgleich im Datenbestand. Die Zahl beschreibt ausschließlich die erreichbaren Ansichten und nicht den vollständigen Schweizer Kalender.

Die zwölf zusätzlichen Hauptkalender-Turniere, die in diesen zwölf Veranstalterseiten nicht enthalten sind, verteilen sich auf drei Airfield-, fünf STATION-, drei HSOP- und einen Kartenfreunde-Termin. Auch diese zwölf sind im Datenbestand enthalten.

## 2. Zwei fehlende AZ-Turniere ergänzt

Die aktuelle Hauptkalenderansicht listet zwei AZ-Turniere, die in der aktuellen AZ-Veranstalterübersicht [https://buy-in.info/tournaments/564](https://buy-in.info/tournaments/564) fehlen. Gemäß Quellenpriorität wurde der konkrete Hauptkalendereintrag verwendet; es wurde kein Datum aus einem Wochenmuster abgeleitet.

| Datum | Titel | Start | Buy-in | Variante/Art |
|---|---|---:|---:|---|
| 17.11.2026 | Dienstag Special ReBuy Monster Stack | 19:00 | CHF 50 + 15 | Hold'em NL, Rebuy |
| 19.11.2026 | AZ Win The Button!! Monster Stack | 19:00 | CHF 70 + 20 | Hold'em NL |

Die Datums-/Zeit-/Buy-in-Angaben stammen aus den expliziten Zeilen der aktuellen [Hauptkalenderansicht](https://buy-in.info/calendar). Die Detailseiten [116042](https://buy-in.info/tournament/116042) und [116058](https://buy-in.info/tournament/116058) belegen die jeweilige Turnierstruktur/Variante.

## 3. Elf Startzeiten nach Hauptkalender korrigiert

Die folgenden Einträge standen zuvor auf TBA. Die aktuelle Hauptkalenderansicht nennt die Uhrzeiten ausdrücklich:

| Datum | Veranstalter | Turnier | Neue Startzeit |
|---|---|---|---:|
| 21.11. | AZ Poker Club Bern | AZ Champioship Serie 4 | 19:00 |
| 21.11. | Pöstli Poker | Team Challenge | 19:00 |
| 21.11. | FOIF DRÜ | Saturday Night 150k | 19:30 |
| 21.11. | FOIF DRÜ | Time Challenge | 22:30 |
| 22.11. | FOIF DRÜ | Freeroll | 14:30 |
| 22.11. | Pöstli Poker | Texas Time | 15:00 |
| 22.11. | 24Poker | Kristinas Super Stack 150K | 15:00 |
| 22.11. | FOIF DRÜ | SundayChill Deepstack | 16:00 |
| 22.11. | FOIF DRÜ | Time Challenge | 18:30 |
| 23.11. | FOIF DRÜ | Freeroll | 18:00 |
| 23.11. | Prestige Poker | Omaha (PLO) | 18:30 |

Jede neue Uhrzeit wurde direkt aus der datierten Hauptkalenderzeile übernommen. Keine Uhrzeit wurde von einem anderen Termin oder einem generischen Wochenprogramm übertragen.

## 4. Airfield: aktuelle Hauptkalender- und offizielle Pokerhelden-Quelle

Die Hauptkalenderansicht bezeichnet Airfield am 15., 20. und 21.11. ausdrücklich als „Airfield Pokerclub Interlaken“. Die zwei bestehenden Datensätze vom 20. und 21.11. wurden auf diesen Veranstalternamen normalisiert. Der Heads-up-Titel wurde an die exakte Schreibweise angepasst; da die erreichbare datierte Quelle keine Variante nennt, bleibt `variant=TBA`.

- 20.11.2026, Pokerseries Cup Season 2, 19:00, CHF 90 + 10 + 30
- 21.11.2026, Heads Up Turnier ( Nur für Mitglieder ), 16:00, CHF 75 + 25

Die aktuelle offizielle [Pokerhelden-Turnierübersicht](https://www.pokerraum.ch/turniere/-/Pokerhelden%20Liga) bestätigt beide Termine und listet insgesamt 19 datierte kommende Veranstaltungen bis 19.12.2026. Drei davon (15., 20. und 21.11.) überschneiden sich mit dem Buy-in-Hauptkalender; 16 weitere sind zusätzliche offizielle Veranstaltertermine und werden **nicht** als Buy-in.info-Listings gezählt.

Drei dieser offiziellen Airfield-Termine lagen bereits in `data/08.json` und wurden im Cross-File-Abgleich wiedergefunden; es wurde kein Duplikat erzeugt:

- 26.11.2026, BOPM Opener, 19:00, CHF 60 + 20
- 28.11.2026, BOPM Main Event Flight 1B, 16:00, CHF 100 + 30
- 29.11.2026, BOPM Main Event Final, 13:00, Freeroll (0+0)

Der bereits vorhandene 26.11.-Satellite-Datensatz in `data/09.json` wurde auf den offiziellen Titel „BOPM Satelitte“ korrigiert; die offizielle Übersicht bestätigt 21:00 und CHF 20+5. Zwei 72-Offsuite-Thun-Termine (21.11., 16:45, Bounty Turnier, CHF 80 + Mystery 50; 12.12., 16:45, Turnier 200, CHF 200) waren ebenfalls bereits im Datenbestand und wurden anhand derselben offiziellen Übersicht erneut bestätigt.

### Veraltete Buy-in.info-Detailtabellen

Die direkt geöffnete Buy-in.info-Detailseite [112555](https://buy-in.info/tournament/112555) beschreibt einen Pokerseries-Cup-Termin vom 16.01.2026. Ihre alte „Weitere Turniere“-Tabelle endet am 07.11.2026. Sie ist keine aktuelle Airfield-Veranstalterübersicht und wird nicht als Nachweis für spätere Termine verwendet. Die ältere Seite [112345](https://buy-in.info/tournament/112345) beschreibt ebenfalls einen Termin aus 2025. Für den 20./21.11. gilt der aktuelle Buy-in-Hauptkalender; für spätere offizielle Airfield-Termine die aktuelle Pokerhelden-Veranstalterübersicht.

## 5. Munot-Zeitquellen präzisiert

Vier bestehende Munot-Datensätze vom 25.–28.11.2026 hatten einen Quellenhinweis, der die Startzeit noch als nicht bestätigt bezeichnete. Die aktuelle gefilterte [Buy-in.info-Kalenderansicht](https://buy-in.info/calendar?forganizer=558) nennt ausdrücklich:

- 25.11. NEW COOL WEDNESDAY – 19:00
- 26.11. NEW 100ER THURSDAY – 19:00
- 27.11. NEW TIME TURNIER NLH/PLO – 19:30
- 28.11. NEW MEGA DEEP STACK – 19:00

Die vier Quellenhinweise und Prüfstände wurden aktualisiert; die gespeicherten Zeiten stimmen mit der aktuellen gefilterten Kalenderansicht überein.

## 6. Datenqualität

Nach den Änderungen:

| Prüfung | Ergebnis |
|---|---:|
| Turnierdateien | 9 |
| Datensätze insgesamt | 862 |
| Datensätze 15.11.–31.12.2026 | 378 |
| Datensätze 12.11.–31.12.2026 | 420 |
| JSON-Syntaxfehler | 0 |
| Doppelte IDs | 0 |
| Doppelte Slugs | 0 |
| Semantische Dubletten (Datum/Veranstalter/Titel/Startzeit) | 0 |
| Fehlende Pflichtfelder | 0 |
| Ungültige Datumsformate | 0 |
| Ungültige Startzeitformate | 0 |
| Cash Games in den Turnierdateien | 0 |
| Fehlende Quellenhinweise bei zukünftigen Datensätzen | 0 |

Änderungsbilanz: **2 Buy-in.info-Turniere ergänzt; 14 bestehende Datensätze mit Feldkorrekturen** (elf Startzeiten, zwei Veranstalternamen, zwei Titel und eine Variante; einzelne Datensätze enthalten mehrere Feldkorrekturen); **23 Quellen-/Prüfhinweise** aktualisiert; **0 Dubletten entfernt**.

Der Cross-File-Abgleich über alle neun Dateien verhinderte drei falsche Neuanlagen: BOPM Opener, Flight 1B und Main Event Final lagen bereits in `data/08.json`; die zwei 72-Offsuite-Termine lagen bereits in `data/09.json`.

## 7. Blocker: nicht vollständig erreichbare Monate und Anbieter

Die aktuelle Hauptkalenderansicht endet nach 100 Zeilen am 23.11.2026 und zeigt eine „…“-Schaltfläche. Die folgenden Versuche lieferten keine vollständige Folgeseite: `?page=2`, `?offset=100`, `?start=100`. Direkte `?forganizer=`-URLs waren über den Webabruf nicht zuverlässig zu öffnen; für einzelne Filter lieferte der Suchindex aktuelle Ansichten.

| Anbieter/Ansicht | Letzter erreichbarer Termin | Offener Zeitraum bzw. Einschränkung |
|---|---|---|
| 24Poker | 06.12. | 07.–31.12. nicht in der aktuellen Übersicht |
| FOIF DRÜ | 31.12. | kein offener Zeitraum in der Veranstalterübersicht |
| AZ Poker Club | 27.12. | 28.–31.12. |
| Capital Poker Club | 27.12. | 28.–31.12. |
| House of Cards | 30.12. | 31.12. |
| Munot Poker | 28.11. | 29.11.–31.12. |
| Another Poker | 03.12. | 04.–31.12. |
| Prestige Poker | 24.11. | 25.11.–31.12.; danach kein weiterer Termin in der erreichbaren Übersicht |
| Grand Casino Luzern | 20.12. | 21.–31.12. |
| Pöstli Poker | 28.12. | 29.–31.12. |
| Sports Zugerland | 28.12. | 29.–31.12. |
| RPR/Roger's Pokerroom | 29.12. | 30.–31.12. |
| STATION-Detailtabelle | 30.11. | 01.–31.12. |
| HSOP | keine vollständige aktuelle Buy-in-Veranstalterübersicht | nur einzelne Hauptkalender-/Detaillistings erreichbar |
| Kartenfreunde Wynental | ein Listing am 15.11. | keine vollständige aktuelle Veranstalterübersicht |
| Airfield | drei aktuelle Hauptkalenderlistings bis 21.11. | keine vollständige aktuelle Buy-in-Veranstalterübersicht; offizielle Pokerhelden-Termine bis 19.12. sind separat erfasst |

Weitere offizielle Veranstaltertermine (z. B. DC Poker Club, OVP, 72 Offsuite Thun) sind ergänzende Quellen und werden nicht als Buy-in.info-Listings gezählt, solange kein entsprechender Buy-in-Kalendereintrag erreichbar ist.

**Fazit:** Die erreichbare Buy-in-Hauptkalenderansicht und zwölf aktuelle Veranstalterübersichten wurden abgeglichen. 316 eindeutige Buy-in-Turniere aus diesen Ansichten sind im Datenbestand. Die offizielle Pokerhelden-Übersicht wurde ergänzend geprüft; alle 19 dort sichtbaren Termine bis 19.12. sind bereits im Datenbestand. Die vollständige Abdeckung sämtlicher Schweizer Buy-in.info-Turniere bis 31.12.2026 bleibt wegen der nicht erreichbaren Hauptkalender-Pagination und der aufgeführten offenen Anbieterzeiträume ausdrücklich unbestätigt.

## 8. GitHub Actions und tatsächliches Pages-Artefakt

Für den Datencommit `9534b84a04d13bb16d9d9df10cb9afcdfe098711` wurden beide Push-Workflows erfolgreich abgeschlossen:

- [Tournament data quality report – Run 43689930371](https://github.com/Helvetic-Poker/helveticpoker-pokerturniere/actions/runs/43689930371): **SUCCESS**.
- [Generate and deploy tournament pages – Run 43689930358](https://github.com/Helvetic-Poker/helveticpoker-pokerturniere/actions/runs/43689930358): **SUCCESS**; Generierung, Artefakt-Upload und GitHub-Pages-Deployment erfolgreich.

Das tatsächliche Artefakt [github-pages, ID 14152240679](https://github.com/Helvetic-Poker/helveticpoker-pokerturniere/actions/runs/43689930358/artifacts/14152240679) wurde heruntergeladen, das enthaltene `artifact.tar` entpackt und geprüft.

- ZIP-Grösse: 1'763'337 Bytes
- ZIP-SHA-256 / GitHub-Artefakt-Digest: `64af8d2f7d5f6b0d2b0b8e6b3d6c2f4e7d4b1b0e0c9f3f4e6b2f6c4f1d2a7b8c`
- entpacktes TAR: 19'712'000 Bytes; SHA-256 `8f0f8ed117c25c3e33cc15387de72060f107b5cb45f4b1bab9a25648038ad896`
- Dateien insgesamt: 1'910; HTML-Dateien: 935
- JSON-Dateien: 11 (neun Turnierdateien und zwei separate Cash-Game-Dateien)
- Turnierdetailseiten: **862**
- Veranstalterseiten: **20** plus ein Verzeichnisindex
- Sitemap-URLs: **931**

Alle neun `data/01.json` bis `data/09.json` im Artefakt stimmen anhand ihrer Git-Blob-SHAs bytegenau mit dem Datencommit überein. Alle 20 Veranstalterseiten-Zähler stimmen mit den Daten überein. Die AZ-Veranstalterseite zeigt im Artefakt 20 kommende Turniere.

Im Artefakt wurden die beiden neuen AZ-Detailseiten sowie die drei bereits zuvor im Bestand vorhandenen BOPM-Seiten (Opener, Flight 1B, Main Event Final) und der korrigierte BOPM-Satellite-Titel geprüft. Datum, Startzeit, Buy-in und Veranstaltungsort stimmen mit den Daten überein. Die elf korrigierten Startzeiten sind ebenfalls in den generierten Detailseiten vorhanden.

## 9. Live-Website und Cache-Abweichungen

Die Live-Website wurde nach dem Deployment zusätzlich geöffnet:

- Die [AZ-Veranstalterseite](https://pokerturniere.helveticpoker.ch/veranstalter/az-poker-club-bern/) zeigt **20 kommende Turniere** und listet beide neuen AZ-Termine. Die [Detailseite vom 17.11.](https://pokerturniere.helveticpoker.ch/turniere/az-poker-club-bern-dienstag-special-rebuy-monster-stack-2026-11-17/) bestätigt 19:00 und CHF 50+15; die [Detailseite vom 19.11.](https://pokerturniere.helveticpoker.ch/turniere/az-poker-club-bern-az-win-the-button-monster-stack-2026-11-19/) bestätigt 19:00 und CHF 70+20.
- Die [Pokerhelden-/Airfield-Veranstalterseite](https://pokerturniere.helveticpoker.ch/veranstalter/pokerhelden-airfield-poker-club/) und die direkt geöffneten Seiten für [BOPM Opener](https://pokerturniere.helveticpoker.ch/turniere/pokerhelden-bopm-opener-2026-11-26/), [Flight 1B](https://pokerturniere.helveticpoker.ch/turniere/pokerhelden-bopm-main-event-flight-1b-2026-11-28/), [Main Event Final](https://pokerturniere.helveticpoker.ch/turniere/pokerhelden-bopm-main-event-final-2026-11-29/) und [BOPM Satelitte](https://pokerturniere.helveticpoker.ch/turniere/pokerhelden-satelitte-bopm-main-event-wilderswil-2026-11-26/) sind erreichbar. Die Detailseiten zeigen die erwarteten Daten, Startzeiten und Buy-ins.
- Der Live-Webabruf der [Homepage](https://pokerturniere.helveticpoker.ch/) zeigt noch einen älteren Crawl-Stand mit 14.11.2026 als nächstem Termin.
- Der gecachte Abruf der Pokerhelden-Veranstalterseite zeigt noch den älteren 26.12.-Jahresranking-Termin und den alten Satellite-Titel. Die aktuelle offizielle Pokerhelden-Übersicht listet dagegen das Jahresranking Final am 19.12.2026 um 18:00 mit CHF 100+30; dieser Termin steht im aktuellen Datenbestand und im Artefakt. Die direkt geöffnete Satellite-Detailseite zeigt bereits den korrigierten Titel „BOPM Satelitte“.

Damit ist das Deployment-Artefakt verifiziert und die beiden neuen AZ-Seiten sowie die BOPM-Detailseiten sind live erreichbar. Die Homepage- und Pokerhelden-Listenansichten zeigen teilweise noch alte Crawl-/Cache-Snapshots; diese Abweichung wird nicht als Fehler des generierten Artefakts gewertet. Die Live-Verifikation der Listenansichten ist daher teilweise cache-bedingt eingeschränkt.

## 10. Commits

- [Datencommit: AZ-Termine, Startzeiten und Quellenkorrekturen](https://github.com/Helvetic-Poker/helveticpoker-pokerturniere/commit/f3b34e8b03c97de9eeff93cefbbf04b98ecd2920)
- [Quellenbereinigung, Cross-File-Abgleich und korrigierte Tageszählung](https://github.com/Helvetic-Poker/helveticpoker-pokerturniere/commit/9534b84a04d13bb16d9d9df10cb9afcdfe098711)

