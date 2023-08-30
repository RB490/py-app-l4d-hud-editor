"""A custom dialog window for selecting options."""
import tkinter as tk
from tkinter import simpledialog

from shared_utils.shared_utils import get_invisible_tkinter_root


class CustomDialog(simpledialog.Dialog):
    """A custom dialog window for selecting options."""

    def __init__(self, master, options):
        """Initialize the custom dialog."""
        self.options = options
        self.root = master
        super().__init__(master)

    def body(self, master):
        """Create the dialog's GUI body."""
        tk.Label(master, text="Select an option:").pack()

    def buttonbox(self):
        """Create the button box with option buttons."""
        box = tk.Frame(self)
        for option in self.options:
            button = tk.Button(box, text=option, command=lambda o=option: self.button_selected(o))
            button.pack(side=tk.LEFT, padx=5, pady=5)
        box.pack()

    def button_selected(self, selected_option):
        """Set the result and close the dialog when a button is selected."""
        self.result = selected_option
        self.ok()


def show_custom_prompt(options):
    """Show the custom dialog with given options and return the selected option."""
    root = get_invisible_tkinter_root()
    root.title("Choice")
    dialog = CustomDialog(root, options)
    selected_option = dialog.result
    return selected_option


def custom_prompt_example_usage():
    """Example usage of the custom prompt."""
    options = ["VPK1", "FOLDER2", "VPK3", "FOLDER4"]
    selected_option = show_custom_prompt(options)
    if selected_option:
        print(f"Selected option: {selected_option}")
    print(selected_option)


if __name__ == "__main__":
    custom_prompt_example_usage()
