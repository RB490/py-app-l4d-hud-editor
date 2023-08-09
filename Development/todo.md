goal -> create core functionality ASAP: ability to edit a hud
-------------------------------------------------Current

refactor -> make the hud class into singleton

refactor -> Where possible create required class instances inside the class itself instead of passing them as parameters

refactor -> improve class instance names
	start_instance -> start_gui
	browsing_instance -> browser_gui


bug -> hud dev folder has functioning pak01.vpk's what happened there?



















-------------------------------------------------Features
-------------------------------------------------Restructuring
-------------------------------------------------Misc
-------------------------------------------------Do-Last---------------------------------------------------------------
-------------------------------------------------Do-Last Features
refactor -> replace assert's with prop error handling. try/catch, show_message boxes and suchs

refactor -> test hud editing to figure out how i want the code path to go. for example:
	1. on script start show start gui
	2. when the 'browser' gui gets closed close script instead of opening the start gui

feature -> browser -> treeview context menu funtionality

feature -> browser -> treeview context menu icons

idea -> refactor -> Make the main gui optional by adding all it's functionality into the menu class

bug -> fix menu l4d1&l4d2 grayscale icons
	is not just these icons but any icon. tried garbage collection fix
	^ started being a problem after i moved the menu into the browser class

feature -> browser -> treeview phsyical context menu buttons (?)

feature -> gui icons
feature -> gui buttons icons
feature -> menu icons
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


feature -> multi game support (?)


bug -> start gui -> all the dev options are broken
	AttributeError: 'GameManager' object has no attribute 'manager'
	^ uh, fixed itself.. can i reproduce this?

-------------------------------------------------Do-Last Misc
testing -> test all menu options

idea -> instead of using a gui for the main control use the default console interface instead
	possibly with a package that has a few more options

-------------------------------------------------Do-Last Restructuring
refactor -> shared_utils base tkinter gui class which gets used by (all) my other guis. should contain all the basics

unit testing -> create test class for hud descriptions
unit testing -> create test class for hud syncer

refactoring -> replace easygui
	refactoring -> replace easygui.diropenbox with tkinter filedialog
	refactoring -> replace easygui.boolbox with show_message
	refactoring -> replace easygui.buttonboxes with show_message
			# Example usage
			response = show_message("This is a message.", "okcancel")
			if response is not None:
				if response:
					print("User clicked OK")
				else:
					print("User clicked Cancel")

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

feature -> menu -> make help > hotkeys > ingame & global hotkey menu entries functional
