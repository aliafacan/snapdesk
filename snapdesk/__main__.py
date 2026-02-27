#!/usr/bin/env python3
"""
SnapDesk - Entry point
Run with:  python3 -m snapdesk
"""

import sys
from PyQt6.QtWidgets import QApplication
from snapdesk.ui.main_window import MainWindow


def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    win = MainWindow()
    # Ekranın ortasına al
    screen = app.primaryScreen().availableGeometry()
    win.move(
        (screen.width()  - win.width())  // 2,
        (screen.height() - win.height()) // 2,
    )
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
