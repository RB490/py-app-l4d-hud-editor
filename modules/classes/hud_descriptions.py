"""Submodule of the hud module. Manages everything related to hud file descriptions"""
import json
from modules.utils.constants import HUD_DESCRIPTIONS_PATH


class HudDescriptions:
    """Subclass of the hud class. Manages everything related to hud file descriptions"""

    def __init__(self):
        print("hi there")
        self.data = self.read_from_disk()

    def get_all_descriptions(self):
        """Get information"""
        # pylint: disable=unused-variable
        all_descriptions = {}
        for rel_path, values in self.data.items():
            file_desc = values["file_description"]
            all_descriptions[values["file_name"]] = file_desc
        return all_descriptions

    def get_description(self, relative_path):
        """Get information"""

        if relative_path in self.data:
            return self.data[relative_path]["file_description"]
        else:
            return " "

    def read_from_disk(self):
        """Read persistent data from disk"""
        print("load_from_disk")

        try:
            with open(HUD_DESCRIPTIONS_PATH, "r", encoding="utf-8") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            # print(f"Error loading data from {file_path}")
            data = {}

        # print(f"read_from_disk: \n{json.dumps(data, sort_keys=True, indent=4)}")
        return data

    def save_to_disk(self, data):
        """Save persistent data to disk"""
        print("save_from_disk")
        try:
            with open(HUD_DESCRIPTIONS_PATH, "w", encoding="utf-8") as file:
                # json.dump(data, file) # fastest, but doesn't allow formatting - and i use tiny jsons
                pretty_json = json.dumps(data, sort_keys=True, indent=4)
                file.write(pretty_json)
        except (FileNotFoundError, TypeError):
            print(f"Error saving data to {HUD_DESCRIPTIONS_PATH}")


def debug_hud_descriptions():
    """Debug hud descriptions class"""
    # pylint: disable=unused-variable
    print("debug_hud_descriptions")
    hud_desc = HudDescriptions()
