import tkinter as tk
import webbrowser

# Define the function to open the main page link
def open_main_page():
    main_page_url = "https://your-main-page-url.com"  # Replace with your actual main page URL
    webbrowser.open(main_page_url)

# Create the main application window
app = tk.Tk()
app.title("Project Information")

# Create a label to display project information
project_info_label = tk.Label(
    app,
    text="Welcome to My Project!\nThis is a brief description of the project.",
    padx=10,
    pady=10
)
project_info_label.pack()

# Create a button to open the main page
open_page_button = tk.Button(
    app,
    text="Open Main Page",
    command=open_main_page
)
open_page_button.pack()

# Run the Tkinter main loop
app.mainloop()
