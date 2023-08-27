import tkinter as tk

class GUIWithStatusBar:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter GUI with Status Bar")

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Create widgets and layout
        self.label = tk.Label(self.main_frame, text="Main Content Goes Here")
        self.label.pack(padx=20, pady=20)

        self.status_frame = tk.Frame(self.root, relief=tk.SUNKEN, bd=1)
        self.status_frame.pack(fill=tk.X, side=tk.BOTTOM)

        self.status_label = tk.Label(self.status_frame, text="Status: Ready", bd=0, padx=10)
        self.status_label.pack(fill=tk.X)

        # Update status bar text
        self.update_status("Status: Initialized")

    def update_status(self, new_text):
        self.status_label.config(text=new_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = GUIWithStatusBar(root)
    root.mainloop()
