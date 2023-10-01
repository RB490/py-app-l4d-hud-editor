"""Subclass of the hud class. Manages everything related to hud file descriptions"""
# pylint: disable=logging-fstring-interpolation
import functools
import json
import os

from loguru import logger
from shared_utils.functions import Singleton, is_valid_file_name_format, is_valid_file_path_format

from src.game.game import Game
from src.utils.constants import HUD_DESCRIPTIONS_PATH


def raise_exception_if_invalid_file_name(func):
    "Check if hwnd is running"

    @functools.wraps(func)
    def wrapper(self, file_name, *args, **kwargs):
        if not is_valid_file_name_format(file_name):
            raise ValueError(f"Invalid file name: {file_name}")
        return func(self, file_name, *args, **kwargs)

    return wrapper

def ensure_file_entry_exists_or_create(func):
    def wrapper(self, file_name, *args, **kwargs):
        self._ensure_file_entry_exists_or_create(file_name)
        return func(self, file_name, *args, **kwargs)
    return wrapper

class HudDescriptions(metaclass=Singleton):
    """Subclass of the hud class. Manages everything related to hud file descriptions"""

    def __init__(self):
        self.data = None
        self.game = Game()
        self.read_from_disk()
        logger.debug("Initialized HudDescriptions instance")

    @raise_exception_if_invalid_file_name
    @ensure_file_entry_exists_or_create
    def add_control(self, file_name, input_control):
        """Set information"""
        if input_control is not None:
            self.data[file_name]["file_control_descriptions"][input_control] = ""
            self.save_to_disk()
            logger.debug(f"Added control '{input_control}' for file name '{file_name}'")
        else:
            logger.warning("Cannot add control with None name")

    @raise_exception_if_invalid_file_name
    def remove_control(self, file_name, input_control):
        """Set information"""
        del self.data[file_name]["file_control_descriptions"][input_control]
        self.save_to_disk()
        logger.debug(f"Removed control '{input_control}' for file name '{file_name}'")

    @raise_exception_if_invalid_file_name
    def remove_entry(self, file_name):
        """Remove an entire entry based on the provided file name"""
        if file_name in self.data:
            del self.data[file_name]
            self.save_to_disk()
            logger.debug(f"Removed entry for file name '{file_name}'")
        else:
            logger.warning(f"No entry found for file name '{file_name}'")

    @raise_exception_if_invalid_file_name
    def _ensure_file_entry_exists_or_create(self, file_name):
        """Create a new entry in data if file_name doesn't exist"""
        if file_name not in self.data:
            self.data[file_name] = {
                "file_control_descriptions": {},
                "file_description": "",
                "file_name": file_name,
                "file_relative_path": "",
                "file_is_custom": "",
            }
            logger.debug(f"Added new description entry:\n{self.data[file_name]}")
            self.save_to_disk()

    @raise_exception_if_invalid_file_name
    @ensure_file_entry_exists_or_create
    def set_control_description(self, file_name, input_control, control_desc):
        """Save control description for a given file name and control"""
        if control_desc:
            self.data[file_name]["file_control_descriptions"][input_control] = control_desc
            self.save_to_disk()
            logger.debug(f"Saved description for control '{input_control}' in file name '{file_name}'")
        else:
            logger.warning("Cannot save an empty control description")

    @raise_exception_if_invalid_file_name
    @ensure_file_entry_exists_or_create
    def set_file_description(self, file_name, file_desc):
        """Set file description for a given file name"""
        self.data[file_name]["file_description"] = file_desc
        self.save_to_disk()
        logger.debug(f"Saved file description for file name '{file_name}'")

    @raise_exception_if_invalid_file_name
    @ensure_file_entry_exists_or_create
    def set_file_relative_path(self, file_name, relative_path):
        """
        Set the file_relative_path for a given file name.
        Args:
        file_name (str): The name of the file.
        relative_path (str): The relative path to set.
        """
        self.data[file_name]["file_relative_path"] = relative_path
        self.save_to_disk()
        logger.debug(f"Set file_relative_path '{relative_path}' for file name '{file_name}'")
        self._set_file_is_custom_status(file_name)

    @raise_exception_if_invalid_file_name
    @ensure_file_entry_exists_or_create
    def _set_file_is_custom_status(self, file_name):
        """Is this a custom file?"""
        # verify we have a relative file path
        relative_file_path = self.get_file_relative_path(file_name)
        if not is_valid_file_path_format(relative_file_path):
            raise ValueError(f"Invalid path: {relative_file_path}")

        # set custom status
        is_custom_file = self.game.dir.is_custom_file(relative_file_path)
        self.data[file_name]["file_is_custom"] = is_custom_file
        self.save_to_disk()
        logger.debug(f"Set file_is_custom '{is_custom_file}' for file name '{file_name}'")

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
        logger.debug("Retrieved all file descriptions")
        return all_descriptions

    @raise_exception_if_invalid_file_name
    def get_control_description(self, file_name, input_control):
        """Get information"""
        description = self.data.get(file_name, {}).get("file_control_descriptions", {}).get(input_control)
        logger.debug(f"Retrieved description for control '{input_control}' in file name '{file_name}': {description}")
        return description

    @raise_exception_if_invalid_file_name
    def get_file_description(self, file_name):
        """
        Get file description for given file name.
        If the file name doesn't exist in the data dictionary, return an empty string.
        """
        description = self.data.get(file_name, {}).get("file_description", "")
        logger.debug(f"Retrieved file description for '{file_name}': {description}")
        return description

    @raise_exception_if_invalid_file_name
    def get_file_relative_path(self, file_name):
        """Get information"""
        relative_path = self.data.get(file_name, {}).get("file_relative_path", "")
        logger.debug(f"Retrieved relative path for file name '{file_name}': {relative_path}")
        return relative_path

    @raise_exception_if_invalid_file_name
    def get_custom_file_status(self, file_name):
        """
        Check if a file has a custom status based on the given file name.
        Return True if the file name has a custom status, otherwise return None.
        """
        is_custom = self.data.get(file_name, {}).get("file_is_custom", None)
        logger.debug(f"Retrieved custom status for file name '{file_name}': {is_custom}")
        return is_custom

    @raise_exception_if_invalid_file_name
    def get_controls(self, file_name):
        """
        Get a list of file control descriptions for the given file name.
        If the file name doesn't exist in the data dictionary, return an empty list.
        """
        file_controls = list(self.data.get(file_name, {}).get("file_control_descriptions", {}))
        logger.debug(f"Retrieved controls for file name '{file_name}': {file_controls}")
        return file_controls

    def read_from_disk(self):
        """Read persistent data from disk"""
        try:
            with open(HUD_DESCRIPTIONS_PATH, "r", encoding="utf-8") as file:
                data = json.load(file)
                logger.debug("Read data from disk")
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
                logger.debug(f"Saved data to {HUD_DESCRIPTIONS_PATH}")
        except (FileNotFoundError, TypeError):
            logger.error(f"Error saving data to {HUD_DESCRIPTIONS_PATH}")


def debug_hud_descriptions_class():
    """Debug descriptions"""
    print("hi there!")
    desc = HudDescriptions()
    # file_name = "hudlayout.res"
    file_name = "debug_file.txt"
    # result = desc.get_control_description(file_name, "HudWeaponSelection")
    result = desc.set_file_relative_path(file_name, "some\\path")

    print(f"desc result = {result}")


def test():
    """Test hud description class"""
    # Create a HudDescriptions instance
    descr = HudDescriptions()

    # Sample data for testing
    file_name = "sample.txt"
    input_control = "control1"
    control_desc = "Control description"
    file_desc = "File description"
    rela_path = "scripts\\sample.txt"

    # Test add_control
    descr.add_control(file_name, input_control)

    # Test set_control_description
    descr.set_control_description(file_name, input_control, control_desc)

    # Test set_file_description
    descr.set_file_description(file_name, file_desc)

    # Test set_file_relative_path
    descr.set_file_relative_path(file_name, rela_path)

    # Test get_control_description
    retrieved_control_desc = descr.get_control_description(file_name, input_control)
    assert retrieved_control_desc == control_desc

    # Test get_file_description
    retrieved_file_desc = descr.get_file_description(file_name)
    assert retrieved_file_desc == file_desc

    # Test get_file_relative_path
    retrieved_rela_path = descr.get_file_relative_path(file_name)
    assert rela_path == retrieved_rela_path

    # Test get_custom_file_status
    custom_status = descr.get_custom_file_status(file_name)
    assert custom_status is False  # Assuming it's not custom in this test

    # Test get_controls
    retrieved_controls = descr.get_controls(file_name)
    assert input_control in retrieved_controls

    # Test remove_control
    descr.remove_control(file_name, input_control)
    retrieved_controls = descr.get_controls(file_name)
    assert input_control not in retrieved_controls

    # Test get_all_descriptions
    all_descriptions = descr.get_all_descriptions()
    assert file_name in all_descriptions

    # Test remove_entry
    descr.remove_entry(file_name)
    retrieved_file_desc = descr.get_file_description(file_name)
    assert retrieved_file_desc == ""  # File should be removed

    logger.info("All HudDescriptions methods tested successfully!")


if __name__ == "__main__":
    test()
