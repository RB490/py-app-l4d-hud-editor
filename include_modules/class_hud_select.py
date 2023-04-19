"""Module import modules that should be available when the package is imported"""
import os
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from include_modules.functions import start_hud_editing
from include_modules.functions import copy_directory_contents
from include_modules.constants import NEW_HUD_DIR
from include_modules.constants import IMAGES_DIR


class HudSelectGui:
    """Class for the hud select gui"""

    def __init__(self, persistent_data):
        self.persistent_data = persistent_data
        self.root = tk.Tk()
        self.root.title("Game List")
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        # self.root.geometry("865x390")
        self.root.minsize(865, 375)

        # # load saved geometry
        try:
            geometry = self.persistent_data["HudSelectGuiGeometry"]
            self.root.geometry(geometry)
        except KeyError:
            self.root.geometry("1000x1000+100+100")

        # create a frame for all widgets
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill="both", anchor="nw", expand=True)

        # create a treeview with three columns
        self.treeview = ttk.Treeview(self.frame, columns=("name", "directory"), height=10)
        self.treeview.heading("#0", text="")
        self.treeview.heading("name", text="Name")
        self.treeview.heading("directory", text="Directory")
        self.treeview.column("#0", width=10, stretch=False)
        self.treeview.column("name", width=125, stretch=False)
        self.treeview.column("directory", width=400)
        self.treeview.pack(side="left", expand=True, fill="both", padx=5, pady=5)

        # Bind the function to the selection event
        self.treeview.bind("<<TreeviewSelect>>", self.tree_get_selected_item)

        # create a button above the picture frame
        self.add_button = tk.Button(self.frame, text="Add", width=35, height=1, command=self.prompt_add_gui)
        self.add_button.pack(pady=5, padx=5)

        # create a button above the picture frame
        self.new_button = tk.Button(self.frame, text="New", width=35, height=1, command=self.prompt_new_gui)
        self.new_button.pack(pady=5, padx=5)

        # create a picture frame on the right side
        self.picture_frame = tk.Frame(self.frame, width=250, height=250, bg="white")
        self.picture_frame.pack(padx=5, pady=5)

        # Load the image
        image = Image.open(os.path.join(IMAGES_DIR, "cross128.png"))
        photo = ImageTk.PhotoImage(image)

        # Add the image to a label and display it in the frame
        self.picture_viewport = tk.Label(self.picture_frame, image=photo)
        self.picture_viewport.image = photo  # Keep a reference to the image to prevent it from being garbage collected
        self.picture_viewport.pack()

        # create a button above the picture frame
        self.edit_button = tk.Button(self.frame, text="Edit", width=35, height=1, command=self.edit_selected_hud)
        self.edit_button.pack(pady=5, padx=5)

        # create a menu bar
        menu_bar = tk.Menu(self.root)

        # File menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", accelerator="Ctrl+N", command=self.prompt_new_gui)
        file_menu.add_command(label="Add", accelerator="Ctrl+O", command=self.prompt_add_gui)
        file_menu.add_separator()
        file_menu.add_command(label="Edit", accelerator="Enter", command=self.edit_selected_hud)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", accelerator="Ctrl+Q", command=self.on_close)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Edit menu
        dev_menu = tk.Menu(menu_bar, tearoff=0)
        dev_menu.add_command(label="User Dir")
        dev_menu.add_command(label="Dev Dir")
        dev_menu.add_separator()
        dev_menu.add_command(label="Enable")
        dev_menu.add_command(label="Disable")
        dev_menu.add_separator()
        dev_menu.add_command(label="Install")
        dev_menu.add_command(label="Update")
        dev_menu.add_command(label="Repair")
        dev_menu.add_command(label="Verify")
        dev_menu.add_separator()
        dev_menu.add_command(label="Remove")
        menu_bar.add_cascade(label="Dev", menu=dev_menu)

        # Help menu with a submenu
        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About")
        help_sub_menu = tk.Menu(help_menu, tearoff=0)
        help_sub_menu.add_command(label="Documentation")
        help_sub_menu.add_command(label="Examples")
        help_menu.add_cascade(label="Help", menu=help_sub_menu)
        menu_bar.add_cascade(label="Help", menu=help_menu)

        # Configure the root window with the menubar
        self.root.config(menu=menu_bar)
        self.update_treeview()

    def start_editing_hud(self):
        """Start editing hud"""
        self.save_window_geometry()
        self.root.destroy()

    def save_window_geometry(self):
        """Save size & position"""
        # Get the current position and size of the window
        geometry = self.root.geometry()
        print(f"geometry: {geometry}")
        self.persistent_data["HudSelectGuiGeometry"] = geometry

    def update_treeview(self):
        """Clear treeview & load up-to-date content"""

        # Clear the existing items in the Treeview
        self.treeview.delete(*self.treeview.get_children())

        # Insert the new items from the list into the Treeview
        for stored_hud_dir in self.persistent_data["stored_huds"]:
            hud_name = os.path.basename(os.path.dirname(stored_hud_dir))
            self.treeview.insert("", "end", values=(hud_name, stored_hud_dir))

    def change_addon_image(self, path):
        """Load specified image into the image control"""
        # Load the second image
        image2 = Image.open(path)
        photo2 = ImageTk.PhotoImage(image2)

        # Change the image displayed in the label
        print(path)
        self.picture_viewport.configure(image=photo2)
        self.picture_viewport.image = (
            photo2  # Keep a reference to the new image to prevent it from being garbage collected
        )

    # pylint: disable=unused-argument
    def tree_get_selected_item(self, event):
        """Get select item from treeview"""
        selected_item = self.treeview.selection()
        for item in selected_item:
            item_values = self.treeview.item(item)["values"]
            print(item_values)
            name = self.treeview.item(item)["values"][0]
            dir = self.treeview.item(item)["values"][1]
            image = os.path.normpath(os.path.join(dir, "addonimage.jpg"))
            print(dir)
            print(name)

            self.change_addon_image(image)

    def prompt_for_folder(self, title):
        """Prompt user for a folder"""
        root = tk.Tk()
        root.withdraw()
        return filedialog.askdirectory(title=title)

    def prompt_add_gui(self):
        """Prompt user for hud folder to add"""
        folder_path = self.prompt_for_folder("Add HUD: Select folder")
        if folder_path:
            self.persistent_data["stored_huds"].append(folder_path)
            self.update_treeview()
            print(f'stored_huds: {self.persistent_data["stored_huds"]}')

    def prompt_new_gui(self):
        """Prompt user for hud folder to create a new hud in"""
        folder_path = self.prompt_for_folder("New HUD: Select folder")
        if folder_path:
            self.persistent_data["stored_huds"].append(folder_path)
            copy_directory_contents(NEW_HUD_DIR, folder_path)
            self.update_treeview()
            print(f'stored_huds: {self.persistent_data["stored_huds"]}')

    def edit_selected_hud(self):
        """Start hud editing for selected hud"""
        start_hud_editing()

    def on_close(self):
        """Exit script"""
        self.save_window_geometry()
        self.root.destroy()
        input("Press enter to quit script")
        quit()


def debug_hud_select_gui(persistent_data):
    """Debug the gui"""
    app = HudSelectGui(persistent_data)
    app.root.mainloop()
