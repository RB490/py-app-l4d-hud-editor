"""Module for the hud select gui class"""
# pylint: disable=broad-exception-caught
import os
import subprocess
import tkinter as tk
from tkinter import filedialog, ttk

from PIL import Image, ImageTk

from game.constants import DirectoryMode
from game.game import Game
from utils.constants import APP_ICON
from utils.functions import (
    prompt_add_existing_hud,
    prompt_create_new_hud,
    retrieve_hud_name_for_dir,
)
from utils.shared_utils import Singleton, show_message
from utils.vpk import VPKClass


class GuiHudStart(metaclass=Singleton):
    """Class for the hud select gui"""

    def __init__(self, persistent_data):
        # pylint: disable=import-outside-toplevel # importing outside top level to avoid circular imports
        self.persistent_data = persistent_data
        self.game = Game(persistent_data)

        from hud.hud import Hud  # avoid recursive import

        self.is_hidden = None
        self.hud = Hud(persistent_data)
        self.root = tk.Tk()
        self.hide()
        self.root.title("Select")
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.root.iconbitmap(APP_ICON)
        # self.root.geometry("865x390")
        self.root.minsize(865, 375)

        # load saved geometry
        try:
            geometry = self.persistent_data["HudSelectGuiGeometry"]
            self.root.geometry(geometry)
        except KeyError:
            self.root.geometry("1000x1000+100+100")

        # initialize variables
        self.picture_canvas_photo = None
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
        self.add_button = tk.Button(self.frame, text="Add", width=35, height=1, command=self.prompt_add_hud_btn)
        self.add_button.pack(pady=5, padx=5)

        # create a button above the picture frame
        self.new_button = tk.Button(self.frame, text="New", width=35, height=1, command=self.prompt_new_hud_btn)
        self.new_button.pack(pady=5, padx=5)

        # create a picture frame on the right side
        self.picture_frame = tk.Frame(self.frame, bg="black")
        self.picture_frame.pack(padx=5, pady=5)

        # Add the image viewport, display it in the picture frame and set the initial image
        self.picture_canvas = tk.Canvas(self.picture_frame, relief="ridge", bd=4)
        self.picture_canvas.pack()
        self.picture_canvas.config(width=250, height=200)
        # setting the image isn't possible before calling mainloop()
        # self.change_addon_image(os.path.join(IMAGES_DIR, "cross128.png"))

        # create a button above the picture frame
        self.edit_button = tk.Button(self.frame, text="Edit", width=35, height=1, command=self.edit_selected_hud)
        self.edit_button.pack(pady=5, padx=5)

        # Create a context menu for the treeview
        self.context_menu = tk.Menu(self.treeview, tearoff=0)
        self.context_menu.add_command(label="Edit", command=self.tree_edit_item)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="Open dir", command=self.tree_open_dir)
        self.context_menu.add_command(label="Export VPK", command=self.tree_export_vpk)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="Remove", command=self.tree_remove_item)

        # Bind the right-click event to show the context menu
        self.treeview.bind("<Button-3>", self.show_tree_context_menu)

        # create a menu bar
        menu_bar = tk.Menu(self.root)

        # File menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", accelerator="Ctrl+N", command=self.prompt_new_hud_btn)
        file_menu.add_command(label="Add", accelerator="Ctrl+O", command=self.prompt_add_hud_btn)
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
        menu_bar.add_cascade(label="Develop", menu=dev_menu)

        # Configure the root window with the menubar
        self.root.config(menu=menu_bar)
        self.update_treeview()

        # self.change_addon_image(os.path.join(IMAGES_DIR, "cross128.png"))

    def run(self):
        "Show & start main loop"
        print("start: run")
        self.show()
        self.root.mainloop()  # neccessary for the gui to fully work. for example changing the img in a widget

    def installer_user_dir(self):
        """This method returns the user directory."""
        print("Opening user directory")
        try:
            directory = self.game.dir.get(DirectoryMode.USER)
            os.startfile(directory)
        except Exception as err_info:
            print(f"Could not open user directory: {err_info}")
            show_message("Directory does not exist!", "error")

    def installer_dev_dir(self):
        """
        This method returns the developer directory.
        """
        print("Opening developer directory")
        try:
            directory = self.game.dir.get(DirectoryMode.DEVELOPER)
            os.startfile(directory)
        except Exception as err_info:
            print(f"Could not open developer directory: {err_info}")
            show_message("Directory does not exist!", "error")

    def installer_enable(self):
        """
        This method enables developer mode.
        """
        print("Enabling developer mode")
        self.game.dir.set(DirectoryMode.DEVELOPER)

    def installer_disable(self):
        """
        This method disables developer mode.
        """
        print("Disabling developer mode")
        self.game.dir.set(DirectoryMode.USER)

    def installer_install(self):
        """
        This method installs developer mode.
        """
        print("Install developer mode")
        self.game.installer.install()

    def installer_update(self):
        """
        This method updates developer mode.
        """
        print("Updating developer mode")
        self.game.installer.update()

    def installer_repair(self):
        """
        This method repairs developer mode.
        """
        print("Repairing developer mode")
        self.game.installer.repair()

    def installer_remove(self):
        """
        This method removes developer mode.
        """
        print("Removing developer mode")
        self.game.installer.uninstall()

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
        print("Opening selected tree item directory")

        # Check if the source directory exists
        if os.path.exists(self.selected_hud_dir):
            # Open the source directory in the file explorer
            subprocess.Popen(["explorer", self.selected_hud_dir])
            print(f"Opened directory '{self.selected_hud_dir}'")
        else:
            print(f"Directory '{self.selected_hud_dir}' does not exist.")

    def tree_export_vpk(self):
        """Export the selected hud as a vpk file."""
        print("Exporting selected tree item as vpk")

        export_path = filedialog.asksaveasfilename(
            initialdir="/", title="Export HUD as VPK", filetypes=(("package files", "*.vpk"), ("all files", "*.*"))
        )

        if export_path:
            print(export_path)
            vpk_class = VPKClass()
            vpk_class.create(self.selected_hud_dir, os.path.dirname(export_path), os.path.basename(export_path))
            # vpk_class.create(self, input_dir, output_dir, output_file_name):

    def tree_remove_item(self):
        """Remove the selected hud."""
        print("Remove tree item")

        self.persistent_data["stored_huds"].remove(self.selected_hud_dir.replace("\\", "/"))  # convert path to json
        self.selected_hud_dir = ""
        self.selected_hud_name = ""

        self.update_treeview()

    def save_window_geometry(self):
        """Save size & position if GUI is loaded and visible"""
        if self.root and self.root.winfo_viewable():
            # Get the current position and size of the window
            geometry = self.root.geometry()
            print(f"geometry: {geometry}")
            self.persistent_data["HudSelectGuiGeometry"] = geometry
        else:
            print("GUI is not loaded or visible. Skipping window geometry save.")

    def update_treeview(self):
        """Clear treeview & load up-to-date content"""

        # Clear the existing items in the Treeview
        self.treeview.delete(*self.treeview.get_children())

        # Insert the new items from the list into the Treeview
        for stored_hud_dir in self.persistent_data["stored_huds"]:
            # retrieve hud name (from addoninfo.txt if available)
            hud_name = retrieve_hud_name_for_dir(stored_hud_dir)

            self.treeview.insert("", "end", values=(hud_name, os.path.normpath(stored_hud_dir)))

    def change_addon_image(self, path):
        """Load specified image into the image control"""
        # if not os.path.isfile(path):
        #     print(f"change_addon_image: File does not exist: {path}")
        #     return

        # # Load the second image
        # raw_img_handle = Image.open(path)
        # img_handle = ImageTk.PhotoImage(raw_img_handle)
        # # Keep a reference to the new image to prevent it from being garbage collected
        # self.picture_canvas.image = img_handle

        # # Change the image displayed in the label
        # print(path)
        # # self.picture_viewport.configure(image=img_handle)
        # # self.picture_viewport.configure(image=self.picture_viewport.image)
        # self.picture_canvas.create_image(0, 0, anchor="nw", image=self.picture_canvas.image)

        image = Image.open(path)  # Replace with your image file path
        self.picture_canvas_photo = ImageTk.PhotoImage(image)

        # Calculate the center coordinates to place the image
        center_x = self.picture_canvas.winfo_reqwidth() // 2
        center_y = self.picture_canvas.winfo_reqheight() // 2

        # Configure the canvas to display the image
        self.picture_canvas.create_image(center_x, center_y, anchor="center", image=self.picture_canvas_photo)

        # Adjust the canvas size to match the image size
        # self.picture_canvas.config(width=self.photo.width(), height=self.photo.height())

        # Adjust the canvas's scrollable region to fit the image
        self.picture_canvas.config(scrollregion=self.picture_canvas.bbox("all"))

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

    def prompt_add_hud_btn(self):
        """Prompt user for hud folder to add"""
        if prompt_add_existing_hud(self.persistent_data):
            self.update_treeview()

    def prompt_new_hud_btn(self):
        """Prompt user for hud folder to create a new hud in"""
        if prompt_create_new_hud(self.persistent_data):
            self.update_treeview()

    def edit_selected_hud(self):
        """Start hud editing for selected hud"""

        # hide gui
        self.hide()
        self.save_window_geometry()
        # self.destroy_gui()

        # edit hud
        self.hud.start_editing(self.selected_hud_dir)

    def hide(self):
        """Hide gui"""
        # Hide the root window instead of closing it
        self.root.withdraw()
        self.is_hidden = True

    def show(self):
        """Show gui"""
        # Show the window again
        self.is_hidden = False
        self.root.deiconify()

    def destroy_gui(self):
        "Close & start main loop"
        self.save_window_geometry()
        self.root.destroy()

    def on_close(self):
        """Exit script"""
        self.save_window_geometry()
        # self.root.destroy()
        self.hide()


def show_start_gui(persistent_data):
    "Show start gui"
    start_instance = GuiHudStart(persistent_data)
    start_instance.run()
