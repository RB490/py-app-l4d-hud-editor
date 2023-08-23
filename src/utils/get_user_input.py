"""A window for the user to input text."""
import tkinter as tk
from tkinter import font

from gui.base import BaseGUI


class UserInputWindow(BaseGUI):
    """
    A window for the user to input text.

    Attributes:
        root (Tk): The main Tkinter window.
        prompt (str): The prompt displayed to the user.
        input_box (Entry): The input box where the user enters text.
        callback (callable): The function to call with the user's input after it has been submitted.
    """

    def __init__(self, title: str, prompt: str) -> None:
        """
        Initialize a new UserInputWindow.

        Args:
            title: The title to display at the top of the window.
            prompt: The prompt to display to the user.
        """
        BaseGUI.__init__(self, is_toplevel_gui=True)
        self.root.title = title
        self.prompt = prompt
        # self.input_box = None
        self.callback = None

        self.create_widgets()

    def create_widgets(self) -> None:
        """Create the widgets for the window."""
        # Set default font size for all widgets
        self.root.option_add("*Font", font.Font(size=20))

        # Create label and entry box for user input
        input_label_font = font.Font(size=10)
        input_label = tk.Label(self.root, text=self.prompt, font=input_label_font)
        input_label.pack(pady=5, padx=5)
        input_box_font = font.Font(size=15)
        self.input_box = tk.Entry(self.root, font=input_box_font)
        self.input_box.config(width=50)
        self.input_box.pack(pady=5, padx=5)

        # Bind Enter key to submit input
        self.set_hotkey("<Return>", self.submit_input)

        # Create button to submit input
        submit_button_font = font.Font(size=10)
        submit_button = tk.Button(self.root, text="Submit", command=self.submit_input, font=submit_button_font)
        submit_button.pack(pady=5, padx=5)

        # Focus on input box
        self.input_box.focus()

    def submit_input(self, event=None) -> None:
        # pylint: disable=unused-argument
        """Submit the user's input and call the callback function (if provided)."""
        # Retrieve user input from entry box and store it in 'command' attribute
        command = self.input_box.get()
        self.destroy()
        if self.callback:
            self.callback(command)


def get_user_input(title: str, prompt: str, callback=None) -> None:
    """
    Open a window to allow the user to enter text.

    Args:
        title: The title to display at the top of the window.
        prompt: The prompt to display to the user.
        callback: A function to call with the user's input after it has been submitted (optional).
    """
    root = tk.Tk()
    root.withdraw()  # Hide parent window
    command_window = UserInputWindow(title, prompt)
    command_window.callback = callback
    command_window.show()
