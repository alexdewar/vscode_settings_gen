import os
import platform
from pathlib import Path

template_path = Path(__file__).parent / 'settings_template.json'

def get_settings_path():
    """Get path to VS code's settings.json file."""
    # Get settings folder
    if platform.system() == "Linux":
        settings_root = Path.home() / ".config"
    elif platform.system() == "Windows":
        settings_root = Path(os.getenv("APPDATA"))
    else:
        settings_root = Path.home() / "Library" / "Application Support"
    return settings_root / "Code" / "User" / "settings.json"
