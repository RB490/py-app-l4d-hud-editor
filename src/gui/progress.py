import tkinter as tk
from tkinter import ttk

from utils.constants import APP_ICON


class ProgressGUI:
    def __init__(self, total_steps):
        self.root = tk.Tk()
        self.root.title("Installation Progress")
        self.root.minsize(400, 0)
        self.root.iconbitmap(APP_ICON)
        self.root.resizable(True, False)  # only resizable in width

        self.total_steps = total_steps
        self.current_step = 0

        # self.step_info_label = tk.Label(self.root, text="", font=("Helvetica", 14))
        self.step_info_label = tk.Label(
            self.root, text="", font=("Helvetica", 14), wraplength=400
        )  # Adjust wraplength as needed
        self.step_info_label.pack(padx=10, pady=(10, 0))

        # self.progress_var = tk.DoubleVar()
        # self.progress = ttk.Progressbar(self.root, variable=self.progress_var, maximum=total_steps)
        # self.progress.pack(padx=10, pady=10)

        self.steps_remaining_label = tk.Label(self.root, text="")
        self.steps_remaining_label.pack(padx=10, pady=(0, 10))

    def update_progress(self, step_information):
        self.current_step += 1
        # self.progress_var.set(self.current_step)
        self.step_info_label.config(text=step_information)  # Update step information
        self.steps_remaining_label.config(text=f"Step {self.current_step} of {self.total_steps}")
        self.root.update()

    def close(self):
        self.root.destroy()
