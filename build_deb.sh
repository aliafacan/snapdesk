#!/bin/bash
# SnapDesk .deb paketi oluşturma scripti
# Kullanım: chmod +x build_deb.sh && ./build_deb.sh

set -e

NAME="snapdesk"
VERSION="1.0.0"
ARCH="all"
PKG="${NAME}_${VERSION}_${ARCH}"
DIST="dist"

echo "==> SnapDesk .deb paketi oluşturuluyor: ${PKG}.deb"

# Temizle
rm -rf "${DIST}/${PKG}"

# Dizin yapısı
install -d "${DIST}/${PKG}/DEBIAN"
install -d "${DIST}/${PKG}/usr/lib/${NAME}"
install -d "${DIST}/${PKG}/usr/bin"
install -d "${DIST}/${PKG}/usr/share/applications"
install -d "${DIST}/${PKG}/usr/share/icons/hicolor/256x256/apps"
install -d "${DIST}/${PKG}/usr/share/doc/${NAME}"

# Python kaynak kodları
cp -r snapdesk          "${DIST}/${PKG}/usr/lib/${NAME}/snapdesk"
cp    main.py           "${DIST}/${PKG}/usr/lib/${NAME}/main.py"

# İkon
if [ -f "snapdesk.png" ]; then
    cp snapdesk.png "${DIST}/${PKG}/usr/share/icons/hicolor/256x256/apps/snapdesk.png"
fi

# Çalıştırılabilir wrapper
cat > "${DIST}/${PKG}/usr/bin/${NAME}" << 'EOF'
#!/bin/bash
cd /usr/lib/snapdesk
exec python3 -m snapdesk "$@"
EOF
chmod 755 "${DIST}/${PKG}/usr/bin/${NAME}"

# .desktop dosyası
cat > "${DIST}/${PKG}/usr/share/applications/${NAME}.desktop" << EOF
[Desktop Entry]
Name=SnapDesk
GenericName=Desktop Layout Manager
GenericName[tr]=Masaüstü Düzen Yöneticisi
Comment=Save and restore Nemo desktop icon positions
Comment[tr]=Nemo masaüstü ikon konumlarını kaydedin ve geri yükleyin
Exec=snapdesk
Icon=snapdesk
Terminal=false
Type=Application
Categories=Utility;Accessibility;
Keywords=desktop;icon;layout;nemo;mint;
StartupNotify=true
EOF

# Copyright
cat > "${DIST}/${PKG}/usr/share/doc/${NAME}/copyright" << EOF
Format: https://www.debian.org/doc/packaging-manuals/copyright-format/1.0/
Upstream-Name: snapdesk
Upstream-Contact: https://github.com/KULLANICI_ADI/snapdesk

Files: *
License: MIT

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
EOF

# DEBIAN/control
cat > "${DIST}/${PKG}/DEBIAN/control" << EOF
Package: ${NAME}
Version: ${VERSION}
Section: utils
Priority: optional
Architecture: ${ARCH}
Depends: python3 (>= 3.10), python3-pyqt6, python3-gi
Maintainer: Ali Afacan <https://github.com/aliafacan>
Description: Desktop Layout Manager for Linux Mint
 SnapDesk saves and restores Nemo desktop icon positions.
 Supports dark/light themes and Turkish/English interface.
 Works with Cinnamon desktop environment.
EOF

# DEBIAN/postinst
cat > "${DIST}/${PKG}/DEBIAN/postinst" << 'EOF'
#!/bin/bash
set -e
# İkon cache güncelle
if command -v gtk-update-icon-cache &>/dev/null; then
    gtk-update-icon-cache -f -t /usr/share/icons/hicolor || true
fi
# .desktop veritabanı güncelle
if command -v update-desktop-database &>/dev/null; then
    update-desktop-database /usr/share/applications || true
fi
EOF
chmod 755 "${DIST}/${PKG}/DEBIAN/postinst"

# DEBIAN/prerm
cat > "${DIST}/${PKG}/DEBIAN/prerm" << 'EOF'
#!/bin/bash
set -e
EOF
chmod 755 "${DIST}/${PKG}/DEBIAN/prerm"

# Paket oluştur
dpkg-deb --build --root-owner-group "${DIST}/${PKG}"

echo ""
echo "==> Tamamlandı: ${DIST}/${PKG}.deb"
echo ""
echo "Kurmak için:"
echo "  sudo dpkg -i ${DIST}/${PKG}.deb"
echo "  sudo apt-get install -f   # bağımlılık eksikse"
