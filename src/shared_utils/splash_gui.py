import tkinter as tk

from gui.base import BaseGUI


class SplashGUI(BaseGUI):
    def __init__(self, title, text, duration_ms=None):
        super().__init__()
        # self.root = tk.Tk()
        self.root.title(title)
        # self.root.geometry("400x300")
        self.root.resizable(width=False, height=False)  # Make the GUI not resizable

        # Centering the label
        self.text_label = tk.Label(self.root, text=text, font=("Helvetica", 20), padx=100, pady=60)
        self.text_label.pack(fill="both", expand=True)  # Fill available space

        self.duration_ms = duration_ms

    def on_show(self):
        if self.duration_ms is not None:
            self.root.after(self.duration_ms, self.root.destroy)
        self.root.update()

    def destroy(self):
        self.root.destroy()


# Example usage
def splash_gui_example():
    splash = SplashGUI("My Splash Screen", "Welcome!")
    splash.show()
    splash.on_show()

    print("this is a test")
    input("wait for enter")
    splash.destroy()
    input("wait for enter2")
