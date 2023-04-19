feature -> main gui -> read addoninfo.txt with some kind of module parser python thing to retrieve addon name

feature -> main gui -> menubar > code dev functionality
	Open user folder
	Open dev folder
	---------------
	Enable (toggle these depending on current status, and/or add sepearate status indicator entry)
	Disable
	---------------
	Install
	Update
	Repair
	Verify
	---------------
	Remove

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

feature -> gameclass/installer -> compare pak01's between user&dev. assume user is up to date - throw a notify if out of date

#optional #do-last
	feature idea -> instead of using a gui for the main control use the default console interface instead - possibly with a package that has a few more options

feature -> read hud's addoninfo.txt and use that name in hud select gui
	keep the current method as a backup incase addoninfo.txt isnt avaiable