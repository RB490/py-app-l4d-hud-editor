import tkinter as tk
from tkinter import ttk
from functools import partial


def focus_treeview(tree, *event):
    tree.focus_set()
    children = tree.get_children()
    if children:
        tree.focus(children[0])
        tree.selection_set(children[0])
    return "break"  # Prevent the default tab behavior (inserting a tab character)


# Create a Tkinter window
root = tk.Tk()
root.title("Treeview Focus Example")

# Create a Treeview widget
tree = ttk.Treeview(root, columns=("Name", "Age"))
tree.heading("#1", text="Name")
tree.heading("#2", text="Age")

# Insert some sample data
tree.insert("", "end", text="Person 1", values=("Alice", 30))
tree.insert("", "end", text="Person 2", values=("Bob", 25))
tree.insert("", "end", text="Person 3", values=("Charlie", 35))

# Bind the Tab key to the focus_treeview function
tree.bind("<Tab>", partial(focus_treeview, tree))

# Pack the Treeview widget
tree.pack()

# Create a button to trigger the focus_treeview function
focus_button = tk.Button(root, text="Focus Treeview", command=partial(focus_treeview, tree))
focus_button.pack()

# Start the Tkinter main loop
root.mainloop()
