"""Module containing editor menu methods for GuiEditorMenu to keep things organized"""
import os
from tkinter import messagebox
import pyperclip
import vdf
from packages.utils.constants import UNIVERSAL_GAME_MAP
from packages.utils.functions import prompt_add_existing_hud, prompt_open_temp_hud, remove_stored_hud, remove_temp_hud


class EditorMenuHandler:
    """Class containing editor menu methods for GuiEditorMenu to keep things organized"""

    def __init__(self, editor_menu_instance, persistent_data, game_instance, hud_instance):
        self.editor_menu = editor_menu_instance
        self.persistent_data = persistent_data
        self.game = game_instance
        self.hud = hud_instance

    def editor_menu_game_mode(self, mode):
        """Method to handle the selected game mode in the menu."""
        print(f"The selected option is: {mode}")
        self.persistent_data["game_mode"] = mode
        self.game.command.execute(f"map {UNIVERSAL_GAME_MAP}")
        self.editor_menu.create_and_refresh_menu()

    def editor_menu_game_map(self, map_name, map_code):
        """Method to handle the selected game map in the menu."""
        print(f"The code for {map_name} is {map_code}.")
        self.game.command.execute(f"map {map_code}")

    def editor_menu_game_resolution(self, string_resolution):
        """Method to handle the selected game resolution in the menu."""
        print(f"Selected resolution: {string_resolution}")

        config_dir = self.game.get_dev_config_dir()

        # save new resolution
        width, height = map(int, string_resolution.split("x"))
        self.persistent_data["game_res"] = (width, height)

        # retrieve window settings
        video_settings_path = os.path.join(config_dir, "video.txt")
        if os.path.exists(video_settings_path):
            video_settings = vdf.load(open(video_settings_path, encoding="utf-8"))

            print(video_settings)

            has_border = video_settings["VideoConfig"]["setting.nowindowborder"]
            is_fullscreen = video_settings["VideoConfig"]["setting.fullscreen"]
            # toggle windowMode to conform to the mat_setvideo command; video.txt file saves windowed mode as 0
            # and fullscreen as 1. so the exact opposite as mat_setvideomode
            is_fullscreen = not is_fullscreen
        else:
            # use default video settings
            has_border = 1
            is_fullscreen = 1  # 1=windowed

        # set new resolution
        res_w = self.persistent_data["game_res"][0]
        res_h = self.persistent_data["game_res"][1]
        res_command = (
            f"mat_setvideomode 1 1 1 0; mat_setvideomode {res_w} {res_h} {int(is_fullscreen)} {int(has_border)}"
        )
        self.game.command.execute(f"{res_command}; mat_savechanges")

        # restore game position
        self.game.move(self.persistent_data["game_pos"])

    def editor_menu_game_pos(self, pos):
        """Method to handle the selected game position in the menu."""
        print(f"Selected Game Position: {pos}")

        self.persistent_data["game_pos"] = pos
        self.game.move(pos)
        self.editor_menu.create_and_refresh_menu()

    def editor_menu_game_toggle_insecure(self):
        """Method to handle the selected secure/insecure option in the menu."""
        print("editor_menu_game_security")

        # toggle setting
        if self.persistent_data["game_insecure"] is True:
            self.persistent_data["game_insecure"] = False
            self.editor_menu.editor_menu_game_insecure_checkmark.set(0)
        else:
            self.persistent_data["game_insecure"] = True
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
        self.hud.stop_game_exit_check()
        self.game.close()
        self.game.run("dev")
        self.hud.start_game_exit_check()

    def editor_menu_game_toggle_mute(self):
        """Method to handle the selected secure/insecure option in the menu."""
        if self.persistent_data["game_mute"] is True:
            self.persistent_data["game_mute"] = False
            self.game.command.execute("volume 1")
        else:
            self.persistent_data["game_mute"] = True
            self.game.command.execute("volume 0")

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
        # Do something with the panel value (e.g. print it)
        # print(panel)

        # hide previous panel

        # show selected panel
        # EDITOR_SHOW_PANEL = panel
        self.game.command.show_ui_panel(panel)

    def editor_menu_execute_game_command(self, execute_command):
        """Execute selected command ingame"""
        # Do something with the panel value (e.g. print it)
        print(f"todo: execute {execute_command}")

    def editor_give_items(self, action):
        """TODO: probably redirect the give items menu to editor_menu_execute_command"""
        # Define the function to be called when a menu item is selected
        print(f"Executing action '{action}'")

    def editor_add_existing_hud(self):
        """Add exiting hud to the menu"""
        prompt_add_existing_hud(self.persistent_data)
        self.editor_menu.create_and_refresh_menu()

    def editor_remove_stored_hud(self, hud_dir):
        """Remove existing hud"""
        remove_stored_hud(self.persistent_data, hud_dir)
        self.editor_menu.create_and_refresh_menu()

    def editor_remove_temp_hud(self, hud_dir):
        """Remove existing hud"""
        print(f"todo: {hud_dir}")
        remove_temp_hud(self.persistent_data, hud_dir)
        self.editor_menu.create_and_refresh_menu()

    def editor_open_temp_hud(self):
        """Open temporary hud in the menu"""
        prompt_open_temp_hud(self.persistent_data)
        self.editor_menu.create_and_refresh_menu()

    def editor_edit_hud(self, hud_dir):
        """Start editing selected hud"""
        print(f"todo: {hud_dir}")

    def editor_exit_script(self):
        """Exit script"""
        print("editor_exit_script: todo")

    def editor_open_hud_select(self):
        """Open hud select gui"""
        print("editor_open_hud_select: todo")

    def editor_open_hud_browser(self):
        """Open hud browser"""
        print("editor_open_hud_browser: todo")

    def editor_open_folder(self, input_dir):
        """Open folder"""
        print(f"editor_open_folder todo: {input_dir}")

    def editor_open_folder_in_vscode(self, input_dir):
        """Open folder"""
        print(f"editor_open_folder_in_vscode todo: {input_dir}")

    def editor_prompt_game_command(self):
        """Prompt & execute game command"""
        print("editor_prompt_game_command")

    def editor_inspect_hud(self):
        """Show inspect hud gui (vgui_drawtree)"""
        print("editor_inspect_hud")

    def editor_chat_debug_spam_w(self):
        """Spam W's to debug chat"""
        print("editor_chat_debug_spam_w")

    def editor_hide_game_world(self):
        """Hide game world"""
        print("Hide game world")

    def editor_unsync_hud(self):
        """Unsync hud"""
        print("editor_unsync_hud")

    def editor_save_as_vpk(self):
        """Export hud as vpk"""
        print("editor_save_as_vpk")

    def editor_save_as_folder(self):
        """Export hud as folder"""
        print("editor_save_as_folder")

    def editor_menu_reload_click(self):
        """Toggle reload click coordinate"""
        print("editor_save_as_folder")
        self.persistent_data["reload_mouse_clicks_enabled"] = not self.persistent_data["reload_mouse_clicks_enabled"]
        self.editor_menu.reload_mode_menu_coord_clicks_checkmark.set(
            self.persistent_data["reload_mouse_clicks_enabled"]
        )
        self.editor_menu.create_and_refresh_menu()
        print(self.persistent_data["reload_mouse_clicks_enabled"])

    def editor_menu_reload_click_coord1(self):
        """Set reload click coordinate"""
        print("editor_menu_reload_click_coord1")

    def editor_menu_reload_click_coord2(self):
        """Set reload click coordinate"""
        print("editor_menu_reload_click_coord2")

    def editor_menu_send_keys(self, keys):
        """Send input keys to game"""
        print(f"editor_menu_send_keys: {keys}")
