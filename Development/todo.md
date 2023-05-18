-------------------------------------------------Features

feature -> menu -> finish remaining menu handlers
	feature -> menu -> code game position -> Custom (Save)
	feature -> menu -> make help > hotkeys > ingame & global hotkey menu entries functional
	& more

-------------------------------------------------Restructuring
-------------------------------------------------Misc





















-------------------------------------------------Do-Last---------------------------------------------------------------
-------------------------------------------------Do-Last Features
feature -> gui's icons
feature -> gui's position saving&loading
feature -> gui's button icons
feature -> gui's menu icons
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

feature -> browser -> display if a file is custom & whether it's added to the hud
	do i still want to display this?
	how do i want to display this?
		adding more columns
		status bar
	
	logic into there

feature -> progress gui for the installer class
	install
	update_or_repair
	remove

feature -> Make the main gui optional? By adding all it's functionality into the hud? class and then
	linking them both to the select gui and editor menu

feature -> multi game support (?)


-------------------------------------------------Do-Last Misc
testing -> test all menu options

idea -> instead of using a gui for the main control use the default console interface instead
	possibly with a package that has a few more options

-------------------------------------------------Do-Last Restructuring
cleanup -> move various video settings video.txt calls into a general function

restructuring -> break up game commands execute method by for example making a separate reload_hud method that moves

restructuring -> consider how i want the overall script to behave
	i could get rid of the main gui
	when does the dev installer hit
	etc

restructuring -> right now i'm passing persistent_data into various classes such as GameCommands and GameManager
	since persistent_data seemingly only gets used in most instances to call steam_info would it be better
	to create a steam info class that gets passed instead? or pass the required info from the steam function

restructuring -> consider using a different way to use subclasses so i can directly reference them back and forth
	currently not sure this is possible(or better) and kind of like the way im doing it now
	current:
		self.manager.install()
	new:
		self.install()

	and from inside GameManager
		current:
			self.game.get_title()
		new:
			self.get_title()

restructuring -> get rid of as many editor commands as posssible. for example directly execute game command method
	for example callvotes & map changing

restructuring -> move related hud/.json related functions to a class
	^ ask gpt about it. should i have a specific settings class that makes these modifications or something
	prompt_add_existing_hud()
	prompt_open_temp_hud()
	prompt_create_new_hud()
	remove_stored_hud()
	remove_temp_hud()
	retrieve_hud_name_for_dir()

restructuring -> constants.py key_scancodes & key_map same key names & availability

restructuring -> aided with gpt's go through the script improving functions, methods and the overall structure