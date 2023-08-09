goal -> create core functionality ASAP: ability to edit a hud
-------------------------------------------------Current


bug -> edit hud -> unsync hud -> unsync hud again -> second time it still tries to unsync according to terminal
	un_sync item: D:\Programming and projects\py-app-l4d-hud-editor\development\debug\hud_debug\Workspace\2020HUD\scripts\mod_textures.txt
	_unsync_item: D:\Programming and projects\py-app-l4d-hud-editor\development\debug\hud_debug\Workspace\2020HUD\scripts\mod_textures.txt
	un_sync item: D:\Programming and projects\py-app-l4d-hud-editor\development\debug\hud_debug\Workspace\2020HUD\scripts\stats_crawl.txt
	_unsync_item: D:\Programming and projects\py-app-l4d-hud-editor\development\debug\hud_debug\Workspace\2020HUD\scripts\stats_crawl.txt

testing -> ability to edit a hud





-------------------------------------------------Features
-------------------------------------------------Restructuring
-------------------------------------------------Misc
-------------------------------------------------Do-Last---------------------------------------------------------------
-------------------------------------------------Do-Last Features
refactor -> self.game.run("dev", "wait on close")
	should be wait_on_close=True, or false

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

bug -> dev -> update install -> game starts to rebuild audio but nothing happens
bug -> dev -> update install -> rebuild audio -> manually closed game during process causing the script to hang
	File "D:\Programming and projects\py-app-l4d-hud-editor\packages\utils\functions.py", line 301, in wait_for_process_and_get_hwnd
		raise RuntimeError(f"Process '{executable_name}' not found within {timeout_seconds} seconds")
	RuntimeError: Process 'left4dead2.exe' not found within 60 seconds

feature -> browser -> treeview phsyical context menu buttons (?)

refactor -> xonsider and test how i want to do error handling in the sync class. possibly after or during creating unit test
	eg: sync() raises exceptions currently. which caused an error then pressing the sync hotkey
	& target_dir_main_name is not checked for validty in sync()

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

In the context of Tkinter GUIs, whether you choose to use the singleton pattern depends on factors such as the complexity of your application, your team's coding practices, and your familiarity with the design pattern. If your application is relatively small and doesn't require extensive management of GUI instances, using a singleton might be overengineering. On the other hand, if your application has complex interactions between different parts of the code and you want to ensure a single point of GUI access, a singleton could be beneficial
	refactor -> Make the browser gui into a simpleton?
	refactor -> Make the start gui into a simpleton?
	^ doesn't really make much of a difference either way i suppose

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
