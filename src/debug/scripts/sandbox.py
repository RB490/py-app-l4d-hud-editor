import tkinter as tk


def create_toplevel():
    top_level = tk.Toplevel(root)
    # Configure your Toplevel window here
    top_level.withdraw()


root = tk.Tk()
root.withdraw()  # Hide the root window

create_toplevel()

root.mainloop()
