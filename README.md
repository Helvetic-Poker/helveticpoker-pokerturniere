# HELVETIC POKER – Pokerturniere Schweiz

GitHub Pages production smoke-test package.

**Important:** This package is a technical production test, not the final exhaustive Swiss event database. Only currently verified seed events are published. The automated source adapters are deliberately not enabled yet.

## GitHub Pages
Settings → Pages → Deploy from branch → `main` / `/(root)`.

## Safe publish
The updater must build a candidate version, run all preflight checks, and only then replace the published version. If a check fails, the last known-good version stays online.
