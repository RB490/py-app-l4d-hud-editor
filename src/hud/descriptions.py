# pylint: disable=logging-fstring-interpolation
import json
import logging
import os

from game.game import Game
from shared_utils.logging_manager import LoggingManager
from shared_utils.shared_utils import Singleton
from utils.constants import HUD_DESCRIPTIONS_PATH

logging_manager = LoggingManager(__name__, level=logging.DEBUG)
# logging_manager = LoggingManager(__name__, level=logging.INFO)
log = logging_manager.get_logger()


class HudDescriptions(metaclass=Singleton):
    """Subclass of the hud class. Manages everything related to hud file descriptions"""

    def __init__(self):
        self.data = None
        self.game = Game()
        self.read_from_disk()
        log.debug("Initialized HudDescriptions instance")

    def add_control(self, file_name, input_control):
        """Set information"""
        if input_control is not None:
            self._add_entry_if_new(file_name)
            self.data[file_name]["file_control_descriptions"][input_control] = ""
            self.save_to_disk()
            log.debug(f"Added control '{input_control}' for file name '{file_name}'")
        else:
            log.warning("Cannot add control with None name")

    def remove_control(self, file_name, input_control):
        """Set information"""
        del self.data[file_name]["file_control_descriptions"][input_control]
        self.save_to_disk()
        log.debug(f"Removed control '{input_control}' for file name '{file_name}'")

    def remove_entry(self, file_name):
        """Remove an entire entry based on the provided file name"""
        if file_name in self.data:
            del self.data[file_name]
            self.save_to_disk()
            log.debug(f"Removed entry for file name '{file_name}'")
        else:
            log.warning(f"No entry found for file name '{file_name}'")

    def _add_entry_if_new(self, file_name):
        """Create a new entry in data if file_name doesn't exist"""
        if file_name not in self.data:
            is_custom_file = bool(self.game.dir.is_custom_file(file_name))

            self.data[file_name] = {
                "file_control_descriptions": {},
                "file_description": "",
                "file_name": file_name,
                "file_relative_path": "",
                "file_is_custom": is_custom_file,
            }
            log.debug(f"Added new description entry:\n{self.data[file_name]}")
            self.save_to_disk()

    def set_control_description(self, file_name, input_control, control_desc):
        """Save control description for a given file name and control"""
        if control_desc:
            self._add_entry_if_new(file_name)
            self.data[file_name]["file_control_descriptions"][input_control] = control_desc
            self.save_to_disk()
            log.debug(f"Saved description for control '{input_control}' in file name '{file_name}'")
        else:
            log.warning("Cannot save an empty control description")

    def set_file_description(self, file_name, file_desc):
        """Set file description for a given file name"""
        self._add_entry_if_new(file_name)
        self.data[file_name]["file_description"] = file_desc
        self.save_to_disk()
        log.debug(f"Saved file description for file name '{file_name}'")

    def set_file_relative_path(self, file_name, relative_path):
        """
        Set the file_relative_path for a given file name.
        Args:
        file_name (str): The name of the file.
        relative_path (str): The relative path to set.
        """
        self._add_entry_if_new(file_name)
        self.data[file_name]["file_relative_path"] = relative_path
        self.save_to_disk()
        log.debug(f"Set file_relative_path '{relative_path}' for file name '{file_name}'")

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
            for file_name, values in self.data.items()
        }
        log.debug("Retrieved all file descriptions")
        return all_descriptions

    def get_control_description(self, file_name, input_control):
        """Get information"""
        description = self.data.get(file_name, {}).get("file_control_descriptions", {}).get(input_control)
        log.debug(f"Retrieved description for control '{input_control}' in file name '{file_name}': {description}")
        return description

    def get_file_description(self, file_name):
        """
        Get file description for given file name.
        If the file name doesn't exist in the data dictionary, return an empty string.
        """
        description = self.data.get(file_name, {}).get("file_description", "")
        log.debug(f"Retrieved description for file name '{file_name}': {description}")
        return description

    def get_custom_file_status(self, file_name):
        """
        Check if a file has a custom status based on the given file name.
        Return True if the file name has a custom status, otherwise return None.
        """
        is_custom = self.data.get(file_name, {}).get("file_is_custom", None)
        log.debug(f"Retrieved custom status for file name '{file_name}': {is_custom}")
        return is_custom

    def get_controls(self, file_name):
        """
        Get a list of file control descriptions for the given file name.
        If the file name doesn't exist in the data dictionary, return an empty list.
        """
        file_controls = list(self.data.get(file_name, {}).get("file_control_descriptions", {}))
        log.debug(f"Retrieved controls for file name '{file_name}': {file_controls}")
        return file_controls

    def read_from_disk(self):
        """Read persistent data from disk"""
        try:
            with open(HUD_DESCRIPTIONS_PATH, "r", encoding="utf-8") as file:
                data = json.load(file)
                log.debug("Read data from disk")
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}
            log.warning("No data found on disk")
        self.data = data

    def save_to_disk(self):
        """Save persistent data to disk"""
        data = self.data
        
        try:
            with open(HUD_DESCRIPTIONS_PATH, "w", encoding="utf-8") as file:
                pretty_json = json.dumps(data, sort_keys=True, indent=4)
                file.write(pretty_json)
                log.debug(f"Saved data to {HUD_DESCRIPTIONS_PATH}")
        except (FileNotFoundError, TypeError):
            log.error(f"Error saving data to {HUD_DESCRIPTIONS_PATH}")
