



import tkinter as tk

class MyGUI1:
    def __init__(self, root):
        self.root = root
        self.add_image = tk.PhotoImage(file="E:\\Games\\Steam\\steamapps\\common\\SteamVR\\tools\\steamvr_environments\\game\\core\\tools\\images\\common\\add.png")
        self.add_button = tk.Button(self.root, image=self.add_image, compound="left", command=self.open_gui2)
        self.add_button.pack()

    def open_gui2(self):
        gui2 = MyGUI2()  # Create an instance of MyGUI2
        gui2.show()

class MyGUI2:
    def __init__(self):
        # self.root = tk.Toplevel() # this works great!
        self.root = tk.Tk() # This causes gui1 to be garbage collected and image errors to show up
        self.root.title("GUI 2")
        self.add_image = tk.PhotoImage(file="E:\\Games\\Steam\\steamapps\\common\\SteamVR\\tools\\steamvr_environments\\game\\core\\tools\\images\\common\\add.png")
        self.add_button = tk.Button(self.root, image=self.add_image, compound="left", command=self.some_action)
        self.add_button.pack()

    def some_action(self):
        print("Button in GUI 2 clicked!")

    def show(self):
        self.root.mainloop()

def main():
    root = tk.Tk()
    gui1 = MyGUI1(root)
    root.mainloop()

if __name__ == "__main__":
    main()
