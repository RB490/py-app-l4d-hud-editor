"""Handles storage, retrieval, and management of HUD-related data and folders."""
import os

from loguru import logger
from shared_managers.valve_vdf_addoninfo_manager import ValveVdfAddoninfoManager
from shared_utils.functions import copy_directory

from src.utils.constants import DATA_MANAGER  # Assuming you have vdf library imported
from src.utils.constants import NEW_HUD_DIR
from src.utils.functions import prompt_for_folder


class HudManager:
    """Handles storage, retrieval, and management of HUD-related data and folders."""

    def __init__(self):
        self.data_manager = DATA_MANAGER

    def prompt_add_existing_hud(self):
        """Prompt user for hud folder to add"""
        folder_path = prompt_for_folder("Add HUD: Select folder")
        if folder_path:
            self.data_manager.append("stored_huds", folder_path)
            return folder_path
        return False

    def prompt_open_temp_hud(self):
        """Prompt user for temp hud folder to add"""
        folder_path = prompt_for_folder("Add HUD: Select folder")
        if folder_path:
            self.data_manager.append("stored_temp_huds", folder_path)
            return folder_path
        return False

    def prompt_create_new_hud(self):
        """Prompt user for hud folder to create a new hud in"""
        folder_path = prompt_for_folder("New HUD: Select folder")
        if folder_path:
            self.data_manager.append("stored_huds", folder_path)
            copy_directory(NEW_HUD_DIR, folder_path)
            return folder_path
        return False

    def remove_stored_hud(self, hud_dir):
        """Remove stored hud"""
        if hud_dir in self.data_manager.get("stored_huds"):
            self.data_manager.remove_item_from_list("stored_huds", hud_dir)

    def remove_temp_hud(self, hud_dir):
        """Remove temp hud"""
        if hud_dir in self.data_manager.get("stored_temp_huds"):
            self.data_manager.remove_item_from_list("stored_temp_huds", hud_dir)

    def retrieve_hud_name_for_dir(self, hud_dir):
        """Retrieve hud name for a directory. Either directory name or from addoninfo.txt"""
        if hud_dir is None or not os.path.isdir(hud_dir):
            raise NotADirectoryError(f"Invalid hud_dir directory path: '{hud_dir}'")

        hud_name = os.path.basename(hud_dir)
        addoninfo_path = os.path.normpath(os.path.join(hud_dir, "addoninfo.txt"))

        if os.path.exists(addoninfo_path):
            addinfo_instance = ValveVdfAddoninfoManager(addoninfo_path)
            hud_name = addinfo_instance.get("addontitle")
            if not hud_name:
                logger.info(f"Hud name: Addoninfo.txt does not have addontitle set! @ '{addoninfo_path}'")
        else:
            logger.info(
                f"Hud name: Addoninfo.txt does not exist @ '{addoninfo_path}' setting hud_name to '{hud_name}'"
            )
        return hud_name
