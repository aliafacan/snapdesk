#!/bin/bash
# SnapDesk .deb paketi oluşturma scripti
# Kullanım: chmod +x build_deb.sh && ./build_deb.sh

set -e

NAME="snapdesk"
VERSION="1.0.0"
ARCH="all"
PKG="${NAME}_${VERSION}_${ARCH}"

# NTFS/exFAT disk izin sorununu önlemek için /tmp içinde build ediyoruz
TMPBUILD=$(mktemp -d /tmp/snapdesk_build.XXXXXX)
PKGDIR="${TMPBUILD}/${PKG}"
OUTDIR="$(pwd)/dist"

echo "==> SnapDesk .deb paketi oluşturuluyor: ${PKG}.deb"
echo "    Build dizini: ${PKGDIR}"

# Çıktı dizini
mkdir -p "${OUTDIR}"

# Dizin yapısı
install -d "${PKGDIR}/DEBIAN"
install -d "${PKGDIR}/usr/lib/${NAME}"
install -d "${PKGDIR}/usr/bin"
install -d "${PKGDIR}/usr/share/applications"
install -d "${PKGDIR}/usr/share/icons/hicolor/scalable/apps"

# Python kaynak kodları
cp -r snapdesk   "${PKGDIR}/usr/lib/${NAME}/snapdesk"
cp    main.py    "${PKGDIR}/usr/lib/${NAME}/main.py"

# İkon (SVG)
if [ -f "snapdesk.svg" ]; then
    cp snapdesk.svg "${PKGDIR}/usr/share/icons/hicolor/scalable/apps/snapdesk.svg"
fi

# Çalıştırılabilir wrapper
cat > "${PKGDIR}/usr/bin/${NAME}" << 'EOF'
#!/bin/bash
cd /usr/lib/snapdesk
exec python3 -m snapdesk "$@"
EOF
chmod 755 "${PKGDIR}/usr/bin/${NAME}"

# .desktop dosyası
cat > "${PKGDIR}/usr/share/applications/${NAME}.desktop" << EOF
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
cat > "${PKGDIR}/usr/share/doc/${NAME}/copyright" << EOF
Format: https://www.debian.org/doc/packaging-manuals/copyright-format/1.0/
Upstream-Name: snapdesk
Upstream-Contact: https://github.com/aliafacan

Files: *
License: MIT
EOF

# DEBIAN/control
cat > "${PKGDIR}/DEBIAN/control" << EOF
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
cat > "${PKGDIR}/DEBIAN/postinst" << 'EOF'
#!/bin/bash
set -e
if command -v gtk-update-icon-cache &>/dev/null; then
    gtk-update-icon-cache -f -t /usr/share/icons/hicolor || true
fi
if command -v update-desktop-database &>/dev/null; then
    update-desktop-database /usr/share/applications || true
fi
EOF
chmod 755 "${PKGDIR}/DEBIAN/postinst"

# DEBIAN/prerm
cat > "${PKGDIR}/DEBIAN/prerm" << 'EOF'
#!/bin/bash
set -e
EOF
chmod 755 "${PKGDIR}/DEBIAN/prerm"

# İzinleri ayarla (dpkg-deb zorunluluğu)
chmod 755 "${PKGDIR}/DEBIAN"
chmod 644 "${PKGDIR}/DEBIAN/control"
chmod 644 "${PKGDIR}/DEBIAN/copyright" 2>/dev/null || true

# Paket oluştur
dpkg-deb --build --root-owner-group "${PKGDIR}"

# Sonucu projeye kopyala, temp dizini temizle
cp "${TMPBUILD}/${PKG}.deb" "${OUTDIR}/${PKG}.deb"
rm -rf "${TMPBUILD}"

echo ""
echo "==> Tamamlandi: dist/${PKG}.deb"
echo ""
echo "Kurmak icin:"
echo "  sudo dpkg -i dist/${PKG}.deb"
echo "  sudo apt-get install -f   # bagimlilik eksikse"
