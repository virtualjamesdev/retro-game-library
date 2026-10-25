#!/usr/bin/env bash
# Builds every desktop version of Retro Game Library into ./release
# Needs: Node.js 18+, Python 3, zip, tar. Optional: rcodesign (ad-hoc signs the Mac app).
# Usage: build/build.sh            (from the repository root)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
L="$ROOT/lite"; B="$L/dist/retro-game-library"
P="$ROOT/release/_stage"; O="$ROOT/release"
rm -rf "$O"; mkdir -p "$P"/{win,mac,linux,linux-arm64}

# 1. Tools and Neutralino binaries
(cd "$L" && npm install --no-audit --no-fund >/dev/null && [ -d bin ] || npx neu update)

# 2. Desktop index.html from the shared app
python3 build/make_lite_index.py "app/Retro Game Library.html" "$L/resources/index.html"

# 3. Single-file binaries
(cd "$L" && npx neu build --embed-resources)

# 4. Windows: one .exe with icon and file details
cp "$B/retro-game-library-win_x64.exe" "$P/win/Retro Game Library.exe"
NODE_PATH="$L/node_modules" node build/set_win_info.js "$P/win/Retro Game Library.exe" icons/icon.ico >/dev/null

# 5. Mac: universal .app bundle
A="$P/mac/Retro Game Library.app"; mkdir -p "$A/Contents/MacOS" "$A/Contents/Resources"
cp "$B/retro-game-library-mac_universal" "$A/Contents/MacOS/retro-game-library"; chmod +x "$A/Contents/MacOS/retro-game-library"
cp icons/icon.icns "$A/Contents/Resources/icon.icns"
cat > "$A/Contents/Info.plist" <<'PLIST'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>CFBundleName</key><string>Retro Game Library</string>
  <key>CFBundleDisplayName</key><string>Retro Game Library</string>
  <key>CFBundleIdentifier</key><string>com.virtualjames.retrogamelibrary</string>
  <key>CFBundleExecutable</key><string>retro-game-library</string>
  <key>CFBundleIconFile</key><string>icon.icns</string>
  <key>CFBundlePackageType</key><string>APPL</string>
  <key>CFBundleShortVersionString</key><string>1.2.0</string>
  <key>CFBundleVersion</key><string>1.2.0</string>
  <key>LSMinimumSystemVersion</key><string>12.0</string>
  <key>LSApplicationCategoryType</key><string>public.app-category.entertainment</string>
  <key>NSHighResolutionCapable</key><true/>
  <key>NSHumanReadableCopyright</key><string>@VirtualJames 2026</string>
  <key>NSAppTransportSecurity</key><dict><key>NSAllowsLocalNetworking</key><true/></dict>
</dict>
</plist>
PLIST
if command -v codesign >/dev/null && [ "$(uname)" = Darwin ]; then codesign --force --deep -s - "$A"
elif command -v rcodesign >/dev/null; then rcodesign sign "$A" >/dev/null 2>&1
else echo "Note: Mac app not signed (install rcodesign, or build on a Mac)"; fi

# 6. Linux PC and Raspberry Pi
for pair in "linux:linux_x64" "linux-arm64:linux_arm64"; do d=${pair%%:*}; b=${pair#*:}
  cp "$B/retro-game-library-$b" "$P/$d/retro-game-library"; chmod +x "$P/$d/retro-game-library"
  cp icons/icon.png "$P/$d/icon.png"
  cat > "$P/$d/Add to app menu.sh" <<'EOF'
#!/bin/sh
# Adds Retro Game Library to your applications menu. Run it again if you move the folder.
DIR="$(cd "$(dirname "$0")" && pwd)"
mkdir -p "$HOME/.local/share/applications"
cat > "$HOME/.local/share/applications/retro-game-library.desktop" <<DESK
[Desktop Entry]
Type=Application
Name=Retro Game Library
Comment=Catalogue the retro games you own
Exec="$DIR/retro-game-library"
Path=$DIR
Icon=$DIR/icon.png
Categories=Game;Utility;
Terminal=false
DESK
chmod +x "$HOME/.local/share/applications/retro-game-library.desktop"
echo "Done. Retro Game Library is now in your applications menu."
EOF
  chmod +x "$P/$d/Add to app menu.sh"
done

# 7. Read-mes and archives
python3 build/gen_readme_lite.py "$P"
pk(){ rm -rf "$P/_pkg"; mkdir -p "$P/_pkg/Retro Game Library"; cp -a "$P/$1/." "$P/_pkg/Retro Game Library/"; }
pk win;  (cd "$P/_pkg" && zip -qr -9 "$O/Retro Game Library Lite (Windows).zip" "Retro Game Library")
pk mac;  (cd "$P/_pkg" && zip -qry -9 "$O/Retro Game Library Lite (Mac).zip" "Retro Game Library")
pk linux; (cd "$P/_pkg" && tar -czf "$O/Retro Game Library Lite (Linux).tar.gz" "Retro Game Library")
pk linux-arm64; (cd "$P/_pkg" && tar -czf "$O/Retro Game Library Lite (Linux ARM64, Raspberry Pi).tar.gz" "Retro Game Library")
# Browser version
rm -rf "$P/_pkg"; mkdir -p "$P/_pkg/Retro Game Library"
cp "app/Retro Game Library.html" "$P/_pkg/Retro Game Library/"
cp "docs/READ ME FIRST (browser version).txt" "$P/_pkg/Retro Game Library/READ ME FIRST.txt"
(cd "$P/_pkg" && zip -qr -9 "$O/Retro Game Library (browser version).zip" "Retro Game Library")
rm -rf "$P"
ls -l "$O"
