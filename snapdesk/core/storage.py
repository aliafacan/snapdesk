"""
desktopok.core.storage
~~~~~~~~~~~~~~~~~~~~~~
JSON tabanlı düzen kayıt / yükleme.
"""

import json
import os

SAVE_FILE = os.path.expanduser("~/.local/share/snapdesk/layouts.json")


def load() -> dict:
    if os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE, encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {}


def save(data: dict) -> None:
    os.makedirs(os.path.dirname(SAVE_FILE), exist_ok=True)
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
