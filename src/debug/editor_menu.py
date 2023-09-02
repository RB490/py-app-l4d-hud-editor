from gui.base import BaseGUI
from gui.popup import GuiEditorMenuPopup
from menu.menu import EditorMenuClass
from shared_utils.shared_utils import Singleton, get_invisible_tkinter_root


class debug_editor_menu_class(BaseGUI, metaclass=Singleton):
    def __init__(self, parent_root):
        super().__init__(gui_type="sub", parent_root=parent_root)
        self.root.title("main_debug_editor_menu")
        self.root.minsize(width=400, height=10)
        self.root.maxsize(width=400, height=10)

        self.editor_menu = EditorMenuClass(self, self.root)
        # debug_menu = self.editor_menu.create_and_refresh_menu(is_context_menu=True)
        debug_menu = self.editor_menu.get_context_menu_dev(self.root)

        pos_x, pos_y = self.root.winfo_pointerxy()
        self.show_post_menu(debug_menu, pos_x, pos_y)


def main_debug_editor_menu():
    root = get_invisible_tkinter_root()
    app = debug_editor_menu_class(root)
