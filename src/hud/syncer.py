"""Module providing hud syncing capability between a source dir and the game dir"""

# pylint: disable=invalid-name, broad-exception-caught, broad-exception-raised, logging-fstring-interpolation

import hashlib
import os
import shutil

from loguru import logger
from shared_utils.functions import Singleton

from game.constants import DirectoryMode, SyncState
from game.game import Game
from utils.functions import get_backup_path


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


class ChangeItem:
    """Represents a change item with action, source, and target."""

    def __init__(self, action, source, target=None):
        self.action = action  # 'rename', 'create', or 'copy'
        self.source = source
        self.target = target

    def as_dict(self):
        """Convert the ChangeItem to a dictionary."""
        return {
            "action": self.action,
            "source": self.source,
            "target": self.target,
        }


class FileOperations:
    """Handles file operations like renaming, creating, and copying."""

    def __init__(self, hud_syncer):
        self.hud_syncer = hud_syncer

    def perform_rename(self, hud_item, source_item, target_item):
        """Rename a file or directory."""
        try:
            os.rename(source_item, target_item)
            change = ChangeItem("rename", source_item, target_item)
            self.hud_syncer._record_item_change(hud_item, change.as_dict())
            logger.info(f"Renamed '{source_item}' to '{target_item}'")
        except Exception as e:
            error_message = f"Failed to rename '{source_item}' to '{target_item}': {e}"
            logger.error(error_message)
            raise Exception(error_message) from e

    def perform_create_dir(self, hud_item, source_item, target_item):
        """Create a directory if it doesn't exist."""
        try:
            if not os.path.exists(target_item):
                os.makedirs(target_item)
                change = ChangeItem("create", source_item, target_item)
                self.hud_syncer._record_item_change(hud_item, change.as_dict())
                logger.info(f"Created folder '{target_item}'")
        except OSError as e:
            error_message = f"Failed to create folder '{target_item}': {e}"
            logger.error(error_message)
            raise Exception(error_message) from e

    def perform_copy(self, hud_item, source_item, target_item):
        """Copy a file or directory."""
        try:
            if any(
                change["action"] == "copy" and change["source"] == source_item and change["target"] == target_item
                for change in self.hud_syncer.item_changes.get(hud_item, [])
            ):
                logger.info(f"Copy operation for '{source_item}' to '{target_item}' already exists.")
                return

            shutil.copy(source_item, target_item)
            change = ChangeItem("copy", source_item, target_item)
            self.hud_syncer._record_item_change(hud_item, change.as_dict())  # Convert to dictionary
            logger.info(f"Copied '{source_item}' to '{target_item}'")
        except Exception as e:
            error_message = f"Failed to copy '{source_item}' to '{target_item}': {e}"
            logger.error(error_message)
            raise Exception(error_message) from e


class HudSyncer(metaclass=Singleton):
    """The HudSyncer"""

    def __init__(self):
        """
        Initialize the HudSyncer.

        Initializes various attributes and objects needed for synchronization.
        """
        self.game = Game()
        self.sync_state = None
        self.source_dir = None
        self.target_dir_root = None
        self.target_dir_main_name = None
        self.target_sub_dir_names = []
        self.hud_items_custom = []
        self.hud_items_previous = []
        self.hud_items = None
        self.item_changes = self.game.dir.id.get_sync_changes(DirectoryMode.DEVELOPER)
        self.file_operations = FileOperations(self)

    def _record_item_change(self, hud_item, change):
        """
        Record a change for a HUD item.

        Args:
            hud_item (str): The HUD item to record the change for.
            change (dict): A dictionary representing the change.
        """
        if hud_item in self.item_changes:
            if change not in self.item_changes[hud_item]:
                self.item_changes[hud_item].append(change)
        else:
            self.item_changes[hud_item] = [change]

    def __perform_rename(self, hud_item, source_item, target_item):
        """
        Perform a rename operation for a HUD item.

        Args:
            hud_item (str): The HUD item to be renamed.
            source_item (str): The source item path.
            target_item (str): The target item path.
        """
        self.file_operations.perform_rename(hud_item, source_item, target_item)

    def __perform_create_dir(self, hud_item, source_item, target_item):
        """
        Perform a directory creation operation for a HUD item.

        Args:
            hud_item (str): The HUD item to create a directory for.
            source_item (str): The source directory path.
            target_item (str): The target directory path.
        """
        self.file_operations.perform_create_dir(hud_item, source_item, target_item)

    def __perform_copy(self, hud_item, source_item, target_item):
        """
        Perform a copy operation for a HUD item.

        Args:
            hud_item (str): The HUD item to be copied.
            source_item (str): The source item path.
            target_item (str): The target item path.
        """
        self.file_operations.perform_copy(hud_item, source_item, target_item)

    def __undo_changes_for_item(self, item):
        """
        Undo changes for a specific HUD item.

        Args:
            item (str): The HUD item to undo changes for.
        """
        logger.debug(f"Unsyncing: {item}")
        try:
            changes_for_item = self.item_changes.get(item)
            if changes_for_item is not None:
                for change in reversed(changes_for_item):
                    action = change.get("action")  # Get the action from the dictionary
                    source = change.get("source")
                    target = change.get("target")

                    if action == "rename":
                        os.rename(target, source)
                        logger.info(f"Undone rename of '{target}' to '{source}'")
                    elif action == "create":
                        if os.path.isfile(target):
                            os.remove(target)
                            logger.info(f"Undone create of file '{target}'")
                        elif os.path.isdir(target):
                            shutil.rmtree(target)
                            logger.info(f"Undone create of folder '{target}'")
                    elif action == "copy":
                        if os.path.isfile(target):
                            os.remove(target)
                            logger.info(f"Undone copy of file '{source}' to '{target}'")
                        elif os.path.isdir(target):
                            shutil.rmtree(target)
                            logger.info(f"Undone copy of folder '{source}' to '{target}'")

                    # Since we are iterating and modifying the list, it's better to use a copy of the list
                    # to avoid potential issues with modifying the original list during iteration.
                    changes_for_item.remove(change.copy())
        except Exception as e:
            error_message = f"Failed to undo changes for '{item}': {e}"
            logger.error(error_message)
            raise Exception(error_message) from e

    def __undo_changes_for_all_items(self):
        """
        Undo changes for all HUD items.
        """
        logger.debug("Undoing changes for all items...")
        for hud_item in self.item_changes:
            self.__undo_changes_for_item(hud_item)
        logger.info("Undoing changes for all items completed.")
        self.__set_sync_state(SyncState.NOT_SYNCED)
        self.game.dir.id.set_sync_changes(DirectoryMode.DEVELOPER, {})

    def __set_sync_state(self, sync_state):
        """
        Set the synchronization state.

        Args:
            sync_state (SyncState): The synchronization state to set.
        """
        self.sync_state = sync_state
        self.game.dir.id.set_sync_state(DirectoryMode.DEVELOPER, sync_state)

    def get_source_dir(self):
        """
        Get the source directory.

        Returns:
            str: The source directory path.
        """
        return self.source_dir

    def get_sync_status(self):
        """
        Get the synchronization status.

        Returns:
            SyncState: The synchronization state.
        """
        if self.game.installation_exists(DirectoryMode.DEVELOPER):
            self.__set_sync_state(self.game.dir.id.get_sync_state(DirectoryMode.DEVELOPER))
        else:
            self.__set_sync_state(SyncState.UNKNOWN)

        return self.game.dir.id.get_sync_state(DirectoryMode.DEVELOPER)

    def is_synced(self):
        """
        Check if the HUD is fully synced.

        Returns:
            bool: True if fully synced, False otherwise.
        """
        if self.get_sync_status() == SyncState.FULLY_SYNCED:
            return True
        else:
            return False

    def unsync(self):
        """
        Unsync the HUD.

        Returns:
            bool: True if successfully unsynced, False otherwise.
        """
        logger.debug("Unsyncing...")

        if not self.is_synced():
            logger.debug("debug: No HUD to unsync!")
            return False
        if self.hud_items is None:
            raise ValueError("Code tried to unsync without self.hud_items set!")

        self.__undo_changes_for_all_items()  # also sets sync status

        logger.info("Unsynced!")
        return True

    def sync(self, source_dir: str, target_dir: str, target_dir_main_name: str) -> None:
        """
        Sync the HUD.

        Args:
            source_dir (str): The source directory path.
            target_dir (str): The target directory path.
            target_dir_main_name (str): The main target directory name.
        """
        logger.debug("Synching...")
        logger.debug(f"Source: {source_dir}")
        logger.debug(f"Target: {target_dir}")

        self.source_dir = source_dir
        self.target_dir_root = target_dir
        self.target_dir_main_name = target_dir_main_name
        self.target_sub_dir_names = get_subdirectories_names(target_dir)
        self.hud_items = get_all_files_and_dirs(self.source_dir)
        self.__undo_changes_for_all_items()  # cleanup previously not undone changes eg. program unexpected exit
        self.item_changes = {}

        if source_dir is None or not os.path.isdir(source_dir):
            raise NotADirectoryError(f"Invalid source directory: '{source_dir}'")
        if target_dir is None or not os.path.isdir(target_dir):
            raise NotADirectoryError(f"Invalid target directory: '{target_dir}'")
        if target_dir_main_name not in self.target_sub_dir_names:
            raise NotADirectoryError(
                f"Main directory name '{target_dir}' is not a subdirectory '{self.target_sub_dir_names}"
            )
        no_materials_subdir_msg = (
            f"Main directory name '{target_dir}' is not a valid subdirectory\n"
            "because it doesn't have a materials subdirectory!"
        )

        if not os.path.isdir(os.path.join(target_dir, target_dir_main_name, "materials")):
            raise NotADirectoryError(f"{no_materials_subdir_msg}")

        logger.debug("")
        logger.debug(f"Sync source_dir: {self.source_dir}")
        logger.debug(f"Sync target_dir_root: {self.target_dir_root}")
        logger.debug(f"Sync target_dir_main_name: {self.target_dir_main_name}")
        logger.debug(f"Sync target_sub_dir_names: {self.target_sub_dir_names}")

        self.__backup_and_overwrite_target()
        # self.__overwrite_target()
        self.__unsync_deleted_source_items()

        self.__set_sync_state(SyncState.FULLY_SYNCED)
        self.game.dir.id.set_sync_changes(DirectoryMode.DEVELOPER, self.item_changes)

        logger.info("Synced!")

    def __backup_and_overwrite_target(self):
        """
        Backup and overwrite target directories and files.
        """
        for target_sub_dir_name in self.target_sub_dir_names:
            for item in self.hud_items:
                self.__backup_item(item, target_sub_dir_name)

                if target_sub_dir_name == self.target_dir_main_name:
                    self.__overwrite_item(item, target_sub_dir_name)

    def __backup_item(self, item, target_sub_dir_name):
        """
        Backup a HUD item.

        Args:
            item (str): The HUD item to backup.
            target_sub_dir_name (str): The target subdirectory name.
        """
        target_sub_dir = os.path.join(self.target_dir_root, target_sub_dir_name)
        target_item = item.replace(self.source_dir, target_sub_dir)
        target_item_backup = get_backup_path(target_item)

        # keep track of custom items
        if target_sub_dir_name == self.target_dir_main_name:
            if not os.path.exists(target_item) and (target_item not in self.hud_items_custom):
                self.hud_items_custom.append(target_item)
                logger.debug(f"Adding custom item: {target_item}")

        # backup vanilla files
        if all(
            (
                os.path.isfile(target_item),
                not os.path.exists(target_item_backup),
                target_item not in self.hud_items_custom,
            )
        ):
            self.__perform_rename(item, target_item, target_item_backup)

    def __overwrite_item(self, item, target_sub_dir_name):
        """
        Overwrite a target HUD item.

        Args:
            item (str): The HUD item to overwrite.
            target_sub_dir_name (str): The target subdirectory name.
        """
        target_sub_dir = os.path.join(self.target_dir_root, target_sub_dir_name)
        target_item = item.replace(self.source_dir, target_sub_dir)

        if os.path.isdir(item):
            if not os.path.isdir(target_item):
                self.__perform_create_dir(item, item, target_item)
            return

        overwrite_target = False

        if os.path.isfile(target_item):
            if files_differ(item, target_item):
                overwrite_target = True
        else:
            overwrite_target = True

        if overwrite_target:
            self.__perform_copy(item, item, target_item)

    def __unsync_deleted_source_items(self):
        """
        Unsync deleted source items.
        """
        for item in self.hud_items_previous:
            if item not in self.hud_items:
                self.__undo_changes_for_item(item)
        self.hud_items_previous = self.hud_items
