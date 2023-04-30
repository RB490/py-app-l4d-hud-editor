"""Module for the hud file descriptions gui"""
import os
import tkinter as tk

from modules.utils.constants import IMAGES_DIR


class GuiHudDescriptions:
    """Class for the hud file descriptions gui"""

    def __init__(self, hud_instance, relative_path):
        self.root = tk.Tk()
        self.root.title("File")
        self.hud = hud_instance
        self.relative_path = relative_path

        # self.root.minsize(450, 400)

        # Create image buttons
        self.add_image = tk.PhotoImage(file=os.path.join(IMAGES_DIR, "plus.png"))
        self.delete_image = tk.PhotoImage(file=os.path.join(IMAGES_DIR, "delete.png"))
        self.save_image = tk.PhotoImage(file=os.path.join(IMAGES_DIR, "saveas.png"))

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
        self.ctrl_menu_variable.set("Option 1")  # default value
        controls_list = ["Option 1", "Option 2", "Option 3"]
        self.ctrl_menu = tk.OptionMenu(
            ctrl_button_frame, self.ctrl_menu_variable, *controls_list, command=self.selected_ctrl
        )
        self.ctrl_menu.config(width=25)
        self.ctrl_menu.pack(side="left", padx=pad_x, pady=pad_y, fill="x", expand=True)

        add_ctrl_button = tk.Button(ctrl_button_frame, text="", justify="center", command=self.add_control)
        add_ctrl_button.config(width=25, height=23)
        add_ctrl_button.config(image=self.add_image, compound="center")
        add_ctrl_button.pack(side="left", padx=pad_x, pady=pad_y)

        remove_ctrl_button = tk.Button(ctrl_button_frame, text="", justify="center", command=self.remove_control)
        remove_ctrl_button.config(width=25, height=23)
        remove_ctrl_button.config(image=self.delete_image, compound="center")
        remove_ctrl_button.pack(side="left", padx=pad_x, pady=pad_y)

        ctrl_desc_frame = tk.Frame(ctrl_label_frame)
        ctrl_desc_frame.pack(anchor="nw", side="top", fill="both", expand=True, padx=pad_x, pady=(pad_y, 0))

        ctrl_desc_scrollbar = tk.Scrollbar(ctrl_desc_frame)
        ctrl_desc_scrollbar.pack(side="right", fill="y")

        self.ctrl_desc_text = tk.Text(ctrl_desc_frame, height=4, width=ctrl_w, yscrollcommand=ctrl_desc_scrollbar.set)
        self.ctrl_desc_text.pack(side="bottom", fill="both", expand=True, padx=pad_x, pady=(pad_y, 0))

        ctrl_desc_scrollbar.config(command=self.ctrl_desc_text.yview)

        save_button_frame = tk.Frame(self.root)
        save_button_frame.pack(side="bottom", expand=False, fill="x", padx=pad_x, pady=(0, pad_y))

        save_button = tk.Button(
            save_button_frame, text="", justify="center", height=25, width=ctrl_w, command=self.save_gui
        )
        save_button.config(image=self.save_image, compound="center")
        save_button.pack(side="bottom", expand=True, fill="x", padx=pad_x, pady=(0, pad_y))

        self.load_description(relative_path)

    def load_control(self, input_ctrl):
        # set options menu
        self.ctrl_menu_variable.set(input_ctrl)

        # set control description
        self.ctrl_desc_text.delete("1.0", tk.END)  # delete all existing text
        self.ctrl_desc_text.insert(tk.END, self.hud.get_file_control_description(self.relative_path, input_ctrl))

    def load_description(self, relative_path):
        """Load description for hud file into the gui"""

        # save relative path
        self.relative_path = relative_path

        # set gui title
        self.root.title(relative_path)

        # set file description
        self.file_desc_text.delete("1.0", tk.END)  # delete all existing text
        self.file_desc_text.insert(tk.END, self.hud.get_file_description(relative_path))

        # update the controls list and OptionMenu with new values
        controls_list = self.hud.get_file_controls(relative_path)
        menu = self.ctrl_menu["menu"]  # get the OptionMenu menu object
        menu.delete(0, "end")  # delete all existing options from the menu
        for item in controls_list:
            # iterate over the new controls list and add commands to the menu for each item
            menu.add_command(label=item, command=lambda selected_item=item: self.selected_ctrl(selected_item))
        self.load_control(controls_list[0])

    def selected_ctrl(self, input_ctrl):
        """Handle control menu selection"""
        print("You selected:", input_ctrl)
        self.load_control(input_ctrl)

    def add_control(self):
        """Add new control"""
        print("add_control")

    def remove_control(self):
        """Remove control"""
        print("remove_control")

    def save_gui(self):
        """Submit gui"""
        print("save_gui")
