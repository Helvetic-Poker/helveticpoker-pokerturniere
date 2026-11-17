# Buy-in.info-Abgleich – 17.11.2026

## Ergebnis und Umfang

Prüfzeitraum: 17.11.2026 bis 31.12.2026.

Die direkte Hauptkalenderansicht `https://buy-in.info/calendar` lieferte 100 sichtbare Zeilen. Davon entfallen 13 auf den 16.11. und liegen vor dem Prüfzeitraum. Für den Zeitraum ab 17.11. wurden 87 Zeilen aus der Hauptansicht geprüft. Der Suchindex lieferte zusätzlich sechs weitere datierte Zeilen für den 25.11., die hinter der sichtbaren 100-Zeilen-Grenze liegen. Zusammen sind das 93 Hauptkalender-Ansichtszeilen im Prüfzeitraum.

Zusätzlich wurden zwölf aktuelle Veranstalter-/Clubübersichten geprüft: Another Poker Basel, Pöstli Poker, AZ Poker Club Bern, Munot Poker, FOIF DRÜ, Capital Poker Club Bern, House of Cards Luzern, 24Poker, RPR/Roger's Pokerroom, Sports Zugerland, Prestige Poker Dietlikon und Grand Casino Luzern. In diesen Ansichten liegen 289 Zeilen im Prüfzeitraum.

| Kennzahl | Anzahl |
|---|---:|
| Hauptkalender-Ansichtszeilen ab 17.11. | 93 |
| Veranstalter-/Club-Ansichtszeilen | 289 |
| Ansichtszeilen insgesamt | 382 |
| Cash-Game-Ansichtszeilen (Haupt- und Clubansichten) | 4 |
| Geschlossene Platzhalter | 3 |
| Turnier-Listing-Vorkommen nach Ausschlüssen | 375 |
| Überschneidungen Hauptkalender ↔ Veranstalteransichten | 80 |
| Eindeutige Turniere in den erreichbaren Ansichten | 295 |

Überschneidungen wurden anhand von Datum, Startzeit, Veranstalter und Veranstaltungsidentität gezählt; abweichende Snapshot-Titel für denselben Slot wurden nicht als zusätzliches Turnier gezählt.

## Änderungen

- **2 fehlende Turniere ergänzt:** Another Poker Basel – Classic Wednesday (25.11.2026, 19:00, CHF 100+30) und Time Poker Turnier PL Omaha (25.11.2026, 19:30, CHF 100+30).
- **3 bestehende Datensätze korrigiert:**
  1. Another Poker Basel am 23.11.2026, 18:40: Die aktuelle direkte Hauptkalenderansicht listet „Hyper Turbo Satelitte - 1 Ticket garantiert“, CHF 24+6. Die Veranstalterübersicht `/tournaments/226` zeigt dagegen „Satellite 350 Master Freezeout“, CHF 30+10. Gewählt wurde die aktuell geöffnete Hauptkalenderzeile; der Konflikt ist im Datensatz dokumentiert.
  2. AZ Poker Club Bern – Monster Stack 100K am 25.11.: Startzeit TBA → 19:00, direkt aus der datierten Hauptkalenderfortsetzung.
  3. Pöstli Poker – Mittwuch Spez am 25.11.: Startzeit TBA → 20:15, direkt aus der datierten Hauptkalenderfortsetzung.
- **Dubletten bereinigt:** 0.

## Quellen

- Hauptkalender: https://buy-in.info/calendar
- Another Poker Basel: https://buy-in.info/tournaments/226
- Pöstli Poker: https://buy-in.info/tournaments/554
- AZ Poker Club Bern: https://buy-in.info/tournaments/564
- Munot Poker: https://buy-in.info/tournaments/558
- FOIF DRÜ: https://buy-in.info/tournaments/520
- Capital Poker Club Bern: https://buy-in.info/tournaments/493
- House of Cards Luzern: https://buy-in.info/tournaments/570
- 24Poker: https://buy-in.info/tournaments/132
- RPR/Roger's Pokerroom: https://buy-in.info/tournaments/540
- Sports Zugerland: https://buy-in.info/tournaments/553
- Prestige Poker Dietlikon: https://buy-in.info/tournaments/189
- Grand Casino Luzern: https://buy-in.info/club/458
- Detailbestätigung Classic Wednesday: https://buy-in.info/tournament/117808
- Detailbestätigung Time Poker PL Omaha: https://buy-in.info/tournament/117623

## Blocker und Abdeckungsgrenzen

Die Hauptkalenderansicht ist auf 100 Zeilen begrenzt. Die sechs zusätzlichen 25.11.-Zeilen waren über den Suchindex auffindbar; eine vollständige Folgeseite bzw. eine vollständige Kalenderansicht für Dezember konnte nicht abgerufen werden. Datums-/Offset-/Organizer-Filter wurden versucht, aber eine vollständige zweite Kalenderseite war nicht zugänglich.

Letzte sichtbare Termine in den aktuellen Veranstalterübersichten:
- Another Poker Basel: 03.12.2026
- 24Poker: 06.12.2026
- Prestige Poker Dietlikon: 24.11.2026
- Munot Poker: 28.11.2026
- Grand Casino Luzern: 20.12.2026
- AZ Poker Club Bern: 27.12.2026
- Capital Poker Club Bern: 27.12.2026
- Pöstli Poker: 28.12.2026
- Sports Zugerland: 28.12.2026
- RPR/Roger's Pokerroom: 29.12.2026
- House of Cards Luzern: 30.12.2026
- FOIF DRÜ: 31.12.2026 (die Übersicht reicht zusätzlich bis 02.01.2027)

Diese letzten sichtbaren Termine belegen nicht, dass danach keine weiteren Turniere veröffentlicht werden. Für Airfield Pokerclub Interlaken, HSOP und STATION Poker Club wurde keine vollständige aktuelle Buy-in.info-Veranstalterübersicht mit Monatsabdeckung abgerufen; einzelne datierte Buy-in.info-Listings sind vorhanden. Für 72 Offsuite Thun, Kartenfreunde Wynental, DC Poker Club und Open Valais ergab die heutige Buy-in.info-Suche keine vollständige aktuelle Veranstalterübersicht. Cash Games bleiben ausgeschlossen.

## Datenprüfung vor Commit

Alle neun `data/*.json`-Dateien wurden geladen und JSON-parsed. IDs und Slugs sind eindeutig; Datum und Zeitformate sind valide. Die zwei neuen Datensätze wurden mit fortlaufenden globalen `_ord`-Werten versehen. Eine vollständige Abdeckung sämtlicher Buy-in.info-Kalenderseiten bis 31.12.2026 wird wegen der genannten Blocker ausdrücklich nicht behauptet.


## Nachprüfung des Pages-Artefakts und Generator-Korrektur

Das erste Artefakt für Commit `8494326` enthielt alle neun JSON-Dateien (871 Datensätze), 871 Turnierdetailseiten und 20 Veranstalterseiten. Alle fünf geänderten/neuen Detailseiten waren vorhanden und zeigten Datum, Startzeit und Buy-in korrekt.

Bei der Zähler-/Listenprüfung wurde eine Darstellungsgrenze gefunden: Die FOIF-DRÜ-Veranstalterseite enthielt nur 60 Eventkarten, obwohl 75 kommende FOIF-Datensätze im JSON stehen. `scripts/generate-landing-pages.py` begrenzte die sichtbare Liste und die zugehörigen ItemList-Einträge auf `upcoming[:60]`. Diese Grenze wurde entfernt, damit die Veranstalterseite sämtliche kommenden Einträge zeigt und der sichtbare Umfang zum Zähler passt.

Der Qualitätsworkflow hatte außerdem zwei mögliche Dubletten für die PCSM-Main-Event-Satellites am 16.12. und 17.12. gemeldet. Die Datensätze unterscheiden sich jeweils durch Startzeit und Buy-in (13:15 / CHF 125+25 gegenüber 19:00 / CHF 180+30). Der bisherige Prüfschlüssel ignorierte diese Felder. `scripts/check-event-data.py` vergleicht nun zusätzlich Startzeit und Buy-in-Label; echte identische Veranstaltungen mit leicht abweichenden IDs bleiben erkennbar, die beiden unterschiedlichen Satellites werden nicht mehr fälschlich als Dubletten gemeldet.

Die Korrekturen an Generator und Qualitätsprüfer wurden nach dem Datencommit separat auf `main` committed; das nachfolgende Pages-Artefakt und beide Workflows werden erneut geprüft.
