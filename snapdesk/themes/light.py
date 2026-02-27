"""
desktopok.themes.light
~~~~~~~~~~~~~~~~~~~~~~
Açık tema — Temiz, profesyonel Linux stili.
"""

LIGHT = """
/* ══════════════════════════════════════════════════════
   DesktopOK  ·  Açık Tema
   Palet: slate-50 tabanı, yeşil vurgu
   ══════════════════════════════════════════════════════ */

* {
    font-family: 'Ubuntu', 'Inter', 'Segoe UI', sans-serif;
    font-size: 13px;
}

QWidget {
    background-color: #f8fafc;
    color: #0f172a;
}

QWidget#Root {
    background-color: #f8fafc;
}

/* ── Başlık Çubuğu ───────────────────────────────────── */
QFrame#Header {
    background: #ffffff;
    border-bottom: 1px solid #e2e8f0;
    border-radius: 0px;
}

QLabel#AppName {
    color: #16a34a;
    font-size: 20px;
    font-weight: 700;
    letter-spacing: -0.5px;
}

QLabel#AppSub {
    color: #94a3b8;
    font-size: 11px;
    letter-spacing: 0.2px;
}

/* ── Tablo ───────────────────────────────────────────── */
QTableWidget {
    background-color: #ffffff;
    color: #1e293b;
    border: none;
    border-top: 1px solid #e2e8f0;
    gridline-color: #f1f5f9;
    selection-background-color: #dcfce7;
    selection-color: #14532d;
    alternate-background-color: #f8fafc;
    outline: none;
}
QTableWidget::item {
    padding: 6px 12px;
    border: none;
    border-bottom: 1px solid #f1f5f9;
}
QTableWidget::item:selected {
    background-color: #dcfce7;
    color: #14532d;
}
QHeaderView {
    background: #f8fafc;
}
QHeaderView::section {
    background-color: #f8fafc;
    color: #94a3b8;
    padding: 8px 12px;
    border: none;
    border-bottom: 2px solid #16a34a;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.8px;
    text-transform: uppercase;
}
QScrollBar:vertical {
    background: #f1f5f9;
    width: 6px;
    border-radius: 3px;
}
QScrollBar::handle:vertical {
    background: #cbd5e1;
    border-radius: 3px;
    min-height: 24px;
}
QScrollBar::handle:vertical:hover {
    background: #16a34a;
}
QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical { height: 0; }

/* ── Alt Araç Çubuğu ─────────────────────────────────── */
QFrame#Toolbar {
    background: #f8fafc;
    border-top: 1px solid #e2e8f0;
}

/* ── Ortak Buton ─────────────────────────────────────── */
QPushButton {
    background: #f1f5f9;
    color: #475569;
    border: 1px solid #e2e8f0;
    border-radius: 7px;
    padding: 8px 16px;
    font-weight: 600;
    font-size: 12px;
    min-width: 96px;
}
QPushButton:hover {
    background: #f0fdf4;
    border-color: #16a34a;
    color: #15803d;
}
QPushButton:pressed {
    background: #dcfce7;
    color: #14532d;
    border-color: #15803d;
}
QPushButton:disabled {
    background: #f8fafc;
    color: #cbd5e1;
    border-color: #f1f5f9;
}

/* ── Kaydet ─────────────────────────────────────────── */
QPushButton#BtnSave {
    background: #f0fdf4;
    border-color: #16a34a;
    color: #15803d;
    font-weight: 700;
}
QPushButton#BtnSave:hover {
    background: #dcfce7;
    border-color: #15803d;
    color: #14532d;
}

/* ── Geri Yükle ─────────────────────────────────────── */
QPushButton#BtnRestore {
    background: #eff6ff;
    border-color: #3b82f6;
    color: #1d4ed8;
}
QPushButton#BtnRestore:hover {
    background: #dbeafe;
    border-color: #1d4ed8;
    color: #1e3a8a;
}

/* ── Sil ─────────────────────────────────────────────── */
QPushButton#BtnDelete {
    background: #fff1f2;
    border-color: #f43f5e;
    color: #be123c;
}
QPushButton#BtnDelete:hover {
    background: #ffe4e6;
    border-color: #be123c;
    color: #881337;
}

/* ── Küçük Butonlar ─────────────────────────────────── */
QPushButton#SmallBtn {
    background: #f1f5f9;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    color: #94a3b8;
    font-size: 11px;
    font-weight: 700;
    padding: 4px 10px;
    min-width: 48px;
}
QPushButton#SmallBtn:hover {
    background: #f0fdf4;
    border-color: #16a34a;
    color: #15803d;
}

/* ── Durum Çubuğu ────────────────────────────────────── */
QFrame#StatusBar {
    background: #ffffff;
    border-top: 1px solid #e2e8f0;
}
QLabel#StatusMsg {
    color: #94a3b8;
    font-size: 11px;
}
QLabel#StatusRight {
    color: #cbd5e1;
    font-size: 11px;
}

/* ── İlerleme ────────────────────────────────────────── */
QProgressBar {
    background: #e2e8f0;
    border: none;
    border-radius: 2px;
    max-height: 2px;
    color: transparent;
}
QProgressBar::chunk {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
        stop:0 #16a34a, stop:1 #4ade80);
    border-radius: 2px;
}

/* ── Dialoglar ───────────────────────────────────────── */
QDialog, QMessageBox, QInputDialog {
    background: #ffffff;
}
QDialog QLabel, QMessageBox QLabel, QInputDialog QLabel {
    color: #0f172a;
}
QLineEdit {
    background: #f8fafc;
    color: #0f172a;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    padding: 6px 10px;
    selection-background-color: #dcfce7;
    selection-color: #14532d;
}
QLineEdit:focus {
    border-color: #16a34a;
}
"""
