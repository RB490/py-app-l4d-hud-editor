

feature -> finish hud editor menu + hotkey
	^ apparently this isn't quite possible very conveniently with python
	looks like i will probably create a gui with a menu bar. and some big buttons for commonly used features

	- visually display hotkeys
	- menu bar
	^ have every option in the menubar and certain more useful options also on the gui

	^ could also consider adding a hide window command to every menu entry so that it closes on selecting
		^ could do both. keep the gui and buttons but also hide it on selecting - i want to do that anyways

feature -> code menu options
	self.persistent_data["game_mute"]
	self.persistent_data["game_insecure"]
	self.persistent_data["game_pos"]
	self.persistent_data["game_mode"]

feature -> code switch hud menu <- check ahk version for feature parity
	stored huds
	temp huds (add functionality)

feature -> make help > hotkeys > ingame & global hotkey menu entries functional

feature -> detect game close to automatically run this function

cleanup -> get rid of as many editor commands as posssible. a decent amount of them can just use the execute game command method
	for example callvotes & map changing

cleanup -> consider removing menu option specific code and just refresh the entire menu everywhere for example
	for game pos, insecure toggle & game mode

cleanup -> move related hud/.json related functions to a class
	^ ask gpt about it. should i have a specific settings class that makes these modifications or something

feature -> gui icons
feature -> gui position saving&loading
feature -> gui button icons
feature -> gui menu icons

feature -> consider how i want the overall script to behave
	i could get rid of the main gui
	when does the dev installer hit
	etc

feature -> add multi game support

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

	feature -> browser -> display if a file is custom & whether it's added to the hud
		do i still want to display this?
		how do i want to display this?
			adding more columns
			status bar
			

	feature -> progress gui for the installer class
		install
		update_or_repair
		remove

	feature -> multi game support?

	cleanup -> right now i'm passing persistent_data into various classes such as GameCommands and GameManager
		since persistent_data seemingly only gets used in most instances to call steam_info would it be better
		to create a steam info class that gets passed instead? or pass the required info from the steam function

	cleanup -> consider using a different way to use subclasses so i can directly reference them back and forth
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

	feature -> Make the main gui optional? By adding the functionality into the hud class and then linking them both to the select gui and editor menu

	cleanup -> aided with gpt's go through the script improving functions, methods and maybe also the overall structure

------------------------------------------------------

#optional #do-last
	feature idea -> instead of using a gui for the main control use the default console interface instead - possibly with a package that has a few more options