"""
desktopok.core.nemo
~~~~~~~~~~~~~~~~~~~
GIO / Nemo metadata okuma-yazma işlemleri.
"""

import re
import subprocess

try:
    from gi.repository import Gio
    _GIO = True
except ImportError:
    _GIO = False

_ATTR = "metadata::nemo-icon-position"


def get_position(path: str) -> str | None:
    """Dosyanın Nemo masaüstü koordinatını döner. Bulunamazsa None."""
    if _GIO:
        try:
            f    = Gio.File.new_for_path(path)
            info = f.query_info(_ATTR, Gio.FileQueryInfoFlags.NONE, None)
            pos  = info.get_attribute_string(_ATTR)
            if pos and re.match(r"^\d+,\d+$", pos):
                return pos
        except Exception:
            pass

    # Fallback: gio CLI
    try:
        out = subprocess.run(
            ["gio", "info", "-a", _ATTR, path],
            capture_output=True, text=True, timeout=5,
        ).stdout
        for line in out.splitlines():
            if _ATTR in line and ":" in line:
                pos = line.split(":")[-1].strip()
                if re.match(r"^\d+,\d+$", pos):
                    return pos
    except Exception:
        pass
    return None


def set_position(path: str, pos: str) -> bool:
    """Dosyaya Nemo masaüstü koordinatı yazar. Başarılı ise True."""
    if _GIO:
        try:
            f    = Gio.File.new_for_path(path)
            info = Gio.FileInfo.new()
            info.set_attribute_string(_ATTR, pos)
            f.set_attributes_from_info(info, Gio.FileQueryInfoFlags.NONE, None)
            return True
        except Exception:
            pass

    try:
        subprocess.run(
            ["gio", "set", "-t", "string", path, _ATTR, pos], timeout=4
        )
        return True
    except Exception:
        return False
