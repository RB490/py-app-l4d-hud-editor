import tkinter as tk


def show_menu(event):
    x, y = event.x_root, event.y_root
    menu.tk_popup(x, y)


root = tk.Tk()

# Create the right-click menu
menu = tk.Menu(root, tearoff=0)

# Add items to the menu
menu.add_command(label="Option 1", icon="icon1.png")
menu.add_command(label="Option 2")

# Add a submenu with more options
submenu = tk.Menu(menu, tearoff=0)
submenu.add_command(label="Suboption 1")
submenu.add_command(label="Suboption 2")
menu.add_cascade(label="Options", menu=submenu)

# Add a divider
menu.add_separator()

# Add another option with an icon
menu.add_command(label="Option 3", icon="icon2.png")

# Bind the menu to a right-click event
root.bind("<Button-3>", show_menu)

root.mainloop()
