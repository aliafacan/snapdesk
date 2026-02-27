# SnapDesk

<p align="center">
  <a href="#turkce"><strong>🇹🇷 Türkçe</strong></a> &nbsp;|&nbsp;
  <a href="#english"><strong>🇬🇧 English</strong></a>
</p>

---

<a id="turkce"></a>

## 🇹🇷 Türkçe

> **Masaüstü düzen yöneticisi** — Linux Mint / Nemo için ikon konumlarını kaydedin ve tek tıkla geri yükleyin.

### Özellikler

- Masaüstü ikon pozisyonlarını anında kaydet ve geri yükle
- Koyu / Açık tema desteği
- Türkçe ve İngilizce arayüz
- Python `gi.repository.Gio` ile hızlı GIO metadata yazımı
- Cinnamon ile tam uyumlu

### Gereksinimler

| Paket | Versiyon |
|-------|----------|
| Linux Mint (Cinnamon) | 21+ |
| Python | 3.10+ |
| python3-pyqt6 | herhangi |
| python3-gi | herhangi |

### Dağıtım Uyumluluğu

| Dağıtım | Durum | Açıklama |
|---------|-------|----------|
| Linux Mint Cinnamon | ✅ Tam uyumlu | Birincil hedef platform |
| Manjaro Cinnamon | ✅ Çalışır | Nemo masaüstü mevcut |
| Fedora Cinnamon Spin | ✅ Çalışır | Nemo masaüstü mevcut |
| Debian + Cinnamon | ✅ Çalışır | Nemo masaüstü mevcut |
| Ubuntu (GNOME) | ❌ Çalışmaz | Nautilus kullanır |
| Linux Mint MATE/XFCE | ❌ Çalışmaz | Nemo masaüstü yok |
| Elementary OS | ❌ Çalışmaz | Pantheon masaüstü |

> **Kural:** Cinnamon masaüstü + Nemo gerektiren uygulamalarda çalışır.

### Kurulum

**1) .deb Paketi (Önerilen)**

```bash
wget https://github.com/aliafacan/snapdesk/releases/latest/download/snapdesk_1.0.0_all.deb
sudo apt install ./snapdesk_1.0.0_all.deb
```

Kurulumdan sonra Uygulama Menüsü'nde **SnapDesk** olarak görünür.

**2) Kaynak Koddan**

```bash
sudo apt install python3-pyqt6 python3-gi
git clone https://github.com/aliafacan/snapdesk.git
cd snapdesk
python3 -m snapdesk
```

### Nasıl Kullanılır?

1. Uygulamayı açın
2. **Kaydet** — Mevcut masaüstü düzenini kaydedin
3. **Geri Yükle** — Listeden bir düzen seçip butona basın
4. Nemo masaüstü otomatik yenilenir, ikonlar yerlerine gelir

> **Not:** Çöp Kutusu, Bilgisayar gibi sistem ikonlarının konumu Nemo tarafından ayrıca yönetilir.

### .deb Paketi Oluşturma

```bash
git clone https://github.com/aliafacan/snapdesk.git
cd snapdesk
chmod +x build_deb.sh
./build_deb.sh
# → dist/snapdesk_1.0.0_all.deb
```

### Düzen Dosyası Konumu

```
~/.local/share/snapdesk/layouts.json
```

---

<a id="english"></a>

## 🇬🇧 English

> **Desktop layout manager** — Save and restore Nemo icon positions with one click on Linux Mint.

### Features

- Save and restore desktop icon positions instantly
- Dark / Light theme toggle
- Turkish and English interface
- Fast GIO metadata writes via Python `gi.repository.Gio`
- Fully compatible with Cinnamon desktop

### Requirements

| Package | Version |
|---------|---------|
| Linux Mint (Cinnamon) | 21+ |
| Python | 3.10+ |
| python3-pyqt6 | any |
| python3-gi | any |

### Compatibility

| Distribution | Status | Notes |
|--------------|--------|-------|
| Linux Mint Cinnamon | ✅ Full support | Primary target platform |
| Manjaro Cinnamon | ✅ Works | Nemo desktop available |
| Fedora Cinnamon Spin | ✅ Works | Nemo desktop available |
| Debian + Cinnamon | ✅ Works | Nemo desktop available |
| Ubuntu (GNOME) | ❌ Does not work | Uses Nautilus instead |
| Linux Mint MATE/XFCE | ❌ Does not work | No Nemo desktop |
| Elementary OS | ❌ Does not work | Pantheon desktop |

> **Rule of thumb:** Works on any distro using **Cinnamon desktop + Nemo** as the desktop manager.

### Installation

**1) .deb Package (Recommended)**

```bash
wget https://github.com/aliafacan/snapdesk/releases/latest/download/snapdesk_1.0.0_all.deb
sudo apt install ./snapdesk_1.0.0_all.deb
```

After installation, **SnapDesk** will appear in the Application Menu.

**2) From Source**

```bash
sudo apt install python3-pyqt6 python3-gi
git clone https://github.com/aliafacan/snapdesk.git
cd snapdesk
python3 -m snapdesk
```

### How to Use

1. Open the application
2. **Save** — Save the current desktop layout and give it a name
3. **Restore** — Select a layout from the list and click Restore
4. The Nemo desktop refreshes automatically and icons snap into place

> **Note:** System icons (Trash, Computer) are managed separately by Nemo.

### Building the .deb Package

```bash
git clone https://github.com/aliafacan/snapdesk.git
cd snapdesk
chmod +x build_deb.sh
./build_deb.sh
# → dist/snapdesk_1.0.0_all.deb
```

### Layout File Location

```
~/.local/share/snapdesk/layouts.json
```

---

## License / Lisans

MIT License — Free to use, distribute, and modify.

---

## Developer / Geliştirici

**Ali Afacan** — Electrical & Electronics Engineer / Elektrik Elektronik Mühendisi

[![GitHub](https://img.shields.io/badge/GitHub-aliafacan-181717?logo=github)](https://github.com/aliafacan)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-aliafacan-0A66C2?logo=linkedin)](https://linkedin.com/in/aliafacan)
[![Web](https://img.shields.io/badge/Web-aliafacan.com.tr-4ade80?logo=firefox)](https://aliafacan.com.tr)
