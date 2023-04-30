"""Submodule of the hud module. Manages everything related to hud file descriptions"""
import json
from modules.utils.constants import HUD_DESCRIPTIONS_PATH


class HudDescriptions:
    """Subclass of the hud class. Manages everything related to hud file descriptions"""

    def __init__(self):
        self.data = self.read_from_disk()

    def get_all_descriptions(self):
        """
        Collects all file names and their corresponding descriptions from the dictionary of data,
        and returns them in a new dictionary.

        Returns:
        --------
        dict
            A dictionary with file names as keys and descriptions as values.
        """

        # Create a new dictionary called all_descriptions using a dictionary comprehension that
        #  extracts the file names and descriptions from the existing dictionary (self.data)
        all_descriptions = {values["file_name"]: values["file_description"] for rel_path, values in self.data.items()}

        # Return the newly created dictionary
        return all_descriptions

    def get_control_description(self, relative_path, input_control):
        """Get information"""
        return self.data[relative_path]["file_control_descriptions"][input_control]

    def get_description(self, relative_path):
        """
        Get file description for given relative path.

        If the relative path doesn't exist in the data dictionary, return an empty string.
        """

        return self.data.get(relative_path, {}).get("file_description", "")

    def get_controls(self, relative_path):
        """
        Get a list of file control descriptions for the given relative path.

        If the relative path doesn't exist in the data dictionary, return an empty list.
        """

        # Retrieve file control descriptions from the data dictionary using the provided relative path.
        # If the key is not present, default to an empty dictionary.
        file_controls = self.data.get(relative_path, {}).get("file_control_descriptions", {})

        # Convert the dictionary of file control descriptions to a list and return it.
        return list(file_controls)

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
