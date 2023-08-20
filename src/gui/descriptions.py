"""Module for the hud file descriptions gui"""
import os
import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import simpledialog

from utils.constants import APP_ICON, IMAGES_DIR


class GuiHudDescriptions:
    """Class for the hud file descriptions gui"""

    def __init__(self, persistent_data, relative_path, parent_gui):
        self.is_hidden = None
        self.root = tk.Toplevel()
        self.hide()
        self.root.title("File")
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.root.iconbitmap(APP_ICON)

        from hud.hud import Hud

        self.hud = Hud(persistent_data)
        self.relative_path = relative_path
        self.parent = parent_gui

        # self.root.minsize(450, 400)

        # Create image buttons
        # self.add_image = tk.PhotoImage(file=os.path.join(IMAGES_DIR, "plus.png"))
        # self.delete_image = tk.PhotoImage(file=os.path.join(IMAGES_DIR, "delete.png"))
        # self.save_image = tk.PhotoImage(file=os.path.join(IMAGES_DIR, "saveas.png"))
        self.add_image = tk.PhotoImage(file=os.path.join(IMAGES_DIR, "fullscreen.png"))
        # self.delete_image = tk.PhotoImage(file=os.path.join(IMAGES_DIR, "delete.png"))
        # self.save_image = tk.PhotoImage(file=os.path.join(IMAGES_DIR, "saveas.png"))

        # define constants for padding and sizing
        pad_x = 10
        pad_y = 10
        ctrl_w = 40

        file_desc_frame = tk.Frame(self.root)
        file_desc_frame.pack(fill="both", expand=True, padx=pad_x, pady=(0, 0))

        file_desc_label = tk.Label(file_desc_frame, text="File description")
        file_desc_label.pack(side="top", anchor="w", padx=pad_x, pady=pad_y)

        file_desc_scrollbar = tk.Scrollbar(file_desc_frame)
        file_desc_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.file_desc_text = tk.Text(file_desc_frame, height=6, width=ctrl_w, yscrollcommand=file_desc_scrollbar.set)
        self.file_desc_text.pack(side="top", fill="both", expand=True, padx=pad_x, pady=0)

        file_desc_scrollbar.config(command=self.file_desc_text.yview)

        ctrl_label_frame = tk.LabelFrame(self.root, text="Control descriptions")
        ctrl_label_frame.pack(fill="both", expand=True, padx=pad_x * 2, pady=pad_y * 2)

        ctrl_button_frame = tk.Frame(ctrl_label_frame)
        ctrl_button_frame.pack(side="bottom", fill="x", expand=False, padx=pad_x, pady=(0, pad_y))

        self.ctrl_menu_variable = tk.StringVar(self.root)
        self.ctrl_menu_variable.set("None")  # default value
        controls_list = ["None"]
        self.ctrl_menu = tk.OptionMenu(
            ctrl_button_frame, self.ctrl_menu_variable, *controls_list, command=self.selected_ctrl
        )
        self.ctrl_menu.config(width=25)
        self.ctrl_menu.pack(side="left", padx=pad_x, pady=pad_y, fill="x", expand=True)

        add_ctrl_button = tk.Button(ctrl_button_frame, text="", justify="center", command=self.add_control)
        add_ctrl_button.config(width=25, height=23)
        add_ctrl_button.config(image=self.add_image, compound="center")
        add_ctrl_button.pack(side="left", padx=pad_x, pady=pad_y)

        # remove_ctrl_button = tk.Button(ctrl_button_frame, text="", justify="center", command=self.remove_control)
        # remove_ctrl_button.config(width=25, height=23)
        # remove_ctrl_button.config(image=self.delete_image, compound="center")
        # remove_ctrl_button.pack(side="left", padx=pad_x, pady=pad_y)

        ctrl_desc_frame = tk.Frame(ctrl_label_frame)
        ctrl_desc_frame.pack(anchor="nw", side="top", fill="both", expand=True, padx=pad_x, pady=(pad_y, 0))

        ctrl_desc_scrollbar = tk.Scrollbar(ctrl_desc_frame)
        ctrl_desc_scrollbar.pack(side="right", fill="y")

        self.ctrl_desc_text = tk.Text(ctrl_desc_frame, height=4, width=ctrl_w, yscrollcommand=ctrl_desc_scrollbar.set)
        self.ctrl_desc_text.pack(side="bottom", fill="both", expand=True, padx=pad_x, pady=(pad_y, 0))

        ctrl_desc_scrollbar.config(command=self.ctrl_desc_text.yview)

        save_button_frame = tk.Frame(self.root)
        save_button_frame.pack(side="bottom", expand=False, fill="x", padx=pad_x, pady=(0, pad_y))

        # save_button = tk.Button(
        #     save_button_frame, text="", justify="center", height=25, width=ctrl_w, command=self.save_gui
        # )
        # save_button.config(image=self.save_image, compound="center")
        # save_button.pack(side="bottom", expand=True, fill="x", padx=pad_x, pady=(0, pad_y))

        self.load_file(relative_path)

    def run(self):
        "Show & start main loop"

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

    def load_file(self, relative_path):
        """Load description for hud file into the gui"""

        # save relative path
        self.relative_path = relative_path

        # set gui title
        self.root.title(relative_path)

        # set file description
        self.file_desc_text.delete("1.0", tk.END)  # delete all existing text
        self.file_desc_text.insert(tk.END, self.hud.desc.get_description(relative_path))

        # load controls
        self.load_controls()

    def load_controls(self):
        """Load controls into option menu & load the first one"""

        # update the controls list and OptionMenu with new values
        controls_list = self.hud.desc.get_controls(self.relative_path)

        # controls available at all?
        if not controls_list:
            return

        menu = self.ctrl_menu["menu"]  # get the OptionMenu menu object
        menu.delete(0, "end")  # delete all existing options from the menu
        for item in controls_list:
            # iterate over the new controls list and add commands to the menu for each item
            menu.add_command(label=item, command=lambda selected_item=item: self.selected_ctrl(selected_item))
        self.load_control(controls_list[0])

    def load_control(self, input_ctrl):
        """Load hud file control into the gui"""

        # set options menu
        self.ctrl_menu_variable.set(input_ctrl)

        # set control description
        self.ctrl_desc_text.delete("1.0", tk.END)  # delete all existing text
        self.ctrl_desc_text.insert(tk.END, self.hud.desc.get_control_description(self.relative_path, input_ctrl))

    def save_control_desc(self):
        """Save control description"""
        selected_control = self.ctrl_menu_variable.get()
        control_desc = self.ctrl_desc_text.get("1.0", "end-1c")
        self.hud.desc.save_control_desc(self.relative_path, selected_control, control_desc)
        print(control_desc)

    def selected_ctrl(self, input_ctrl):
        """Handle control menu selection"""

        # save currently loaded control
        self.save_control_desc()

        # load selected control
        print("You selected:", input_ctrl)
        self.load_control(input_ctrl)

    def add_control(self):
        """Add new control"""
        # Show a dialog box to get the name of the new control
        new_control = simpledialog.askstring("New Control", "Enter the name of the new control:")

        # If user entered a name and clicked OK, add the control
        if new_control:
            # save currently loaded control
            self.save_control_desc()

            # Add control
            self.hud.desc.add_control(self.relative_path, new_control)
            self.load_controls()
            self.load_control(new_control)
            print(f"Added {new_control}")

    def remove_control(self):
        """Remove control"""
        selected_control = self.ctrl_menu_variable.get()

        # Show a message box to confirm removal
        if messagebox.askyesno("Remove Control", f"Are you sure you want to remove {selected_control}?"):
            # save currently loaded control
            self.save_control_desc()

            # User clicked Yes, so remove the control
            print(f"Removed {selected_control}")
            self.hud.desc.remove_control(self.relative_path, selected_control)
            self.load_controls()

    def save_gui(self):
        """Submit gui"""

        # save currently loaded control
        self.save_control_desc()

        # save changes to disk
        self.hud.desc.save_to_disk()

        # close gui
        self.root.destroy()

        # call parent
        self.parent.treeview_refresh()

    def on_close(self):
        """On gui close"""

        # undo changes by reloading from disk
        self.hud.desc.read_from_disk()

        # close gui
        self.root.destroy()
