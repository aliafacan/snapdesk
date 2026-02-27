"""
desktopok.themes.dark
~~~~~~~~~~~~~~~~~~~~~
Koyu tema — Profesyonel Linux stili.
"""

DARK = """
/* ══════════════════════════════════════════════════════
   DesktopOK  ·  Koyu Tema
   Palet: slate-900 tabanı, yeşil vurgu
   ══════════════════════════════════════════════════════ */

* {
    font-family: 'Ubuntu', 'Inter', 'Segoe UI', sans-serif;
    font-size: 13px;
}

QWidget {
    background-color: #0f1117;
    color: #e2e8f0;
}

QWidget#Root {
    background-color: #0f1117;
}

/* ── Başlık Çubuğu ───────────────────────────────────── */
QFrame#Header {
    background: #141920;
    border-bottom: 1px solid #1e2a1e;
    border-radius: 0px;
}

QLabel#AppName {
    color: #4ade80;
    font-size: 20px;
    font-weight: 700;
    letter-spacing: -0.5px;
}

QLabel#AppSub {
    color: #4b5563;
    font-size: 11px;
    letter-spacing: 0.2px;
}

/* ── Tablo ───────────────────────────────────────────── */
QTableWidget {
    background-color: #0f1117;
    color: #cbd5e1;
    border: none;
    border-top: 1px solid #1e293b;
    gridline-color: #1e293b;
    selection-background-color: #14532d;
    selection-color: #ffffff;
    alternate-background-color: #111827;
    outline: none;
}
QTableWidget::item {
    padding: 6px 12px;
    border: none;
    border-bottom: 1px solid #1a2035;
}
QTableWidget::item:selected {
    background-color: #14532d;
    color: #ffffff;
}
QHeaderView {
    background: #111827;
}
QHeaderView::section {
    background-color: #111827;
    color: #6b7280;
    padding: 8px 12px;
    border: none;
    border-bottom: 2px solid #16a34a;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.8px;
    text-transform: uppercase;
}
QScrollBar:vertical {
    background: #111827;
    width: 6px;
    border-radius: 3px;
}
QScrollBar::handle:vertical {
    background: #374151;
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
    background: #0d1117;
    border-top: 1px solid #1e293b;
}

/* ── Ortak Buton ─────────────────────────────────────── */
QPushButton {
    background: #1e293b;
    color: #94a3b8;
    border: 1px solid #334155;
    border-radius: 7px;
    padding: 8px 16px;
    font-weight: 600;
    font-size: 12px;
    min-width: 96px;
}
QPushButton:hover {
    background: #1e3a2f;
    border-color: #16a34a;
    color: #4ade80;
}
QPushButton:pressed {
    background: #14532d;
    color: #ffffff;
}
QPushButton:disabled {
    background: #0f172a;
    color: #374151;
    border-color: #1e293b;
}

/* ── Kaydet ─────────────────────────────────────────── */
QPushButton#BtnSave {
    background: #14532d;
    border-color: #16a34a;
    color: #4ade80;
    font-weight: 700;
}
QPushButton#BtnSave:hover {
    background: #166534;
    border-color: #4ade80;
    color: #ffffff;
}

/* ── Geri Yükle ─────────────────────────────────────── */
QPushButton#BtnRestore {
    background: #1e3a5f;
    border-color: #2563eb;
    color: #93c5fd;
}
QPushButton#BtnRestore:hover {
    background: #1d4ed8;
    border-color: #93c5fd;
    color: #ffffff;
}

/* ── Sil ─────────────────────────────────────────────── */
QPushButton#BtnDelete {
    background: #450a0a;
    border-color: #b91c1c;
    color: #fca5a5;
}
QPushButton#BtnDelete:hover {
    background: #7f1d1d;
    border-color: #f87171;
    color: #ffffff;
}

/* ── Küçük Butonlar (Dil / Tema) ────────────────────── */
QPushButton#SmallBtn {
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 6px;
    color: #64748b;
    font-size: 11px;
    font-weight: 700;
    padding: 4px 10px;
    min-width: 48px;
}
QPushButton#SmallBtn:hover {
    background: #1e3a2f;
    border-color: #16a34a;
    color: #4ade80;
}

/* ── Durum Çubuğu ────────────────────────────────────── */
QFrame#StatusBar {
    background: #0d1117;
    border-top: 1px solid #1e293b;
}
QLabel#StatusMsg {
    color: #374151;
    font-size: 11px;
}
QLabel#StatusRight {
    color: #1f2937;
    font-size: 11px;
}

/* ── İlerleme ────────────────────────────────────────── */
QProgressBar {
    background: #111827;
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
    background: #141920;
}
QDialog QLabel, QMessageBox QLabel, QInputDialog QLabel {
    color: #e2e8f0;
}
QLineEdit {
    background: #1e293b;
    color: #e2e8f0;
    border: 1px solid #334155;
    border-radius: 6px;
    padding: 6px 10px;
    selection-background-color: #14532d;
}
QLineEdit:focus {
    border-color: #16a34a;
}
"""
