"""Module for the hud browser gui class"""
import os
import tkinter as tk
from datetime import datetime
from tkinter import ttk

import keyboard
import send2trash
import win32gui
from PIL import Image, ImageTk

from game.constants import DirectoryMode
from game.game import Game
from gui.descriptions import GuiHudDescriptions
from menu.menu import EditorMenuClass
from utils.constants import APP_ICON, HOTKEY_TOGGLE_BROWSER, IMAGES_DIR
from utils.functions import (
    get_backup_path,
    get_image_for_file_extension,
    save_and_exit_script,
)
from utils.shared_utils import Singleton


class GuiHudBrowser(metaclass=Singleton):
    """Class for the hud browser gui"""

    def __init__(self, persistent_data):
        # pylint: disable=c-extension-no-member
        print("GuiHudBrowser")

        # pylint: disable=import-outside-toplevel # importing outside top level to avoid circular imports
        from hud.hud import Hud

        # set variables
        self.is_hidden = None
        self.hud = Hud(persistent_data)
        self.game = Game(persistent_data)
        self.root = tk.Tk()
        self.hide()
        self.persistent_data = persistent_data
        self.root.title("Browser")
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.root.minsize(300, 100)
        self.root.iconbitmap(APP_ICON)
        self.descriptions_gui = GuiHudDescriptions(self.persistent_data, self)
        # self.root.wm_attributes("-topmost", 1)  # python can't focus windows so always on top it is

        # Store PhotoImage objects in a list to prevent garbage collection
        self.treeview_photo_images = []

        # load saved geometry
        try:
            geometry = self.persistent_data["BrowserGuiGeometry"]
            self.root.geometry(geometry)
        except KeyError:
            self.root.geometry("1000x1000+100+100")

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

        # Create a context menu
        self.context_menu = tk.Menu(self.treeview, tearoff=False)
        self.context_menu.add_command(label="Open File", command=self.treeview_open_file)
        self.context_menu.add_command(label="Open Default File", command=self.treeview_open_default_file)
        self.context_menu.add_command(label="Open Folder", command=self.treeview_open_folder)
        self.context_menu.add_command(label="Open Game Folder", command=self.treeview_open_game_folder)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="Description", command=self.treeview_description)
        self.context_menu.add_command(label="Integers", command=self.treeview_integers)
        self.context_menu.add_command(label="Describe", command=self.treeview_describe)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="Recycle", command=self.treeview_recycle)

        # Bind the context menu to the right-click event on the treeview
        self.treeview.bind("<Button-3>", self.treeview_show_context_menu)

        # editor menu
        self.my_editor_menu = EditorMenuClass(self, self.root, persistent_data)
        self.my_editor_menu.create_and_refresh_menu()

        # set hwnd
        self.hwnd = win32gui.GetParent(self.frame.winfo_id())

        self.treeview_refresh(self.treeview)
        self.treeview_sort_column("modified", True)

    def dummy_handler(self):
        "Dummy method"
        print("dummy")

    def run(self):
        "Show & start main loop"
        # hotkeys
        keyboard.add_hotkey(HOTKEY_TOGGLE_BROWSER, self.toggle_visibility, suppress=True)

        self.show()
        self.root.mainloop()

    def show(self):
        """Show gui"""
        self.root.deiconify()
        self.is_hidden = False

    def hide(self):
        """Hide gui"""
        self.root.withdraw()
        self.is_hidden = True

    def toggle_visibility(self):
        """
        Toggles the visibility of the window between visible and hidden.

        Because python can't focus windows (win32 has a function but it doesn't work, wow.) set it to always on top
        """
        if self.is_hidden:
            self.show()
        else:
            self.hide()

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

    def treeview_get_selected_full_path(self):
        """Retrieve selected treeview row path"""
        relative_path = self.treeview_get_selected_relative_path()
        full_path = os.path.join(self.hud.get_dir(), relative_path)
        return full_path if full_path else "No item selected"

    def treeview_get_selected_relative_path(self):
        "Treeview get info"
        values = self.treeview_get_selected_values()
        if values:
            return values[4]
        return None

    def treeview_on_double_click(self, event):
        """Handle user clicks"""
        # pylint: disable=unused-argument

        file_path = self.treeview_get_selected_full_path()
        if os.path.isfile(file_path):
            os.startfile(file_path)

    def treeview_refresh(self, treeview, search_term=None):
        """Clear treeview & load up-to-date content"""

        hud_dir = self.hud.get_dir()

        print(f"Treeview: Refreshing directory: '{hud_dir}'")

        print(f"display choice: '{self.display_choice.get()}'")
        display_choice = self.display_choice.get().lower()
        if display_choice == "all":
            data_dict = self.hud.get_all_files_dict()
        else:
            data_dict = self.hud.get_files_dict()

        # check if there is anything to refresh
        if not data_dict:
            print("Treeview: No data to display")
            return

        # Clear existing items in the Treeview
        treeview.delete(*treeview.get_children())

        # Add items from the data_dict to the Treeview
        for file_name, desc_relpath_tuple in data_dict.items():
            file_desc = desc_relpath_tuple[0]

            # path
            file_relative_path = desc_relpath_tuple[1]
            file_path = os.path.join(hud_dir, file_relative_path)

            # custom file?
            if self.game.installed(DirectoryMode.DEVELOPER) and self.hud.synced():
                main_dir = self.game.dir.get_main_dir(DirectoryMode.DEVELOPER)
                file_path_backup = get_backup_path(os.path.join(main_dir, file_relative_path))

                is_custom = "N" if os.path.isfile(file_path_backup) else "Y"
            else:
                is_custom = "-"

            # modified
            if os.path.isfile(file_path):
                timestamp = os.path.getmtime(file_path)
                last_modified = datetime.fromtimestamp(timestamp).strftime("%Y.%m.%d @ %H:%M:%S")
            else:
                last_modified = "not_added"

            # image
            if os.path.isfile(file_path):
                image_path = get_image_for_file_extension(file_path)
            else:
                image_path = os.path.join(IMAGES_DIR, "cross128.png")
            image = Image.open(image_path)
            image = image.resize((16, 16), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            self.treeview_photo_images.append(photo)  # Store the PhotoImage object

            # search
            if (
                search_term
                and search_term.lower() not in str(file_name).lower()
                and search_term.lower() not in str(file_desc).lower()
                and search_term.lower() not in str(file_relative_path).lower()
            ):
                # Skip this item if search term is provided and not found in key or value
                continue

            # add item
            treeview.insert(
                "", "end", values=(file_name, file_desc, is_custom, last_modified, file_relative_path), image=photo
            )
            # treeview.insert("", "end", values=(file_name, file_desc, "", file_relative_path)) # legacy

        print("Treeview: Refreshed")

    def save_window_geometry(self):
        """Save size & position if GUI is loaded and visible"""
        if self.root and self.root.winfo_viewable():
            # Get the current position and size of the window
            geometry = self.root.geometry()
            print(f"geometry: {geometry}")
            self.persistent_data["BrowserGuiGeometry"] = geometry
        else:
            print("GUI is not loaded or visible. Skipping window geometry save.")

    def destroy_gui(self):
        "Close & stop main loop"
        keyboard.remove_hotkey(HOTKEY_TOGGLE_BROWSER)
        self.save_window_geometry()
        self.root.destroy()

    def on_close(self):
        """Runs on close"""
        self.descriptions_gui.on_close()
        self.save_window_geometry()
        save_and_exit_script(self.persistent_data)

    def treeview_open_file(self):
        "Treeview Handle 'Open File' option"
        print("Method: treeview_open_file - Handle 'Open File' option")
        full_path = self.treeview_get_selected_full_path()
        os.startfile(full_path)

    def treeview_open_default_file(self):
        "Treeview handle Open Default File' option"
        print("Method: treeview_open_default_file - handle 'Open Default File' option")
        full_path = self.treeview_get_selected_full_path()
        backup_path = get_backup_path(full_path)
        if os.path.isfile(backup_path):
            print(f"Opening default file: '{backup_path}'")
            os.startfile(backup_path)
        else:
            print(f"Default file unavailable: '{backup_path}'")

    def treeview_open_folder(self):
        "Treeview Handle 'Open Folder' option"
        print("Method: treeview_open_folder - Handle 'Open Folder' option")
        full_path = self.treeview_get_selected_full_path()
        directory = os.path.dirname(full_path)
        if os.path.isdir(directory):
            print(f"Opening directory: '{directory}'")
            os.startfile(directory)
        else:
            print(f"Directory unavailable: '{directory}'")

    def treeview_open_game_folder(self):
        "Treeview Handle 'Open Game Folder' option"
        print("Method: treeview_open_game_folder - Handle 'Open Game Folder' option")

        if not self.game.installed(DirectoryMode.DEVELOPER):
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

    def treeview_description(self):
        "Treeview Handle 'Description' option"
        print("Method: treeview_description - TODO: Handle 'Description' option")

        rel_path = self.treeview_get_selected_relative_path()
        self.descriptions_gui.load_file(rel_path)

    def treeview_integers(self):
        "Treeview Handle 'Integers' option"
        print("Method: treeview_integers - TODO: Handle 'Integers' option")

    def treeview_describe(self):
        "Treeview Handle 'Describe' option"
        print("Method: treeview_describe - TODO: Handle 'Describe' option")

    def treeview_recycle(self):
        "Treeview Handle 'Recycle' option"
        print("Method: treeview_recycle - TODO: Handle 'Recycle' option")

        full_path = self.treeview_get_selected_full_path()
        send2trash.send2trash(full_path)
        self.treeview_refresh(self.treeview)
