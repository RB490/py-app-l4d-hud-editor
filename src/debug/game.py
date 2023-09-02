"debug game class"
from game.constants import DirectoryMode, InstallationState, SyncState
from game.game import Game


def debug_game_set_states_synced_and_installed():
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

    # result = gamez.installation_completed(DirectoryMode.DEVELOPER)

    ###########################
    # Installer
    ###########################
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
    # result = gamez.dir.set(DirectoryMode.USER)
    # result = gamez.dir.set(DirectoryMode.USER)

    # result = gamez.dir.get(DirectoryMode.USER)
    # result = gamez.dir.get(DirectoryMode.USER)

    # result = gamez.dir._get_main_subdir(DirectoryMode.DEVELOPER, "materials")
    # result = gamez.dir.get_main_dir_backup(DirectoryMode.DEVELOPER)

    # result = gamez.dir.is_custom_file("scripts\\hudlayout.res")
    # result = gamez.dir.is_custom_file("scripts\\custom_hudlayout.res")

    # result = gamez.dir.check_for_invalid_id_file_structure()

    # result = gamez.dir.dev_out_of_date()

    result = gamez.dir.get_resource_file_relative_path("clientscheme_borders.res")
    result = gamez.dir.get_resource_file_relative_path("hudlayout.res")

    ###########################
    # Result
    ###########################
    print(f"result = {result}")
