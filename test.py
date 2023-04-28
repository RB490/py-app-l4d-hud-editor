import tkinter as tk
from tkinter import ttk


def refresh_treeview(treeview, data_dict):
    # Clear existing items in the Treeview
    treeview.delete(*treeview.get_children())

    # Add items from the data_dict to the Treeview
    for key, value in data_dict.items():
        treeview.insert("", "end", values=(key, value))


# Create a tkinter window
root = tk.Tk()

# Create a Treeview widget
treeview = ttk.Treeview(root, columns=("key", "value"))
treeview.heading("key", text="Key")
treeview.heading("value", text="Value")
treeview.pack()

# Create a sample dictionary
data_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}

# Load the dictionary into the Treeview
refresh_treeview(treeview, data_dict)

# Start the tkinter event loop
root.mainloop()
