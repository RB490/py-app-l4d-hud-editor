feature -> start hud editing
feature -> finish hud editing

feature -> create hud editor menu + hotkey

feature -> detect game close to automatically run this function

feature -> send alt+f4 to game window (if needed) in GameCommands using this:
        import pydirectinput
		
		# Press the Alt key
        pydirectinput.keyDown("alt")

        # Press and release the F4 key
        pydirectinput.press("f4")

        # Release the Alt key
        pydirectinput.keyUp("alt")

#do-last
	feature -> main gui -> menu icons
		import tkinter as tk

		root = tk.Tk()

		menu_bar = tk.Menu(root)

		file_menu = tk.Menu(menu_bar, tearoff=0)
		file_icon = tk.PhotoImage(file="file_icon.gif")
		file_menu.add_command(label="Open", compound="left", image=file_icon)
		menu_bar.add_cascade(label="File", menu=file_menu)

		root.config(menu=menu_bar)

		root.mainloop()

	feature -> progress gui for the installer class
		install
		update_or_repair
		remove

	feature -> multi game support?

	cleanup -> right now i'm passing persistent_data into various classes such as GameCommands and GameManager
		since persistent_data seemingly only gets used in most instances to call steam_info would it be better
		to create a steam info class that gets passed instead? or pass the required info from the steam function

------------------------------------------------------

#optional #do-last
	feature idea -> instead of using a gui for the main control use the default console interface instead - possibly with a package that has a few more options