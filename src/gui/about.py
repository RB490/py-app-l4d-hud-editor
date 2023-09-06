"""Class for the hud browser gui"""
import tkinter as tk
import webbrowser

from gui.base import BaseGUI
from shared_utils.shared_utils import Singleton
from utils.constants import APP_ICON, PROGRAM_NAME, PROGRAM_URL, VERSION_NO, VERSION_NO_GITHUB, ImageConstants
from utils.persistent_data_manager import PersistentDataManager


class GuiAbout(BaseGUI, metaclass=Singleton):
    """Class for the hud browser gui"""

    def __init__(self, parent_root):
        # set variables
        self.settings_geometry_key = "GuiGeometryAbout"
        self.project_url = PROGRAM_URL
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
            text=f"{PROGRAM_NAME} (Version {VERSION_NO})",
            padx=10,
            pady=10,
            font=("Helvetica", 13),
        )
        project_info_header.pack()

        project_info_latest_version_label = tk.Label(
            self.root,
            text=f"Github Version: {VERSION_NO_GITHUB}",
            padx=10,
            pady=10,
        )
        project_info_latest_version_label.pack()

        # Create and configure the synchronization hotkey button
        self.open_project_url_btn = tk.Button(
            self.root,
            text="Github Page",
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
