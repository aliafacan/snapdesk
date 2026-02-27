"""
desktopok.core.workers
~~~~~~~~~~~~~~~~~~~~~~
Arka plan (QThread) iş parçacıkları.
"""

import os
import subprocess
import time

from PyQt6.QtCore import QThread, pyqtSignal

from snapdesk.core.nemo import get_position, set_position


class SaveWorker(QThread):
    """Masaüstü ikon koordinatlarını okur."""

    finished = pyqtSignal(dict, int)   # layout, found_count
    error    = pyqtSignal(str)         # error_code

    def __init__(self, paths: list[str]):
        super().__init__()
        self._paths = paths

    def run(self):
        layout = {}
        for path in self._paths:
            pos = get_position(path)
            if pos:
                layout[os.path.basename(path)] = pos

        if layout:
            self.finished.emit(layout, len(layout))
        else:
            self.error.emit("NO_COORD")


class RestoreWorker(QThread):
    """Koordinatları yazar ve Nemo masaüstünü yeniler."""

    finished = pyqtSignal(int)   # restored_count
    error    = pyqtSignal(str)

    def __init__(self, layout: dict, desktop: str):
        super().__init__()
        self._layout  = layout
        self._desktop = desktop

    def run(self):
        restored = 0
        for name, pos in self._layout.items():
            path = os.path.join(self._desktop, name)
            if os.path.exists(path) and set_position(path, pos):
                restored += 1

        self._refresh_nemo()
        self.finished.emit(restored)

    def _refresh_nemo(self):
        """Cinnamon ile uyumlu Nemo masaüstü yenileme."""
        try:
            subprocess.run(["pkill", "-KILL", "-x", "nemo-desktop"],
                           capture_output=True, timeout=3)
            # Ölmesini bekle (max 1 sn)
            for _ in range(10):
                time.sleep(0.1)
                if subprocess.run(["pgrep", "-x", "nemo-desktop"],
                                  capture_output=True).returncode != 0:
                    break
            # Cinnamon'un otomatik başlatmasını bekle (max 3 sn)
            alive = False
            for _ in range(30):
                time.sleep(0.1)
                if subprocess.run(["pgrep", "-x", "nemo-desktop"],
                                  capture_output=True).returncode == 0:
                    alive = True
                    break
            if not alive:
                subprocess.Popen(["nemo-desktop"],
                                 stdout=subprocess.DEVNULL,
                                 stderr=subprocess.DEVNULL)
        except Exception:
            pass
