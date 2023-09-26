import tkinter as tk
from shared_managers.image_manager import ImageManager

# Create a Tkinter window
root = tk.Tk()
root.title("Window with Icon")

image_manager = ImageManager()

# Load and set the window icon using root.iconphoto()
icon_image = tk.PhotoImage(file=image_manager.get_image_path("folder"))  # Replace with the path to your .png file
root.iconphoto(True, icon_image)

# Run the Tkinter main loop
root.mainloop()
