"debug game class"
import logging

from game.constants import DirectoryMode, InstallationState, SyncState
from game.game import Game
from shared_utils.logging_manager import get_logger

logger = get_logger(__name__, log_level=logging.DEBUG)


def debug_game_set_states_synced_and_installed():
    """Debug"""
    game_class = Game()
    game_class.dir.id.set_sync_state(
        DirectoryMode.DEVELOPER, SyncState.NOT_SYNCED
    )  # Prevent restore_developer_directory from activating
    game_class.dir.id.set_installation_state(
        DirectoryMode.DEVELOPER, InstallationState.COMPLETED
    )  # Prevent restore_developer_directory from activating


def main_debug_game():
    "debug game class"
    print("debug game class")

    gamez = Game()

    ###########################
    # Game
    ###########################

    gamez.window.close()

    ###########################
    # Installer
    ###########################
    # result = gamez.installation_completed(DirectoryMode.DEVELOPER)
    # result = gamez.installer.install()
    # result = gamez.installer.repair()
    # result = gamez.installer.uninstall()
    # result = gamez.installer._main_dir_backup()
    # print("hi there!")
    # result = gamez.window.run(DirectoryMode.DEVELOPER)
    # result = gamez.command.execute("noclip")
    # result = gamez.command._get_reload_fonts_command()
    # result = gamez.command.execute()
    # result = gamez.command.execute()
    # result = gamez.installer._uninstall()
    # gamez.installer._install()

    # result = gamez.installer._uninstall()
    # result = gamez.installer.__install_mods()
    # result = gamez.window.run(DirectoryMode.DEVELOPER, wait_on_close=120)
    # result = gamez._disable_addons()
    # result = gamez._write_config()

    ###########################
    # ID
    ###########################
    # result = gamez.dir.id.get_installation_state
    # result = gamez.dir.id._get_filename(DirectoryMode.USER)

    # result = gamez.dir.id.get_installation_state(DirectoryMode.USER)
    # result = gamez.dir.id.get_sync_state(DirectoryMode.DEVELOPER)
    # result = gamez.dir.id.get_sync_state(DirectoryMode.USER)
    # result = SyncState["COMPLETED"]

    ###########################
    # Directory
    ###########################
    # result = gamez.dir.set(DirectoryMode.USER) # FIXME this is testing for the duplicate messages
    # result = gamez.dir.set(DirectoryMode.DEVELOPER)
    # result = gamez.dir.set(DirectoryMode.USER)
    # logger.debug("what the fuck?????????????????")
    # result = gamez.dir.set(DirectoryMode.USER)
    # result = gamez.dir.set(DirectoryMode.DEVELOPER)
    # result = gamez.dir.set(DirectoryMode.DEVELOPER)

    # result = gamez.dir.get(DirectoryMode.USER)
    # result = gamez.dir.get(DirectoryMode.DEVELOPER)

    # result = gamez.dir._get_main_subdir(DirectoryMode.DEVELOPER, "materials")
    # result = gamez.dir.get_main_dir_backup(DirectoryMode.DEVELOPER)

    # result = gamez.dir.is_custom_file("scripts\\hudlayout.res")
    # result = gamez.dir.is_custom_file("scripts\\custom_hudlayout.res")

    # result = gamez.dir.check_for_invalid_id_file_structure()

    # result = gamez.dir.dev_out_of_date()

    ###########################
    # Result
    ###########################
    # print(f"result = {result}")
