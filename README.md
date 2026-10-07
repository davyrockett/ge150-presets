# GE150 Presets

The presets on my Mooer GE150 Pro Li, bank by bank (1A–40D), with notes on each one.
It runs as an app on iPhone and iPad Home Screens and the Mac's Dock, and works with no signal once installed.

## Using it

- The gear button opens **Settings**: Auto / Light / Dark appearance, and **Check for updates**.
- Tap a preset card to edit its name, style and notes. Change its **Slot** to move it;
  picking a slot that already has a preset swaps the two.
- Or **drag a card** onto another slot (on a phone, press and hold until it lifts). Dropping on an empty
  slot moves it; dropping on another preset swaps them. On a phone you can also lift your finger
  after the card lifts, then tap the slot where it goes. **Undo** appears for a few seconds after.
- **Duplicate** (in a preset's edit window) copies it: tap the slot where the copy goes.
  **Copy bank** (next to a bank's name) copies all its presets into the bank you tap, A→A, B→B….
  Copying onto a filled slot replaces it; **Undo** is there for a few seconds.
- Empty banks show small slot buttons (3A, 3B…). Tap one to add a preset there.
- **Sync:** the list lives in `data.json` in the public GitHub project
  [`davyrockett/ge150-presets-data`](https://github.com/davyrockett/ge150-presets-data).
  Anyone with the app's link sees it, with no setup. To **edit** on a device, open
  Settings → Sync and editing, paste your access key once, and tap Connect.
  Without the key a device is view only.
- Each device syncs when the app opens, a moment after an edit, when you come back to it,
  and every 2 minutes while it's on screen. With no signal, edits are saved on the device
  and sync later. If the same slot is changed on two devices, the newest change wins.
  GitHub keeps every sync as a version, so older lists can be recovered from the project's history.
- **Save a backup file** / **Restore from backup** at the bottom still work as an extra copy.

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
