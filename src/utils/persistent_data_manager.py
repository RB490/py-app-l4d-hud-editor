"Manages persistent data storage and retrieval."
# pylint: disable=broad-exception-caught
import json
import logging

from shared_utils.logging_manager import LoggerManager
from shared_utils.shared_utils import Singleton
from utils.constants import PERSISTENT_DATA_PATH

logger_manager = LoggerManager(__name__, level=logging.WARNING)  # Pass the desired logging level
# logger_manager = LoggerManager(__name__, level=logging.CRITICAL + 1)  # turns off
logger = logger_manager.get_logger()  # Get the logger instance


class PersistentDataManager(metaclass=Singleton):
    """
    Manages persistent data storage and retrieval.
    """

    def __init__(self):
        """Initialize the PersistentDataManager."""
        self.file_path = PERSISTENT_DATA_PATH
        self.default_data = {
            "BrowserGuiGeometry": "828x517+114+776",
            "HudSelectGuiGeometry": "865x528+100+100",
            "VDFGuiGeometry": "875x425+159+110",
            "VDFGui_annotate": 1,
            "VDFGui_indent_values": 1,
            "VDFGui_modify_int": 1,
            "VDFGui_sort_keys": 0,
            "editor_reload_mode": "reload_hud",
            "game_insecure": False,
            "game_mode": "Coop",
            "game_mute": True,
            "game_pos": "Top Left",
            "game_pos_custom_coord": None,
            "game_res": [1600, 900],
            "reload_mouse_clicks_coord_1": (10, 20),
            "reload_mouse_clicks_coord_2": (30, 40),
            "reload_mouse_clicks_enabled": False,
            "reload_reopen_menu_on_reload": False,
            "steam_root_dir": "E:/games/steam",
            "stored_huds": ["D:/Programming and projects/l4d-addons-huds/4. l4d2-2020HUD/source"],
            "stored_temp_huds": [],
        }
        self.data = self.load()

    def load(self):
        """Load data from disk or create defaults if missing."""
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                loaded_data = json.load(file)
                data = {**self.default_data, **loaded_data}
                logger.info("Loaded data from disk.")
        except Exception:
            logger.warning("Resetting settings file")
            data = self.__reset()
            self.save()
        return data

    def __reset(self):
        """Reset data to default values and save to disk."""
        self.data = self.default_data
        self.save()
        return self.data

    def print(self):
        """Print formatted JSON data."""
        logger.info(self._get_pretty_json())

    def _get_pretty_json(self):
        """Return formatted JSON string."""
        return json.dumps(self.data, sort_keys=True, indent=4)

    def save(self):
        """Save data to disk."""
        try:
            with open(self.file_path, "w", encoding="utf-8") as file:
                pretty_json = self._get_pretty_json()
                file.write(pretty_json)
                logger.info("Wrote data to disk!")
        except Exception:
            logger.error(f"Error saving data to {self.file_path}")

    def get(self, key):
        """Get data value by key."""
        return self.data.get(key, self.default_data.get(key))

    def set(self, key, value):
        """Set data value for key."""
        self.data[key] = value
        self.save()
        logger.info(f"Set data for key '{key}' to: {value}")

    def append(self, key, value):
        """Append value to a list in data."""
        if key in self.data and isinstance(self.data[key], list):
            self.data[key].append(value)
            self.save()
            logger.info(f"Appended value '{value}' to key '{key}'")
        else:
            logger.error(f"Cannot append to key '{key}' as it is not a list.")

    def remove_data(self, key):
        """Remove data entry by key."""
        if key in self.data:
            del self.data[key]
            self.save()
            logger.info(f"Removed key '{key}' from data.")
        else:
            logger.warning(f"Key '{key}' not found in data.")

    def remove_item_from_list(self, key, item):
        """Remove item from a list in data."""
        if key in self.data and isinstance(self.data[key], list):
            if item in self.data[key]:
                self.data[key].remove(item)
                self.save()
                logger.info(f"Removed item '{item}' from list key '{key}'")
            else:
                logger.warning(f"Item '{item}' not found in list key '{key}'")
        else:
            logger.error(f"Cannot remove item from key '{key}' as it is not a list.")

    def get_obj(self):
        """Get the entire data object."""
        return self.data
