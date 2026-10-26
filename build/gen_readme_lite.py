import os
COMMON_TAIL = """
SETTING UP (ONE TIME)
1. Your library folder: click "Choose folder…" and pick (or make) a folder
   for your collection. Put it inside your Google Drive, OneDrive, iCloud
   Drive or Dropbox folder and your collection is backed up online
   automatically.
2. The game database: click "Download the game database". It's about 100 MB
   and takes a minute or two.
3. Click "Open my library".

Next time, it opens straight into your library.


ADDING A GAME
1. Click "+ Add game".
2. Pick the system from the list.
3. Start typing the title. Matching games appear with their box art.
   Pick yours and the cover, description, year and publisher fill in by
   themselves. If you type the full title and save, it's looked up for you.
4. Set what you have (loose, boxed, complete in box, sealed
   or digital), the condition
   and any notes.
5. Own it on other machines too? Under "Also own it on", pick each extra
   system and click "Add system". Each one gets its own entry with the right
   box art for that machine.
6. Click "Save game".

The cover is downloaded and saved into your library folder (as a small
picture, about 30-50 KB each), so it works offline and is backed up with
everything else.

Bought it digitally (GOG, Steam, eShop and so on)? Choose "Digital" under
"What you have" and pick the store.
Not in the database? Save it anyway and drop your own photo of the box onto
the picture area.
No box art? Open the game and click "Look up box art" to pick from the
matching games in the databases, or "Find online…" to search the web. Right-click the
picture you want, choose "Copy image", then press Ctrl+V (Cmd+V on a Mac)
in the app. You can also drag a picture straight from a web page.
ZX Spectrum and ZX81: rare games LaunchBox doesn't have are also looked up
in ZXDB, the Spectrum community's database, with cover scans and loading
screens.
Two copies? Open the game and click "+ Another copy".
Found another version later? Open the game and click "+ Same game, another
system".
The drop-down next to the search box shows only duplicates, games on
several systems, physical or digital games only, or games missing box art.


HARDWARE
Click "Hardware" at the top to keep track of your consoles, computers,
handhelds, controllers and accessories: model and version, colour or
edition, region, serial number, boxed or not, condition, whether it works,
and any mods or repairs. Add a photo of your own machine (drop, paste or
"Choose picture…"). Filter by type or by "Needs repair or not working".
Hardware is saved in library.json with your games, gets its own
"Retro Game Library hardware.csv", its own sheet in the Excel export and
its own section in the PDF.

IMPORTING FROM A SPREADSHEET
Already have your collection in a spreadsheet? Open "Backup & tools" and,
under "Import games", click "Template (Excel)…" to get a ready-made sheet
with drop-down lists. Put one game per row (only Title and System are
needed), save it, then click "Import spreadsheet…". Excel (.xlsx) and CSV
both work, and so do most spreadsheets with a Title and System column.
Short system names are fine: Spectrum, C64, Mega Drive, SNES, PS2 and so on.
Box art and descriptions are looked up as the games are added (using the
first match), so check any you're unsure of with "Look up box art".

YOUR FILES
Everything is saved straight away into your library folder:
- library.json                 your full collection
- Retro Game Library.csv       the same list as a spreadsheet (Excel, Numbers,
                               LibreOffice, Google Sheets)
- covers                       all the box art and your own pictures
- backups                      a dated copy for each day you make changes
- Retro Game Library hardware.csv   your hardware list (once you add some)

The top of the app shows the folder it's "Saving to". Click it to move your
library somewhere else; if the new folder is empty, everything is copied
across.

To restore, open "Backup & tools" and choose a file from the backups folder.
Under "Export" you can also save your collection as:
- a PDF catalogue with the box art, grouped by system (handy on your phone
  when you're out hunting for games and have no signal)
- an Excel workbook, with a sheet counting games per system
- a CSV file, the simplest no-frills copy

The same library folder works on Windows, Mac and Linux, so you can share
one collection between computers through Google Drive, OneDrive or Dropbox.
(Use it on one computer at a time.)
{portable}

KEEPING THE DATABASE UP TO DATE
LaunchBox adds new games every day. When your copy is a couple of weeks old
and a newer one is out, the app offers "Update now". You can also update
any time from "Backup & tools".


PRIVACY
No account, no tracking, nothing uploaded. The app only goes online to
download the game database and box art from LaunchBox.


ABOUT
Retro Game Library is for cataloguing the games you own. It isn't
a game launcher and is in no way a replacement for LaunchBox, which is
brilliant for organising and playing your games on PC. Check it out at
launchbox-app.com.

CREDITS
Retro Game Library 1.4.1  ·  @VirtualJames 2026
Game information and box art: LaunchBox Games Database
(gamesdb.launchbox-app.com), built by the LaunchBox community.
This app isn't made by, or affiliated with, LaunchBox.
ZX Spectrum and ZX81 games that LaunchBox doesn't have are looked up in
ZXDB, the open Spectrum database (zxinfo.dk, spectrumcomputing.co.uk).
Made with Claude Code. Built with Neutralinojs.
"""
PORTABLE = """

PORTABLE
The app is a single small file. Nothing is installed, so you can run it from
a USB stick or move the folder anywhere. Its settings live in a "Retro Game
Library Data" folder it makes next to itself.

The 100 MB game database is kept in one place on your computer
(%LOCALAPPDATA%\\Retro Game Library on Windows, ~/.local/share/Retro Game
Library on Linux), so every copy and version of the app shares the same file.
Updating to a new version? Just replace the app; you won't download the
database again. Delete that folder to free the space if you stop using the app.
"""
PORTABLE_MAC = """

WHERE THE APP KEEPS ITS SETTINGS
Settings and the game database are kept in
~/Library/Application Support/Retro Game Library. Delete that folder to
start the app from scratch (your library folder isn't touched).
"""
HEAD = """RETRO GAME LIBRARY  ({os})
Catalogue the games you own: carts, tapes, discs, boxes and digital copies,
from the Atari 2600 and ZX Spectrum right up to PS5 and Switch 2.
Box art and descriptions come from the free LaunchBox Games Database.
You don't need LaunchBox installed.

"""
WIN = """WHAT YOU NEED
Windows 10 or 11. The app uses the Microsoft Edge WebView2 component that
comes with Windows 11 and most Windows 10 PCs. If the app doesn't open, get
the free "Evergreen Bootstrapper" from
   https://developer.microsoft.com/microsoft-edge/webview2/
and run it, then try again.

INSTALLING
1. Unzip this folder anywhere you like, for example Documents, C:\\Games or a
   USB stick.
2. Double-click "Retro Game Library.exe".
3. Windows may show "Windows protected your PC", because the app isn't from
   a big publisher. Click "More info", then "Run anyway". You only see this
   the first time.
Tip: right-click "Retro Game Library.exe" and choose "Send to > Desktop
(create shortcut)" or "Pin to Start".
Example library folders:
   G:\\My Drive\\Retro Game Library
   C:\\Users\\you\\OneDrive\\Retro Game Library
"""
MAC = """WHAT YOU NEED
macOS 12 Monterey or later. Works on both Apple Silicon and Intel Macs.

INSTALLING
1. Double-click the zip to unzip it (Safari may already have done this).
2. Drag "Retro Game Library" into your Applications folder.
3. Open it. Because the app isn't from the App Store or a registered Apple
   developer, macOS blocks it the first time:
   - Click "Done" (or "OK") on the warning.
   - Open System Settings > Privacy & Security, scroll down and click
     "Open Anyway" next to Retro Game Library, then confirm.
   You only need to do this once.
   On older macOS you can instead right-click the app, choose "Open", then
   "Open".
4. If macOS says the app "is damaged and can't be opened", it's macOS being
   cautious with downloads, not real damage. Open Terminal and run:
       xattr -cr "/Applications/Retro Game Library.app"
   then open the app again.
Example library folders:
   iCloud Drive > Retro Game Library
   Google Drive > My Drive > Retro Game Library
"""
LIN = """WHAT YOU NEED
A Linux desktop with WebKitGTK and curl, which most desktops already have.
If the app doesn't open, install WebKitGTK:
   Ubuntu, Mint, Debian, Pop!_OS:  sudo apt install libwebkit2gtk-4.1-0
   Fedora:                         sudo dnf install webkit2gtk4.1
   Arch, Manjaro, SteamOS:         sudo pacman -S webkit2gtk-4.1
There are two downloads: "Linux" for normal PCs (x86_64) and
"Linux ARM64" for a Raspberry Pi 4 or 5 running 64-bit Raspberry Pi OS.

INSTALLING
1. Extract the archive anywhere, for example ~/Apps/Retro Game Library or a
   USB stick.
2. Run "retro-game-library" (double-click it, or from a terminal:
       ./retro-game-library
   ). If your file manager opens it as text or does nothing, right-click it,
   open Properties and tick "Allow executing file as program".
3. Optional: run "Add to app menu.sh" once to add Retro Game Library to your
   applications menu. Run it again if you move the folder.
Example library folders:
   ~/Dropbox/Retro Game Library
   ~/Google Drive/Retro Game Library (if you sync Drive with Insync or similar)
"""
import sys
OUT=sys.argv[1]
for folder, osname, inst, port, nl in [
    ("win", "Windows", WIN, PORTABLE, "\r\n"),
    ("mac", "Mac", MAC, PORTABLE_MAC, "\n"),
    ("linux", "Linux", LIN, PORTABLE, "\n"),
    ("linux-arm64", "Linux ARM64 / Raspberry Pi", LIN, PORTABLE, "\n")]:
    txt = HEAD.format(os=osname) + inst + COMMON_TAIL.replace("{portable}", port)
    open(os.path.join(OUT, folder, "READ ME FIRST.txt"), "w", newline="").write(txt.replace("\n", nl))
print("readmes ok")
