import tkinter as tk
from tkinter import simpledialog


class CustomDialog(simpledialog.Dialog):
    def __init__(self, master, options):
        self.options = options
        self.root = master  # Store the reference to the root window
        super().__init__(master)

    def body(self, master):
        tk.Label(master, text="Select an option:").pack()

    def buttonbox(self):
        box = tk.Frame(self)

        for option in self.options:
            button = tk.Button(box, text=option, command=lambda o=option: self.button_selected(o))
            button.pack(side=tk.LEFT, padx=5, pady=5)

        box.pack()

    def button_selected(self, selected_option):
        self.result = selected_option
        self.ok()


def show_custom_prompt(options):
    root = tk.Tk()  # Create the main root window
    root.title("Choice")
    root.withdraw()  # Hide the main root window

    dialog = CustomDialog(root, options)
    selected_option = dialog.result

    return selected_option


def custom_prompt_example_usage():
    options = ["VPK1", "FOLDER2", "VPK3", "FOLDER4"]
    selected_option = show_custom_prompt(options)

    if selected_option:
        print(f"Selected option: {selected_option}")

    print(selected_option)


if __name__ == "__main__":
    custom_prompt_example_usage()
