"""
desktopok.ui.main_window
~~~~~~~~~~~~~~~~~~~~~~~~
SnapDesk - Ana uygulama penceresi.
"""

import os
from datetime import datetime

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QFrame,
    QLabel, QPushButton, QTableWidget, QTableWidgetItem,
    QHeaderView, QAbstractItemView, QProgressBar,
    QMessageBox, QInputDialog, QLineEdit,
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QColor, QIcon

from snapdesk.core.storage import load as _load, save as _save
from snapdesk.core.workers import SaveWorker, RestoreWorker
from snapdesk.i18n.tr import TR
from snapdesk.i18n.en import EN
from snapdesk.themes.dark  import DARK
from snapdesk.themes.light import LIGHT

_LANGS   = {"tr": TR, "en": EN}
_THEMES  = {"dark": DARK, "light": LIGHT}

# Durum mesajı renkleri — tema × tip
_STATUS_COLORS = {
    "dark" : {"ok": "#4ade80", "info": "#93c5fd", "warn": "#fca5a5", "idle": "#374151"},
    "light": {"ok": "#15803d", "info": "#1d4ed8", "warn": "#be123c", "idle": "#94a3b8"},
}


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setObjectName("Root")
        self._lang   = "tr"
        self._theme  = "dark"
        self._worker = None
        self._build()
        self._refresh()

    # ── Translation ──────────────────────────────────────────────────────────
    def _(self, key, **kw):
        s = _LANGS[self._lang].get(key, key)
        return s.format(**kw) if kw else s

    def _sc(self, kind):
        return _STATUS_COLORS[self._theme][kind]

    # ── Build UI ─────────────────────────────────────────────────────────────
    def _build(self):
        self.setWindowTitle(self._("win_title"))
        self.setMinimumSize(760, 500)
        self.resize(860, 580)
        self._apply_theme()

        root = QVBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        root.addWidget(self._mk_header())
        root.addWidget(self._mk_progress())
        root.addWidget(self._mk_table(), stretch=1)
        root.addWidget(self._mk_toolbar())
        root.addWidget(self._mk_statusbar())

    # ── Header ───────────────────────────────────────────────────────────────
    def _mk_header(self):
        frame = QFrame()
        frame.setObjectName("Header")
        frame.setFixedHeight(64)
        lay = QHBoxLayout(frame)
        lay.setContentsMargins(20, 0, 14, 0)

        col = QVBoxLayout()
        col.setSpacing(2)
        self._lbl_name = QLabel(self._("header"))
        self._lbl_name.setObjectName("AppName")
        self._lbl_name.setFont(QFont("Ubuntu", 18, QFont.Weight.Bold))

        self._lbl_sub = QLabel(self._("subheader"))
        self._lbl_sub.setObjectName("AppSub")
        col.addWidget(self._lbl_name)
        col.addWidget(self._lbl_sub)

        lay.addLayout(col)
        lay.addStretch()

        # Sag - Dil + Tema butonlari
        self._btn_lang  = QPushButton(self._("lang_btn"))
        self._btn_theme = QPushButton(self._("theme_to_light"))
        for b in [self._btn_lang, self._btn_theme]:
            b.setObjectName("SmallBtn")
            b.setFixedHeight(26)
            lay.addWidget(b, alignment=Qt.AlignmentFlag.AlignVCenter)
        lay.setSpacing(6)

        self._btn_lang.clicked.connect(self._toggle_lang)
        self._btn_theme.clicked.connect(self._toggle_theme)
        return frame

    def _mk_progress(self):
        self._progress = QProgressBar()
        self._progress.setRange(0, 0)
        self._progress.setVisible(False)
        self._progress.setFixedHeight(3)
        return self._progress

    # ── Table ─────────────────────────────────────────────────────────────────
    def _mk_table(self):
        self._table = QTableWidget(0, 4)
        self._update_headers()
        hh = self._table.horizontalHeader()
        hh.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        hh.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        hh.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        hh.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        self._table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self._table.setAlternatingRowColors(True)
        self._table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self._table.verticalHeader().setVisible(False)
        self._table.setShowGrid(False)
        self._table.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        return self._table

    def _update_headers(self):
        self._table.setHorizontalHeaderLabels([
            self._("col_name"), self._("col_date"),
            self._("col_count"), self._("col_status"),
        ])

    # ── Toolbar ───────────────────────────────────────────────────────────────
    def _mk_toolbar(self):
        frame = QFrame()
        frame.setObjectName("Toolbar")
        frame.setFixedHeight(52)
        lay = QHBoxLayout(frame)
        lay.setContentsMargins(14, 0, 14, 0)
        lay.setSpacing(8)

        self._btn_save    = QPushButton(self._("btn_save"))
        self._btn_restore = QPushButton(self._("btn_restore"))
        self._btn_rename  = QPushButton(self._("btn_rename"))
        self._btn_delete  = QPushButton(self._("btn_delete"))
        self._btn_exit    = QPushButton(self._("btn_exit"))

        self._btn_save.setObjectName("BtnSave")
        self._btn_restore.setObjectName("BtnRestore")
        self._btn_delete.setObjectName("BtnDelete")

        self._btn_save.clicked.connect(self._save)
        self._btn_restore.clicked.connect(self._restore)
        self._btn_rename.clicked.connect(self._rename)
        self._btn_delete.clicked.connect(self._delete)
        self._btn_exit.clicked.connect(self.close)

        for b in [self._btn_save, self._btn_restore, self._btn_rename,
                  self._btn_delete, self._btn_exit]:
            lay.addWidget(b)
        return frame

    # ── Status bar ────────────────────────────────────────────────────────────
    def _mk_statusbar(self):
        frame = QFrame()
        frame.setObjectName("StatusBar")
        frame.setFixedHeight(28)
        lay = QHBoxLayout(frame)
        lay.setContentsMargins(14, 0, 14, 0)

        self._lbl_status = QLabel()
        self._lbl_status.setObjectName("StatusMsg")
        self._lbl_desktop = QLabel()
        self._lbl_desktop.setObjectName("StatusRight")

        lay.addWidget(self._lbl_status)
        lay.addStretch()
        lay.addWidget(self._lbl_desktop)
        return frame

    # ── Theme / Lang ──────────────────────────────────────────────────────────
    def _apply_theme(self):
        self.setStyleSheet(_THEMES[self._theme])

    def _toggle_theme(self):
        self._theme = "light" if self._theme == "dark" else "dark"
        next_key = "theme_to_light" if self._theme == "dark" else "theme_to_dark"
        self._btn_theme.setText(self._(next_key))
        self._apply_theme()
        self._refresh()

    def _toggle_lang(self):
        self._lang = "en" if self._lang == "tr" else "tr"
        self._retranslate()

    def _retranslate(self):
        self.setWindowTitle(self._("win_title"))
        self._lbl_name.setText(self._("header"))
        self._lbl_sub.setText(self._("subheader"))
        self._btn_lang.setText(self._("lang_btn"))
        next_key = "theme_to_light" if self._theme == "dark" else "theme_to_dark"
        self._btn_theme.setText(self._(next_key))
        self._btn_save.setText(self._("btn_save"))
        self._btn_restore.setText(self._("btn_restore"))
        self._btn_rename.setText(self._("btn_rename"))
        self._btn_delete.setText(self._("btn_delete"))
        self._btn_exit.setText(self._("btn_exit"))
        self._update_headers()
        self._refresh()

    # ── Helpers ───────────────────────────────────────────────────────────────
    def _desktop(self):
        return os.path.expanduser("~/Desktop")

    def _desktop_items(self):
        p = self._desktop()
        return [os.path.join(p, f) for f in os.listdir(p)
                if not f.startswith(".")] if os.path.isdir(p) else []

    def _set_status(self, msg, kind="idle"):
        self._lbl_status.setText(msg)
        self._lbl_status.setStyleSheet(
            f"color: {self._sc(kind)}; font-size: 11px;"
        )

    def _set_desktop_lbl(self):
        n = len(self._desktop_items())
        c = _STATUS_COLORS[self._theme]["idle"]
        self._lbl_desktop.setText(self._("desktop_label", n=n))
        self._lbl_desktop.setStyleSheet(f"color: {c}; font-size: 11px;")

    def _set_busy(self, busy):
        self._progress.setVisible(busy)
        for b in [self._btn_save, self._btn_restore,
                  self._btn_rename, self._btn_delete]:
            b.setEnabled(not busy)

    # ── List refresh ──────────────────────────────────────────────────────────
    def _refresh(self):
        saves = _load()
        self._table.setRowCount(0)

        ok_color   = self._sc("ok")
        warn_color = self._sc("warn")
        text_color = "#e2e8f0" if self._theme == "dark" else "#1e293b"
        dim_color  = "#4b5563" if self._theme == "dark" else "#94a3b8"

        for key in reversed(list(saves)):
            e   = saves[key]
            cnt = len(e.get("layout", {}))
            r   = self._table.rowCount()
            self._table.insertRow(r)

            ni = QTableWidgetItem(f"  {e.get('name', key)}")
            ni.setData(Qt.ItemDataRole.UserRole, key)
            ni.setFont(QFont("Ubuntu", 12, QFont.Weight.Medium))
            ni.setForeground(QColor(text_color))

            di  = QTableWidgetItem(f"  {e.get('saved_at', '')}")
            di.setForeground(QColor(dim_color))

            ci  = QTableWidgetItem(f"  {cnt}")
            ci.setTextAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)
            ci.setForeground(QColor(dim_color))

            stat = self._("item_ready") if cnt else self._("item_empty")
            si   = QTableWidgetItem(f"  {stat}")
            si.setForeground(QColor(ok_color if cnt else warn_color))

            for col, item in enumerate([ni, di, ci, si]):
                item.setTextAlignment(Qt.AlignmentFlag.AlignVCenter
                                      | (Qt.AlignmentFlag.AlignHCenter if col == 2
                                         else Qt.AlignmentFlag.AlignLeft))
                self._table.setItem(r, col, item)

        self._table.resizeRowsToContents()
        n = len(saves)
        self._set_status(
            self._("status_total", n=n) if n else self._("status_empty"),
            "ok" if n else "idle",
        )
        self._set_desktop_lbl()

    # ── Save ──────────────────────────────────────────────────────────────────
    def _save(self):
        items = self._desktop_items()
        if not items:
            QMessageBox.warning(self, "", self._("err_no_desktop"))
            return
        dt = datetime.now().strftime("%d.%m %H:%M")
        name, ok = QInputDialog.getText(
            self, self._("dlg_save_title"), self._("dlg_save_label"),
            QLineEdit.EchoMode.Normal, self._("dlg_save_default", dt=dt),
        )
        if not ok or not name.strip():
            return
        self._set_busy(True)
        self._set_status(self._("saving"), "info")
        self._worker = SaveWorker(items)
        self._worker.finished.connect(lambda lay, n: self._on_saved(lay, n, name.strip()))
        self._worker.error.connect(self._on_error)
        self._worker.start()

    def _on_saved(self, layout, count, name):
        self._set_busy(False)
        key   = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        saves = _load()
        saves[key] = {
            "name"    : name,
            "saved_at": datetime.now().strftime("%d.%m.%Y  %H:%M"),
            "layout"  : layout,
        }
        _save(saves)
        self._refresh()
        self._set_status(self._("saved_ok", name=name, n=count), "ok")

    # ── Restore ───────────────────────────────────────────────────────────────
    def _restore(self):
        row = self._table.currentRow()
        if row < 0:
            QMessageBox.warning(self, "", self._("err_no_select"))
            return
        key   = self._table.item(row, 0).data(Qt.ItemDataRole.UserRole)
        saves = _load()
        entry = saves.get(key, {})
        if not entry.get("layout"):
            QMessageBox.warning(self, "", self._("err_no_data"))
            return
        name  = entry.get("name", key)
        reply = QMessageBox.question(
            self, self._("dlg_rst_title"), self._("dlg_rst_msg", name=name),
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        if reply != QMessageBox.StandardButton.Yes:
            return
        self._set_busy(True)
        self._set_status(self._("restoring", name=name), "info")
        self._worker = RestoreWorker(entry["layout"], self._desktop())
        self._worker.finished.connect(lambda n: self._on_restored(n, name))
        self._worker.error.connect(self._on_error)
        self._worker.start()

    def _on_restored(self, count, name):
        self._set_busy(False)
        self._set_status(self._("restored_ok", name=name, n=count), "ok")
        QMessageBox.information(
            self, self._("done_title"),
            self._("done_msg", name=name, n=count),
        )

    # ── Rename ────────────────────────────────────────────────────────────────
    def _rename(self):
        row = self._table.currentRow()
        if row < 0:
            QMessageBox.warning(self, "", self._("err_no_select"))
            return
        key      = self._table.item(row, 0).data(Qt.ItemDataRole.UserRole)
        saves    = _load()
        old_name = saves[key].get("name", "")
        new_name, ok = QInputDialog.getText(
            self, self._("dlg_rename_title"), self._("dlg_rename_label"),
            QLineEdit.EchoMode.Normal, old_name,
        )
        if ok and new_name.strip():
            saves[key]["name"] = new_name.strip()
            _save(saves)
            self._refresh()
            self._set_status(
                self._("renamed_ok", old=old_name, new=new_name.strip()), "info"
            )

    # ── Delete ────────────────────────────────────────────────────────────────
    def _delete(self):
        row = self._table.currentRow()
        if row < 0:
            QMessageBox.warning(self, "", self._("err_no_select"))
            return
        key   = self._table.item(row, 0).data(Qt.ItemDataRole.UserRole)
        saves = _load()
        name  = saves.get(key, {}).get("name", key)
        reply = QMessageBox.question(
            self, self._("dlg_del_title"), self._("dlg_del_msg", name=name),
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        if reply == QMessageBox.StandardButton.Yes:
            saves.pop(key, None)
            _save(saves)
            self._refresh()
            self._set_status(self._("deleted_ok", name=name), "warn")

    # ── Error ─────────────────────────────────────────────────────────────────
    def _on_error(self, code):
        self._set_busy(False)
        self._set_status(self._("failed"), "warn")
        msg = self._("err_no_coord") if code == "NO_COORD" else code
        QMessageBox.warning(self, "", msg)
