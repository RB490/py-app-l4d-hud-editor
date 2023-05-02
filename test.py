import tkinter as tk


class MyForm(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("My Form")

        # Create your form widgets here
        # ...

        # Add a button to submit the form
        btn_ok = tk.Button(self, text="OK", command=self.on_ok)
        btn_ok.pack()

        # Initialize your instance variables
        self.result = None
        self.var1 = tk.StringVar()
        self.var2 = tk.StringVar()

    def on_ok(self):
        # Save the input data to the instance variables
        self.result = {"var1": self.var1.get(), "var2": int(self.var2.get())}

        # Close the window
        self.destroy()


# In the main program, create and show the form dialog
def show_form():
    form = MyForm()
    form.wait_window()  # Wait for the window to be closed

    # Access the result from the form
    if form.result:
        print(form.result)


# Call the function to show the form
show_form()
