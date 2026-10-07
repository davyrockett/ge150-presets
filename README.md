# GE150 Presets

The presets on my Mooer GE150 Pro Li, bank by bank (1A–40D), with notes on each one.
It runs as an app on iPhone and iPad Home Screens and the Mac's Dock, and works with no signal once installed.

## Using it

- The gear button opens **Settings**: Auto / Light / Dark appearance, and **Check for updates**.
- Tap a preset card to edit its name, style and notes. Change its **Slot** to move it;
  picking a slot that already has a preset swaps the two.
- Or **drag a card** onto another slot (on a phone, press and hold it first). Dropping on an empty
  slot moves it; dropping on another preset swaps them. **Undo** appears for a few seconds after.
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
2. **Run `tools/bump.sh`** to bump the version (v3 → v4 …) in `sw.js` and `index.html`. Without this, devices keep the old copy.
3. Commit and push (`git add -A && git commit -m "…" && git push`).
4. GitHub Pages updates within a minute or two. Reopen the app and it updates itself,
   or use **Settings → Check for updates**.
