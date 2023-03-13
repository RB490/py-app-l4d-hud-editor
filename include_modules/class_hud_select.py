import tkinter as tk
from tkinter import ttk


class Application:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Game List")
        self.root.geometry("800x370")

        # create a frame for all widgets
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill="both", expand=True)

        # create a treeview with three columns
        self.treeview = ttk.Treeview(self.frame, columns=("name", "directory", "game_version"), height=10)
        self.treeview.heading("#0", text="Index")
        self.treeview.heading("name", text="Name")
        self.treeview.heading("directory", text="Directory")
        self.treeview.heading("game_version", text="Game Version")
        self.treeview.column("#0", width=50)
        self.treeview.column("name", width=100)
        self.treeview.column("directory", width=200)
        self.treeview.column("game_version", width=200)
        self.treeview.pack(side="left", fill="y", padx=5, pady=5)

        # Bind the function to the selection event
        self.treeview.bind("<<TreeviewSelect>>", self.tree_get_selected_item)

        # insert sample data into the treeview
        self.treeview.insert("", "end", text="1", values=("Hud 1", "Directory 1", "Left 4 Dead"))
        self.treeview.insert("", "end", text="2", values=("Hud 2", "Directory 2", "Left 4 Dead 2"))
        self.treeview.insert("", "end", text="3", values=("Hud 3", "Directory 3", "Left 4 Dead"))

        # create a button above the picture frame
        self.add_button = tk.Button(self.frame, text="Add", width=45, height=1, command=self.prompt_add_gui)
        self.add_button.pack(pady=5, padx=5)

        # create a button above the picture frame
        self.new_button = tk.Button(self.frame, text="New", width=45, height=1, command=self.prompt_add_gui)
        self.new_button.pack(pady=5, padx=5)

        # create a picture frame on the right side
        self.picture_frame = tk.Frame(self.frame, width=250, height=250, bg="white")
        self.picture_frame.pack(padx=5, pady=5)

        # create a button above the picture frame
        self.edit_button = tk.Button(self.frame, text="Edit", width=45, height=1, command=self.prompt_add_gui)
        self.edit_button.pack(pady=5, padx=5)

        # create a menu bar
        menu_bar = tk.Menu(self.root)

        # File menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", accelerator="Ctrl+N")
        file_menu.add_command(label="Open...", accelerator="Ctrl+O")
        file_menu.add_separator()
        file_menu.add_command(label="Edit", accelerator="Enter")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", accelerator="Ctrl+Q", command=self.root.quit)
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

    def tree_get_selected_item(self, event):
        selected_item = self.treeview.selection()
        for item in selected_item:
            item_values = self.treeview.item(item)["values"]
            print(item_values)

    def prompt_add_gui(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Game")

        tk.Label(add_window, text="Game Name:").pack(padx=5, pady=5)
        game_name_entry = tk.Entry(add_window, width=50)
        game_name_entry.pack(padx=5, pady=5)

        tk.Label(add_window, text="Directory Path:").pack(padx=5, pady=5)
        directory_entry = tk.Entry(add_window, width=50)
        directory_entry.pack(padx=5, pady=5)

        # create a frame for radio buttons
        radio_frame = tk.Frame(add_window)
        radio_frame.pack(padx=5, pady=5, anchor="w")

        # create two radio buttons for game version
        game_version = tk.StringVar()
        game_version.set("Left 4 Dead")

        ttk.Radiobutton(radio_frame, text="Left 4 Dead", variable=game_version, value="Left 4 Dead").pack(side="left")
        ttk.Radiobutton(radio_frame, text="Left 4 Dead 2", variable=game_version, value="Left 4 Dead 2").pack(
            side="left", padx=10
        )

        def add_game():
            values = (game_name_entry.get(), directory_entry.get(), game_version.get())
            self.treeview.insert("", "end", text=str(len(self.treeview.get_children()) + 1), values=values)
            add_window.destroy()

        add_button = tk.Button(add_window, text="Add", command=add_game)
        add_button.pack(pady=5, padx=5)


if __name__ == "__main__":
    app = Application()
    app.root.mainloop()
    # app.prompt_add_gui()
