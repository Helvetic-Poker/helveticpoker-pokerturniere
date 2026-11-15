# Buy-in.info-Nachprüfung – 15.11.2026

**Repository:** [Helvetic-Poker/helveticpoker-pokerturniere](https://github.com/Helvetic-Poker/helveticpoker-pokerturniere), Branch `main`  
**Datencommit dieser Nachprüfung:** [`813149f`](https://github.com/Helvetic-Poker/helveticpoker-pokerturniere/commit/813149fc14ee417d0dfecec98a84ef35f19e04d9)  
**Ergebnis:** Sieben zusätzliche AZ-Turniere ergänzt; sechs bestehende AZ-Turnierarten korrigiert; sechs fehlerhafte Detailquellen-Verweise ersetzt. Der vorherige Tagespass hatte bereits zwei AZ-Turniere ergänzt und elf datierte Startzeiten korrigiert. Damit sind am 15.11. insgesamt neun AZ-Listings neu hinzugekommen und 17 bestehende Turnierfelder korrigiert worden. Keine Dubletten entfernt.

Eine vollständige Abdeckung des gesamten Schweizer Buy-in.info-Kalenders bis 31.12.2026 ist ausdrücklich **nicht** bestätigt.

## 1. Neu entdeckte AZ-Listings

Die aktuelle [AZ-Veranstalterübersicht](https://buy-in.info/tournaments/564) enthält 27 konkrete zukünftige Termine vom 17.11. bis 27.12.2026. Der erste Tagespass hatte nur 18 zukünftige Listings gezählt. Der erneute direkte Crosscheck fand sieben Termine, die in den neun Turnierdateien fehlten. Alle sieben wurden in `data/09.json` ergänzt.

| Datum | Turnier | Start | Buy-in | Variante | Turnierart |
|---|---|---:|---:|---|---|
| 24.11.2026 | Dienstag Special ReBuy Monster Stack | TBA | CHF 50 + 15 | NLH | Rebuy |
| 26.11.2026 | AZ Win The Button!! Monster Stack | TBA | CHF 70 + 20 | NLH | Regular |
| 01.12.2026 | Dienstag Special ReBuy Monster Stack | TBA | CHF 50 + 15 | NLH | Rebuy |
| 03.12.2026 | AZ Win The Button!! Monster Stack | TBA | CHF 70 + 20 | NLH | Regular |
| 08.12.2026 | Dienstag Special ReBuy Monster Stack | TBA | CHF 50 + 20 | NLH | Rebuy |
| 10.12.2026 | AZ Win The Button!! Monster Stack | TBA | CHF 70 + 20 | NLH | Regular |
| 12.12.2026 | AZ Champioship Serie 4 | TBA | CHF 120 + 20 + 20 | NLH | Regular |

**Startzeiten:** Die aktuelle Veranstalterübersicht veröffentlicht für diese sieben Termine keine Uhrzeit. Deshalb steht bei allen sieben `TBA`. Die 19:00-Uhrzeit der älteren Detailseiten vom 03.11., 05.11. oder 07.11. wurde nicht auf andere Termine übertragen.

**Quellenentscheidungen:**
- Die aktuelle Veranstalterübersicht ist für die konkreten Daten und Buy-ins maßgeblich.
- Die Detailseite [116047](https://buy-in.info/tournament/116047) beschreibt den gleichen Titel „Dienstag Special ReBuy Monster Stack“ als Hold'em NL mit Re-Buy.
- Die Detailseite [116064](https://buy-in.info/tournament/116064) beschreibt „AZ Win The Button!! Monster Stack“ als Hold'em NL.
- Die Detailseite [116985](https://buy-in.info/tournament/116985) beschreibt „AZ Champioship Serie 4“ als Hold'em NL und nennt CHF 120+20+20.
- **Gebührenkonflikt 08.12.:** Die ältere Detailseite 116047 zeigt für den 03.11. CHF 50+15. Die aktuelle AZ-Veranstalterübersicht listet den konkreten 08.12. ausdrücklich mit CHF 50+20. Eingetragen wurde CHF 50+20; kein Gebührenwert wurde vom 03.11. übernommen.
- **12.12.:** Die aktuelle Veranstalterübersicht und die Detailseite 116985 stimmen bei CHF 120+20+20 überein.

## 2. Sechs bestehende AZ-Turnierarten korrigiert

Die sechs vorhandenen Einträge „Monster Stack 100K, 20 min Level“ am 18.11., 25.11., 02.12., 09.12., 16.12. und 23.12. waren fälschlich als `Regular` klassifiziert. Die Detailseite [116506](https://buy-in.info/tournament/116506) beschreibt denselben Turniertitel ausdrücklich als Hold'em NL mit Re-Buy 70+20. Die sechs `event_type`-Werte wurden daher auf `Rebuy` korrigiert und die Quellenhinweise aktualisiert.

Die 19:00-Uhrzeit vom 18.11. bleibt erhalten, weil sie in der datierten Hauptkalenderzeile ausdrücklich steht. Für die übrigen fünf Termine bleibt die Startzeit TBA; es wurde keine Uhrzeit von einem anderen Datum übernommen. Für den 23.12. liefert die aktuelle Veranstalterübersicht das konkrete Datum; die ältere Detailseite wird nur als Beleg für die gleichnamige Turnierstruktur verwendet.

## 3. STATION-Crosscheck

Die aktuelle Buy-in.info-Detailtabelle [117909](https://buy-in.info/tournament/117909) enthält zehn STATION-Zeilen vom 14.11. bis 30.11.2026. Neun davon liegen im Prüfzeitraum ab 15.11. (15., 16., 19., 21., 22., 23., 26., 29. und 30.11.). Alle neun sind bereits in den neun JSON-Dateien enthalten; insbesondere die drei nach dem sichtbaren Hauptkalender liegenden Termine 26., 29. und 30.11. wurden nicht doppelt angelegt.

Die Detailtabelle nennt für diese zukünftigen Zeilen keine Startzeit. Die bereits gespeicherten Zeiten für 26., 29. und 30.11. stammen aus datierten STATION-Registrierungsseiten des Veranstalters, nicht aus einer Übernahme des Wochenmusters.

Die aktuelle HSOP-Detailseite [112967](https://buy-in.info/tournament/112967) zeigt nur ältere Oktobertermine in ihrer „Weitere Turniere“-Tabelle; kein zusätzlicher zukünftiger HSOP-Termin wurde daraus abgeleitet.

## 4. Zählung der erreichbaren Buy-in.info-Ansichten

| Ansicht | Sichtbare Zeilen | Turnierlistings im Prüfzeitraum |
|---|---:|---:|
| Hauptkalender | 100 | 97 |
| 12 aktuelle Veranstalterübersichten | 315 | 313 |
| STATION-Detailtabelle | 10 | 9 (eine Zeile vom 14.11. liegt vor dem Prüfzeitraum) |
| **Gesamt** | **425** | **419** |

Ausgeschlossen wurden zwei Cash Games, drei geschlossene Prestige-Platzhalter und eine STATION-Zeile vom 14.11. Die 419 Listing-Vorkommen enthalten 93 Wiederholungen zwischen den Ansichten. Damit ergeben sich **326 eindeutige Turniere** in den heute erreichbaren Ansichten. Alle 326 sind nach dieser Nachprüfung im Datenbestand enthalten.

Die 12 Veranstalterübersichten verteilen sich wie folgt (die zwei Prestige-Schliessplatzhalter sind in den sichtbaren Zeilen, nicht in den Turnierlistings enthalten):

| Veranstalter | Sichtbare Zeilen / Turnierlistings |
|---|---:|
| 24Poker | 19 |
| FOIF DRÜ EFFRETIKON | 80 |
| AZ Poker Club Bern | 27 |
| Capital Poker Club Bern | 28 |
| House of Cards Luzern | 14 |
| Munot Poker Schaffhausen | 8 |
| Another Poker Basel | 29 |
| Prestige Poker Dietlikon | 17 / 15 |
| Grand Casino Luzern | 41 |
| Pöstli Poker | 33 |
| Sports Zugerland | 12 |
| RPR/Roger's Pokerroom | 7 |
| **Gesamt** | **315 / 313** |

Die aktuelle [Hauptkalenderansicht](https://buy-in.info/calendar) endet nach 100 Zeilen am 23.11.2026. Die Versuche mit `?page=2`, `?offset=100` und `?start=100` lieferten keine vollständige Folgeseite. Einige Organizerfilter sind über Suchindex-Ergebnisse sichtbar, lassen sich aber nicht zuverlässig als vollständige Kalenderseite öffnen.

## 5. Offene Kalenderzeiträume und Blocker

| Ansicht / Veranstalter | Letzter erreichbarer Termin | Nicht vollständig erreichbarer Zeitraum |
|---|---|---|
| Hauptkalender | 23.11.2026 (100-Zeilen-Limit) | Folgeseiten ab 24.11. bis 31.12. |
| 24Poker | 06.12. | 07.–31.12. |
| FOIF DRÜ | 31.12. | kein offener Zeitraum in der aktuellen Veranstalterübersicht |
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
| HSOP | keine aktuelle vollständige Veranstalterübersicht | nur einzelne Hauptkalender-/Detailansichten |
| Airfield | drei aktuelle Hauptkalenderlistings bis 21.11. | keine vollständige aktuelle Buy-in-Veranstalterübersicht; offizielle Pokerhelden-Termine sind separat erfasst |
| Kartenfreunde Wynental | ein Listing am 15.11. | keine vollständige aktuelle Veranstalterübersicht |

Offizielle Casino-/Veranstalterquellen aus dem ersten Tagespass (Grand Casino Basel, Grand Casino Luzern und Pokerhelden/Airfield) wurden als ergänzende Quellen beibehalten. In dieser Nachprüfung ergab sich daraus kein neuer, konkret datierter zusätzlicher Buy-in.info-Eintrag und kein neuer Anbieter. Eine bestätigte Absage wurde nicht gefunden.

## 6. Datenqualität über alle neun Turnierdateien

| Datei | Datensätze |
|---|---:|
| `data/01.json` | 15 |
| `data/02.json` | 15 |
| `data/03.json` | 15 |
| `data/04.json` | 15 |
| `data/05.json` | 15 |
| `data/06.json` | 14 |
| `data/07.json` | 15 |
| `data/08.json` | 10 |
| `data/09.json` | 755 |
| **Gesamt** | **869** |

Davon liegen 385 Datensätze zwischen dem 15.11. und 31.12.2026.

- JSON-Syntax: 9/9 gültig
- Doppelte IDs: 0
- Doppelte Slugs: 0
- Semantische Dubletten (Datum/Veranstalter/Titel/Startzeit): 0
- Fehlende Pflichtfelder: 0
- Ungültige Datumsformate: 0
- Ungültige Startzeitformate: 0
- Cash Games in den neun Turnierdateien: 0
- Zukünftige Datensätze ohne Quellenhinweis: 0
- Neue AZ-Datensätze: 7, alle mit `time=TBA`
- Korrigierte AZ-Turnierarten: 6, jeweils `Regular` → `Rebuy`

Die sieben neuen Datensätze wurden mit fortlaufenden `_ord`-Werten 767–773 in `data/09.json` ergänzt. Der Cross-File-Abgleich wurde über alle neun Dateien ausgeführt.

## 7. GitHub Actions und tatsächliches Pages-Artefakt

Datencommit: [813149fc14ee417d0dfecec98a84ef35f19e04d9](https://github.com/Helvetic-Poker/helveticpoker-pokerturniere/commit/813149fc14ee417d0dfecec98a84ef35f19e04d9)

- [Tournament data quality report – Run 43691206498](https://github.com/Helvetic-Poker/helveticpoker-pokerturniere/actions/runs/43691206498): **SUCCESS**; alle Schritte einschließlich „Check tournament data“ erfolgreich.
- [Generate and deploy tournament pages – Run 43691206506](https://github.com/Helvetic-Poker/helveticpoker-pokerturniere/actions/runs/43691206506): **SUCCESS**; Generierung, Artefakt-Upload und GitHub-Pages-Deployment erfolgreich.
- Tatsächlich heruntergeladenes Artefakt: [github-pages, ID 14152556167](https://github.com/Helvetic-Poker/helveticpoker-pokerturniere/actions/runs/43691206506/artifacts/14152556167)
- ZIP-Grösse: 1'773'614 Bytes
- SHA-256 des ZIP: `d2e3b766aa082ce7c9a5198fad9b1f8a75a17547ccc70cef53dda1a79a4a0f84`
- TAR-Einträge: 1'924
- HTML-Dateien: 942
- Turnierdetailseiten: **869**
- Veranstalterseiten: **20** (plus Veranstalter-Verzeichnisindex)
- Sitemap-URLs: **938**
- JSON-Dateien: 11 (neun Turnierdateien plus zwei separate Cash-Game-Dateien)

Alle neun Turnier-JSON-Dateien im Artefakt stimmen anhand ihrer Git-Blob-SHAs bytegenau mit dem Datencommit überein. Alle 20 Veranstalterseiten-Zähler stimmen mit den zukünftigen Datensätzen überein; AZ Poker Club Bern zeigt im Artefakt **27 kommende Turniere**. Alle sieben neuen Turnierseiten sind vorhanden und in der Sitemap enthalten. Auf jeder Seite wurden Datum, TBA-Start, Buy-in und sichtbare Spielart geprüft.

## 8. Live-Website: Cache-Abweichung

Der Webabruf der [AZ-Veranstalterseite](https://pokerturniere.helveticpoker.ch/veranstalter/az-poker-club-bern/) zeigt noch **20 kommende Turniere**, während das tatsächlich heruntergeladene Artefakt **27** enthält. Der Live-Homepage-Abruf zeigt zudem weiterhin den 14.11.2026 als nächsten Termin. Die sieben neuen Detail-URLs waren über den Live-Webabruf nicht abrufbar (interner Abruffehler), obwohl alle sieben Seiten im Artefakt und in der Sitemap vorhanden sind.

Das ist eine **Live-/Crawler-/Cache-Abweichung**; sie wird nicht als Fehler des generierten Artefakts gewertet. Die Live-Veröffentlichung der sieben neuen Seiten ist damit nicht bestätigt. Der erfolgreiche Pages-Workflow und das geprüfte Artefakt sind bestätigt, die Aktualisierung des öffentlichen Cache-/Live-Abrufs bleibt offen.

## 9. Tagesbilanz

| Kennzahl | Ergebnis |
|---|---:|
| Sichtbare Ansichtszeilen | 425 |
| Listing-Vorkommen im Prüfzeitraum | 419 |
| Überschneidungen | 93 |
| Eindeutige Turniere in erreichbaren Ansichten | 326 |
| Fehlende Turniere in diesem Follow-up ergänzt | 7 |
| Fehlende Turniere am 15.11. insgesamt (inkl. erster Pass) | 9 |
| Bestehende Felder im Follow-up korrigiert | 6 Turnierarten |
| Bestehende Felder am 15.11. insgesamt (inkl. erster Pass) | 17 |
| Quellenhinweise korrigiert | 6 |
| Dubletten bereinigt | 0 |
| JSON-Dateien valide | 9/9 |
| Detailseiten im Artefakt | 869/869 |
| Veranstalterzähler im Artefakt | 20/20 |
| Qualitätsworkflow / Pages-Deploy | SUCCESS / SUCCESS |

**Fazit:** Die sieben neu entdeckten AZ-Termine sind auf `main` ergänzt, die sechs falsch klassifizierten AZ-Monster-Stack-Turniere sind auf Rebuy korrigiert, alle neun Turnierdateien sind valide und das tatsächliche Pages-Artefakt enthält alle 869 Turnierseiten. Die vollständige Abdeckung bis 31.12.2026 bleibt wegen der nicht erreichbaren Hauptkalender-Pagination und der offenen Veranstalterzeiträume ausdrücklich unbestätigt; zusätzlich ist die Live-Auslieferung der sieben neuen Seiten wegen der beobachteten Cache-Abweichung noch nicht bestätigt.
