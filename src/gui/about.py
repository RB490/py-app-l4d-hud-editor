import tkinter as tk
import webbrowser

from gui.base import BaseGUI
from shared_utils.shared_utils import Singleton
from utils.constants import APP_ICON, SCRIPT_NAME, VERSION_NO, ImageConstants
from utils.persistent_data_manager import PersistentDataManager


class GuiAbout(BaseGUI, metaclass=Singleton):
    """Class for the hud browser gui"""

    def __init__(self, parent_root):
        # set variables
        self.settings_geometry_key = "GuiGeometryAbout"
        self.project_url = "https://github.com/RB490"
        self.img = ImageConstants()
        self.data_manager = PersistentDataManager()

        # create gui
        super().__init__(gui_type="sub", parent_root=parent_root)
        self.root.title("About")
        self.set_resizable(False)
        self.root.iconbitmap(APP_ICON)
        self.set_window_geometry(self.data_manager.get(self.settings_geometry_key))
        self.__create_widgets()

    def __create_widgets(self):
        # Create a label to display project information
        project_info_header = tk.Label(
            self.root,
            text=f"{SCRIPT_NAME} (Version {VERSION_NO})",
            padx=10,
            pady=10,
            font=("Helvetica", 15),
        )
        project_info_header.pack()
        project_info_label = tk.Label(
            self.root,
            text="Barbeque Bacon Burger.",
            padx=10,
            pady=10,
        )
        project_info_label.pack()

        # Create and configure the synchronization hotkey button
        self.open_project_url_btn = tk.Button(
            self.root,
            text="Project Page",
            justify="center",
            command=self.open_main_page,
            state="normal",
            image=self.img.link,
            compound="left",
            padx=10,
            width=125,
            height=25,
        )
        self.open_project_url_btn.pack(padx=10, pady=10)

    def open_main_page(self):
        """Open main page"""
        main_page_url = self.project_url
        webbrowser.open(main_page_url)