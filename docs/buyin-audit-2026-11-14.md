# Buy-in.info- und Veranstalterabgleich – 14.11.2026

**Prüfstand:** Samstag, 14.11.2026, 08:07 Europe/Zurich  
**Repository:** [Helvetic-Poker/helveticpoker-pokerturniere](https://github.com/Helvetic-Poker/helveticpoker-pokerturniere), Branch `main`  
**Ergebnis:** Alle 332 eindeutigen Turniere aus den heute erreichbaren Buy-in.info-Ansichten sind im Datenbestand vorhanden. Zusätzlich wurden acht konkret datierte Veranstalterturniere ergänzt. Eine vollständige Abdeckung des gesamten Buy-in.info-Kalenders bis 31.12.2026 ist **nicht** bestätigt.

## 1. Buy-in.info-Prüfumfang und Zählung

Die [Hauptkalenderansicht](https://buy-in.info/calendar) lieferte 100 sichtbare Zeilen vom 13.11. bis 21.11.2026 (letzter sichtbarer Termin 21.11., 18:40). Davon liegen 85 Zeilen ab dem 14.11. im Prüfzeitraum.

Zwölf aktuelle Veranstalterübersichten wurden einzeln geöffnet und mit allen neun `data/*.json`-Dateien abgeglichen:

| Veranstalter | Ansichtszeilen gesamt | Zeilen ab 14.11. | Letzter erreichbarer Termin |
|---|---:|---:|---|
| 24Poker ([Übersicht](https://buy-in.info/tournaments/132)) | 22 | 20 | 06.12.2026 |
| FOIF DRÜ EFFRETIKON ([Übersicht](https://buy-in.info/tournaments/520)) | 85 | 82 | 31.12.2026 |
| AZ Poker Club Bern ([Übersicht](https://buy-in.info/tournaments/564)) | 20 | 19 | 27.12.2026 |
| Capital Poker Club Bern ([Übersicht](https://buy-in.info/tournaments/493)) | 30 | 29 | 27.12.2026 |
| House of Cards Luzern ([Übersicht](https://buy-in.info/tournaments/570)) | 14 | 14 | 30.12.2026 |
| Munot Poker Schaffhausen ([Übersicht](https://buy-in.info/tournaments/558)) | 10 | 9 | 28.11.2026 |
| Another Poker Basel ([Übersicht](https://buy-in.info/tournaments/226)) | 32 | 31 | 03.12.2026 |
| Prestige Poker Dietlikon ([Übersicht](https://buy-in.info/tournaments/189)) | 21 | 19 | 24.11.2026 |
| Grand Casino Luzern ([Übersicht](https://buy-in.info/club/458)) | 43 | 42 | 20.12.2026 |
| Sports Zugerland ([Übersicht](https://buy-in.info/tournaments/553)) | 12 | 12 | 28.12.2026 |
| RPR/Roger's Pokerroom ([Übersicht](https://buy-in.info/tournaments/540)) | 7 | 7 | 29.12.2026 |
| Pöstli Poker ([Übersicht](https://buy-in.info/tournaments/554)) | 35 | 34 | 28.12.2026 |
| **Summe** | **331** | **318** | |

Zusätzlich enthält die Buy-in.info-Detailseite [STATION Poker Club – Turnier 116563](https://buy-in.info/tournament/116563) zehn konkret datierte Termine vom 14.11. bis 30.11.2026. Diese Termine wurden mit der aktuellen [STATION-Veranstalterübersicht auf Check-Raise](https://check-raise.ch/de/room/station-poker-club) abgeglichen; diese aktuelle Raumübersicht zeigt dieselben zehn zukünftigen Termine mit Startzeit und Buy-in.

**Zählung im Zeitraum 14.11.–31.12.2026:**

| Kennzahl | Anzahl |
|---|---:|
| Hauptkalender-Zeilen im Zeitraum | 85 |
| Veranstalterübersichten-Zeilen im Zeitraum | 318 |
| STATION-Detailtabellen-Zeilen | 10 |
| **Ansichtszeilen insgesamt** | **413** |
| Cash-Game-Ansichtszeilen ausgeschlossen | 2 |
| Geschlossene Prestige-Platzhalter ausgeschlossen | 3 |
| **Tatsächliche Turnier-Listing-Vorkommen** | **408** |
| Wiederholte Vorkommen zwischen Ansichten | 76 |
| **Eindeutige Turniere in den erreichbaren Ansichten** | **332** |

Die zwei Cash-Game-Zeilen sind zwei Ansichten desselben Grand-Casino-Luzern-Cash-Games am 14.11. Die drei geschlossenen Platzhalter sind zwei unterschiedliche Prestige-Schliesstage, wobei der 17.11. sowohl in der Haupt- als auch in der Veranstalteransicht erscheint. Cash Games und geschlossene Spieltage werden nicht als Turniere gezählt.

**Abgleich:** Alle 332 eindeutigen Turniere aus diesen erreichbaren Buy-in.info-Ansichten sind im Datenbestand enthalten. Es wurde kein fehlendes Buy-in.info-Turnier aus diesen Ansichten entdeckt. Diese Zahl ist ausdrücklich keine Gesamtzahl aller Schweizer Buy-in.info-Turniere.

## 2. Bestehende Buy-in.info-Datensätze korrigiert

### AZ Poker Club Bern – drei Titel normalisiert

Die aktuelle [Buy-in.info-Veranstalterübersicht](https://buy-in.info/tournaments/564) und der [offizielle AZ-Kalender](https://azpoker.club/tournament/) verwenden die Schreibweise **„AZ Sunday Freezout 30`000 max pot“**. In drei vorhandenen Datensätzen stand zuvor ein Apostroph statt des auf beiden aktuellen Quellen sichtbaren Backticks.

Korrigiert wurden die Titel für:

- 22.11.2026
- 06.12.2026
- 27.12.2026

Datum, 15:00 Uhr und CHF 300 + 40 bleiben unverändert. Die Variante bleibt TBA, weil die Quellen keine Variante nennen.

### STATION Poker Club – zehn Varianten und sechs Startzeiten

Die [aktuelle STATION-Raumübersicht](https://check-raise.ch/de/room/station-poker-club) listet zehn kommende Veranstaltungen mit Datum und Uhrzeit. Die datierten Einzelseiten bestätigen für alle zehn Veranstaltungen ausdrücklich **Type Holdem**. Die Buy-in.info-Detailtabelle 116563 liefert Titel und Buy-in; die aktuelle Raumübersicht und die datierten Eventseiten ergänzen die konkreten Startzeiten und Varianten.

Alle zehn vorhandenen STATION-Datensätze wurden bei `variant` von TBA auf Hold'em aktualisiert. Sechs zuvor nicht belegte Startzeiten wurden ergänzt:

| Datum | Turnier | Startzeit |
|---|---|---:|
| 21.11.2026 | Red or Black Progr. Bounty | 19:00 |
| 22.11.2026 | Sunday Friends | 15:00 |
| 23.11.2026 | League Pro3 Team Swiss | 19:00 |
| 26.11.2026 | Super Bomb Pot Edition Add-on | 19:00 |
| 29.11.2026 | Sunday Friends | 15:00 |
| 30.11.2026 | Final League Pro3 Swiss Points- X2 | 19:00 |

Die vier bereits bekannten Startzeiten vom 14., 15., 16. und 19.11. wurden nicht verändert. Keine Uhrzeit wurde von einem anderen Termin übernommen. Für den 16.11. bestätigt die datierte Einzelseite ebenfalls Holdem; deshalb bleibt dort nicht länger TBA.

**Korrekturbilanz:** 13 vorhandene Datensätze korrigiert (drei AZ-Titel, zehn STATION-Varianten); darunter sechs wiederhergestellte Startzeiten.

## 3. Ergänzende offizielle Veranstalterquellen – acht zusätzliche Termine

Diese acht Termine sind **nicht** als Buy-in.info-Listings gezählt. Sie wurden ergänzend aufgenommen, weil die offiziellen Veranstalterseiten die Anmeldung über die jeweilige Check-Raise-Veranstalterseite verlinken und die konkreten datierten Eventseiten Datum, Uhrzeit, Buy-in und Variante nennen.

### Open Valais Poker (OVP) – sieben Termine

Die offizielle [OVP-Turnierseite](https://casino-formation.ch/tournois-ovp/) verlinkt die Anmeldung zu Check-Raise. Die datierten Veranstalterseiten führen OVP als Veranstalter und nennen Rue du Casino 4, 1907 Saxon.

| Datum | Titel | Start | Buy-in |
|---|---|---:|---:|
| 15.11.2026 | OVP Big Game 100K | 14:00 | CHF 100 + 30 |
| 17.11.2026 | K.O Progressif | 19:00 | CHF 40 + 20 + 20 |
| 19.11.2026 | OVP Décalé | 19:00 | CHF 47 + 18 |
| 20.11.2026 | OVP Switch 200 Equipe - 2 x 100 | 19:00 | CHF 80 + 20 |
| 22.11.2026 | Sat. Fiesta Poker - Lloret de Mar | 14:00 | CHF 90 + 20 |
| 26.11.2026 | OVP Décalé | 19:00 | CHF 47 + 18 |
| 28.11.2026 | OVP Regular Bounty | 18:00 | CHF 50 + 30 + 50 |

Die Variante Hold'em ist auf den datierten Veranstalterseiten angegeben. Die Turnierart wurde nur dort gesetzt, wo sie aus der konkreten Veranstaltung hervorgeht: Bounty, Team oder Satellite; andernfalls bleibt sie TBA. Beim Fiesta-Satellite ist CHF 90 + 20 das Turnier-Buy-in; der im Beschreibungstext erwähnte Paketwert von CHF 620 ist kein Buy-in.

### RPR/Roger's Pokerroom – ein Termin

Die offizielle [RPR-Website](https://rpr.poker/) verweist für Anmeldungen ausdrücklich auf Buy-in.info oder Check-Raise. Die datierte [RPR-TimePoker-Veranstaltungsseite](https://check-raise.ch/tournament/rpr-timepoker-18-11-2026) bestätigt:

- 18.11.2026, 18:30
- RPR TimePoker
- No Limit Hold'em / Shot Clock
- CHF 100 Buy-in + CHF 30 Rake
- UNIQUE Düdingen Poker & Sport Lounge, Bonnstrasse 22, 3186 Düdingen

Die allgemeine Beschreibung nennt mehrere alternative Stack-/Buy-in-Stufen, darunter 100 + 20. Gewählt wurde der spezifischere Wert aus dem datierten Abschnitt „Details“ (Buy-in 100, Rake 30) und der aktuellen Eventliste (100 + 30). Dieser Termin ist in den zugänglichen Buy-in.info-Haupt- und RPR-Veranstalteransichten nicht als eigenes Listing sichtbar und wird deshalb nicht zur Buy-in-Abdeckungszahl addiert.

## 4. Weitere Quellenkonflikte und nicht übernommene Kandidaten

- **Another Poker Basel:** Der ältere gecachte HTML-Stand zum Satellite vom 11.11. zeigte CHF 30 + 10; die aktuelle Hauptkalender-/Veranstalteransicht zeigte CHF 40 + 10. Der bereits gespeicherte aktuelle Wert CHF 40 + 10 bleibt gewählt. Der alte Wert bleibt als Quellenkonflikt dokumentiert.
- **RDC Poker Club:** Aktuelle Check-Raise-Seiten zeigen „Le big 50“ (14./21./28.11.), „Casino Master 10 Championship“ (17.11.) und „Low Cost Clash“ (18./25.11. und 02.12.). Die verlinkte offizielle Website `rueducasino.ch` war nicht erreichbar. Diese Kandidaten wurden deshalb nicht ohne zugängliche offizielle Veranstalterbestätigung ergänzt.
- **AZ Poker Club:** „AZ Win The Button“ am 19.11. und „Amazing Friday Structure“ am 20.11. erscheinen auf Check-Raise, aber nicht in der aktuellen Buy-in.info-AZ-Übersicht oder im zugänglichen offiziellen AZ-Kalender. Sie wurden nicht als bestätigte Veranstaltertermine übernommen.
- Es wurde in den zugänglichen offiziellen Quellen keine eindeutig bestätigte Absage eines aktuell gelisteten Buy-in.info-Turniers gefunden.

## 5. Datenbestand und Qualitätsprüfung

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
| `data/09.json` | 746 |
| **Gesamt** | **860** |

Davon liegen **390 Turniere vom 14.11. bis 31.12.2026** im Prüfzeitraum.

| Qualitätsprüfung | Ergebnis |
|---|---:|
| Gültige Turnier-JSON-Dateien | 9/9 |
| Doppelte IDs | 0 |
| Doppelte Slugs | 0 |
| Semantische Dubletten | 0 |
| Fehlende Pflichtfelder | 0 |
| Ungültige Datumsformate | 0 |
| Ungültige Startzeitformate | 0 |
| Cash Games in Turnierdateien | 0 |
| Zukünftige Datensätze ohne source_note | 0 |
| Startzeiten TBA | 142 |
| Varianten TBA | 116 |
| Turnierarten TBA | 68 |
| Buy-in TBA | 2 |

TBA bleibt dort stehen, wo die konkret datierte Quelle keine Angabe macht. Es wurden keine Wochenmuster hochgerechnet.

## 6. Nicht vollständig erreichbare Kalenderbereiche

Die Hauptkalenderansicht bleibt auf 100 sichtbare Zeilen beschränkt und endet aktuell am 21.11.2026 um 18:40. Versuche mit `?page=2`, `?offset=100`, `?start=100`, Datumsbereichen (`start_date/end_date`, `from/to`), `year/month`, `date_start` und Organizer-Parametern lieferten keine zuverlässig abrufbare vollständige Folgeseite. Die direkte Hauptansicht ist erreichbar; die Folgeseiten-/Monatsfilter sind es nicht.

Letzte erreichbare Termine der aktuellen Veranstalteransichten und offene Restzeiträume:

| Veranstalter | Letzter erreichbarer Termin | Nicht vollständig erreichbarer Rest |
|---|---|---|
| 24Poker | 06.12. | 07.–31.12. |
| FOIF DRÜ | 31.12. | kein offener Rest im sichtbaren Filter |
| AZ Poker Club | 27.12. | 28.–31.12. |
| Capital Poker Club | 27.12. | 28.–31.12. |
| House of Cards | 30.12. | 31.12. |
| Munot Poker | 28.11. | 29.11.–31.12. |
| Another Poker | 03.12. | 04.–31.12. |
| Prestige Poker | 24.11. | 25.11.–31.12. |
| Grand Casino Luzern | 20.12. | 21.–31.12. |
| Sports Zugerland | 28.12. | 29.–31.12. |
| RPR | 29.12. | 30.–31.12. |
| Pöstli Poker | 28.12. | 29.–31.12. |
| STATION | 30.11. | 01.–31.12. ohne weitere sichtbare Listingzeile |

Weitere konkrete Einschränkungen:

- **HSOP:** Die offizielle Turnierseite zeigt datierte Novembertermine bis 29.11. Der Dezemberbereich ist nur als generischer Monats-/Programmhinweis sichtbar; daraus wurden keine einzelnen Termine erzeugt.
- **Airfield/Pokerhelden:** Die offizielle Pokerraum-/Veranstalteransicht zeigt konkrete Termine bis 18.12.; eine vollständige Buy-in.info-Veranstalterübersicht für den ganzen Dezember ist nicht erreichbar.
- **DC Poker Club:** Eine aktuelle Check-Raise-Liste zeigt konkrete Termine bis 31.12.; die offizielle Clubwebsite war nicht ausreichend auslesbar. Die bereits vorhandenen 14 zukünftigen Datensätze wurden nicht durch Muster ergänzt.
- **RDC Poker Club:** Offizielle Website nicht erreichbar; die oben genannten Check-Raise-Kandidaten bleiben offen.
- Die Hauptkalender-Pagination nach dem 21.11. und die offenen Veranstalterzeiträume verhindern weiterhin eine vollständige Abdeckungsbestätigung bis 31.12.2026.

## 7. GitHub Actions und Pages-Artefakt

**Wird nach Abschluss des Datencommits, der Workflows und der tatsächlichen Artefaktprüfung ergänzt.** Der Build-Erfolg allein gilt nicht als Nachweis der Buy-in.info-Vollständigkeit oder der Live-Auslieferung.


## 8. Erneute Quellenprüfung – 14.11.2026, 08:35 Europe/Zurich

### Aktuelle Veranstalterübersichten erneut direkt geöffnet

Die zwölf Buy-in.info-Veranstalterübersichten sind weiterhin erreichbar. Ihre aktuellen Hauptlisten enthalten zusammen 331 Zeilen; 318 davon liegen im Prüfzeitraum 14.11.–31.12.2026. Zusätzlich enthält die aktuelle STATION-Detailtabelle zehn ausdrücklich datierte Termine bis 30.11.2026. Die aktuelle Suchindexansicht des Hauptkalenders enthält die Termine vom 13.11. bis 21.11.; 85 sichtbare Zeilen liegen ab 14.11. im Prüfzeitraum.

| Quelle | Ansichtszeilen |
|---|---:|
| Hauptkalender-Suchansicht ab 14.11. | 85 |
| Zwölf Veranstalterübersichten ab 14.11. | 318 |
| STATION-Detailtabelle | 10 |
| **Gesamt** | **413** |
| Cash Games ausgeschlossen | 2 |
| Geschlossene Prestige-Platzhalter ausgeschlossen | 3 |
| **Turnier-Listing-Vorkommen** | **408** |
| Wiederholungen zwischen Ansichten | 76 |
| **Eindeutige Turniere** | **332** |

Alle 332 eindeutigen Turniere sind im Datenbestand enthalten. Die 12 Organizer-Hauptlisten wurden einzeln mit den Datensätzen abgeglichen: 24Poker 20 Zeilen, FOIF DRÜ 82, AZ Poker Club 19, Capital Poker Club 29, House of Cards 14, Munot Poker 9, Another Poker 31, Prestige Poker 19 (davon zwei geschlossene Platzhalter), Grand Casino Luzern 42 (davon zwei Cash Games), Pöstli Poker 34, Sports Zugerland 12 und RPR 7. Die 318 Zeilen ab 14.11. entsprechen den jeweiligen zukünftigen Turnierlistings.

### Zwei sekundäre „Weitere Turniere“-Konflikte nicht übernommen

- **Capital Poker Club Bern:** Die aktuelle primäre Veranstalterliste führt den konkreten 2026-Block bis 27.12. Ein separater sekundärer „Weitere Turniere“-Block enthält zusätzlich „CPC THE GRAND Freezeout 300.-“ am 26.12.2026 und wiederholt andere Termine. Der 26.12.-Eintrag ist nicht in der primären aktuellen Veranstalterliste und wurde nicht als neues Turnier angelegt. Die aktuelle Hauptkalender-/primäre Veranstalteransicht hat Vorrang; der 26.12.-Kandidat bleibt als nicht bestätigter sekundärer Eintrag dokumentiert.
- **Grand Casino Luzern:** Die aktuelle primäre Veranstalterliste führt PCSM Day 1A am 16.12.2026 um 15:00 mit CHF 800+80. Ein sekundärer „Weitere Turniere“-Block zeigt einen unqualifizierten 15.12.-Eintrag. Dieser gehört zur nachfolgenden 2027-Terminserie (15.12.2027 ist ein Mittwoch); er wird nicht als 2026-Termin interpretiert. Der bestehende Datensatz 16.12.2026 bleibt unverändert.

### Quellenhinweis Another Poker Basel korrigiert

Für „Big Fish (80K Startstack)“ am 14.11.2026 um 20:00 stimmen die aktuelle Buy-in.info-Hauptkalenderansicht und die aktuelle Veranstalterübersicht `/tournaments/226` überein: **CHF 50+20**. Ein alter Quellenvermerk im bestehenden Datensatz behauptete fälschlich, die Hauptkalenderzeile habe CHF 60+20 gezeigt. Das Turnierfeld war bereits CHF 50+20; korrigiert wurden nur source_note und last_checked (14.11.2026). Variante und Turnierart bleiben TBA.

### Pagination und Cache-Status

Die direkt geöffnete HTML-Hauptkalenderansicht lieferte weiterhin einen älteren Ausschnitt vom 01.–09.11.2026. Die aktuelle Suchindexansicht enthält dagegen datierte Listings vom 13.–21.11.2026. Direkte Aufrufe von `?page=2`, `?offset=100`, `?start=100` sowie `?forganizer=`-Kalender-URLs waren über den Webabruf nicht zugänglich. Die direkten Veranstalterübersichten unter `/tournaments/{id}` waren erreichbar. Suchindex-Snapshots ersetzen keine vollständige Kalenderpagination.

### Änderungen und Datenqualität

- Fehlende Buy-in.info-Turniere ergänzt: **0**.
- Bestehende Turnierfelder korrigiert: **0**.
- Quellenhinweise korrigiert: **6** (Another Poker Big Fish sowie fünf Pöstli-Termine).
- Dubletten bereinigt: **0**.
- Bestand: 860 Datensätze; 390 vom 14.11. bis 31.12.2026.
- Alle neun JSON-Dateien gültig; 0 doppelte IDs/Slugs/semantische Events, 0 fehlende Pflichtfelder, 0 ungültige Datums-/Zeitformate, 0 Cash Games in den Turnierdateien.
- Im Prüfzeitraum: 142 Startzeiten TBA, 116 Varianten TBA, 68 Turnierarten TBA, 2 Buy-in-Angaben TBA; 0 zukünftige Datensätze ohne Quellenhinweis.

Die aktuelle Hauptkalender-Pagination hinter dem 21.11. bleibt der zentrale Blocker. Eine vollständige Buy-in.info-Abdeckung bis 31.12.2026 wird ausdrücklich nicht behauptet.

## 9. Workflow- und Artefaktprüfung

Wird nach dem Commit dieser Nachprüfung ergänzt. Der erfolgreiche Build allein gilt nicht als Beleg der Kalender-Vollständigkeit oder der Live-Auslieferung.


### Ergänzende Bestätigung von fünf Pöstli-Startzeiten

Die aktuelle Buy-in.info-Hauptkalender-Suchansicht vom 14.11.2026 führt fünf Pöstli-Termine ausdrücklich mit Uhrzeit. Die bereits gespeicherten Startzeiten wurden erneut bestätigt und die jeweiligen Quellenhinweise sowie last_checked aktualisiert:

| Datum | Turnier | Startzeit |
|---|---|---:|
| 14.11.2026 | Saturday Deep Century | 19:30 |
| 15.11.2026 | Omaha PL | 15:00 |
| 16.11.2026 | Pokemon | 19:30 |
| 19.11.2026 | Donschti Gämbler | 20:15 |
| 20.11.2026 | Progressiv-Bounty | 20:00 |

Die Veranstalterübersicht bestätigt jeweils Datum, Titel und Buy-in; die aktuelle Hauptkalender-Suchansicht bestätigt die konkrete Uhrzeit. Für die übrigen Pöstli-Termine bleibt TBA, da keine aktuelle datierte Hauptkalender- oder offizielle Veranstalterquelle eine Startzeit nennt.
