# Pokerturniere Schweiz – Helvetic Poker

Zentraler Kalender der Schweizer Pokerszene.

## Aktueller Stand
- Datenstand: 12.11.2026
- Zeitraum im Datenbestand: Oktober 2026 bis mindestens Dezember 2026
- 846 eindeutige Turnierdatensätze in 9 Dateien unter `data/*.json`
- 404 Datensätze vom 12.11.2026 bis 31.12.2026
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
- Der Bestand umfasst nun 846 Datensätze, davon 404 vom 12.11. bis 31.12.2026.
- Hauptkalender-Pagination und mehrere weitere Veranstalterzeiträume bleiben eingeschränkt; eine vollständige Buy-in.info-Abdeckung bis 31.12.2026 wird nicht behauptet. Details: [Tagesaudit 12.11.2026](docs/buyin-audit-2026-11-12.md).
