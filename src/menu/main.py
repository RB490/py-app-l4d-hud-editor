# pylint: disable=attribute-defined-outside-init
"""Module containing editor menu methods for GuiEditorMenu to keep things organized"""
import threading
import tkinter as tk
from tkinter import Menu

from loguru import logger
from shared_gui.menu_debug import menu_debug_gui

from src.game.game import Game
from src.menu.handler import EditorMenuHandler
from src.menu.sub.clipboard import MenuClipboard
from src.menu.sub.dev_install import MenuDevInstall
from src.menu.sub.game_map import MenuGameMap
from src.menu.sub.game_mode import MenuGameMode
from src.menu.sub.game_pos import MenuGamePos
from src.menu.sub.game_res import MenuGameRes
from src.menu.sub.give_items import MenuGiveItems
from src.menu.sub.help import MenuHelp
from src.menu.sub.hotkeys import MenuHotkeys
from src.menu.sub.hud import MenuHud
from src.menu.sub.load_hud import MenuLoadHud
from src.menu.sub.open import MenuOpen
from src.menu.sub.reload_mode import MenuReloadMode
from src.menu.sub.show_panel import MenuShowPanel
from src.menu.sub.switch import MenuSwitch
from src.menu.sub.voting import MenuVoting
from src.utils.constants import DATA_MANAGER


class EditorMenuClass:
    """Class containing editor menu methods for GuiEditorMenu to keep things organized

    using this in the main gui because a context menu hotkey doesn't work right in python"""

    def __init__(self, parent_gui):
        self.data_manager = DATA_MANAGER
        self.handler = EditorMenuHandler(self)
        self.parent_gui = parent_gui
        self.img = self.parent_gui.img
        self.game = Game()

        self.menu_game_map = MenuGameMap(self)
        self.menu_game_res = MenuGameRes(self)
        self.menu_game_pos = MenuGamePos(self)
        self.menu_game_mode = MenuGameMode(self)

        self.menu_hud = MenuHud(self)
        self.menu_load_hud = MenuLoadHud(self)
        self.menu_voting = MenuVoting(self)
        self.menu_show_panel = MenuShowPanel(self)
        self.menu_switch = MenuSwitch(self)
        self.menu_hotkeys = MenuHotkeys(self)
        self.menu_help = MenuHelp(self)
        self.menu_reload_mode = MenuReloadMode(self)
        self.menu_clipboard = MenuClipboard(self)
        self.menu_open = MenuOpen(self)
        self.menu_give_items = MenuGiveItems(self)
        self.menu_dev_install = MenuDevInstall(self)
        # pylint: disable=import-outside-toplevel # importing outside top level to avoid circular imports

        from src.hud.hud import Hud

        self.hud = Hud()
        self.create_and_refresh_menu()

    def get_context_menu_dev(self):
        """Retrieve developer installer menu (for adding it to a context menu for example)"""
        self.create_and_refresh_menu(is_context_menu=True)
        return self.dev_install_menu

    def get_context_menu_main(self):
        """Retrieve developer installer menu (for adding it to a context menu for example)"""
        self.create_and_refresh_menu(is_context_menu=True)
        return self.main_menu

    def get_context_menu_help(self):
        """Retrieve developer installer menu (for adding it to a context menu for example)"""
        self.create_and_refresh_menu(is_context_menu=True)
        return self.help_menu

    def get_main_menu(self):
        """Retrieve main menu (for adding as menu bar)"""
        # this line is replaced by 'gui_refresh' in 'create_and_refresh_menu'
        #       self.create_and_refresh_menu(is_context_menu=False)

        return self.main_menu

    def create_and_refresh_menu(self, is_context_menu=False):
        """
        Creates the menu bar for the application
        if not is_context_menu:
        """
        logger.debug("Refreshing editor menu!")

        self.data_manager.save()

        self.main_menu = Menu(self.parent_gui.root, tearoff=False)

        self.reload_mode_menu = self.menu_reload_mode.get(self.main_menu)
        self.hud_menu = self.menu_hud.get(self.main_menu)
        self.game_map_menu = self.menu_game_map.get(self.main_menu)
        self.game_res_menu = self.menu_game_res.get(self.main_menu)
        self.game_pos_menu = self.menu_game_pos.get(self.main_menu)
        self.game_mode_menu = self.menu_game_pos.get(self.main_menu)
        self.load_hud_menu = self.menu_load_hud.get(self.main_menu)
        self.voting_menu = self.menu_voting.get(self.main_menu)
        self.show_panel_menu = self.menu_show_panel.get(self.main_menu)
        self.switch_menu = self.menu_switch.get(self.main_menu)
        self.hotkeys_menu = self.menu_hotkeys.get(self.main_menu)
        self.help_menu = self.menu_help.get(self.main_menu)
        self.give_items_menu = self.menu_give_items.get(self.main_menu)
        self.clipboard_menu = self.menu_clipboard.get(self.main_menu)
        self.open_menu = self.menu_open.get(self.main_menu)
        self.dev_install_menu = self.menu_dev_install.get(self.main_menu)

        # ----------------------------------
        #       Parent tools menu
        # ----------------------------------

        self.tools_menu = tk.Menu(self.main_menu, tearoff=0)
        self.editor_menu_inspect_hud_checkmark = tk.BooleanVar()
        self.tools_menu.add_checkbutton(
            label="Inspect",
            variable=self.editor_menu_inspect_hud_checkmark,
            command=self.handler.editor_inspect_hud,
            columnbreak=False,
            image=self.img.get("plus_sign_on_zoom_magnifier.png", 2),
            compound="left",
        )
        self.editor_menu_hide_world_checkmark = tk.BooleanVar()
        self.tools_menu.add_checkbutton(
            label="Hide world",
            variable=self.editor_menu_hide_world_checkmark,
            command=self.handler.editor_hide_game_world,
            columnbreak=False,
            image=self.img.get("minus", 2),
            compound="left",
        )
        self.tools_menu.add_command(
            label="Chat Debug (WWWW)",
            image=self.img.get("chat_oval_black_interface_symbol_with_text_lines.png", 2),
            compound="left",
            command=self.handler.editor_chat_debug_spam_w,
            columnbreak=True,
        )
        self.tools_menu.add_cascade(
            label="Clipboard",
            image=self.img.get("clipboard", 2),
            compound="left",
            menu=self.clipboard_menu,
        )

        # ----------------------------------
        #       Parent File menu
        # ----------------------------------

        self.file_menu = tk.Menu(self.main_menu, tearoff=0)
        self.file_menu.add_command(
            label="Start",
            image=self.img.get("flag_black_cutted_shape.png", 2),
            compound="left",
            command=self.handler.editor_open_start_gui,
        )
        # only show browser option on context menu
        if is_context_menu:
            self.file_menu.add_command(
                label="Browser",
                image=self.img.get("book", 2),
                compound="left",
                command=self.handler.editor_open_browser_gui,
            )
        self.file_menu.add_cascade(
            label="Open",
            image=self.img.get("arrow_angle_pointing_to_right.png", 2),
            compound="left",
            menu=self.open_menu,
        )
        self.file_menu.add_cascade(
            label="Developer", image=self.img.get("settings", 2), compound="left", menu=self.dev_install_menu
        )
        self.file_menu.add_separator()
        self.file_menu.add_cascade(label="Help", image=self.img.get("help", 2), compound="left", menu=self.help_menu)
        self.file_menu.add_command(
            label="Exit",
            image=self.img.get("close", 2),
            compound="left",
            command=self.handler.editor_save_and_exit_script,
        )

        # ----------------------------------
        #       Parent Tools menu
        # ----------------------------------

        self.debug_menu = tk.Menu(self.main_menu, tearoff=0)
        self.debug_menu.add_command(
            label="Game cmd",
            command=self.handler.editor_prompt_game_command,
            image=self.img.get("game_alt.png", 2),
            compound="left",
        )
        self.debug_menu.add_cascade(
            label="Show panel",
            menu=self.show_panel_menu,
            image=self.img.get("window_black_rounded_square_interface_symbol.png", 2),
            compound="left",
        )
        self.debug_menu.add_cascade(
            label="Call vote",
            menu=self.voting_menu,
            image=self.img.get("window_black_rounded_square_interface_symbol.png", 2),
            compound="left",
        )
        self.debug_menu.add_cascade(
            label="Switch", menu=self.switch_menu, image=self.img.get("switch", 2), compound="left"
        )
        self.debug_menu.add_cascade(
            label="Give items", menu=self.give_items_menu, image=self.img.get("giftbox.png", 2), compound="left"
        )
        self.debug_menu.add_cascade(
            label="Tools", menu=self.tools_menu, image=self.img.get("settings", 2), compound="left"
        )

        # ----------------------------------
        #       Parent Game menu
        # ----------------------------------
        self.game_menu = tk.Menu(self.main_menu, tearoff=0)

        self.game_menu.add_cascade(
            label="Position",
            menu=self.game_pos_menu,
            image=self.img.get("two_opposite_diagonal_arrows_in_black_square.png", 2),
            compound="left",
        )
        self.game_menu.add_cascade(
            label="Resolution",
            menu=self.game_res_menu,
            image=self.img.get("monitor_black_tool.png", 2),
            compound="left",
        )
        self.game_menu.add_cascade(
            label="Map",
            menu=self.game_map_menu,
            image=self.img.get("black_map_folded_paper_symbol.png", 2),
            compound="left",
        )
        self.game_menu.add_cascade(
            label="Mode", menu=self.game_mode_menu, image=self.img.get("switch", 2), compound="left"
        )
        self.game_menu.add_command(
            label="Restart",
            columnbreak=False,
            command=self.handler.editor_menu_game_restart,
            image=self.img.get("reload", 2),
            compound="left",
        )

        self.editor_menu_game_insecure_checkmark = tk.BooleanVar()
        self.game_menu.add_checkbutton(
            label="Insecure",
            variable=self.editor_menu_game_insecure_checkmark,
            command=self.handler.editor_menu_game_toggle_insecure,
            columnbreak=True,
            image=self.img.get("unlocked_padlock.png", 2),
            compound="left",
        )
        if self.data_manager.get("game_insecure.png") is True:
            self.editor_menu_game_insecure_checkmark.set(1)
        else:
            self.editor_menu_game_insecure_checkmark.set(0)

        self.editor_menu_game_always_on_top_checkmark = tk.BooleanVar()
        self.game_menu.add_checkbutton(
            label="Topmost",
            variable=self.editor_menu_game_always_on_top_checkmark,
            command=self.handler.editor_menu_game_toggle_always_on_top,
            image=self.img.get("up_arrow_button.png", 2),
            compound="left",
        )
        if self.data_manager.get("game_always_on_top") is True:
            self.editor_menu_game_always_on_top_checkmark.set(1)
        else:
            self.editor_menu_game_always_on_top_checkmark.set(0)

        self.editor_menu_game_mute_checkmark = tk.BooleanVar()
        self.game_menu.add_checkbutton(
            label="Muted",
            variable=self.editor_menu_game_mute_checkmark,
            command=self.handler.editor_menu_game_toggle_mute,
            image=self.img.get("mute", 2),
            compound="left",
        )
        if self.data_manager.get("game_mute"):
            self.editor_menu_game_mute_checkmark.set(1)
        else:
            self.editor_menu_game_mute_checkmark.set(0)

        self.game_menu.add_command(
            label="Run",
            columnbreak=False,
            command=self.handler.editor_menu_game_run,
            image=self.img.get("game_alt.png", 2),
            compound="left",
        )
        self.game_menu.add_command(
            label="Close",
            columnbreak=False,
            command=self.handler.editor_menu_game_close,
            image=self.img.get("close", 2),
            compound="left",
        )

        # ----------------------------------
        #       Parent menu
        # ----------------------------------

        if not is_context_menu:
            # add without images
            self.main_menu.add_cascade(label="File", menu=self.file_menu)
            if self.hud.edit.is_opened():
                self.main_menu.add_cascade(label="Hud", menu=self.hud_menu)
            self.main_menu.add_cascade(label="Mode", menu=self.reload_mode_menu)
            self.main_menu.add_cascade(label="Game", menu=self.game_menu)
            self.main_menu.add_cascade(label="Debug", menu=self.debug_menu)
        else:
            # add with images
            self.main_menu.add_cascade(
                label="File", image=self.img.get("file", 2), compound="left", menu=self.file_menu
            )
            if self.hud.edit.is_opened():
                self.main_menu.add_cascade(
                    label="Hud",
                    image=self.img.get("paintbrush", 2),
                    compound="left",
                    menu=self.hud_menu,
                )
            self.main_menu.add_cascade(
                label="Mode",
                image=self.img.get("reload", 2),
                compound="left",
                menu=self.reload_mode_menu,
            )
            self.main_menu.add_cascade(
                label="Game", image=self.img.get("game_alt.png", 2), compound="left", menu=self.game_menu
            )
            self.main_menu.add_cascade(
                label="Debug",
                image=self.img.get("hot_or_burn_interface_symbol.png", 2),
                compound="left",
                menu=self.debug_menu,
            )
            self.main_menu.add_command(
                label="Close (ESC)", image=self.img.get("cross", 2), compound="left", command=None
            )  # useful when displaying menu as popup

        # if not self.hud.edit.is_opened():
        #     self.main_menu.entryconfig("Hud", state="disabled")

        # call method to update menu
        if (
            self.parent_gui.has_been_run()
            and hasattr(self.parent_gui, "gui_refresh")
            and callable(getattr(self.parent_gui, "gui_refresh"))
            and not is_context_menu  # don't update if showing a context menu. only if menu.handler is refreshing
        ):
            # self.parent_gui.gui_refresh(called_by_editor_menu=True)
            gui_refresh_thread = threading.Thread(target=self.run_gui_refresh)
            gui_refresh_thread.start()

    def run_gui_refresh(self):
        """Refresh gui"""
        self.parent_gui.gui_refresh(called_by_editor_menu=True)


def main():
    """debug"""
    gui = menu_debug_gui()
    menu = EditorMenuClass(gui)
    menu.create_and_refresh_menu(is_context_menu=True)
    gui.debug_menu(menu.get_main_menu())
    gui.show()


if __name__ == "__main__":
    main()
