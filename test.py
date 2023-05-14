import tkinter as tk
from tkinter import font


class UserInputWindow:
    """
    A window for the user to input text.

    Attributes:
        root (Tk): The main Tkinter window.
        prompt (str): The prompt displayed to the user.
        input_box (Entry): The input box where the user enters text.
        command (str): The user's input after it has been submitted.
    """

    def __init__(self, title, prompt):
        self.root = tk.Tk()
        self.root.title(title)
        self.prompt = prompt
        self.input_box = None
        self.command = None

        self.create_widgets()

    def create_widgets(self):
        # Set default font size for all widgets
        self.root.option_add("*Font", font.Font(size=20))

        # Create label and entry box for user input
        input_label_font = font.Font(size=10)
        input_label = tk.Label(self.root, text=self.prompt, font=input_label_font)
        input_label.pack(pady=5, padx=5)
        input_box_font = font.Font(size=15)
        self.input_box = tk.Entry(self.root, font=input_box_font)
        self.input_box.config(width=30)
        self.input_box.pack(pady=5, padx=5)

        # Bind Enter key to submit input
        self.input_box.bind("<Return>", self.submit_input)

        # Create button to submit input
        submit_button_font = font.Font(size=10)
        submit_button = tk.Button(self.root, text="Submit", command=self.submit_input, font=submit_button_font)
        submit_button.pack(pady=5, padx=5)

        # Focus on input box
        self.input_box.focus()

    def submit_input(self, event=None):
        # Retrieve user input from entry box and store it in 'command' attribute
        self.command = self.input_box.get()
        self.root.destroy()

    def run(self):
        self.root.mainloop()
        return self.command


def get_user_input(title, prompt):
    """Open window for user to enter input and return it"""
    command_window = UserInputWindow(title, prompt)
    return command_window.run()


if __name__ == "__main__":
    user_command = get_user_input("Execute game command", "Enter game command:")
    print(f"User entered: {user_command}")
