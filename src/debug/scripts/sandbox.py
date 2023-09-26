import ctypes
import tkinter as tk

# Replace 'your_icon.ico' with the path to your custom icon file (.ico format)
icon_path = "your_icon.ico"
icon_path = r"D:\Downloads\py-app-content-manager-main\py-app-content-manager-main\Assets\Images\app.ico"

import ctypes
from tkinter import Tk

# Define a unique identifier for your application
myappid = 'rb.python.program.version'
# Set the application and taskbar icon
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


# Create a Tkinter window
window = Tk()
window.title("My Application")
window.iconbitmap(icon_path)

# Run the Tkinter event loop
window.mainloop()
