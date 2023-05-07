import tkinter as tk

root = tk.Tk()
menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar)
menubar.add_cascade(label="File", menu=file_menu)


def add_entry():
    file_menu.add_command(label="New Entry")


def delete_entry():
    file_menu.delete("New Entry")


add_button = tk.Button(root, text="Add Entry", command=add_entry)
add_button.pack()

delete_button = tk.Button(root, text="Delete Entry", command=delete_entry)
delete_button.pack()

root.mainloop()
