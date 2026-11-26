# Tagesaudit – Buy-in.info-Abgleich vom 26.11.2026

## Ergebnis

- Hauptkalender: https://buy-in.info/calendar
- Direkte Hauptkalenderzeilen im ab heute relevanten sichtbaren Abschnitt (26.11.–01.12.2026): **84**.
- Cash Games ausgeschlossen: **2** (Grand Casino Luzern, 27.11. und 28.11.).
- Geschlossener Platzhalter ausgeschlossen: **1** (Prestige Poker, 01.12.).
- Gültige Turnierlistings im sichtbaren Abschnitt: **81**.
- Alle **81** sichtbaren gültigen Listings sind im Datenbestand vorhanden; keine fehlende Ergänzung aus diesem Hauptkalenderabschnitt.
- Deduplizierte Gesamtzahl über sämtliche Veranstalterseiten wird nicht ausgewiesen, da die dynamischen Veranstalteransichten und ihre Überschneidungen nicht vollständig als maschinenlesbarer Gesamtexport verfügbar waren.

## Geprüfte Detailansichten und Suchindizes

Zusätzlich zur Hauptansicht wurden die datierten Veranstalter-/Filteransichten für Grand Casino Luzern (ID 458) und Prestige Poker Dietlikon (ID 189) geprüft. Die GCL-Ansicht liefert aktuelle Listings vom 26.11. bis 20.12.2026 sowie einzelne Termine 2027; Prestige reicht in der abgerufenen Ansicht bis 02.12.2026. Weitere Suchindex-Ausschnitte bestätigen Termine am 30.11.–03.12.

- Grand Casino Luzern: Alle sichtbaren Turniere vom 26.–29.11. und die gelisteten PCSM-Veranstaltungen vom 10.–20.12. sind im Datenbestand vorhanden.
- Prestige Poker: Die sichtbaren Termine vom 26.11.–02.12. sind vorhanden.
- Die Hauptkalenderzeilen vom 26.–30.11. und die drei sichtbaren Zeilen vom 01.12. wurden gegen alle neun Turnier-JSON-Dateien geprüft; keine fehlenden Datensätze festgestellt.
- Die Hauptansicht enthält u.a. die BOPM-Termine von Airfield, HSOP, STATION, die Grand-Casino-Autumn-Special-Tage, Another Poker, 24Poker, FOIF DRÜ, Capital, AZ, Munot, Pöstli und Prestige.

## Datenbestand und Qualitätsprüfung

Alle neun Dateien data/01.json bis data/09.json wurden frisch von main gelesen und geparst.

| Datei | Einträge |
|---|---:|
| data/01.json | 15 |
| data/02.json | 15 |
| data/03.json | 15 |
| data/04.json | 15 |
| data/05.json | 15 |
| data/06.json | 14 |
| data/07.json | 15 |
| data/08.json | 10 |
| data/09.json | 844 |
| **Gesamt** | **958** |

- Einträge vom 26.11.–31.12.2026: **337**.
- Doppelte IDs über alle neun Dateien: **0**.
- Doppelte Slugs über alle neun Dateien: **0**.
- Fehlende Kernfelder (ID, Datum, Zeit/TBA, Titel, Veranstalter, Ort/Stadt, Variante, Turnierart, Buy-in-Angabe, Slug) im Zielzeitraum: **0**.
- Cash Games in den neun Turnierdateien: **0**.
- Datenänderungen an Turnierdatensätzen: **0**.
- Neue Turniere: **0**.
- Bestehende Datensätze korrigiert: **0**.
- Dubletten bereinigt: **0**.

Die Werte TBA bleiben bestehen, wenn die jeweilige Quelle keine belastbare Angabe liefert.

## Quellenkonflikte und Absagen

Es wurde heute kein neuer, durch eine offizielle datierte Veranstalterquelle belegter Absagefall gefunden. Frühere dokumentierte Konflikte wurden nicht gelöscht oder aufgrund eines Wochenmusters verändert.

## Konkrete Blocker

1. Die Hauptkalenderansicht ist auf 100 Zeilen begrenzt; sie endet hier beim 01.12.2026 um 18:30 Uhr. Eine vollständige Folgeseite bzw. ein vollständiger Dezember-Export konnte nicht gewonnen werden.
2. Die direkten Filter-/Organizer-Seiten sind nicht alle gleichermassen aktuell und vollständig maschinenlesbar. Die Grand-Casino- und Prestige-Ansichten waren lesbar; eine vollständige deduplizierte Extraktion sämtlicher zwölf Clubübersichten über alle Monate gelang nicht.
3. Weitere Veranstalter-/Monatsbereiche ab 03.12. bis 31.12. sind deshalb nicht vollständig quellenübergreifend abgeglichen. Einzelne GCL-Termine bis 20.12. sind jedoch konkret gelistet und vorhanden.
4. Keine vollständige aktuelle Monatsübersicht wurde heute für alle Anbieter wie Airfield, HSOP, STATION, DC, RDC, OVP, 72 Offsuite und Grand Casino Basel bestätigt.

Letzte sichtbare Termine sind keine Garantie, dass danach keine weiteren Turniere veröffentlicht werden. Eine vollständige Abdeckung bis 31.12.2026 wird ausdrücklich **nicht** behauptet.

## Live- und Deployment-Status

Dieses Audit ist ein Dokumentationscommit ohne Änderung an den Turnierdaten. Ein neuer Pages-Build wurde deshalb nicht durch eine Datenänderung ausgelöst. Der zuletzt bekannte erfolgreiche Pages-Build ist separat im Actions-Verlauf sichtbar; die heutige Prüfung beansprucht keinen neuen Artefakt- oder Live-Deploy-Nachweis.

- Repository: https://github.com/Helvetic-Poker/helveticpoker-pokerturniere
- Geprüfter main-Stand: 4c4c31c53cad7cdde06db915d6442360edd3e7d5
- Tagesprüfung: 26.11.2026
