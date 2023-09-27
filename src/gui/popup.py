"""Module for the editor menu"""
# pylint: disable=import-outside-toplevel
from shared_gui.base import BaseGUI
from shared_managers.hotkey_manager import HotkeyManager
from shared_utils.functions import Singleton

from src.game.game import Game
from src.hud.hud import Hud
from src.utils.constants import DATA_MANAGER, HOTKEY_EDITOR_MENU


class GuiEditorMenuPopup(BaseGUI, metaclass=Singleton):
    """
    A class representing a toggle window with hotkey functionality and a menu bar.

    Attributes:
        root (tkinter.Tk): The main window of the application.
        is_hidden (bool): A flag indicating whether the window is currently hidden.

    Methods:
        __init__(self): Initializes the ToggleWindow instance and runs the main event loop.
        toggle_visibility(self): Toggles the visibility of the window.
        setup_hotkey(self): Sets up the hotkey for toggling window visibility.
        create_menu(self): Creates the menu bar for the application.
        do_nothing(self): A dummy function that does nothing.
    """

    def __init__(self, parent_root, debug_instantly_show_menu=False):
        """
        Initializes a new instance of the ToggleWindow class and runs the main event loop.

        Create a fully transparent GUI the size of the entire screen so clicking out of the context menu closes it
        """
        super().__init__(gui_type="sub", parent_root=parent_root)
        self.hotkey_manager = HotkeyManager()

        # root
        self.debug_instantly_show_menu = debug_instantly_show_menu
        self.set_title("Editor Context Menu Popup")
        self.set_transparency(0.3)  # fully transparent makes it less reliable somehow
        self.set_decorations(False)
        self.set_always_on_top(False)  # not setting this because it causes prompts to be behind the gui

        # Set size to entire screen because set_fullscreen has a 0.1 visible delay ;-)
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.set_window_geometry(f"{screen_width}x{screen_height}")

        self.data_manager = DATA_MANAGER
        self.game = Game()
        self.hud = Hud()

        from src.menu.menu import EditorMenuClass

        self.my_editor_menu = EditorMenuClass(self, self.root)
        self.enable_hotkey()

        if self.debug_instantly_show_menu:
            self.show_popup()

    def enable_hotkey(self):
        """Enable hotkey"""
        self.hotkey_manager.add_hotkey(HOTKEY_EDITOR_MENU, self.show_popup, suppress=False)

    def disable_hotkey(self):
        """Disable hotkey"""
        self.hotkey_manager.remove_hotkey(HOTKEY_EDITOR_MENU)  # prevent it from being pressed while menu is open

    def show_popup(self):
        """Show menu at mouse cursor"""

        # Show gui so context menu can be closed by clicking out & Resize the GUI to the entire screen
        self.maximize()  # not setting fullscreen because it disables alt+tab

        # get coordinates
        pos_x, pos_y = self.root.winfo_pointerxy()

        # show menu
        # self.dev_context_menu = self.my_editor_menu.get_developer_installer_menu(self.root)
        # self.dev_context_menu.post(pos_x, pos_y)
        self.my_editor_menu.create_and_refresh_menu(is_context_menu=True)
        self.show_post_menu(self.my_editor_menu.main_menu, pos_x, pos_y)

        # hide gui after context menu closed
        self.hide()
        print(f"show_editor_menu_popup_gui_at_cursor: end hidden = {self.is_hidden}")
