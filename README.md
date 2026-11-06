# Pokerturniere Schweiz – Helvetic Poker

Zentraler Kalender der Schweizer Pokerszene.

## Aktueller Stand
- Datenstand: 06.11.2026
- Zeitraum im Datenbestand: Oktober bis Dezember 2026
- 764 eindeutige Turnierdatensätze in 9 Dateien unter `data/*.json`
- Davon 399 Datensätze vom 06.11.2026 bis 31.12.2026
- Direktlinks zu den jeweiligen Veranstaltern
- Filter: Heute, Morgen, Wochenende, Monat, Region, Buy-in, Variante, Turnierart, Veranstalter und Suche
- Mobile-first Darstellung

## Datenprinzip
- Buy-in.info ist die verbindliche Mindestquelle für Schweizer Turnierlistings.
- Konkrete Daten werden nur aus ausdrücklich datierten Kalender- oder Veranstalterquellen übernommen; Wochenmuster werden nicht hochgerechnet.
- Fehlende Startzeiten, Varianten oder Turnierarten bleiben `TBA`, solange keine datierte Quelle sie bestätigt.
- Cash Games werden nicht in den Turnierdatenbestand übernommen.
- Bei widersprüchlichen Buy-in.info-Ansichten hat die aktuelle Hauptkalender-/Veranstalterübersicht Vorrang; Abweichungen werden dokumentiert.

## Quellenabgleich 06.11.2026
- Die zugängliche Hauptkalenderansicht zeigte 100 Zeilen vom 06.11. bis 13.11.2026: 96 Turnierlistings, 3 Cash Games und 1 Hinweis auf einen geschlossenen Spieltag.
- Alle 96 Turnierlistings sind im Datenbestand vorhanden.
- Die HSOP-Titel für 09., 10. und 13.11. wurden an die aktuelle Buy-in.info-Hauptkalenderbezeichnung angeglichen; offizielle HSOP-Details bleiben in Untertitel/Quellenhinweisen erhalten.
- Bei Prestige wurden drei Varianten-/Formatangaben anhand datierter Buy-in.info-Detail-/Folgelistings präzisiert.
- Zwei semantische Dubletten der Airfield/Pokerhelden-Liga aus 02. und 03.10. wurden dateiübergreifend zusammengeführt.
- Hauptkalender-Pagination hinter dem 13.11. sowie mehrere Veranstalterfilter nach ihrem jeweils letzten sichtbaren Termin waren nicht vollständig auslesbar. Daher wird keine vollständige Buy-in.info-Abdeckung bis 31.12.2026 behauptet.

Der tägliche Quellenabgleich wird fortgeführt. Ein erfolgreicher JSON-/Pages-Build ersetzt nicht die Prüfung der tatsächlich erreichbaren Buy-in.info-Monate und der öffentlichen Live-Auslieferung.
