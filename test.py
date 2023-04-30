import tkinter as tk
from tkinter import messagebox


class Genie_GUI:
    def __init__(self, master):
        self.master = master
        master.title("Genie's OptionMenu Example")

        # Create the OptionMenu widget
        options = ["Option 1", "Option 2", "Option 3"]
        self.selected_var = tk.StringVar(value=options[0])
        self.option_menu = tk.OptionMenu(master, self.selected_var, *options, command=self.selected_option)
        self.option_menu.pack()

    def selected_option(self, value):
        print("Selected option:", value)
        messagebox.showinfo("Selected Option", f"You selected {value}")


root = tk.Tk()
gui = Genie_GUI(root)
root.mainloop()
