# Retro Game Library

**A visual catalogue for the games you own.** Carts, tapes, discs, boxes and digital copies, from the Atari 2600 and ZX Spectrum right up to PS5 and Switch 2.

I'd been keeping track of my retro collection in a spreadsheet. It worked, but it was just rows of text, and I wanted something more visual that also backed itself up to the cloud. Add a game, pick the system, and the box art, description, year and publisher fill themselves in.

## Download

**[Get it on itch.io](ITCH_LINK)**: free, or pay what you like to support it.

| System | Download |
| --- | --- |
| Windows 10/11 | Retro Game Library Lite (Windows).zip |
| Mac (macOS 12+, Apple Silicon and Intel) | Retro Game Library Lite (Mac).zip |
| Linux PC | Retro Game Library Lite (Linux).tar.gz |
| Raspberry Pi 4/5 (64-bit) | Retro Game Library Lite (Linux ARM64, Raspberry Pi).tar.gz |
| Any PC, no install (Chrome or Edge) | Retro Game Library (browser version).zip |

The same downloads are also on the [Releases](../../releases) page. Each one has a *READ ME FIRST* file with setup steps for that system.

## Features

- **Box art and descriptions filled in automatically** from the free [LaunchBox Games Database](https://gamesdb.launchbox-app.com). You don't need LaunchBox installed.
- **One game, several systems.** Add R-Type once, tick the other machines you own it on, and each gets the right box art.
- **Multiple copies**, with a filter for duplicates, games on several systems, or games missing box art.
- **Loose, boxed, complete in box, sealed or digital**, plus condition, date acquired and notes. Digital games record the store (GOG, Steam, eShop and others), and you can filter to physical or digital only.
- **Covers saved locally** as small pictures, so the app works offline.
- **Cloud backup.** Keep your library folder in Google Drive, OneDrive, iCloud or Dropbox and every change is backed up, plus a dated backup copy for each day you make changes.
- **Export** a PDF catalogue with box art, an Excel workbook, or a CSV.
- **Tiny and portable**: about 1–2 MB, with nothing to install.
- No accounts, no tracking and no ads.

## Not a LaunchBox replacement

Retro Game Library is only for cataloguing your collection. It isn't a game launcher and is in no way a replacement for the brilliant [LaunchBox](https://www.launchbox-app.com). If you play games on PC, check it out.

Game information and box art come from the LaunchBox Games Database, built by the LaunchBox community. This project isn't made by, or affiliated with, LaunchBox. The app downloads the database straight from LaunchBox; none of their data is stored in this repository.

## How it's built

The whole app is one HTML file, [`app/Retro Game Library.html`](app/Retro%20Game%20Library.html), with no frameworks. It runs in two ways:

- **Browser version:** open the file in Chrome or Edge. It saves to a folder you choose using the File System Access API.
- **Desktop versions:** the same file wrapped with [Neutralinojs](https://neutralino.js.org), which gives it normal file access and lets it download the database and save box art. Each build is a single small file per system.

### Building the desktop versions

You'll need Node.js 18+, Python 3, `zip` and `tar`. `rcodesign` is optional and gives the Mac app an ad-hoc signature.

```sh
build/build.sh
```

The finished downloads appear in `release/`.

| Path | What it is |
| --- | --- |
| `app/` | The app (shared by all versions) |
| `lite/` | Neutralinojs config and runtime files |
| `build/` | Build script, read-me generator, Windows icon and details |
| `icons/` | App icons |
| `docs/` | Read-me for the browser version |

## Reporting problems

Found a bug or have an idea? [Open an issue](../../issues) and say which system you're on.

## Credits

Retro Game Library 1.0 · @VirtualJames 2026

Made with [Claude Code](https://claude.com/claude-code). I didn't code this one myself: I designed it, tested it and told Claude what my collection needed.

Released under the [MIT Licence](LICENSE).
