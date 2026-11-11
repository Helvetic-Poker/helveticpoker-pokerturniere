# Pokerturniere Schweiz – Helvetic Poker

Zentraler Kalender der Schweizer Pokerszene.

## Aktueller Stand
- Datenstand: 11.11.2026
- Zeitraum im Datenbestand: Oktober 2026 bis mindestens Dezember 2026
- 814 eindeutige Turnierdatensätze in 9 Dateien unter `data/*.json`
- 384 Datensätze vom 11.11.2026 bis 31.12.2026
- Direktlinks zu den jeweiligen Veranstaltern
- Filter: Heute, Morgen, Wochenende, Monat, Region, Buy-in, Variante, Turnierart, Veranstalter und Suche
- Mobile-first Darstellung

## Datenprinzip
- Buy-in.info ist die verbindliche Mindestquelle für Schweizer Turnierlistings.
- Konkrete Daten werden nur aus ausdrücklich datierten Kalender- oder Veranstalterquellen übernommen; Wochenmuster werden nicht hochgerechnet.
- Fehlende Startzeiten, Varianten oder Turnierarten bleiben `TBA`, solange keine datierte Quelle sie bestätigt.
- Cash Games werden nicht in den Turnierdatenbestand übernommen.
- Bei widersprüchlichen Buy-in.info-Ansichten hat die aktuelle Hauptkalender-/Veranstalterübersicht Vorrang; Abweichungen werden dokumentiert.

## Quellenabgleich 11.11.2026
- Die aktuelle Hauptkalenderansicht zeigte 100 sichtbare Zeilen; 7 Zeilen betrafen den 10.11.2026, 2 waren Cash Games. Für den Prüfzeitraum ab 11.11. wurden 91 Turnierlistings gezählt.
- Zwölf aktuelle Veranstalterübersichten enthielten zusammen 320 ausdrücklich datierte Turnierlistings ab 11.11.2026.
- Nach 85 Überschneidungen zwischen Hauptkalender und Veranstalterübersichten ergeben sich 326 eindeutige Turniere in den heute erreichbaren Ansichten.
- Ein fehlendes RPR-TimePOKER-++-Turnier am 11.11.2026 wurde ergänzt; Another-Poker-Buy-ins/Titel, HSOP-Haupttitel, sieben FOIF-Titel, 15 House-of-Cards-Titel und ein GCL-Titel wurden nach aktueller Quelle korrigiert.
- 16 ausdrücklich in der aktuellen Hauptkalenderansicht sichtbare Startzeiten wurden von TBA auf die datierten Uhrzeiten gesetzt.
- Alle neun JSON-Dateien wurden erneut auf Syntax, doppelte IDs/Slugs, semantische Dubletten, Pflichtfelder, Uhrzeitformate und Cash Games geprüft.
- Die Hauptkalender-Pagination hinter der sichtbaren ersten Ansicht bleibt nicht vollständig auslesbar. Für HSOP, Airfield und weitere nicht separat gefilterte Anbieter ist der Zeitraum nach dem sichtbaren Hauptkalender-Ausschnitt nicht vollständig verifizierbar. Es wird keine vollständige Buy-in.info-Abdeckung bis 31.12.2026 behauptet.

Der tägliche Quellenabgleich wird fortgeführt. Ein erfolgreicher JSON-/Pages-Build ersetzt nicht die Prüfung der tatsächlich erreichbaren Buy-in.info-Monate und der öffentlichen Live-Auslieferung.
