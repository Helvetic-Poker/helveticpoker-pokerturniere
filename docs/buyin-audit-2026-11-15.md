# Buy-in.info- und Veranstalterabgleich – 15.11.2026

**Prüfstand:** Sonntag, 15.11.2026, 08:06 Europe/Zurich  
**Repository:** [Helvetic-Poker/helveticpoker-pokerturniere](https://github.com/Helvetic-Poker/helveticpoker-pokerturniere), Branch `main`  
**Ausgangs-HEAD:** `a286f4463be58ee4feee5438b4e293da32c7f594`  
**Ergebnis:** Zwei fehlende AZ-Turniere ergänzt, elf explizite Startzeiten korrigiert und mehrere Quellenangaben bereinigt. Alle 328 eindeutigen Turniere aus den heute erreichbaren Buy-in.info-Ansichten sind nach dem Abgleich im Datenbestand. Eine vollständige Kalenderabdeckung bis 31.12.2026 ist **nicht** bestätigt.

## 1. Prüfumfang und Zählung

Die aktuelle [Buy-in.info-Hauptkalenderansicht](https://buy-in.info/calendar) enthält 100 sichtbare Zeilen vom 15.11. bis 23.11.2026 (L4–L103). Davon sind 97 Turnierlistings, zwei Cash Games und ein Prestige-Platzhalter „Dienstag PP geschlossen“. Cash Games und der geschlossene Platzhalter wurden nicht als Turniere gezählt.

Zwölf aktuelle Veranstalterübersichten wurden geöffnet und gegen alle neun `data/*.json`-Dateien geprüft:

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

Die Prestige-Seite enthält zusätzlich zwei geschlossene Platzhalter; damit umfassen die zwölf Veranstalterseiten 306 sichtbare Zeilen, davon 304 Turnierlistings.

Zusätzlich wurde die aktuelle [Airfield-/Pokerhelden-Buy-in-Detailseite](https://buy-in.info/tournament/112345) geprüft. Sie listet 15 konkrete Turniertermine vom 15.11. bis 18.12.2026. Die aktuelle Hauptkalenderansicht überschneidet sich mit drei dieser Airfield-Termine.

| Ansicht | Sichtbare Zeilen | Davon Turnierlistings |
|---|---:|---:|
| Hauptkalender | 100 | 97 |
| Zwölf Veranstalterseiten | 306 | 304 |
| Airfield-Detailseite | 15 | 15 |
| **Gesamt** | **421** | **416** |

Von den 416 Turnier-Listing-Vorkommen sind 88 Wiederholungen zwischen den Ansichten. Damit ergeben sich **328 eindeutige Turniere** in den heute erreichbaren Ansichten. Alle 328 sind nach dem Abgleich im Datenbestand. Die Zahl beschreibt nur die erreichbaren Ansichten, nicht den vollständigen Schweizer Kalender.

Die neun zusätzlichen Hauptkalender-Turniere ohne passende der zwölf Veranstalterseiten bzw. Airfield-Detailseite betreffen die dort sichtbaren STATION-, HSOP- und Kartenfreunde-Termine. Sie wurden ebenfalls im Datenbestand abgeglichen.

## 2. Zwei fehlende AZ-Turniere ergänzt

Die aktuelle Hauptkalenderansicht listet zwei AZ-Turniere, die in der aktuellen AZ-Veranstalterübersicht [https://buy-in.info/tournaments/564](https://buy-in.info/tournaments/564) nicht enthalten sind. Gemäß Quellenpriorität wurde der konkrete Hauptkalendereintrag verwendet; es wurde kein Datum aus einem Wochenmuster abgeleitet.

| Datum | Titel | Start | Buy-in | Quelle für Variante/Art |
|---|---|---:|---:|---|
| 17.11.2026 | Dienstag Special ReBuy Monster Stack | 19:00 | CHF 50 + 15 | [Buy-in-Detailseite 116042](https://buy-in.info/tournament/116042): Hold'em NL, Rebuy |
| 19.11.2026 | AZ Win The Button!! Monster Stack | 19:00 | CHF 70 + 20 | [Buy-in-Detailseite 116058](https://buy-in.info/tournament/116058): Hold'em NL |

Beide Datums-/Zeit-/Buy-in-Angaben stammen aus den expliziten Zeilen der aktuellen [Hauptkalenderansicht](https://buy-in.info/calendar). Die Detailseiten liefern nur die Turnierstruktur/Variante der gleichnamigen Formate. Beide Datensätze wurden in `data/09.json` angelegt, mit Veranstaltungsort AZ Poker Club Bern, Zentweg 19, 3006 Bern.

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

Jede neue Uhrzeit ist direkt aus der datierten Hauptkalenderzeile übernommen. Keine Uhrzeit wurde von einem anderen Termin oder einem generischen Wochenprogramm übertragen.

## 4. Airfield-Veranstaltername und Variantenangabe

Die Hauptkalenderansicht bezeichnet Airfield am 20.11. und 21.11. ausdrücklich als „Airfield Pokerclub Interlaken“. Zwei bereits vorhandene Datensätze führten stattdessen „Pokerhelden / Airfield Poker Club“:

- 20.11.2026, Pokerseries Cup Season 2, 19:00, CHF 90 + 10 + 30
- 21.11.2026, Heads Up Turnier ( Nur für Mitglieder ), 16:00, CHF 75 + 25

Der Veranstaltername wurde auf die aktuelle Hauptkalenderbezeichnung geändert; der Heads-up-Titel wurde an die exakte aktuelle Schreibweise angepasst. Für das Heads-up-Turnier nennt die erreichbare datierte Quelle keine Variante. `variant` steht deshalb nun auf TBA; `event_type` bleibt „Heads Up“, da dies ausdrücklich im Titel steht. Die Pokerseries-Cup-Variante Hold'em NL ist durch die [Buy-in-Detailseite des gleichnamigen Formats](https://buy-in.info/tournament/112194) belegt.

## 5. Munot-Zeitquellen präzisiert

Vier bestehende Munot-Datensätze vom 25.–28.11.2026 hatten einen Quellenhinweis, der die Startzeit noch als nicht bestätigt bezeichnete. Die aktuelle gefilterte [Buy-in.info-Kalenderansicht](https://buy-in.info/calendar?forganizer=558) nennt ausdrücklich:

- 25.11. NEW COOL WEDNESDAY – 19:00
- 26.11. NEW 100ER THURSDAY – 19:00
- 27.11. NEW TIME TURNIER NLH/PLO – 19:30
- 28.11. NEW MEGA DEEP STACK – 19:00

Die vier Quellenhinweise und Prüfstände wurden aktualisiert; die gespeicherten Zeiten stimmen mit der aktuellen gefilterten Kalenderansicht überein.

## 6. Weitere Quellen und Konflikte

- Die aktuelle [AZ-Veranstalterübersicht](https://buy-in.info/tournaments/564) enthält die zwei am 17. und 19.11. im Hauptkalender gelisteten AZ-Termine nicht. Gewählt wurde die aktuelle Hauptkalenderansicht; beide Einträge sind dokumentiert.
- Die aktuellen gefilterten Kalender-Suchansichten für [Another Poker](https://buy-in.info/calendar?forganizer=226), [Capital Poker Club](https://buy-in.info/calendar?forganizer=493), [Munot Poker](https://buy-in.info/calendar?forganizer=558) und [House of Cards](https://buy-in.info/calendar?forganizer=570) bestätigen die in den Daten gespeicherten datierten Startzeiten.
- Die offizielle [AZ-Poker-Club-Seite](https://azpoker.club/) wurde ergänzend geprüft. Sie bestätigt Standort und wiederkehrende Turnierformate, ersetzt aber keine datierte Buy-in-Kalenderzeile für die beiden neu ergänzten Termine.
- Es wurde keine neue eindeutig bestätigte Turnierabsage festgestellt. Cash Games und geschlossene Spieltage wurden ausgeschlossen.

## 7. Datenqualität

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

Änderungsbilanz: **2 fehlende Turniere ergänzt; 13 bestehende Datensätze mit Feldkorrekturen (11 Startzeiten, zwei Veranstalternamen, ein Titel, eine Variante; einzelne Datensätze enthalten mehrere Feldkorrekturen); 4 weitere Munot-Quellenhinweise aktualisiert; 0 Dubletten entfernt.**

## 8. Blocker: nicht vollständig erreichbare Monate und Anbieter

Die aktuelle Hauptkalenderansicht endet nach 100 Zeilen am 23.11.2026 und zeigt eine „…“-Schaltfläche. Die folgenden Versuche lieferten keine vollständige Folgeseite: `?page=2`, `?offset=100`, `?start=100`. Direkte `?forganizer=`-URLs waren über den Webabruf nicht zuverlässig zu öffnen; für einzelne Filter lieferte der Suchindex jedoch aktuelle Ansichten.

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
| Airfield-Detailseite | 18.12. | 19.–31.12. |
| STATION-Detailtabelle | 30.11. | 01.–31.12. |
| HSOP | keine vollständige aktuelle Buy-in-Veranstalterübersicht | nur einzelne Hauptkalender-/Detaillistings erreichbar |
| Kartenfreunde Wynental | ein Listing am 15.11. | keine vollständige aktuelle Veranstalterübersicht |

Weitere offizielle Veranstaltertermine im Repository (z. B. DC Poker Club, OVP, 72 Offsuite Thun) sind ergänzende Quellen und werden nicht als Buy-in.info-Listings gezählt, solange kein entsprechender Buy-in-Kalendereintrag erreichbar ist.

**Fazit:** Der sichtbare Hauptkalender und die 13 erreichbaren Veranstalter-/Detailansichten wurden abgeglichen. Zwei fehlende AZ-Turniere sind ergänzt, elf belegte Startzeiten korrigiert und alle 328 eindeutigen Turniere aus diesen Ansichten sind im Datenbestand. Die vollständige Abdeckung aller Schweizer Buy-in.info-Turniere bis 31.12.2026 bleibt wegen der nicht erreichbaren Hauptkalender-Pagination und der aufgeführten offenen Anbieterzeiträume ausdrücklich unbestätigt.
