# GE150 Presets

The presets on my Mooer GE150 Pro Li, bank by bank (1A–40D), with notes on each one.
It runs as an app on iPhone and iPad Home Screens and the Mac's Dock, and works with no signal once installed.

## Using it

- Tap a preset card to edit its name, style and notes.
- Empty banks show small slot buttons (3A, 3B…). Tap one to add a preset there.
- **Presets are saved on each device**, so an iPhone and a Mac each keep their own list.
  Use **Save a backup file** at the bottom to keep a copy (e.g. in Dropbox),
  and **Restore from backup** to load it on another device.

## What's in here

| File | What it does |
|---|---|
| `index.html` | The whole app |
| `sw.js` | The "service worker": saves the app on the device so it works offline |
| `manifest.webmanifest` | Tells the device the app's name, icon, and to open full-screen |
| `icons/` | App icons (redraw with `python3 tools/make-icons.py`) |
| `Start GE150 Presets.command` | Double-click to run a local test copy on this Mac |

## Installing it

- **iPhone / iPad:** open the live app in Safari → Share → **Add to Home Screen**.
- **Mac:** open the live app in Safari → **File → Add to Dock**.

## Publishing a change

1. Edit the files.
2. **In `sw.js`, bump `VERSION`** (v1 → v2 …). Without this, devices keep the old copy.
3. Commit and push (`git add -A && git commit -m "…" && git push`).
4. GitHub Pages updates within a minute or two. Open the app and an
   **Update** banner appears. Tap it.
