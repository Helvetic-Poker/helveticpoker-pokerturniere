# Buy-in.info / Helvetic Poker Audit — 2026-11-06

## Umfang und Quellenabgleich
- Buy-in.info-Hauptkalender: 100 sichtbare Zeilen für 06.–13.11.2026; 96 Turnierlistings nach Ausschluss von 3 Cash-Game-Zeilen und 1 Schliessungshinweis.
- 12 Veranstalterkalender/Filter und aktuelle Suchindex-Snapshots geprüft: FOIF DRÜ, 24Poker, Another Poker Basel, Munot Poker, House of Cards, Capital Poker Club, Prestige Poker, Grand Casino Luzern, Pöstli Poker, Sports Zugerland, RPR und AZ Poker Club.
- Sichtbare Buy-in.info-Listing-Vorkommen zusammen: 414 (96 Hauptkalender-Turniere plus 318 Veranstalterfilter-Zeilen; Überschneidungen mitgezählt).
- Nach semantischer Deduplizierung: 333 eindeutige Buy-in.info-Turnierlistings; 81 wiederholte Vorkommen über mehrere Ansichten.
- Die 333 sind nur die Vereinigungsmenge der zugänglichen Ansichten, keine vollständige Kalender-Gesamtzahl.

## Änderungen aus Buy-in.info
- 18 fehlende Buy-in.info-Turniere ergänzt: 11 aus dem Hauptkalenderfenster 06.–13.11., 2 zusätzliche Prestige-Turniere am 14.11. und 5 fehlende FOIF-Termine aus dem aktuellen Veranstalterkalender.
- 5 bestehende Datensätze korrigiert: FOIF-Titel 16.11., FOIF-Titel/Buy-in 01.12., Capital-Startzeit 15.11., Capital-Buy-in 22.11. und Pöstli-Startzeit 13.11.
- 5 FOIF-Datensätze für 24.–25.12. entfernt, weil diese Termine im aktuellen FOIF-Veranstalterkalender nicht mehr gelistet sind. Das wird nicht als offizielle Absage behauptet; die Termine sind nur nicht mehr aktuell bestätigt.
- Quellenkonflikt-Hinweise für AZ Championship und Capital aktualisiert.
- Dubletten bereinigt: 0.

## Ergänzungen aus datierten Veranstalterquellen (nicht als Buy-in.info-Listings gezählt)
- 21 ausdrücklich datierte DC-Poker-Club-Turniere aus dem offiziellen Clubkalender/Check-Raise-Einbettung (06.11.–31.12.).
- 3 ausdrücklich datierte zusätzliche STATION-Termine aus der aktuellen Raumübersicht (16., 23., 30.11.); 08. und 09.11. sind Buy-in.info-Listings.
- 3 Stufen des offiziellen OVP-Winter-2026-Events: Day 1A (04.12. 19:00), Day 1B (05.12. 13:00), Day 2 Fortsetzung (05.12. 20:30). Der Flyer nennt CHF 240 (200+40); für Day 2 ist kein separater Buy-in angegeben.
- Diese 27 offiziellen Zusatzdatensätze sind nicht in der Zahl 333 enthalten.

## Datenqualität
- Alle neun data/*.json-Dateien erfolgreich geparst.
- Datensätze insgesamt nach diesem Lauf: 766.
- Datensätze 06.11.–31.12.2026: 399.
- Doppelte IDs: 0; doppelte Slugs: 0; exakte semantische Dublettengruppen (Datum/Startzeit/Veranstalter/Titel): 0.
- Cash Games im Turnier-JSON: 0.
- Neue DC-Datensätze: 21; OVP: 3; STATION-Zukunftstermine: 5; FOIF-Zukunftstermine: 99.
- Historische STATION-Ortskorrektur Bern → Biel/Bienne: 3 Datensatz/Datensätze.

## Quellenkonflikte
- Capital CPC THE GRAND am 15.11.: aktuelle Buy-in.info-Veranstalterübersicht nennt 15:00, Check-Raise-Detail 16:00. Buy-in.info wird beibehalten.
- Capital Ranking Final am 22.11.: aktuelle Buy-in.info-Veranstalterübersicht nennt CHF 100+30, Check-Raise-Detail Freeroll/CHF 0. Buy-in.info wird beibehalten; Konflikt offen.
- AZ Championship Serie 4: Buy-in.info-Gebührenaufteilung weicht von Check-Raise ab (CHF 120+20[+20] gegenüber CHF 100+40). Buy-in.info-Werte bleiben.
- FOIF 16.11., 01.12., 07.12.: aktueller FOIF-Veranstalterkalender überschreibt alte Einträge; 24.–25.12. aus vorherigem Snapshot sind dort nicht mehr gelistet und wurden ohne Absagebehauptung entfernt.
- STATION-Website listet die Postleitzahl 2503/2504 uneinheitlich; gespeichert wird nur Biel/Bienne, keine Postleitzahl.

## Nicht erreichbare Quellen/Zeiträume
- Die Buy-in.info-Hauptansicht ist auf die ersten 100 sichtbaren Zeilen (06.–13.11.) begrenzt. Der Auslassungs-/Pagination-Button lieferte keine nutzbare Folgeseite. Versuche mit ?page=2, ?offset=100, ?date=2026-11-14, ?date_from=2026-11-14, ?datum-ab=2026-11-14 und ?month=2026-11 lieferten keine vollständige Folgeseite.
- Zugängliche Veranstalterfilter enden unterschiedlich: FOIF 31.12.; 24Poker 06.12.; Another 03.12.; Munot 28.11.; House of Cards 30.12.; Prestige 16.11.; Grand Casino Luzern 16.12.; Pöstli 03.12.; Sports Zugerland 28.12.; RPR 29.12.; AZ 27.12.
- Capital-Buy-in.info-Filter/Suchindex-Snapshots sind nur teilweise auslesbar; der offizielle Capital/Check-Raise-Raumkalender liefert zusätzliche datierte Einträge bis 27.12., ersetzt aber nicht die fehlende Buy-in.info-Pagination.
- STATION-Buy-in.info-Veranstalterfilter ist veraltet; aktuelle Hauptkalenderzeilen decken 08.–09.11. ab, die aktuelle Raumübersicht 16.–30.11.
- Kartenfreunde Wynental ist nur im Hauptkalender sichtbar; kein vollständiger Veranstalterfilter gefunden.
- HSOP und Airfield haben keine vollständigen aktuellen Buy-in.info-Veranstalterfilter bis 31.12.; offizielle Quellen wurden nur für einzeln datierte Ergänzungen genutzt.
- Eine vollständige Extraktion des gesamten Kalenders bis 31.12. wird ausdrücklich nicht behauptet.
