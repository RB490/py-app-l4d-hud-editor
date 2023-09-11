"""A window for the user to input text."""
import tkinter as tk
from tkinter import font

from loguru import logger
from shared_gui.base import BaseGUI


class UserInputWindow(BaseGUI):
    """
    A window for the user to input text.

    Attributes:
        root (Tk): The main Tkinter window.
        prompt (str): The prompt displayed to the user.
        input_box (Entry): The input box where the user enters text.
        callback (callable): The function to call with the user's input after it has been submitted.
    """

    def __init__(self, parent_root, title: str, prompt: str) -> None:
        """
        Initialize a new UserInputWindow.

        Args:
            title: The title to display at the top of the window.
            prompt: The prompt to display to the user.
        """
        super().__init__(gui_type="sub", parent_root=parent_root)
        self.root.title(title)
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

    def submit_input(self, event=None) -> None:
        # pylint: disable=unused-argument
        """Submit the user's input and call the callback function (if provided)."""
        # Retrieve user input from entry box and store it in 'command' attribute
        user_input = self.input_box.get()
        logger.info(f"User input: {user_input}")
        self.destroy()
        if self.callback:
            self.callback(user_input)

    def on_show(self):
        # Focus on input box
        self.input_box.focus()


def get_user_input(parent_root, title: str, prompt: str, callback=None) -> None:
    """
    Open a window to allow the user to enter text.

    Args:
        title: The title to display at the top of the window.
        prompt: The prompt to display to the user.
        callback: A function to call with the user's input after it has been submitted (optional).
    """
    # root = tk.Tk()
    # root.withdraw()  # Hide parent window
    input_win = UserInputWindow(parent_root, title, prompt)
    input_win.callback = callback
    input_win.show()


if __name__ == "__main__":
    from shared_utils.functions import get_invisible_tkinter_root

    root = get_invisible_tkinter_root()
    get_user_input(root, "my title", "my prompt")
    input("press enter to exit script!")
