feature -> ClassCommands

feature -> start hud editing
feature -> finish hud editing

feature -> create hud editor menu + hotkey

feature -> detect game close to automatically run this function


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

------------------------------------------------------

#optional #do-last
	feature idea -> instead of using a gui for the main control use the default console interface instead - possibly with a package that has a few more options