import time
import tkinter as tk
from tkinter import Menu
from loguru import logger
from shared_gui.base import BaseGUI
from shared_managers.hotkey_manager import HotkeyManager
from shared_managers.hwnd_manager import HwndManager
from shared_utils.functions import Singleton
from src.game.game import Game
from src.hud.hud import Hud
from src.utils.constants import DATA_MANAGER, HOTKEY_EDITOR_MENU


def do_nothing():
    pass


class GuiEditorMenuPopup(BaseGUI, metaclass=Singleton):
    def __init__(self, parent_root, debugging_mode_enabled=False):
        if debugging_mode_enabled:
            self.debug_menu = Menu(parent_root, tearoff=0)
            self.debug_menu.add_command(label="Option 1", command=do_nothing)
            self.debug_menu.add_command(label="Option 2", command=do_nothing)
            self.debug_menu.add_command(label="Option 3", command=do_nothing)
            super().__init__(gui_type="main")
        else:
            super().__init__(gui_type="sub", parent_root=parent_root)
        self.hotkey_manager = HotkeyManager()
        self.hwnd_tools = HwndManager()
        self.debugging_mode_enabled = debugging_mode_enabled
        self.set_title("Editor Context Menu Popup")
        self.set_transparency(0.3)
        self.set_decorations(False)
        self.set_always_on_top(False)
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.set_window_geometry(f"{screen_width}x{screen_height}")
        self.data_manager = DATA_MANAGER
        self.game = Game()
        self.hud = Hud()
        if not self.debugging_mode_enabled:
            from src.menu.main import EditorMenuClass

            self.my_editor_menu = EditorMenuClass(self)
        self.enable_hotkey()

    def enable_hotkey(self):
        self.hotkey_manager.add_hotkey(HOTKEY_EDITOR_MENU, self.show_popup, suppress=False)

    def disable_hotkey(self):
        self.hotkey_manager.remove_hotkey(HOTKEY_EDITOR_MENU)

    def on_menu_close(self):
        print("Menu closed")
        logger.debug("Menu closed")
        self.hide()
        self.hwnd_tools.restore_focus_state()

    def check_menu_closed(self):
        if not self.is_popup_visible():
            self.on_menu_close()
        else:
            self.root.after(100, self.check_menu_closed)

    def is_popup_visible(self):
        try:
            return (
                self.debug_menu.winfo_ismapped()
                if self.debugging_mode_enabled
                else self.my_editor_menu.main_menu.winfo_ismapped()
            )
        except:
            return False

    def show_popup(self):
        self.root.after(0, self._show_popup)

    def _show_popup(self):
        self.hwnd_tools.save_focus_state()
        self.show(hide=False)
        pos_x, pos_y = self.root.winfo_pointerxy()
        if self.debugging_mode_enabled:
            self.debug_menu.post(pos_x, pos_y)
        else:
            self.my_editor_menu.create_and_refresh_menu(is_context_menu=True)
            self.my_editor_menu.main_menu.post(pos_x, pos_y)
        self.root.after(100, self.check_menu_closed)
        logger.debug(f"show_editor_menu_popup_gui_at_cursor: end hidden = {self.is_hidden}")


def main():
    root = tk.Tk()
    root.withdraw()
    app = GuiEditorMenuPopup(root, debugging_mode_enabled=True)
    app.show(hide=True)
    # app.show(hide=True, callback="show_popup") # show_popup callback immediately shows the menu
    input("Press enter to exit script...")


if __name__ == "__main__":
    main()
