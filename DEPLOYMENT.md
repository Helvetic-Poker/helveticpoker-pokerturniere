# Helvetic Poker Calendar – Fertigstellung & Deployment

## Was fertig ist
- responsive Kalender
- Suche + Zeitraumfilter
- Region / Buy-in / Variante / Eventtyp
- 43 aktuelle Seed-Datensätze aus der bisherigen Recherche
- einzelne statische Event-URLs
- SEO-Titel + Description pro Event
- direkte Veranstalterlinks, wenn vorhanden
- Prüfstatus + last_checked
- Datenmodell für automatische Änderungen
- GitHub Actions Zeitplan als Automatisierungsgerüst

## Was noch technisch nötig ist
Eine öffentliche HTTPS-Adresse. ChatGPT kann nicht in dein Hosting-Konto veröffentlichen.
Die ZIP-Datei kann auf einem HTTPS-Host deployed werden, danach wird die URL in Wix eingebettet.

## Einfachster Start
1. Den Ordner auf einen statischen HTTPS-Host laden.
2. Prüfen: `/index.html` und `/events/<slug>/`.
3. Die öffentliche HTTPS-URL in `WIX_EMBED_SNIPPET.html` einsetzen.
4. In Wix Harmony:
   + Hinzufügen → Elemente → Embed → HTML-Code.
5. Embed auf der Seite „Pokerturniere Schweiz“ platzieren.
6. Höhe zunächst ca. 1200 px; später je nach Layout anpassen.

## Für den produktiven Auto-Update-Betrieb
Das GitHub-Workflow-Gerüst läuft täglich. Die eigentlichen Source-Adapter müssen für jede zugelassene Quelle gepflegt werden. Die Update-Regeln sollen:
- NEW erkennen
- CHANGED erkennen
- CANCELLED nur bei belastbarer Bestätigung setzen
- MISSING separat markieren
- RESTORED erkennen
- jede Änderung protokollieren

## SEO-Hinweis
Der externe Kalender ist ein Embed. Der eingebettete Inhalt selbst ist nicht automatisch gleichwertig mit Wix-native CMS-Seiten auf helveticpoker.ch. Für maximalen SEO-Nutzen sollte langfristig eine native Wix-CMS- oder serverseitig gerenderte Event-Seiten-Architektur geprüft werden. Der Embed ist die sichere Harmony-kompatible MVP-Route.
