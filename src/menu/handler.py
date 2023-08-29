"""Module containing editor menu methods for GuiEditorMenu to keep things organized"""
# pylint: disable=broad-exception-caught
import os
import sys
from tkinter import messagebox

import pyperclip  # type: ignore

from game.game import DirectoryMode, Game, VideoSettingsModifier
from shared_utils.shared_utils import show_message
from utils.constants import UNIVERSAL_GAME_MAP
from utils.functions import get_mouse_position_on_click, show_start_gui
from utils.get_user_input import get_user_input
from utils.persistent_data_manager import PersistentDataManager


class EditorMenuHandler:
    """Class containing editor menu methods for GuiEditorMenu to keep things organized"""

    def __init__(self, editor_menu_instance):
        self.data_manager = PersistentDataManager()
        self.editor_menu = editor_menu_instance
        self.game = Game()
        # pylint: disable=import-outside-toplevel # importing outside top level to avoid circular imports
        from hud.hud import Hud

        self.hud = Hud()

    def editor_menu_game_mode(self, mode):
        """Method to handle the selected game mode in the menu."""
        print(f"The selected option is: {mode}")
        self.data_manager.set("game_mode", "mode")
        self.game.command.execute(f"map {UNIVERSAL_GAME_MAP}")
        self.editor_menu.create_and_refresh_menu()

    def editor_menu_game_map(self, map_name, map_code):
        """Method to handle the selected game map in the menu."""
        print(f"The code for {map_name} is {map_code}.")
        self.game.command.execute(f"map {map_code}")

    def editor_menu_game_resolution(self, string_resolution):
        """Method to handle the selected game resolution in the menu."""
        print(f"Selected resolution: {string_resolution}")

        config_dir = self.game.dir.get_cfg_dir(DirectoryMode.DEVELOPER)

        # save new resolution
        width, height = map(int, string_resolution.split("x"))
        self.data_manager.set("game_res", (width, height))

        # retrieve window settings
        video_settings_modifier = VideoSettingsModifier(config_dir)
        video_settings = video_settings_modifier.load_video_settings()

        if video_settings:
            has_border = video_settings_modifier.get_nowindowborder()
            is_fullscreen = 1
        else:
            # use default video settings
            has_border = 1
            is_fullscreen = 1

        # set new resolution
        res_w = self.data_manager.get("game_res")[0]
        res_h = self.data_manager.get("game_res")[1]
        res_command = (
            f"mat_setvideomode 1 1 1 0; mat_setvideomode {res_w} {res_h} {int(is_fullscreen)} {int(has_border)}"
        )
        self.game.command.execute(f"{res_command}; mat_savechanges")

        # restore game position
        self.game.window.restore_saved_position()

    def editor_menu_game_pos(self, pos):
        """Method to handle the selected game position in the menu."""
        print(f"Selected Game Position: {pos}")

        if "custom" in pos.lower():
            self.game.window.save_position()
        else:
            self.game.window.set_position(pos)

        self.editor_menu.create_and_refresh_menu()

    def editor_menu_game_toggle_insecure(self):
        """Method to handle the selected secure/insecure option in the menu."""
        print("editor_menu_game_security")

        # toggle setting
        if self.data_manager.get("game_insecure") is True:
            self.data_manager.set("game_insecure", False)
            self.editor_menu.editor_menu_game_insecure_checkmark.set(0)
        else:
            self.data_manager.set("game_insecure", True)
            self.editor_menu.editor_menu_game_insecure_checkmark.set(1)

        # refresh menu
        self.editor_menu.create_and_refresh_menu()

        # prompt to restart game
        message = "Restart needed for changes to take effect.\n\nDo you want to restart now?"
        if messagebox.askyesno("Restart Game", message):
            self.editor_menu_game_restart()

    def editor_menu_game_close(self):
        """Method to handle the selected secure/insecure option in the menu."""
        self.game.close()

    def editor_menu_game_restart(self):
        """Method to handle the selected secure/insecure option in the menu."""
        self.hud.edit.stop_game_exit_check()
        self.game.close()
        self.game.window.run(DirectoryMode.DEVELOPER)
        self.hud.edit.start_game_exit_check()

    def editor_menu_game_toggle_mute(self):
        """Method to handle the selected secure/insecure option in the menu."""
        if self.data_manager.get("game_mute") is True:
            self.data_manager.set("game_mute", False)
            self.game.command.execute("volume 1")
        else:
            self.game.command.execute("volume 0")
            self.data_manager.set("game_mute", True)

        # refresh menu
        self.editor_menu.create_and_refresh_menu()

    def editor_menu_copy_snippet(self, file_path):
        """Copy snippet to clipboard"""
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            pyperclip.copy(content)
            print(content)

    def editor_menu_show_panel(self, panel):
        """Show selected panel ingame"""

        # set selected panel
        self.game.command.set_ui_panel(panel)
        self.game.command.execute(self.data_manager.get("editor_reload_mode"))
        self.editor_menu.create_and_refresh_menu()

    def editor_menu_reload_hud_once(self, reload_mode):
        """Reload the hud once"""
        print(f'TODO editor_menu_reload_hud_once={reload_mode}')
        self.game.command.execute(reload_mode)

    def editor_menu_set_hud_reload_mode(self, reload_mode):
        """Set the hud reload setting & reload hud once"""
        print(f'TODO editor_menu_set_hud_reload_mode={reload_mode}')
        self.data_manager.set("reload_mode", reload_mode)
        self.editor_menu_set_hud_reload_mode(reload_mode)

    def editor_menu_execute_game_command(self, execute_command):
        """Execute selected command ingame"""
        self.game.command.execute(execute_command)

    def editor_give_items(self, action):
        """Method to handle giving items from the menu"""
        # Define the function to be called when a menu item is selected
        self.game.command.execute(action)

    def editor_add_existing_hud(self):
        """Add exiting hud to the menu"""
        self.hud.manager.prompt_add_existing_hud()
        self.editor_menu.create_and_refresh_menu()

    def editor_create_new_hud(self):
        """Add exiting hud to the menu"""
        self.hud.manager.prompt_create_new_hud()
        self.editor_menu.create_and_refresh_menu()

    def editor_remove_stored_hud(self, hud_dir):
        """Remove existing hud"""
        self.hud.manager.remove_stored_hud(hud_dir)
        self.editor_menu.create_and_refresh_menu()

    def editor_remove_temp_hud(self, hud_dir):
        """Remove existing hud"""
        print(f"editor_remove_temp_hud: {hud_dir}")
        self.hud.manager.remove_temp_hud(hud_dir)
        self.editor_menu.create_and_refresh_menu()

    def editor_open_temp_hud(self):
        """Open temporary hud in the menu"""
        self.hud.manager.prompt_open_temp_hud()
        self.editor_menu.create_and_refresh_menu()

    def editor_edit_hud(self, hud_dir):
        """Start editing selected hud"""
        self.hud.edit.start_editing(hud_dir)

        # refresh menu (selected hud)
        self.editor_menu.create_and_refresh_menu()

    def editor_exit_script(self):
        """Exit script"""

        self.hud.edit.finish_editing(open_start_gui=False)
        sys.exit()

    def editor_open_start_gui(self):
        """Open hud select gui"""
        print("editor_open_hud_select")
        show_start_gui()

    def editor_finish_editing(self):
        """Finish editing and sync changes"""
        print("editor_finish_editing")
        self.hud.edit.finish_editing(open_start_gui=True)

    def editor_open_folder(self, input_dir):
        """Open folder"""
        print(f"editor_open_folder: {input_dir}")
        directory = input_dir
        if os.path.isdir(directory):
            os.startfile(directory)
        else:
            messagebox.showerror("Error", "Source directory does not exist!")

    def editor_open_folder_in_vscode(self, input_dir):
        """Open folder"""
        print(f"editor_open_folder_in_vscode: {input_dir}")
        os.system(f'start /b cmd /c code . "{input_dir}"')

    def editor_prompt_game_command(self):
        """Prompt & execute game command"""

        def handle_user_input(result):
            print(f"user_command: {result}")
            if result:
                self.game.command.execute(result)

        get_user_input(self.editor_menu.root, "Execute game command", "Enter game command:", handle_user_input)

    def editor_inspect_hud(self):
        """Show inspect hud gui (vgui_drawtree)"""
        self.game.command.set_inspect_hud(self.editor_menu.editor_menu_inspect_hud_checkmark.get())

    def editor_chat_debug_spam_w(self):
        """Spam W's to debug chat"""

        long_string = "W" * 144
        self.game.command.execute(f"say {long_string}")

    def editor_hide_game_world(self):
        """Hide game world"""
        if self.editor_menu.editor_menu_hide_world_checkmark.get() is True:
            self.game.command.execute("r_drawWorld 0; r_drawEntities 0")
        else:
            self.game.command.execute("r_drawWorld 1; r_drawEntities 1")

    def editor_unsync_hud(self):
        """Unsync hud"""
        self.hud.unsync()
        self.editor_menu.create_and_refresh_menu()

    def editor_save_as_vpk(self):
        """Export hud as vpk"""
        self.hud.edit.save_vpk_file()

    def editor_save_as_folder(self):
        """Export hud as folder"""
        self.hud.edit.save_as_folder()

    def editor_menu_reload_reopen_menu(self):
        """Repen menu on reload setting"""
        reload_reopen_menu_on_reload = self.data_manager.get("reload_reopen_menu_on_reload")
        self.data_manager.set("reload_reopen_menu_on_reload", not reload_reopen_menu_on_reload)
        self.editor_menu.reload_mode_menu_reopen_menu_checkmark.set(not reload_reopen_menu_on_reload)
        self.editor_menu.create_and_refresh_menu()
        print(not reload_reopen_menu_on_reload)

    def editor_menu_reload_click(self):
        """Toggle reload click coordinate"""
        reload_mouse_clicks_enabled = self.data_manager.get("reload_mouse_clicks_enabled")
        self.data_manager.set("reload_mouse_clicks_enabled", not reload_mouse_clicks_enabled)
        self.editor_menu.reload_mode_menu_coord_clicks_checkmark.set(not reload_mouse_clicks_enabled)
        self.editor_menu.create_and_refresh_menu()
        print(not reload_mouse_clicks_enabled)

    def editor_menu_reload_click_coord1(self):
        # pylint: disable=invalid-name
        """Set reload click coordinate"""

        def xy_coord_callback(x, y):
            if x is not None and y is not None:
                print(f"The mouse was clicked at ({x}, {y})")
                coord_1 = (x, y)
                self.data_manager.set("reload_mouse_clicks_coord_1", coord_1)
            else:
                print("The operation was cancelled or the window was closed")

            self.editor_menu.create_and_refresh_menu()
            print(f"Coord #1 set to: {coord_1}")

        get_mouse_position_on_click(xy_coord_callback)

    def editor_menu_reload_click_coord2(self):
        # pylint: disable=invalid-name
        """Set reload click coordinate"""

        def xy_coord_callback(x, y):
            if x is not None and y is not None:
                print(f"The mouse was clicked at ({x}, {y})")
                coord_2 = (x, y)
                self.data_manager.set("reload_mouse_clicks_coord_2", coord_2)
            else:
                print("The operation was cancelled or the window was closed")

            self.editor_menu.create_and_refresh_menu()
            print(f"Coord #2 set to: {coord_2}")

        get_mouse_position_on_click(xy_coord_callback)

    def editor_menu_disconnect(self):
        """Send input keys to game"""
        self.game.command.send_keys_in_background("f11")

    def editor_installer_open_user_dir(self):
        """This method returns the user directory."""
        print("Opening user directory")
        try:
            directory = self.game.dir.get(DirectoryMode.USER)
            os.startfile(directory)
        except Exception as err_info:
            print(f"Could not open user directory: {err_info}")
            show_message("Directory does not exist!", "error")

    def editor_installer_open_dev_dir(self):
        """
        This method returns the developer directory.
        """
        print("Opening developer directory")
        try:
            directory = self.game.dir.get(DirectoryMode.DEVELOPER)
            os.startfile(directory)
        except Exception as err_info:
            print(f"Could not open developer directory: {err_info}")
            show_message("Directory does not exist!", "error")

    def editor_installer_enable_dev_mode(self):
        """
        This method enables developer mode.
        """
        print("Enabling developer mode")
        result = self.game.dir.set(DirectoryMode.DEVELOPER)
        if result:
            show_message(f"Enabled {DirectoryMode.DEVELOPER.name} mode!", "info")
        else:
            show_message(f"Failed to set {DirectoryMode.DEVELOPER.name} mode!", "info")

    def editor_installer_disable_dev_mode(self):
        """
        This method disables developer mode.
        """
        print("Disabling developer mode")
        result = self.game.dir.set(DirectoryMode.USER)
        if result:
            show_message(f"Enabled {DirectoryMode.USER.name} mode!", "info")
        else:
            show_message(f"Failed to set {DirectoryMode.USER.name} mode!", "info")

    def editor_installer_install(self):
        """
        This method installs developer mode.
        """
        print("Install developer mode")
        self.game.installer.install()

    def editor_installer_update(self):
        """
        This method updates developer mode.
        """
        print("Updating developer mode")
        self.game.installer.update()

    def editor_installer_repair(self):
        """
        This method repairs developer mode.
        """
        print("Repairing developer mode")
        self.game.installer.repair()

    def editor_installer_uninstall(self):
        """
        This method removes developer mode.
        """
        print("Removing developer mode")
        self.game.installer.uninstall()
