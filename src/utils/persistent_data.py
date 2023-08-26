"Manages persistent data storage and retrieval."
# pylint: disable=broad-exception-caught
import json

from utils.constants import PERSISTENT_DATA_PATH
from utils.shared_utils import Singleton, show_message


class PersistentDataManager(metaclass=Singleton):
    """
    Manages persistent data storage and retrieval.
    """

    def __init__(self):
        """Initialize the PersistentDataManager."""
        self.file_path = PERSISTENT_DATA_PATH
        self.data = self.load()

    def load(self):
        """Load data from disk or create defaults if missing."""
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
        except Exception:
            show_message("Resetting settings file!", "error")
            data = {
                # Default data...
            }
        return data

    def print(self):
        """Print formatted JSON data."""
        print(self._get_pretty_json())

    def _get_pretty_json(self):
        """Return formatted JSON string."""
        return json.dumps(self.data, sort_keys=True, indent=4)

    def save(self):
        """Save data to disk."""
        try:
            with open(self.file_path, "w", encoding="utf-8") as file:
                pretty_json = self._get_pretty_json()
                file.write(pretty_json)
                print("Wrote data to disk!")
        except Exception:
            print(f"Error saving data to {self.file_path}")

    def get(self, key):
        """Get data value by key."""
        return self.data.get(key)

    def set(self, key, value):
        """Set data value for key."""
        self.data[key] = value
        self.save()
        print(f"Set data for key '{key}' to: {value}")

    def append(self, key, value):
        """Append value to a list in data."""
        if key in self.data and isinstance(self.data[key], list):
            self.data[key].append(value)
            self.save()
            print(f"Appended value '{value}' to key '{key}'")
        else:
            print(f"Cannot append to key '{key}' as it is not a list.")

    def remove_data(self, key):
        """Remove data entry by key."""
        if key in self.data:
            del self.data[key]
            self.save()
            print(f"Removed key '{key}' from data.")
        else:
            print(f"Key '{key}' not found in data.")

    def remove_item_from_list(self, key, item):
        """Remove item from a list in data."""
        if key in self.data and isinstance(self.data[key], list):
            if item in self.data[key]:
                self.data[key].remove(item)
                self.save()
                print(f"Removed item '{item}' from list key '{key}'")
            else:
                print(f"Item '{item}' not found in list key '{key}'")
        else:
            print(f"Cannot remove item from key '{key}' as it is not a list.")

    def get_obj(self):
        """Get the entire data object."""
        return self.data
