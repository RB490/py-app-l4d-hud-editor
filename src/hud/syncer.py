"""Module providing hud syncing capability between a source dir and the game dir"""
# pylint: disable=invalid-name, broad-exception-caught, broad-exception-raised
import hashlib
import os
import shutil

from game.constants import DirectoryMode
from game.game import Game
from utils.constants import SyncState
from utils.shared_utils import Singleton


def calculate_md5_hash(file_path):
    """Calculate MD5 hash of a file."""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def files_differ(file_path1, file_path2):
    """Check if two files are different based on MD5 hash."""
    return calculate_md5_hash(file_path1) != calculate_md5_hash(file_path2)


def get_all_files_and_dirs(directory):
    """Get a list of all files and subdirectories in a directory."""
    file_and_dir_list = []
    for dirpath, dirnames, filenames in os.walk(directory):
        file_and_dir_list.extend([os.path.join(dirpath, name) for name in dirnames + filenames])
    return file_and_dir_list


def get_subdirectories_names(directory):
    """Get a list of names of subdirectories in the given directory."""
    return [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]


class HudSyncer(metaclass=Singleton):
    """functions providing hud syncing/unsyncing capability from the source to game dir"""

    def __init__(self, persistent_data):
        self.game = Game(persistent_data)
        self.sync_state = self.game.dir.id.get_sync_state(DirectoryMode.DEVELOPER)
        # self.sync_state = SyncState.NOT_SYNCED
        self.source_dir = None  # hud folder
        self.target_dir_root = None  # eg: '..\steamapps\common\Left 4 Dead 2'
        self.target_dir_main_name = None  # 'left4dead2' as opposed to 'left4dead2_dlc1'
        self.target_sub_dir_names = None  # eg: 'left4dead2_dlc1'
        self.hud_items_custom = []  # the custom hud files and directories
        self.hud_items_previous = []  # the previous hud files and directories. used to compare and find deletes items
        self.hud_items = None  # the hud files and directories

        # restore game files if a hud is still incorrectly synced (syncer being a singleton makes this once per script)
        if self.sync_state == SyncState.FULLY_SYNCED:
            result = str(input("Press enter to restore developer restory! Or 'no' to leave it as is"))
            if result is not "no":
                self.game.dir.restore_developer_directory()
                self.game.dir.id.set_sync_state(DirectoryMode.DEVELOPER, SyncState.NOT_SYNCED)

    def get_source_dir(self):
        """Return source directory"""
        return self.source_dir

    def get_sync_status(self):
        """Return sync status"""
        return self.sync_state

    def is_synced(self):
        """Return sync status"""
        if self.sync_state == SyncState.FULLY_SYNCED:
            return True
        else:
            return False

    def unsync(self):
        """Unsync the hud"""
        print("Unsyncing...")

        # verify we can unsync
        if not self.is_synced():
            print("Unsync: No hud to unsync!")
            return

        print(f"Unsyncing hud: {self.hud_items}")

        # Copy list to avoid causing issues with the loop
        hud_items_copy = self.hud_items.copy()

        # unsync every item
        for item in hud_items_copy:
            print(f"Unsyncing: {item}")
            self.__unsync_item(item)

        # finished
        self.sync_state = self.game.dir.id.set_sync_state(DirectoryMode.DEVELOPER, SyncState.NOT_SYNCED)
        print("Unsynced!")

    def sync(self, source_dir: str, target_dir: str, target_dir_main_name: str) -> None:
        # pylint: disable=anomalous-backslash-in-string
        """Syncs the contents of the source directory to the target directory.

        Parameters:
        source_dir (str): The path of the source directory to sync from. EG: ..\\l4d-addons-huds\\2020HUD\\source
        target_dir (str): The path of the target directory to sync to. EG: ..\\steamapps\\common\\Left 4 Dead 2
        target_dir_main_name (str): The main name of the target directory,
            used to differentiate from dlc folders and only perform
            certain actions on the main directory. EG: 'Left 4 Dead 2'
        """

        print("Synching...")
        print(f"Source: {source_dir}")
        print(f"Target: {target_dir}")
        # print(f"target_dir_main_name: {target_dir_main_name}")

        # Unsync the previous hud (if syncing different hud)
        if self.is_synced() and self.source_dir != source_dir:
            self.unsync()

        # Save input
        self.source_dir = source_dir
        self.target_dir_root = target_dir
        self.target_dir_main_name = target_dir_main_name
        self.target_sub_dir_names = get_subdirectories_names(target_dir)
        self.hud_items = get_all_files_and_dirs(self.source_dir)

        # Validate input
        if source_dir is None or not os.path.isdir(source_dir):
            raise ValueError(f"Invalid source directory: '{source_dir}'")
        if target_dir is None or not os.path.isdir(target_dir):
            raise ValueError(f"Invalid target directory: '{target_dir}'")
        if target_dir_main_name not in self.target_sub_dir_names:
            raise ValueError(f"Main directory name '{target_dir}' is not a subdirectory '{self.target_sub_dir_names}")
        no_materials_subdir_msg = (
            f"Main directory name '{target_dir}' is not a valid subdirectory\n"
            "because it doesn't have a materials subdirectory!"
        )

        if not os.path.isdir(os.path.join(target_dir, target_dir_main_name, "materials")):
            raise ValueError(f"{no_materials_subdir_msg}")

        # input
        print()
        print(f"Sync source_dir: {self.source_dir}")
        print(f"Sync target_dir_root: {self.target_dir_root}")
        print(f"Sync target_dir_main_name: {self.target_dir_main_name}")
        print(f"Sync target_sub_dir_names: {self.target_sub_dir_names}")
        print(f"Sync hud_items: {self.hud_items}")

        # Backup game files
        self.__backup_target()

        # Overwrite game files
        self.__overwrite_target()

        # Unsync deleted items in target
        self.__remove_deleted_source_items()

        self.sync_state = self.sync_state = self.game.dir.id.set_sync_state(
            DirectoryMode.DEVELOPER, SyncState.FULLY_SYNCED
        )

        print("Synced!")
        # input("end of sync()")

    def __backup_target(self):
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
                # print(f"loop hud item: {item}")
                if (
                    os.path.exists(target_item)
                    and not os.path.exists(target_item_backup)
                    and target_item not in self.hud_items_custom
                    and not os.path.isdir(target_item)
                ):
                    try:
                        os.rename(target_item, target_item_backup)
                        print(f"Backup: {target_item} -> {target_item_backup}")
                    except Exception as e:
                        # print(f"Error backing up {target_item}: {e}")
                        raise Exception(f"Error backing up {target_item}: {e}") from e

        # print(f"custom items: {self.hud_items_custom}")

    def __overwrite_target(self):
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
                        os.makedirs(target_item)
                        print(f"Creating: {target_item}")
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
                    try:
                        shutil.copy(item, target_item)
                        print(f"Copying: {item} -> {target_item}")
                    except Exception as e:
                        # print(f"Error copying {item} to {target_item}: {e}")
                        raise Exception(f"Error copying {item} to {target_item}: {e}") from e

    def __remove_deleted_source_items(self):
        for item in self.hud_items_previous:
            if item not in self.hud_items:
                self.__unsync_item(item)
        self.hud_items_previous = self.hud_items

    def __unsync_item(self, item):
        print(f"Unsyncing: {item}")

        for target_sub_dir_name in self.target_sub_dir_names:
            target_sub_dir = os.path.join(self.target_dir_root, target_sub_dir_name)
            target_item = item.replace(self.source_dir, target_sub_dir)
            target_item_backup = target_item + ".backup"

            print(f"Unsync directory: {target_sub_dir}")
            print(f"& target_item_backup: {target_item_backup}")

            # delete custom directory
            if os.path.isdir(target_item) and target_item in self.hud_items_custom:
                shutil.rmtree(target_item)
                print(f"Deleting custom directory: {target_item}")
                self.hud_items_custom.remove(target_item)
                continue

            # delete custom item
            if os.path.isfile(target_item) and target_item in self.hud_items_custom:
                os.remove(target_item)
                print(f"Deleting custom file: {target_item}")
                self.hud_items_custom.remove(target_item)
                continue

            # restore file to original state
            if os.path.isfile(target_item_backup):
                shutil.move(target_item_backup, target_item)
                print(f"Restoring: {target_item_backup} -> {target_item}")

        # remove file from lists
        if target_item in self.hud_items_custom:
            self.hud_items_custom.remove(target_item)
