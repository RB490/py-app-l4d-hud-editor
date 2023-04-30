import tkinter as tk
import tkinter.font as tkFont


class App:
    def __init__(self, root):
        root.title("File")

        # root.minsize(450, 600)

        # define constants for padding and sizing
        PADX = 10
        PADY = 10
        CTRL_WIDTH = 40
        EXPAND_TRUE = True
        FILL_BOTH = "both"
        SIDE_TOP = "top"
        SIDE_BOTTOM = "bottom"
        ANCHOR_NW = "nw"

        desc_frame = tk.Frame(root)
        desc_frame.pack(fill=FILL_BOTH, expand=EXPAND_TRUE, padx=PADX, pady=(0, 0))

        file_desc_label = tk.Label(desc_frame, text="File description")
        file_desc_label.pack(side=SIDE_TOP, anchor="w", padx=PADX, pady=PADY)

        scrollbar = tk.Scrollbar(desc_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        file_desc_entry = tk.Text(desc_frame, height=6, width=CTRL_WIDTH, yscrollcommand=scrollbar.set)
        file_desc_entry.pack(side=SIDE_TOP, fill=FILL_BOTH, expand=EXPAND_TRUE, padx=PADX, pady=0)

        scrollbar.config(command=file_desc_entry.yview)

        label_frame = tk.LabelFrame(root, text="Control descriptions")
        label_frame.pack(fill=FILL_BOTH, expand=EXPAND_TRUE, padx=PADX * 2, pady=PADY * 2)

        button_frame = tk.Frame(label_frame)
        button_frame.pack(side="bottom", fill="x", expand=False, padx=PADX, pady=(0, PADY))

        variable = tk.StringVar(root)
        variable.set("Option 1")  # default value

        options = ["Option 1", "Option 2", "Option 3"]
        option_menu = tk.OptionMenu(button_frame, variable, *options)
        option_menu.config(width=20)
        option_menu.pack(side="left", padx=PADX, pady=PADY)

        add_button = tk.Button(button_frame, text="Add", justify="center", command=self.add_command)
        add_button.config(width=10)
        add_button.pack(side="left", padx=PADX, pady=PADY)

        remove_button = tk.Button(button_frame, text="Remove", justify="center", command=self.remove_command)
        remove_button.config(width=10)
        remove_button.pack(side="left", padx=PADX, pady=PADY)

        controls_frame = tk.Frame(label_frame)
        controls_frame.pack(
            anchor=ANCHOR_NW, side=SIDE_TOP, fill=FILL_BOTH, expand=EXPAND_TRUE, padx=PADX, pady=(PADY, 0)
        )

        text_scrollbar = tk.Scrollbar(controls_frame)
        text_scrollbar.pack(side="right", fill="y")

        text_control = tk.Text(controls_frame, height=4, width=CTRL_WIDTH, yscrollcommand=text_scrollbar.set)
        text_control.pack(side="bottom", fill="both", expand=True, padx=PADX, pady=(PADY, 0))

        text_scrollbar.config(command=text_control.yview)

        save_frame = tk.Frame(root)
        save_frame.pack(side=SIDE_BOTTOM, expand=False, fill="x", padx=PADX, pady=(0, PADY))

        save_button = tk.Button(save_frame, text="Save", justify="center", width=CTRL_WIDTH, command=self.save_command)
        save_button.pack(side=SIDE_BOTTOM, expand=True, fill="x", padx=PADX, pady=(0, PADY))

    def add_command(self):
        print("command")

    def remove_command(self):
        print("command")

    def save_command(self):
        print("command")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
