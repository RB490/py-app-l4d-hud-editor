# pylint: disable=broad-exception-caught, import-outside-toplevel, c-extension-no-member
"""Module for the hud browser gui class"""
import os
import shutil
import timeit
import tkinter as tk
from datetime import datetime
from tkinter import ttk

import send2trash
import win32gui
from loguru import logger
from PIL import Image, ImageTk
from shared_gui.base import BaseGUI
from shared_managers.hotkey_manager import HotkeyManager
from shared_utils.functions import Singleton, create_temp_file, loguru_setup_logging_filter, show_message

from src.debug.hud import get_hud_debug_instance
from src.game.constants import DirectoryMode
from src.game.game import Game
from src.gui.descriptions import GuiHudDescriptions
from src.gui.popup import GuiEditorMenuPopup
from src.gui.vdf_tool import VDFModifierGUI
from src.hud.hud import Hud
from src.menu.menu import EditorMenuClass
from src.utils.constants import (
    APP_ICON,
    BIG_CROSS_ICON,
    DATA_MANAGER,
    GUI_BROWSER_TITLE,
    HOTKEY_EDITOR_MENU,
    HOTKEY_SYNC_HUD,
    HOTKEY_TOGGLE_BROWSER,
)
from src.utils.functions import get_image_for_file_extension, preform_checks_to_prepare_program_start


class GuiHudBrowser(BaseGUI, metaclass=Singleton):
    """Class for the hud browser gui"""

    def __init__(self, parent_root, parent=None):
        # set variables
        self.parent = parent
        self.settings_geometry_key = "GuiGeometryBrowser"
        self.selected_full_path = None
        self.selected_file_name = None
        self.selected_relative_path = None
        self.treeview_photo_images = []
        self.treeview_photo_images_cache = {}
        self.data_manager = DATA_MANAGER
        self.hud = Hud()
        self.game = Game()

        # create gui
        super().__init__(gui_type="sub", parent_root=parent_root)
        self.popup_gui = GuiEditorMenuPopup(self.root)
        self.descriptions_gui = GuiHudDescriptions(self.root)
        self.set_title(GUI_BROWSER_TITLE)
        self.set_minimum_size(300, 100)
        self.set_icon(APP_ICON)
        self.set_window_geometry(self.data_manager.get(self.settings_geometry_key))
        self.__create_widgets()
        self.__create_context_menu()

        # Bindings
        self.treeview.bind("<<TreeviewSelect>>", self.treeview_set_selected_item)
        self.treeview.bind("<Button-3>", self.treeview_show_context_menu)
        self.treeview.bind("<Up>", self.focus_search_box_if_first_row_selected)
        self.treeview.bind("<Return>", self.action_open_file)
        self.search_box.bind("<Tab>", self.toggle_focus_treeview_and_search)
        self.search_box.bind("<Down>", self.toggle_focus_treeview_and_search)
        self.search_box.bind("<Return>", self.toggle_focus_treeview_and_search)
        self.root.bind("<Control-f>", lambda event: self.search_box.focus_set())
        self.root.bind("<Tab>", self.toggle_focus_treeview_and_search)
        self.root.bind("<Control-Tab>", self.toggle_focus_treeview_and_search)
        self.search_box.bind("<KeyRelease>", self.treeview_search)

        # editor menu
        self.editor_menu = EditorMenuClass(self, self.root)
        self.gui_refresh()

        # set hwnd
        self.hwnd = win32gui.GetParent(self.frame.winfo_id())

        # setup hotkeys
        hotkey_manager = HotkeyManager()
        hotkey_manager.add_hotkey(HOTKEY_TOGGLE_BROWSER, self.toggle_visibility, suppress=True)

        self.treeview_sort_column(self.treeview, "modified", True)

    def focus_search_box_if_first_row_selected(self, *event):
        """Focus search box if first row is selected"""
        # pylint: disable=unused-argument
        selected_item = self.treeview.selection()
        first_row = self.treeview.get_children()[0]  # get the identifier of the first row
        if selected_item and selected_item[0] == first_row:  # compare identifiers
            self.search_box.focus_set()

    def toggle_focus_treeview_and_search(self, *event):
        """Toggle focus between treeview and search"""
        # pylint: disable=unused-argument
        current_focus = self.root.focus_get()
        logger.debug(f"current_focus = {current_focus}")
        if current_focus == self.search_box:
            self.treeview_focus(self.treeview)
            logger.debug("Focused treeview")
        else:
            self.search_box.focus_set()
            logger.debug("Focused searchbox")
        return "break"  # Prevent the default tab behavior (inserting a tab character)

    def __create_widgets(self):
        """Create widgets"""

        # create a frame for all widgets
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill="both", anchor="nw", expand=True)

        # draw controls
        self.__create_toolbar_frame()
        self.__create_search_frame()
        self.__create_treeview()

    def __create_search_frame(self):
        """Search frame"""
        # pylint: disable=attribute-defined-outside-init
        # create a frame for search controls
        self.search_frame = tk.Frame(self.frame)
        self.search_frame.pack(side="bottom", fill="x", padx=5, pady=5)

        self.search_label = tk.Label(self.search_frame, text="Search")
        self.search_label.pack(side="left", padx=5, pady=5)

        self.search_box = tk.Text(self.search_frame, height=1, wrap=None, width=10, takefocus=0)
        self.search_box.pack(side="left", fill="x", expand=True, padx=5, pady=0)

        # create Radiobuttons
        self.display_choice = tk.StringVar(value="Added")

        self.radio_1 = tk.Radiobutton(
            self.search_frame,
            text="Added",
            variable=self.display_choice,
            value="Added",
            command=self.handle_radio_click,
        )
        self.radio_1.pack(side="right", padx=5)

        self.radio_2 = tk.Radiobutton(
            self.search_frame, text="All", variable=self.display_choice, value="All", command=self.handle_radio_click
        )
        self.radio_2.pack(side="right", padx=5)

    def __create_toolbar_frame(self):
        """toolbar frame"""
        # pylint: disable=attribute-defined-outside-init
        # create a frame for toolbar controls
        self.toolbar_frame = tk.Frame(self.frame)
        self.toolbar_frame.pack(side="top", fill="x", padx=5, pady=5)

        btn_img_padx = 10

        # Create and configure the synchronization hotkey button
        self.sync_hotkey_button = tk.Button(
            self.toolbar_frame,
            text=f"Sync {HOTKEY_SYNC_HUD}",
            justify="center",
            command=self.hud.edit.sync,
            state="normal",
            image=self.img.get("reload", 2),
            compound="left",
            padx=btn_img_padx,
            width=125,
            height=25,
        )
        self.sync_hotkey_button.pack(padx=0, pady=0, side="left")

        # Create and configure the browserhronization hotkey button
        self.browser_hotkey_button = tk.Button(
            self.toolbar_frame,
            text=f"{self.get_title()} {HOTKEY_TOGGLE_BROWSER}",
            justify="center",
            command=self.toggle_visibility,
            state="normal",
            image=self.img.get("reload", 2),
            compound="left",
            padx=btn_img_padx,
            width=125,
            height=25,
        )
        self.browser_hotkey_button.pack(padx=5, pady=0, side="left")

        # Create and configure the editor_menuhronization hotkey button
        self.editor_menu_hotkey_button = tk.Button(
            self.toolbar_frame,
            text=f"Menu {HOTKEY_EDITOR_MENU}",
            justify="center",
            command=lambda: self.show_menu_on_button(
                self.editor_menu_hotkey_button, self.editor_menu.get_context_menu_main()
            ),
            state="normal",
            image=self.img.get("book", 2),
            compound="left",
            padx=btn_img_padx,
            width=125,
            height=25,
        )
        self.editor_menu_hotkey_button.pack(padx=5, pady=0, side="left")

        # Create and configure the editor_menuhronization help button
        self.editor_menu_help_button = tk.Button(
            self.toolbar_frame,
            text="Help",
            justify="center",
            # command=self.dummy_handler,
            state="normal",
            image=self.img.get("help", 2),
            compound="left",
            padx=btn_img_padx,
            width=125,
            height=25,
            command=lambda: self.show_menu_on_button(
                self.editor_menu_help_button, self.editor_menu.get_context_menu_dev()
            ),
            # command=lambda: self.show_menu_on_button(
            #     self.editor_menu_help_button, self.editor_menu.get_context_menu_help()
            # ),
        )
        self.editor_menu_help_button.pack(padx=5, pady=0, side="left")

    def __create_treeview(self):
        """Search treeview"""
        # pylint: disable=attribute-defined-outside-init
        # Store PhotoImage objects in a list to prevent garbage collection
        self.treeview_photo_images = []

        # create a treeview with three columns
        self.treeview = ttk.Treeview(
            self.frame, columns=("file", "description", "custom", "modified", "path"), height=15
        )
        self.treeview.heading("#0", text="")
        self.treeview.heading(
            "file", text="File", anchor="w", command=lambda: self.treeview_sort_column(self.treeview, "file", False)
        )
        self.treeview.heading(
            "description",
            text="Description",
            anchor="w",
            command=lambda: self.treeview_sort_column(self.treeview, "description", False),
        )
        self.treeview.heading(
            "custom",
            text="Custom",
            anchor="w",
            command=lambda: self.treeview_sort_column(self.treeview, "custom", False),
        )
        self.treeview.heading(
            "modified",
            text="Modified",
            anchor="w",
            command=lambda: self.treeview_sort_column(self.treeview, "modified", False),
        )
        self.treeview.heading(
            "path", text="Path", anchor="w", command=lambda: self.treeview_sort_column(self.treeview, "path", False)
        )
        self.treeview.column("#0", width=40, minwidth=40, stretch=False)
        self.treeview.column("file", width=260, stretch=False)
        self.treeview.column("description", width=70)
        self.treeview.column("custom", width=25, stretch=False)
        self.treeview.column("modified", width=140, stretch=False)
        self.treeview.column("path", width=50)
        self.treeview.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        # self.treeview.bind("<<TreeviewSelect>>", self.treeview_on_click)
        self.treeview.bind("<Double-1>", self.treeview_on_double_click)

        # Create a Scrollbar widget
        scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.treeview.yview)
        scrollbar.pack(side="right", fill="y")
        # Link the Scrollbar to the Treeview widget
        self.treeview.configure(yscrollcommand=scrollbar.set)

    def __create_context_menu(self):
        """Context menu"""

        if not self.selected_full_path or not os.path.isfile(self.selected_full_path):
            is_new_file = True
        else:
            is_new_file = False

        # Create a context menu
        self.context_menu = tk.Menu(self.treeview, tearoff=False)
        if is_new_file:
            self.context_menu.add_command(
                label="Add File",
                image=self.img.get("plus", 2),
                compound=tk.LEFT,
                command=self.action_add_file,
            )
        else:
            self.context_menu.add_command(
                label="Open File",
                image=self.img.get("file", 2),
                compound=tk.LEFT,
                command=self.action_open_file,
            )
            self.context_menu.add_command(
                label="Open vanilla File",
                image=self.img.get("file", 2),
                compound=tk.LEFT,
                command=self.action_open_vanilla_file,
            )
            self.context_menu.add_command(
                label="Open Folder",
                image=self.img.get("folder", 2),
                compound=tk.LEFT,
                command=self.action_open_folder,
            )
            self.context_menu.add_command(
                label="Open Game Folder",
                image=self.img.get("folder", 2),
                compound=tk.LEFT,
                command=self.action_open_game_folder,
            )
            self.context_menu.add_separator()
            self.context_menu.add_command(
                label="Annotate",
                image=self.img.get("pencil_black_square.png", 2),
                compound=tk.LEFT,
                command=self.action_annotate,
            )
            self.context_menu.add_command(
                label="Description",
                image=self.img.get("list_symbol_of_three_items_with_dots.png", 2),
                compound=tk.LEFT,
                command=self.action_description,
            )
            self.context_menu.add_separator()
            self.context_menu.add_command(
                label="Refresh",
                image=self.img.get("reload", 2),
                compound=tk.LEFT,
                command=self.treeview_refresh,
            )
            self.context_menu.add_command(
                label="Recycle", image=self.img.get("delete", 2), compound=tk.LEFT, command=self.action_recycle
            )

    def dummy_handler(self):
        "Dummy method"
        logger.debug("dummy")

    def handle_radio_click(self):
        """Handle clicks on radio buttons."""
        display_choice = self.display_choice.get()
        # Do something with the selected choice, such as refreshing the UI
        logger.debug(f"Radio button clicked: {display_choice}")
        # self.treeview_refresh()

        # Measure the execution time
        execution_time = timeit.timeit(stmt=self.treeview_refresh, number=1)

        # Print the execution time in seconds
        logger.debug(f"Treeview refreshed in: {execution_time:.6f} seconds")

    def treeview_search(self, event):
        """Search treeview"""
        # pylint: disable=unused-argument

        # Retrieve the search term from the search box
        search_term = self.search_box.get("1.0", "end-1c")

        # Refresh the Treeview with the search term
        self.treeview_refresh(search_term=search_term if search_term else None)

    def treeview_show_context_menu(self, event):
        """Treeview context menu"""

        # Identify the item clicked using event's coordinates
        item = self.treeview.identify_row(event.y)

        # Select the item (optional, but it visually indicates the clicked item)
        if item:
            self.treeview.selection_set(item)
            self.treeview_set_selected_item(item)

            # refresh contexet menu
            self.__create_context_menu()

            # Show the context menu at the event's coordinates
            self.context_menu.post(event.x_root, event.y_root)

    def get_selected_file_name(self):
        "Treeview get info"
        return self.selected_file_name

    def get_selected_full_path(self):
        """Retrieve selected full path"""
        return self.selected_full_path

    def get_selected_relative_path(self):
        """Retrieve selected full path"""
        return self.selected_relative_path

    def treeview_on_double_click(self, event):
        """Handle user double-clicks"""
        region = self.treeview.identify_region(event.x, event.y)

        if region == "cell":
            self.action_open_file()

    # pylint: disable=unused-argument
    def treeview_set_selected_item(self, event):
        """Get select item from treeview"""
        selected_item = self.treeview.selection()
        for item in selected_item:
            item_values = self.treeview.item(item)["values"]

            self.selected_relative_path = item_values[4]
            self.selected_full_path = os.path.join(self.hud.edit.get_dir(), self.selected_relative_path)
            self.selected_file_name = item_values[0]
            logger.debug(f"Selected full path: {self.selected_full_path}")
            logger.debug(f"Selected relative path: {self.selected_relative_path}")
            logger.debug(f"Selected file name: {self.selected_file_name}")

    def on_show(self):
        """Callback on show"""
        self.treeview_refresh()
        self.bring_to_front()
        self.search_box.focus_set()

    def on_hide(self):
        """Callback on hide"""
        if self.has_been_run() and self.descriptions_gui.is_visible():
            self.descriptions_gui.hide()

    def gui_refresh(self, called_by_editor_menu=False):
        """Refresh the menu. Called by self.editor_menu

        Doing this when treeview refreshes because it captures every kind of refresh
        like for example simply when the gui takes focus"""

        # title
        if self.hud.edit.is_opened():
            self.set_title(f"{self.hud.edit.get_name()} {GUI_BROWSER_TITLE}")
        else:
            self.set_title(f"{GUI_BROWSER_TITLE}")

        # editor menu
        if not called_by_editor_menu:
            self.editor_menu.create_and_refresh_menu(is_context_menu=False)
        self.root.config(menu=self.editor_menu.get_main_menu())
        self.root.update_idletasks()  # fixes bug where resetting the menu resizes the gui some

        # treeview
        self.treeview_refresh()

        # refresh start gui
        if self.parent.has_been_run() and self.parent.is_visible():
            self.parent.gui_refresh(called_by_editor_menu=False)

        logger.debug(f"Refreshed {GUI_BROWSER_TITLE} GUI!")

    def treeview_refresh(self, search_term=None):
        """
        Refreshes the provided Treeview with up-to-date content.

        Args:
            treeview (tkinter.Treeview): The Treeview widget to refresh.
            search_term (str, optional): A search term to filter items in the Treeview.

        Returns:
            None
        """
        # don't update tree until has been run
        if not self.get_mainloop_started():
            logger.debug("Not refreshing browser treeview! Mainloop has not been started")
            return

        # Clear existing items in the Treeview
        try:
            self.treeview.delete(*self.treeview.get_children())
        except Exception as e:
            logger.error(f"Treeview items removal error: {e}")
        logger.debug("Cleared treeview!")

        # variables
        treeview = self.treeview
        hud_dir = self.hud.edit.get_dir()

        # verify input
        if not hud_dir or not os.path.isdir(hud_dir):
            logger.debug(f"Not refreshing treeview. No hud dir available: {hud_dir}")
            return

        # Retrieve data based on display choice
        display_choice = self.display_choice.get().lower()
        data_dict = self.hud.edit.get_all_files_dict() if display_choice == "all" else self.hud.edit.get_files_dict()
        if not data_dict:
            logger.debug("Not refreshing browser treeview! No data dict retrieved")
            return

        # Determine if game is in developer mode
        search_term = self.search_box.get("1.0", "end-1c")
        search_term_lower = search_term.lower() if search_term else None

        insert_items = []
        for file_name, (file_desc, file_relative_path) in data_dict.items():
            # Calculate file path
            file_path = os.path.join(hud_dir, file_relative_path)
            # Determine if file is custom based on developer mode
            is_custom = "Y" if self.hud.desc.get_custom_file_status(file_name) else "N"

            # Calculate last modified timestamp and image path
            last_modified = "not_added"
            image_path = BIG_CROSS_ICON
            if os.path.isfile(file_path):
                timestamp = os.path.getmtime(file_path)
                last_modified = datetime.fromtimestamp(timestamp).strftime("%Y.%m.%d @ %H:%M:%S")
                image_path = get_image_for_file_extension(file_path)

            # Check if the search term matches any value
            if search_term_lower and not any(
                search_term_lower in str(value).lower() for value in (file_name, file_desc, file_relative_path)
            ):
                continue

            # Prepare item for insertion
            insert_items.append((file_name, file_desc, is_custom, last_modified, file_relative_path, image_path))

        # Store PhotoImage objects to prevent them from being garbage collected
        self.treeview_photo_images = []

        # First, load the images and create PhotoImage objects
        # (this process is quite slow and caching speeds it up to almost instantaneous)
        # Create a dictionary to store loaded images for each path
        image_photos = []
        for item in insert_items:
            file_name, file_desc, is_custom, last_modified, file_relative_path, image_path = item
            
            # Check if the image has already been loaded
            if image_path in self.treeview_photo_images_cache:
                photo = self.treeview_photo_images_cache[image_path]
            else:
                # If not, load the image, resize it, and store it in the cache
                image = Image.open(image_path).resize((16, 16), Image.LANCZOS)
                photo = ImageTk.PhotoImage(image)
                self.treeview_photo_images_cache[image_path] = photo
                logger.warning(f"adding image to cache: {image_path}")
            
            image_photos.append(photo)

        # Now, insert the items into the Treeview using the preloaded images
        for item, photo in zip(insert_items, image_photos):
            file_name, file_desc, is_custom, last_modified, file_relative_path, _ = item
            self.treeview_photo_images.append(photo)

            # Insert the item into the Treeview
            treeview.insert(
                "",
                "end",
                values=(file_name, file_desc, is_custom, last_modified, file_relative_path),
                image=photo,
            )

        logger.debug("Refreshed treeview!")

    def show_popup_gui(self):
        """Show editor menu as a context menu"""

        self.popup_gui.show(hide=True)

    def save_window_geometry(self):
        """Save size & position if GUI is loaded and visible"""
        self.data_manager.set(self.settings_geometry_key, self.get_window_geometry())

    def action_add_file(self):
        """Treeview Handle 'Add File' option (add new file to hud)"""
        logger.debug("Method: action_add_file - Handle 'Add File' option (add new file to hud)")

        # variables
        full_path = self.get_selected_full_path()
        rel_path = self.get_selected_relative_path()
        vanilla_file = self.game.dir.get_vanilla_file(rel_path)

        # create directory if needed, and copy file
        logger.info(f"Adding new file: '{vanilla_file}' -> '{full_path}'")
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        shutil.copyfile(vanilla_file, full_path)

        # update treeview
        self.treeview_refresh()

    def action_open_file(self):
        """Treeview Handle 'Open File' option"""
        logger.debug("Method: treeview_open_file - Handle 'Open File' option")
        full_path = self.get_selected_full_path()
        os.startfile(full_path)
        self.hide()

    def action_open_vanilla_file(self):
        """Treeview handle Open vanilla File' option"""
        logger.debug("Method: treeview_open_default_file - handle 'Open vanilla File' option")

        rel_path = self.get_selected_relative_path()
        vanilla_path = self.game.dir.get_vanilla_file(rel_path)

        if vanilla_path:
            logger.debug(f"Opening vanilla file: '{vanilla_path}'")

            create_temp_file(vanilla_path)

        else:
            logger.debug("Vanilla file unavailable")

    def action_open_folder(self):
        "Treeview Handle 'Open Folder' option"
        logger.debug("Method: treeview_open_folder - Handle 'Open Folder' option")
        full_path = self.get_selected_full_path()
        directory = os.path.dirname(full_path)
        if os.path.isdir(directory):
            logger.debug(f"Opening directory: '{directory}'")
            os.startfile(directory)
        else:
            logger.debug(f"Directory unavailable: '{directory}'")

    def action_open_game_folder(self):
        "Treeview Handle 'Open Game Folder' option"
        logger.debug("Method: treeview_open_game_folder - Handle 'Open Game Folder' option")

        if not self.game.installation_exists(DirectoryMode.DEVELOPER):
            logger.debug("Unable to open game directory. Developer directory is not installed.")
            return

        rel_path = self.get_selected_full_path()
        main_dir = self.game.dir.get_main_dir(DirectoryMode.DEVELOPER)
        game_directory = os.path.join(main_dir, rel_path)

        if os.path.isdir(game_directory):
            logger.debug(f"Opening game directory: '{game_directory}'")
            os.startfile(game_directory)
        else:
            logger.debug(f"Game directory unavailable: '{game_directory}'")

    def action_description(self):
        "Treeview Handle 'Description' option"
        logger.debug("Method: treeview_description - TODO: Handle 'Description' option")

        file_name = self.get_selected_file_name()
        rel_path = self.get_selected_relative_path()
        self.descriptions_gui.load_file(file_name, rel_path)

    def action_annotate(self):
        "Treeview Handle 'Annotate' option"
        logger.debug("Method: treeview_describe - TODO: Handle 'Annotate' option")

        try:
            app = VDFModifierGUI(self.root, self.selected_full_path)
            app.show()
        except Exception:
            logger.debug("Can't load VDF GUI!")

    def action_recycle(self):
        "Treeview Handle 'Recycle' option"
        logger.debug("Method: treeview_recycle - TODO: Handle 'Recycle' option")

        full_path = self.get_selected_full_path()

        # prompt remove
        result = show_message(f"Move '{os.path.basename(full_path)}' to the recycle bin?", "yesno")
        if not result:
            return

        send2trash.send2trash(full_path)
        self.treeview_refresh()


def main():
    "debug_gui_browser"
    # pylint: disable=unused-variable
    from src.gui.start import GuiHudStart

    print("debug_browser")
    hud_inc = get_hud_debug_instance()  # set active debug hud to load files into browser

    # root = get_invisible_tkinter_root()

    # game_class = Game()
    # game_class.window.run(DirectoryMode.DEVELOPER)

    # browser = GuiHudBrowser(root)
    # browser.show()
    start_instance = GuiHudStart()
    start_instance.show(hide=True, callback="debug_show_browser_gui")  # start mainloop
    # start_instance.browser.show()
    # start_instance.show(hide=False, callback="debug_show_browser_gui")  # start mainloop

    return


if __name__ == "__main__":
    os.system("cls")
    preform_checks_to_prepare_program_start()
    loguru_setup_logging_filter("INFO")
    # loguru_setup_logging_filter("DEBUG")
    # loguru_setup_logging_filter("DEBUG", "include", ["src.gui.browser"])
    main()
