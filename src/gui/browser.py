# pylint: disable=broad-exception-caught, import-outside-toplevel
"""Module for the hud browser gui class"""
import os
import tkinter as tk
from datetime import datetime
from tkinter import ttk

import keyboard
import send2trash
import win32gui
from PIL import Image, ImageTk

from debug.hud import get_hud_debug_instance
from game.constants import DirectoryMode
from game.game import Game
from gui.base import BaseGUI
from gui.vdf import VDFModifierGUI
from hud.hud import Hud
from menu.menu import EditorMenuClass
from shared_utils.shared_utils import Singleton, show_message
from utils.constants import APP_ICON, HOTKEY_TOGGLE_BROWSER, IMAGES_DIR, ImageConstants
from utils.functions import get_image_for_file_extension, save_and_exit_script
from utils.persistent_data_manager import PersistentDataManager


class GuiHudBrowser(BaseGUI, metaclass=Singleton):
    """Class for the hud browser gui"""

    def __init__(self):
        # pylint: disable=c-extension-no-member
        print("GuiHudBrowser")
        super().__init__()
        self.data_manager = PersistentDataManager()

        # set variables
        self.hud = Hud()
        self.game = Game()
        self.root.title("Browser")
        self.root.minsize(300, 100)
        self.root.iconbitmap(APP_ICON)
        self.img = ImageConstants()
        from gui.descriptions import GuiHudDescriptions

        self.selected_full_path = None
        self.descriptions_gui = GuiHudDescriptions()
        self.set_window_geometry(self.data_manager.get("BrowserGuiGeometry"))

        # Store PhotoImage objects in a list to prevent garbage collection
        self.treeview_photo_images = []

        # draw controls
        # create a frame for all widgets
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill="both", anchor="nw", expand=True)

        # create a frame for search controls
        self.search_frame = tk.Frame(self.frame)
        self.search_frame.pack(side="top", fill="x", padx=5, pady=5)

        self.search_label = tk.Label(self.search_frame, text="Search")
        self.search_label.pack(side="left", padx=5, pady=5)

        self.search_box = tk.Text(self.search_frame, height=1, wrap=None, width=10)
        self.search_box.pack(side="left", fill="x", expand=True, padx=5, pady=0)
        self.search_box.bind("<KeyRelease>", self.treeview_search)

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

        # create a treeview with three columns
        self.treeview = ttk.Treeview(
            self.frame, columns=("file", "description", "custom", "modified", "path"), height=15
        )
        self.treeview.heading("#0", text="")
        self.treeview.heading(
            "file", text="File", anchor="w", command=lambda: self.treeview_sort_column("file", False)
        )
        self.treeview.heading(
            "description",
            text="Description",
            anchor="w",
            command=lambda: self.treeview_sort_column("description", False),
        )
        self.treeview.heading(
            "custom", text="Custom", anchor="w", command=lambda: self.treeview_sort_column("custom", False)
        )
        self.treeview.heading(
            "modified", text="Modified", anchor="w", command=lambda: self.treeview_sort_column("modified", False)
        )
        self.treeview.heading(
            "path", text="Path", anchor="w", command=lambda: self.treeview_sort_column("path", False)
        )
        self.treeview.column("#0", width=40, minwidth=40, stretch=False)
        self.treeview.column("file", width=260, stretch=False)
        self.treeview.column("description", width=50)
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

        # Bind the function to the selection event
        self.treeview.bind("<<TreeviewSelect>>", self.tree_set_selected_item)

        # Create a context menu
        self.context_menu = tk.Menu(self.treeview, tearoff=False)
        self.context_menu.add_command(
            label="Open File",
            image=self.img.file_black_rounded_symbol_1,
            compound=tk.LEFT,
            command=self.action_open_file,
        )
        self.context_menu.add_command(
            label="Open vanilla File",
            image=self.img.file_black_rounded_symbol_1,
            compound=tk.LEFT,
            command=self.action_open_vanilla_file,
        )
        self.context_menu.add_command(
            label="Open Folder",
            image=self.img.folder_black_interface_symbol,
            compound=tk.LEFT,
            command=self.action_open_folder,
        )
        self.context_menu.add_command(
            label="Open Game Folder",
            image=self.img.folder_black_interface_symbol,
            compound=tk.LEFT,
            command=self.action_open_game_folder,
        )
        self.context_menu.add_separator()
        self.context_menu.add_command(
            label="Annotate", image=self.img.pencil_black_square, compound=tk.LEFT, command=self.action_annotate
        )
        self.context_menu.add_command(
            label="Description",
            image=self.img.list_symbol_of_three_items_with_dots,
            compound=tk.LEFT,
            command=self.action_description,
        )
        self.context_menu.add_separator()
        self.context_menu.add_command(
            label="Refresh",
            image=self.img.arrows_couple_counterclockwise_rotating_symbol,
            compound=tk.LEFT,
            command=lambda: self.treeview_refresh(self.treeview),
        )
        self.context_menu.add_command(
            label="Recycle", image=self.img.trash_can_black_symbol, compound=tk.LEFT, command=self.action_recycle
        )

        # self.context_menu.entryconfig("Recycle", image=self.delete_icon, compound=tk.LEFT)

        # Bind the context menu to the right-click event on the treeview
        self.treeview.bind("<Button-3>", self.treeview_show_context_menu)

        # editor menu
        self.my_editor_menu = EditorMenuClass(self, self.root)
        self.my_editor_menu.create_and_refresh_menu()

        # set hwnd
        self.hwnd = win32gui.GetParent(self.frame.winfo_id())

        self.treeview_refresh(self.treeview)
        self.treeview_sort_column("modified", True)

    def show(self):
        # destroy other main gui to prevent tkinter issues
        # from gui.start import GuiHudStart

        # start_gui = GuiHudStart()
        # start_gui.destroy()

        self.root.deiconify()
        self.is_hidden = False
        self.root.mainloop()

    def dummy_handler(self):
        "Dummy method"
        print("dummy")

    def handle_radio_click(self):
        """Handle clicks on radio buttons."""
        display_choice = self.display_choice.get()
        # Do something with the selected choice, such as refreshing the UI
        print(f"Radio button clicked: {display_choice}")
        self.treeview_refresh(self.treeview)

    def treeview_sort_column(self, col, reverse):
        """Sort selected treeview column"""
        # pylint: disable=unused-variable
        sorted_items = [(self.treeview.set(k, col), k) for k in self.treeview.get_children("")]
        sorted_items.sort(reverse=reverse)

        # rearrange items in sorted positions
        for index, (val, k) in enumerate(sorted_items):
            self.treeview.move(k, "", index)

        # reverse sort next time
        self.treeview.heading(col, command=lambda: self.treeview_sort_column(col, not reverse))

    def treeview_search(self, event):
        """Search treeview"""
        # pylint: disable=unused-argument

        # Retrieve the search term from the search box
        search_term = self.search_box.get("1.0", "end-1c")

        # Refresh the Treeview with the search term
        self.treeview_refresh(self.treeview, search_term=search_term if search_term else None)

    def treeview_show_context_menu(self, event):
        """Treeview context menu"""

        # Identify the item clicked using event's coordinates
        item = self.treeview.identify_row(event.y)

        # Select the item (optional, but it visually indicates the clicked item)
        if item:
            self.treeview.selection_set(item)

        # Show the context menu at the event's coordinates
        self.context_menu.post(event.x_root, event.y_root)

    def treeview_get_selected_values(self):
        """Get a list of the values of the selected treeview row"""

        selection = self.treeview.selection()
        if not selection:
            return "No item selected"

        item = self.treeview.selection()[0]
        values = self.treeview.item(item)["values"]

        return values

    def treeview_set_selected_full_path(self):
        """Retrieve selected treeview row path"""
        relative_path = self.treeview_get_selected_relative_path()
        full_path = os.path.join(self.hud.edit.get_dir(), relative_path)
        self.selected_full_path = full_path if full_path else "No item selected"

    def treeview_get_selected_relative_path(self):
        "Treeview get info"
        values = self.treeview_get_selected_values()
        if values:
            return values[4]
        return None

    def get_selected_full_path(self):
        """Retrieve selected full path"""
        return self.selected_full_path

    def treeview_on_double_click(self, event):
        """Handle user double-clicks"""
        region = self.treeview.identify_region(event.x, event.y)

        print(region)

        if region == "cell":
            cell = self.treeview.identify_row(event.y)
            print("Double-clicked on row:", cell)
            # Perform your desired action here, e.g., open a file
            self.tree_set_selected_item(cell)
            if os.path.isfile(self.selected_full_path):
                os.startfile(self.selected_full_path)

    # pylint: disable=unused-argument
    def tree_set_selected_item(self, event):
        """Get select item from treeview"""
        selected_item = self.treeview.selection()
        for item in selected_item:
            # item_values = self.treeview.item(item)["values"]
            # print(item_values)
            rel_path = self.treeview.item(item)["values"][4]
            self.selected_full_path = os.path.join(self.hud.edit.get_dir(), rel_path)
            print(f"Selected full path: {self.selected_full_path}")

    def treeview_refresh(self, treeview, search_term=None):
        """
        Refreshes the provided Treeview with up-to-date content.

        Args:
            treeview (tkinter.Treeview): The Treeview widget to refresh.
            search_term (str, optional): A search term to filter items in the Treeview.

        Returns:
            None
        """
        # Get HUD directory and display choice
        hud_dir = self.hud.edit.get_dir()
        display_choice = self.display_choice.get().lower()

        # Retrieve data based on display choice
        data_dict = self.hud.edit.get_all_files_dict() if display_choice == "all" else self.hud.edit.get_files_dict()
        if not data_dict:
            print("Treeview: No data to display")
            return

        # Clear existing items in the Treeview
        treeview.delete(*treeview.get_children())

        # Determine if game is in developer mode
        search_term_lower = search_term.lower() if search_term else None

        insert_items = []

        for file_name, (file_desc, file_relative_path) in data_dict.items():
            # Calculate file path
            file_path = os.path.join(hud_dir, file_relative_path)
            # Determine if file is custom based on developer mode
            is_custom = "Y" if self.hud.desc.get_custom_file_status(file_relative_path) else "N"

            # Calculate last modified timestamp and image path
            last_modified = "not_added"
            image_path = os.path.join(IMAGES_DIR, "cross128.png")
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

        # Insert items into the Treeview
        for item in insert_items:
            file_name, file_desc, is_custom, last_modified, file_relative_path, image_path = item
            image = Image.open(image_path).resize((16, 16), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            self.treeview_photo_images.append(photo)

            # Insert the item into the Treeview
            treeview.insert(
                "",
                "end",
                values=(file_name, file_desc, is_custom, last_modified, file_relative_path),
                image=photo,
            )

        # Add a hotkey and print refresh completion
        keyboard.add_hotkey(HOTKEY_TOGGLE_BROWSER, self.toggle_visibility, suppress=True)
        print("Treeview: Refreshed")

    def save_window_geometry(self):
        """Save size & position if GUI is loaded and visible"""
        self.data_manager.set("BrowserGuiGeometry", self.get_window_geometry())

    def on_close(self):
        """Runs on close"""
        self.descriptions_gui.on_close()
        self.save_window_geometry()
        save_and_exit_script()

    def action_open_file(self):
        """Treeview Handle 'Open File' option"""
        print("Method: treeview_open_file - Handle 'Open File' option")
        full_path = self.get_selected_full_path()
        os.startfile(full_path)

    def action_open_vanilla_file(self):
        """Treeview handle Open vanilla File' option"""
        print("Method: treeview_open_default_file - handle 'Open vanilla File' option")

        full_path = self.game.dir.get_vanilla_file()
        if full_path:
            print(f"Opening vanilla file: '{full_path}'")
            os.startfile(full_path)
        else:
            print(f"vanilla file unavailable: '{full_path}'")

    def action_open_folder(self):
        "Treeview Handle 'Open Folder' option"
        print("Method: treeview_open_folder - Handle 'Open Folder' option")
        full_path = self.get_selected_full_path()
        directory = os.path.dirname(full_path)
        if os.path.isdir(directory):
            print(f"Opening directory: '{directory}'")
            os.startfile(directory)
        else:
            print(f"Directory unavailable: '{directory}'")

    def action_open_game_folder(self):
        "Treeview Handle 'Open Game Folder' option"
        print("Method: treeview_open_game_folder - Handle 'Open Game Folder' option")

        if not self.game.installation_exists(DirectoryMode.DEVELOPER):
            print("Unable to open game directory. Developer directory is not installed.")
            return

        rel_path = self.treeview_get_selected_relative_path()
        main_dir = self.game.dir.get_main_dir(DirectoryMode.DEVELOPER)
        game_directory = os.path.join(main_dir, rel_path)

        if os.path.isdir(game_directory):
            print(f"Opening game directory: '{game_directory}'")
            os.startfile(game_directory)
        else:
            print(f"Game directory unavailable: '{game_directory}'")

    def action_description(self):
        "Treeview Handle 'Description' option"
        print("Method: treeview_description - TODO: Handle 'Description' option")

        rel_path = self.treeview_get_selected_relative_path()
        self.descriptions_gui.load_file(rel_path)

    def action_annotate(self):
        "Treeview Handle 'Annotate' option"
        print("Method: treeview_describe - TODO: Handle 'Annotate' option")

        try:
            app = VDFModifierGUI(self.selected_full_path)
            app.show()
        except Exception:
            print("Browser: Can't load VDF GUI!")

    def action_recycle(self):
        "Treeview Handle 'Recycle' option"
        print("Method: treeview_recycle - TODO: Handle 'Recycle' option")

        full_path = self.get_selected_full_path()

        # prompt remove
        result = show_message(f"Move '{os.path.basename(full_path)}' to the recycle bin?", "yesno")
        if not result:
            return

        send2trash.send2trash(full_path)
        self.treeview_refresh(self.treeview)


def show_browser_gui():
    "There can only be one main Tkinter GUI using root.mainloop() at oncee"
    # from gui.start import GuiHudStart

    # # # destroy other main gui
    # start_gui = GuiHudStart()
    # start_gui.destroy()

    hud_inc = get_hud_debug_instance()  # set active debug hud to load files into browser

    browser_gui = GuiHudBrowser()
    browser_gui.show()
    print("Opened the Browser GUI!")
    return browser_gui
