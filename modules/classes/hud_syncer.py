"""Module providing hud syncing capability between a source dir and the game dir"""
import os
import shutil
import hashlib
from modules.classes.game import Game
from modules.utils.functions import load_data
from modules.utils.constants import DEVELOPMENT_DIR


def files_differ(in_file1, in_file2):
    """Uses a MD5 hash to compare file differences"""
    with open(in_file1, "rb") as file1, open(in_file2, "rb") as file2:
        md5_f1 = hashlib.md5()
        md5_f2 = hashlib.md5()
        while True:
            chunk_f1 = file1.read(1024)
            chunk_f2 = file2.read(1024)
            if not chunk_f1 and not chunk_f2:
                return False  # files are the same
            md5_f1.update(chunk_f1)
            md5_f2.update(chunk_f2)
            if md5_f1.digest() != md5_f2.digest():
                return True  # files are different


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
        self.hud_items_previous = []
        self.hud_items = None

    def get_source_dir(self):
        """Return source directory"""
        return self.source_dir

    def get_sync_status(self):
        """Return sync status"""
        return self.is_synced

    def un_sync(self):
        """Unsync the hud"""
        if not self.get_sync_status():
            return

        print("TODO: write un_sync")

    def sync(self, source_dir: str, target_dir: str, target_dir_main_name: str) -> None:
        # pylint: disable=anomalous-backslash-in-string
        """Syncs the contents of the source directory to the target directory.

        Parameters:
        source_dir (str): The path of the source directory to sync from. EG: ..\l4d-addons-huds\4. l4d2-2020HUD\source
        target_dir (str): The path of the target directory to sync to. EG: ..\steamapps\common\Left 4 Dead 2
        target_dir_main_name (str): The main name of the target directory,
            used to differentiate from dlc folders and only perform
            certain actions on the main directory. EG: 'Left 4 Dead 2'
        """

        print(f"source_dir: {source_dir}")
        print(f"target_dir: {target_dir}")
        # print(f"target_dir_main_name: {target_dir_main_name}")

        # Unsync the previous hud (if syncing different hud)
        if self.get_sync_status() and self.source_dir != source_dir:
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
        self.hud_items = get_all_files_and_dirs(self.source_dir)

        # Backup game files
        self._backup_target()

        # Overwrite game files
        self._overwrite_target()

        # Unsync deleted items in target
        self._remove_deleted_items()

        self.is_synced = True
        # input("end of sync()")

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
                        # print(f"adding custom file: {target_item}")

                # backup existing file
                # print(f"loop hud item: {item}")
                if (
                    os.path.exists(target_item)
                    and not os.path.exists(target_item_backup)
                    and target_item not in self.hud_items_custom
                    and not os.path.isdir(target_item)
                ):
                    os.rename(target_item, target_item_backup)
                    # print(f"{target_item} -> {target_item_backup}")

        # print(f"custom items: {self.hud_items_custom}")

    def _overwrite_target(self):
        for target_sub_dir_name in self.target_sub_dir_names:
            target_sub_dir = os.path.join(self.target_dir_root, target_sub_dir_name)

            # only replace items in the main folder
            if target_sub_dir_name != self.target_dir_main_name:
                continue

            for item in self.hud_items:
                target_item = item.replace(self.source_dir, target_sub_dir)

                # if item is a directory
                if os.path.isdir(item):
                    # create custom folder if needed
                    if not os.path.isdir(target_item):
                        print(f"creating dir: {target_item}")
                        os.makedirs(target_item)
                    continue

                overwrite_target = False
                # if item is a file
                if os.path.isfile(target_item):
                    # target file exists - if modified timestamps differ - overwrite
                    if files_differ(item, target_item):
                        overwrite_target = True
                else:
                    # target file does not exist - overwrite
                    overwrite_target = True

                if overwrite_target:
                    shutil.copy(item, target_item)
                    print(f"{item} -> {target_item}")

        print("overwrite target()")

    def _remove_deleted_items(self):
        for item in self.hud_items_previous:
            if item not in self.hud_items:
                self._unsync_item(item)
        self.hud_items_previous = self.hud_items

    def _unsync_item(self, item):
        print(f"_unsync_item: {item}")

        for target_sub_dir_name in self.target_sub_dir_names:
            target_sub_dir = os.path.join(self.target_dir_root, target_sub_dir_name)
            target_item = item.replace(self.source_dir, target_sub_dir)
            target_item_backup = target_item + ".backup"

            # delete custom folders
            if os.path.isdir(target_item) and target_item in self.hud_items_custom:
                shutil.rmtree(target_item)
                self.hud_items_custom.remove(target_item)
                continue

            # unsync deleted file
            if os.path.isfile(target_item):
                # vanilla file
                os.remove(target_item)
                print(f"removing target item: {target_item}")
                # restore backup, if available
                if os.path.isfile(target_item_backup):
                    shutil.move(target_item_backup, target_item)
                    print(f"{target_item_backup} -> {target_item}")

        # remove custom file from list
        if target_item in self.hud_items_custom:
            self.hud_items_custom.remove(target_item)


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
    input("enter to sync a second time")
    hud_syncer.sync(source_dir_workspace, target_dir_workspace, os.path.basename(game_instance.get_main_dir("dev")))
    # input("enter to sync a third time")
    # hud_syncer.sync(source_dir_workspace, target_dir_workspace, os.path.basename(game_instance.get_main_dir("dev")))
    # input("enter to sync a fourth time")
    # hud_syncer.sync(source_dir_workspace, target_dir_workspace, os.path.basename(game_instance.get_main_dir("dev")))
