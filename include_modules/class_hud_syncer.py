"""Module providing hud syncing capability between a source dir and the game dir"""
import os
import shutil
from include_modules.class_game import Game
from include_modules.functions import load_data
from include_modules.constants import DEVELOPMENT_DIR


def get_all_files_and_dirs(dir_path):
    """Returns a list of all the files and sub directories inside dir_path"""
    # Initialize an empty list
    file_and_dir_list = []
    # Loop over all the files and directories in the tree
    for dirpath, dirnames, filenames in os.walk(dir_path):
        # Append all the files and directories to the list
        file_and_dir_list += [os.path.join(dirpath, name) for name in dirnames + filenames]
    # Return the list
    return file_and_dir_list


def get_all_sub_dirs(dir_path):
    """Returns a list of all the subdirectories in dir_path"""
    files_and_dirs = os.listdir(dir_path)
    dirs = [f for f in files_and_dirs if os.path.isdir(os.path.join(dir_path, f))]
    return dirs


class HudSyncer:
    """functions providing hud syncing/unsyncing capability from the source to game dir"""

    def __init__(self):
        self.is_synced = False
        self.source_dir = None
        self.target_dir_root = None
        self.target_dir_main_name = None
        self.target_sub_dir_names = None
        self.hud_items_custom = []
        self.hud_items = None

    def un_sync(self):
        """Unsync the hud"""
        if not self.is_synced:
            return

        print("TODO: write un_sync")

    def sync(self, source_dir, target_dir, target_dir_main_name):
        """Sync the hud"""
        print(f"source_dir: {source_dir}")
        print(f"target_dir: {target_dir}")
        print(f"target_dir_main_name: {target_dir_main_name}")

        # Unsync the previous hud (if syncing different hud)
        if self.is_synced and self.source_dir != source_dir:
            self.un_sync()

        # Validate input
        if not os.path.isdir(source_dir):
            raise ValueError(f"Invalid source directory! '{source_dir}'")
        if not os.path.isdir(target_dir):
            raise ValueError(f"Invalid target directory! '{target_dir}'")

        # Save input
        self.source_dir = source_dir
        self.target_dir_root = target_dir
        self.target_dir_main_name = target_dir_main_name
        self.target_sub_dir_names = get_all_sub_dirs(target_dir)
        self.hud_items_custom = []
        self.hud_items = list(self.source_dir.glob("**/*"))

        # Backup game files
        self._backup_target()

        self.is_synced = True
        input("end of sync()")

    def _backup_target(self):
        for target_sub_dir_name in self.target_sub_dir_names:
            target_sub_dir = os.path.join(self.target_dir_root, target_sub_dir_name)

            for item in self.hud_items:
                target_item = item.replace(self.source_dir, target_sub_dir)
                target_item_backup = target_item + ".backup"

                # save custom items in the main directory
                if target_sub_dir_name == self.target_dir_main_name:
                    if not os.path.exists(target_item) and target_item not in self.hud_items_custom:
                        self.hud_items_custom.append(target_item)
                        print(f"adding custom file: {target_item}")

                # backup existing file
                if (
                    os.path.exists(target_item)
                    and not os.path.exists(target_item_backup)
                    and target_item not in self.hud_items_custom
                    and not os.path.isdir(target_item)
                ):
                    os.rename(target_item, target_item_backup)
                    print(f"{target_item} -> {target_item_backup}")

        print(f"custom items: {self.hud_items_custom}")


def debug_hud_syncer():
    """Debugs the hud syncer class"""
    os.system("cls")  # clear terminal

    saved_data = load_data()
    game_instance = Game(saved_data)

    sync_debug_dir = os.path.join(DEVELOPMENT_DIR, "Debug", "Hud Syncer")
    if os.path.isdir(os.path.join(sync_debug_dir, "Workspace")):
        shutil.rmtree(os.path.join(sync_debug_dir, "Workspace"))

    source_dir_template = os.path.join(sync_debug_dir, "Templates", "Small", "Debug Hud")
    target_dir_template = os.path.join(sync_debug_dir, "Templates", "Large", "Game Dir")
    source_dir_workspace = os.path.join(sync_debug_dir, "Workspace", "Debug Hud")
    target_dir_workspace = os.path.join(sync_debug_dir, "Workspace", "Game Dir")
    shutil.copytree(source_dir_template, source_dir_workspace)
    shutil.copytree(target_dir_template, target_dir_workspace)

    hud_syncer = HudSyncer()
    hud_syncer.sync(source_dir_workspace, target_dir_workspace, os.path.basename(game_instance.get_main_dir("dev")))
