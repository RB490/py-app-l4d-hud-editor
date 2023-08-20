# mypy: ignore-errors
# pylint: disable=all

# Import tkinter and PIL modules
import os
import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk

# Define the file and folder icons
TEXT_ICON = "D:\\Programming and projects\\py-app-l4d-hud-editor\\assets\\images\\file_extensions\\text.ico"
IMAGE_ICON = "D:\\Programming and projects\\py-app-l4d-hud-editor\\assets\\images\\file_extensions\\image.ico"
FOLDER_ICON = "D:\\Programming and projects\\py-app-l4d-hud-editor\\assets\\images\\file_extensions\\folder.ico"
WARNING_ICON = "D:\\Programming and projects\\py-app-l4d-hud-editor\\assets\\images\\file_extensions\\error.ico"


def get_image_path(file_path):
    # if not os.path.isfile(file_path):  # Handle invalid path
    #     return WARNING_ICON

    if os.path.isdir(file_path):  # Handle directories
        return FOLDER_ICON

    # Define the file types and their corresponding icons
    file_types = {
        ".txt": TEXT_ICON,
        ".res": TEXT_ICON,
        ".cfg": TEXT_ICON,
        ".jpg": IMAGE_ICON,
        ".png": IMAGE_ICON,
        ".gif": IMAGE_ICON,
    }

    # Get the file extension
    file_extension = os.path.splitext(file_path)[1]

    # Get the corresponding image path or return "warning.png"
    output_image_path = file_types.get(file_extension, WARNING_ICON)

    return output_image_path


# Create a root window
root = tk.Tk()

# Create a treeview widget
tree = ttk.Treeview(root)


# Add some items to the treeview with the icons
items = ["Folder 1", "Folder 2", "File 1.txt", "File 2.png", "File3"]

# Store PhotoImage objects in a list to prevent garbage collection
photo_images = []

for item in items:
    image_path = get_image_path(item)
    image = Image.open(image_path)
    image = image.resize((16, 16), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    photo_images.append(photo)  # Store the PhotoImage object
    tree.insert("", "end", text=item, image=photo)


# Pack the treeview widget
tree.pack()

# Start the main loop
root.mainloop()


# Test the function
input_path = "c:\\windows\\my_file.vtf"
output_image_path = get_image_path(input_path)
print(output_image_path)
