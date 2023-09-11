"""Handles storage, retrieval, and management of HUD-related data and folders."""
import os

import vdf  # type: ignore
from shared_utils.functions import copy_directory

from utils.constants import NEW_HUD_DIR
from utils.functions import prompt_for_folder
from utils.persistent_data_manager import PersistentDataManager  # Assuming you have vdf library imported


class HudManager:
    """Handles storage, retrieval, and management of HUD-related data and folders."""

    def __init__(self):
        self.data_manager = PersistentDataManager()

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
            addon_info = vdf.load(open(addoninfo_path, encoding="utf-8"))
            if addon_info.get("AddonInfo", {}).get("addontitle"):
                hud_name = addon_info["AddonInfo"]["addontitle"]
                # print(f"Hud name: Retrieved '{hud_name}' @ '{addoninfo_path}'")
            else:
                print(f"Hud name: Addoninfo.txt does not have addontitle set! @ '{addoninfo_path}'")
        else:
            print(f"Hud name: Addoninfo.txt does not exist @ '{addoninfo_path}' setting hud_name to '{hud_name}'")
        return hud_name
