"""Debug editor menu"""
from shared_gui.base import BaseGUI
from shared_utils.functions import Singleton, get_invisible_tkinter_root

from src.menu.menu import EditorMenuClass


class debug_editor_menu_class(BaseGUI, metaclass=Singleton):
    """Debug editor menu"""

    def __init__(self, parent_root):
        super().__init__(gui_type="sub", parent_root=parent_root)
        self.root.title("main_debug_editor_menu")
        self.root.minsize(width=400, height=10)
        self.root.maxsize(width=400, height=10)

        self.editor_menu = EditorMenuClass(self, self.root)
        self.root.config(menu=self.editor_menu.get_main_menu())

        context_menu = self.editor_menu.get_context_menu_main()
        # context_menu = self.editor_menu.get_context_menu_dev()

        pos_x, pos_y = self.root.winfo_pointerxy()
        self.show_post_menu(context_menu, pos_x, pos_y)


def main_debug_editor_menu():
    """Debug editor menu"""
    root = get_invisible_tkinter_root()
    debug_editor_menu_class(root)
