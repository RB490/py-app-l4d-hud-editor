# Import the required libraries
from tkinter import *
from tkinter import ttk

# Create an instance of tkinter frame or window
win = Tk()

# Set the size of the window
win.geometry("700x350")


# Define a function to make the window above
def lift_window():
    win.lift()
    win.after(1000, lift_window)
    hwnd = win32gui.FindWindowEx(0,0,0, "Window Title")
    win32gui.SetForegroundWindow(hwnd)


# Add A label widget
Label(win, text="Hey Folks, Welcome to TutorialsPoint✨", font=("Aerial 18 italic")).place(x=130, y=150)

lift_window()

win.mainloop()
