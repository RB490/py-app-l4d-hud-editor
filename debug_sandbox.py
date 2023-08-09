import time
import tkinter as tk
from PIL import Image, ImageTk


class YourApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Picture Viewport Example")

        self.frame = tk.Frame(self.root)
        self.frame.pack()

        # create a picture frame on the right side
        self.picture_frame = tk.Frame(self.frame, bg="black")
        self.picture_frame.pack(padx=5, pady=5)

        # Create a canvas to hold the image
        self.canvas = tk.Canvas(self.picture_frame, relief="ridge", bd=4)
        self.canvas.pack()

        # Set initial canvas size
        self.canvas.config(width=200, height=150)

        # time.sleep(1)
        self.load_image()

    def load_image(self):
        image = Image.open("D:\\Downloads\\IMG_0128.JPG")  # Replace with your image file path
        self.photo = ImageTk.PhotoImage(image)

        # Configure the canvas to display the image
        self.canvas.create_image(0, 0, anchor="nw", image=self.photo)

        # Adjust the canvas's scrollable region to fit the image
        self.canvas.config(scrollregion=self.canvas.bbox("all"))


if __name__ == "__main__":
    root = tk.Tk()
    app = YourApp(root)
    root.mainloop()
