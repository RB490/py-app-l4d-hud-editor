"""Module import modules that should be available when the package is imported"""
import subprocess
import os
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
import vdf
from PIL import Image, ImageTk
from include_modules.class_vpk import VPK
from include_modules.functions import copy_directory_contents, start_hud_editing
from include_modules.constants import NEW_HUD_DIR, IMAGES_DIR


class HudSelectGui:
    """Class for the hud select gui"""

    def __init__(self, persistent_data, installer_instance):
        self.persistent_data = persistent_data
        self.installer_instance = installer_instance
        self.root = tk.Tk()
        self.root.title("Game List")
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        # self.root.geometry("865x390")
        self.root.minsize(865, 375)

        # load saved geometry
        try:
            geometry = self.persistent_data["HudSelectGuiGeometry"]
            self.root.geometry(geometry)
        except KeyError:
            self.root.geometry("1000x1000+100+100")

        # initialize variables
        self.selected_hud_name = ""
        self.selected_hud_dir = ""

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

        # Add the image viewport, display it in the picture frame and set the initial image
        self.picture_viewport = tk.Label(self.picture_frame)
        self.picture_viewport.pack()
        self.change_addon_image(os.path.join(IMAGES_DIR, "cross128.png"))

        # create a button above the picture frame
        self.edit_button = tk.Button(self.frame, text="Edit", width=35, height=1, command=self.edit_selected_hud)
        self.edit_button.pack(pady=5, padx=5)

        # Create a context menu for the treeview
        self.context_menu = tk.Menu(self.treeview, tearoff=0)
        self.context_menu.add_command(label="Edit", command=self.tree_edit_item)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="Open dir", command=self.tree_open_dir)
        self.context_menu.add_command(label="Export (as vpk)", command=self.tree_export_vpk)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="Remove (only from program)", command=self.tree_remove_item)

        # Bind the right-click event to show the context menu
        self.treeview.bind("<Button-3>", self.show_tree_context_menu)

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
        dev_menu.add_command(label="User Dir", command=self.installer_user_dir)
        dev_menu.add_command(label="Dev Dir", command=self.installer_dev_dir)
        dev_menu.add_separator()
        dev_menu.add_command(label="Enable", command=self.installer_enable)
        dev_menu.add_command(label="Disable", command=self.installer_disable)
        dev_menu.add_separator()
        dev_menu.add_command(label="Install", command=self.installer_install)
        dev_menu.add_command(label="Update", command=self.installer_update)
        dev_menu.add_command(label="Repair", command=self.installer_repair)
        dev_menu.add_separator()
        dev_menu.add_command(label="Remove", command=self.installer_remove)
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

    def installer_user_dir(self):
        """
        This method returns the user directory.
        """
        print("Opened User Dir")
        directory = self.installer_instance.get_dir("user")
        if os.path.isdir(directory):
            os.startfile(directory)
        else:
            messagebox.showerror("Error", "Directory does not exist!")

    def installer_dev_dir(self):
        """
        This method returns the dev directory.
        """
        print("Opened Dev Dir")
        directory = self.installer_instance.get_dir("dev")
        if os.path.isdir(directory):
            os.startfile(directory)
        else:
            messagebox.showerror("Error", "Directory does not exist!")

    def installer_enable(self):
        """
        This method enables dev mode.
        """
        print("Enable dev mode")
        self.installer_instance.activate_mode("dev")

    def installer_disable(self):
        """
        This method disables dev mode.
        """
        print("Disable dev mode")
        self.installer_instance.activate_mode("user")

    def installer_install(self):
        """
        This method installs dev mode.
        """
        print("Install dev mode")
        self.installer_instance.run_installer()

    def installer_update(self):
        """
        This method updates dev mode.
        """
        print("Update dev mode")
        self.installer_instance.run_installer_update()

    def installer_repair(self):
        """
        This method repairs dev mode.
        """
        print("Repair dev mode")
        self.installer_instance.run_installer_repair()

    def installer_remove(self):
        """
        This method removes dev mode.
        """
        print("Remove dev mode")
        self.installer_instance.run_installer_remove()

    def show_tree_context_menu(self, event):
        """Show the context menu for the treeview item at the position of the mouse cursor."""

        # select row under mouse
        iid = self.treeview.identify_row(event.y)
        if iid:
            # mouse pointer over item
            self.treeview.selection_set(iid)

        self.context_menu.post(event.x_root, event.y_root)

    def tree_edit_item(self):
        """Edit the selected hud."""
        self.edit_selected_hud()

    def tree_open_dir(self):
        """Open the directory of the selected hud."""
        print("Open tree directory")

        # Check if the source directory exists
        if os.path.exists(self.selected_hud_dir):
            # Open the source directory in the file explorer
            subprocess.Popen(["explorer", self.selected_hud_dir])
            print(f"Opened directory '{self.selected_hud_dir}'")
        else:
            print(f"Directory '{self.selected_hud_dir}' does not exist.")

    def tree_export_vpk(self):
        """Export the selected hud as a vpk file."""
        print("Export tree as vpk")

        export_path = filedialog.asksaveasfilename(
            initialdir="/", title="Export HUD as VPK", filetypes=(("package files", "*.vpk"), ("all files", "*.*"))
        )

        if export_path:
            print(export_path)
            vpk_class = VPK()
            vpk_class.create(self.selected_hud_dir, os.path.dirname(export_path), os.path.basename(export_path))
            # vpk_class.create(self, input_dir, output_dir, output_file_name):

    def tree_remove_item(self):
        """Remove the selected hud."""
        print("Remove tree item")

        self.persistent_data["stored_huds"].remove(self.selected_hud_dir.replace("\\", "/"))  # convert path to json
        self.selected_hud_dir = ""
        self.selected_hud_name = ""

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
            # retrieve hud name (from addoninfo.txt if available)
            hud_name = os.path.basename(os.path.dirname(stored_hud_dir))
            addoninfo_path = os.path.join(stored_hud_dir, "addoninfo.txt")
            if os.path.exists(addoninfo_path):
                addon_info = vdf.load(open(addoninfo_path, encoding="utf-8"))
                hud_name = addon_info["AddonInfo"]["addontitle"]

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
            self.selected_hud_name = self.treeview.item(item)["values"][0]
            self.selected_hud_dir = os.path.normpath(self.treeview.item(item)["values"][1])
            image = os.path.join(self.selected_hud_dir, "addonimage.jpg")
            print(self.selected_hud_dir)
            print(self.selected_hud_name)

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
        start_hud_editing(self.selected_hud_dir)

    def on_close(self):
        """Exit script"""
        self.save_window_geometry()
        self.root.destroy()
        input("Press enter to quit script")
        quit()


def debug_hud_select_gui(persistent_data, installer_instance):
    """Debug the gui"""
    app = HudSelectGui(persistent_data, installer_instance)
    app.root.mainloop()
