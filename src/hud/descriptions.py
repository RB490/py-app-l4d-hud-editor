"""Subclass of the hud class. Manages everything related to hud file descriptions"""
# pylint: disable=logging-fstring-interpolation
import json
import logging
import os

from game.game import Game
from shared_utils.logging_manager import LoggerManager
from shared_utils.shared_utils import Singleton
from utils.constants import HUD_DESCRIPTIONS_PATH

# Configure the logging settings
logger_manager = LoggerManager(__name__, level=logging.WARNING)  # Pass the desired logging level
# logger_manager = LoggerManager(__name__, level=logging.CRITICAL + 1)  # turns off
logger = logger_manager.get_logger()  # Get the logger instance


class HudDescriptions(metaclass=Singleton):
    """Subclass of the hud class. Manages everything related to hud file descriptions"""

    def __init__(self):
        self.data = None
        self.game = Game()
        self.read_from_disk()
        logger.info("Initialized HudDescriptions instance")

    def add_control(self, relative_path, input_control):
        """Set information"""
        if input_control is not None:
            self._add_entry(relative_path)
            self.data[relative_path]["file_control_descriptions"][input_control] = ""
            self.save_to_disk()
            logger.info(f"Added control '{input_control}' for relative path '{relative_path}'")
        else:
            logger.warning("Cannot add control with None name")

    def remove_control(self, relative_path, input_control):
        """Set information"""
        del self.data[relative_path]["file_control_descriptions"][input_control]
        self.save_to_disk()
        logger.info(f"Removed control '{input_control}' for relative path '{relative_path}'")

    def remove_entry(self, relative_path):
        """Remove an entire entry based on the provided relative path"""
        if relative_path in self.data:
            del self.data[relative_path]
            self.save_to_disk()
            logger.info(f"Removed entry for relative path '{relative_path}'")
        else:
            logger.info(f"No entry found for relative path '{relative_path}'")

    def _add_entry(self, relative_path):
        """Create a new entry in data if relative_path doesn't exist"""
        if relative_path not in self.data:
            self.data[relative_path] = {
                "file_control_descriptions": {},
                "file_description": "",
                "file_name": os.path.basename(relative_path),
                "file_relative_path": relative_path,
                "file_is_custom": bool(self.game.dir.is_custom_file(relative_path)),
            }
            logger.info(f"Added new description entry:\n{self.data[relative_path]}")
            self.save_to_disk()

    def set_control_description(self, relative_path, input_control, control_desc):
        """Save control description for a given relative path and control"""
        if control_desc:
            self._add_entry(relative_path)
            self.data[relative_path]["file_control_descriptions"][input_control] = control_desc
            self.save_to_disk()
            logger.info(f"Saved description for control '{input_control}' in relative path '{relative_path}'")
        else:
            logger.warning("Cannot save an empty control description")

    def set_file_description(self, relative_path, file_desc):
        """Set file description for a given relative path"""
        self._add_entry(relative_path)
        self.data[relative_path]["file_description"] = file_desc
        self.save_to_disk()
        logger.info(f"Saved file description for relative path '{relative_path}'")

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
        logger.info("Retrieved all file descriptions")
        return all_descriptions

    def get_control_description(self, relative_path, input_control):
        """Get information"""
        description = self.data.get(relative_path, {}).get("file_control_descriptions", {}).get(input_control)
        logger.info(
            f"Retrieved description for control '{input_control}' in relative path '{relative_path}': {description}"
        )
        return description

    def get_file_description(self, relative_path):
        """
        Get file description for given relative path.
        If the relative path doesn't exist in the data dictionary, return an empty string.
        """
        description = self.data.get(relative_path, {}).get("file_description", "")
        logger.info(f"Retrieved description for relative path '{relative_path}': {description}")
        return description

    def get_custom_file_status(self, relative_path):
        """
        Check if a file has a custom status based on the given relative path.
        Return True if the relative path has a custom status, otherwise return None.
        """
        is_custom = self.data.get(relative_path, {}).get("file_is_custom", None)
        logger.info(f"Retrieved custom status for relative path '{relative_path}': {is_custom}")
        return is_custom

    def get_controls(self, relative_path):
        """
        Get a list of file control descriptions for the given relative path.
        If the relative path doesn't exist in the data dictionary, return an empty list.
        """
        file_controls = list(self.data.get(relative_path, {}).get("file_control_descriptions", {}))
        logger.info(f"Retrieved controls for relative path '{relative_path}': {file_controls}")
        return file_controls

    def read_from_disk(self):
        """Read persistent data from disk"""
        try:
            with open(HUD_DESCRIPTIONS_PATH, "r", encoding="utf-8") as file:
                data = json.load(file)
                logger.info("Read data from disk")
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}
            logger.warning("No data found on disk")
        self.data = data

    def save_to_disk(self):
        """Save persistent data to disk"""
        data = self.data
        try:
            with open(HUD_DESCRIPTIONS_PATH, "w", encoding="utf-8") as file:
                pretty_json = json.dumps(data, sort_keys=True, indent=4)
                file.write(pretty_json)
                logger.info(f"Saved data to {HUD_DESCRIPTIONS_PATH}")
        except (FileNotFoundError, TypeError):
            logger.error(f"Error saving data to {HUD_DESCRIPTIONS_PATH}")
