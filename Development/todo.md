goal -> create core functionality ASAP: ability to edit a hud
-------------------------------------------------Current

testing -> ability to edit a hud
	currently the 






bug -> it's possible for the script to close without unsyncing. maybe crashing or whatever. this is currently not handled
	and leaves synced changes in the dev directory
	
	solution -> make changes so that the script will always unsync even when it fails
		first draft ideas:
			keep an always up to date sync file with changes made
			on script startup, if this file exists, unsync

			the file could/should maybe keep track of various additional changes such as whether to restore user/dev folder
				but maybe just the synced items (files/folders)










-------------------------------------------------Features
-------------------------------------------------Restructuring
-------------------------------------------------Misc
-------------------------------------------------Do-Last---------------------------------------------------------------
-------------------------------------------------Do-Last Features
bug -> running longer tasks such as uninstalling the dev folder hangs the main tkinter gui until finished

bug -> treeview -> 'added' files option doesn't work. no data retrieved

bug -> ingame console bugs -> modify hud editor autoexec to clear the console? or do these errors happen after that
	bug -> ingame console -> failed to load malformed vpk addon's -> potential fixes:
		instead of overwriting the vpk's with empty files create a tiny vpk to overwrite it
		
		Can't load malformed vpk "e:\games\steam\steamapps\common\left 4 dead 2\left4dead2\addons\2020HUD cyan-thick-gap.vpk"
		Can't load malformed vpk "e:\games\steam\steamapps\common\left 4 dead 2\left4dead2\addons\2020HUD.vpk"
		Can't load malformed vpk "e:\games\steam\steamapps\common\left 4 dead 2\left4dead2\addons\workshop\1229957234.vpk"
		Can't load malformed vpk "e:\games\steam\steamapps\common\left 4 dead 2\left4dead2\addons\workshop\655424673.vpk"
		etc.

	bug -> ingame console -> not sure why it's failing to load the maps
		CModelLoader::Map_IsValid:  No such map 'maps/{.bsp'
		map load failed: { not found or invalid
		CModelLoader::Map_IsValid:  No such map 'maps/{.bsp'
		map load failed: { not found or invalid
		etc

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
	++ when the game crashes for whatever reason really fast the script won't detect it as being closed either as it will still be looking
	it should maybe first check if the game is still running before waiting for close event
	
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

restructuring -> consider using a global singleton hotkey manager? i got the idea from a gpt response
	import keyboard

	class MyHotkeyManager:
		def __init__(self):
			self.hotkey_instance = keyboard.add_hotkey("ctrl+alt+p", self.my_function, suppress=True)
			
		def my_function(self):
			print("Hotkey pressed")

		def hotkey_exists(self):
			return self.hotkey_instance in keyboard._hotkeys

	hotkey_manager = MyHotkeyManager()

	if hotkey_manager.hotkey_exists():
		print("Hotkey exists")
	else:
		print("Hotkey does not exist")
