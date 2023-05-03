import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_menu()
        self.pack()

    def create_menu(self):
        # Create a menu bar
        self.menu_bar = tk.Menu(self.master)

        # Create a File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New", command=lambda: self.handle_menu_click("New"))
        self.file_menu.add_command(label="Open", command=lambda: self.handle_menu_click("Open"))
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.master.quit)

        # Add the File menu to the menu bar
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        # Attach the menu bar to the application window
        self.master.config(menu=self.menu_bar)

    def handle_menu_click(self, menu_item_name):
        print(f"Menu item '{menu_item_name}' was clicked.")


# Create the application window and run it
root = tk.Tk()
app = Application(master=root)
app.mainloop()
