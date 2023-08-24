"debug game class"
# pylint: disable=protected-access
from game.constants import DirectoryMode
from game.game import Game


def debug_game_class():
    "debug game class"
    print("debug game class")

    gamez = Game()

    ###########################
    # Game
    ###########################

    result = gamez.installed(DirectoryMode.DEVELOPER)

    ###########################
    # Installer
    ###########################
    # result = gamez.installer.install()
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
    result = gamez.dir.id._get_filename(DirectoryMode.USER)

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

    ###########################
    # Result
    ###########################
    print(f"result = {result}")
