"""
A simple splash screen GUI that displays a title and a text message for a specified duration.
"""
import tkinter as tk
from typing import Optional

from gui.base import BaseGUI


class SplashGUI(BaseGUI):
    """
    A simple splash screen GUI that displays a title and a text message for a specified duration.

    Args:
        title (str): The title of the splash screen.
        text (str): The text message to be displayed.
        duration_ms (int, optional): The duration in milliseconds for which the splash screen should be shown.
            If None, the splash screen will remain until manually closed.

    Example:
        # Create and show a splash screen for 3 seconds
        splash = SplashGUI("My Splash Screen", "Welcome!", duration_ms=3000)
        splash.show()
    """

    def __init__(self, title: str, text: str, duration_ms: Optional[int] = None) -> None:
        """
        Initialize the SplashGUI.

        Args:
            title (str): The title of the splash screen.
            text (str): The text message to be displayed.
            duration_ms (int, optional): The duration in milliseconds for which the splash screen should be shown.
                If None, the splash screen will remain until manually closed.
        """
        super().__init__(gui_type="modal")
        self.root.title(title)
        self.root.resizable(width=False, height=False)  # Make the GUI not resizable

        # Centering the label
        self.text_label = tk.Label(self.root, text=text, font=("Helvetica", 20), padx=100, pady=60)
        self.text_label.pack(fill="both", expand=True)  # Fill available space

        self.duration_ms = duration_ms

    def on_show(self):
        """
        Method called when the splash screen is displayed.
        If a duration is specified, the splash screen will close after that duration.
        """
        if self.duration_ms is not None:
            self.root.after(self.duration_ms, self.root.destroy)


# Example usage
def splash_gui_example() -> None:
    """
    Example usage of the SplashGUI class.
    """
    # splash = SplashGUI("My Splash Screen", "Welcome!")
    splash = SplashGUI("My Splash Screen", "Welcome!")
    splash.show()

    print("this is a test")
    input("wait for enter")
    splash.destroy()
    input("wait for enter2")
