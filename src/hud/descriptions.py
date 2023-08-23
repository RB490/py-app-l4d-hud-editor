import json
from utils.constants import HUD_DESCRIPTIONS_PATH

class HudDescriptions:
    """Subclass of the hud class. Manages everything related to hud file descriptions"""

    def __init__(self):
        self.data = None
        self.read_from_disk()
        print("Initialized HudDescriptions instance")

    def add_control(self, relative_path, input_control):
        """Set information"""
        self.data[relative_path]["file_control_descriptions"][input_control] = ""
        print(f"Added control '{input_control}' for relative path '{relative_path}'")

    def remove_control(self, relative_path, input_control):
        """Set information"""
        del self.data[relative_path]["file_control_descriptions"][input_control]
        print(f"Removed control '{input_control}' for relative path '{relative_path}'")

    def save_control_desc(self, relative_path, input_control, control_desc):
        """Set information"""
        self.data[relative_path]["file_control_descriptions"][input_control] = control_desc
        print(f"Saved description for control '{input_control}' in relative path '{relative_path}'")

    def get_all_descriptions(self):
        """
        Collects all file names and their corresponding descriptions from the dictionary of data,
        and returns them in a new dictionary.
        Returns:
        --------
        dict
            A dictionary with file names as keys and tuples with descriptions and relative path as values.
        """
        all_descriptions = {
            values["file_name"]: (values["file_description"], values["file_relative_path"])
            for rel_path, values in self.data.items()
        }
        print("Retrieved all file descriptions")
        return all_descriptions

    def get_control_description(self, relative_path, input_control):
        """Get information"""
        description = self.data.get(relative_path, {}).get("file_control_descriptions", {}).get(input_control)
        print(f"Retrieved description for control '{input_control}' in relative path '{relative_path}': {description}")
        return description

    def get_description(self, relative_path):
        """
        Get file description for given relative path.
        If the relative path doesn't exist in the data dictionary, return an empty string.
        """
        description = self.data.get(relative_path, {}).get("file_description", "")
        print(f"Retrieved description for relative path '{relative_path}': {description}")
        return description

    def get_controls(self, relative_path):
        """
        Get a list of file control descriptions for the given relative path.
        If the relative path doesn't exist in the data dictionary, return an empty list.
        """
        file_controls = list(self.data.get(relative_path, {}).get("file_control_descriptions", {}))
        print(f"Retrieved controls for relative path '{relative_path}': {file_controls}")
        return file_controls

    def read_from_disk(self):
        """Read persistent data from disk"""
        try:
            with open(HUD_DESCRIPTIONS_PATH, "r", encoding="utf-8") as file:
                data = json.load(file)
                print("Read data from disk")
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}
            print("No data found on disk")
        self.data = data

    def save_to_disk(self):
        """Save persistent data to disk"""
        data = self.data
        try:
            with open(HUD_DESCRIPTIONS_PATH, "w", encoding="utf-8") as file:
                pretty_json = json.dumps(data, sort_keys=True, indent=4)
                file.write(pretty_json)
                print(f"Saved data to {HUD_DESCRIPTIONS_PATH}")
        except (FileNotFoundError, TypeError):
            print(f"Error saving data to {HUD_DESCRIPTIONS_PATH}")
