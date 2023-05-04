from tkinter import Tk, Menu

root = Tk()
menu = Menu(root)
root.config(menu=menu)


hotkeys_menu = Menu(menu)
hotkeys_menu.add_command(label="Global")
hotkeys_menu.entryconfig("Global", state="disabled")
hotkeys_menu.add_separator()
hotkeys_menu.add_command(label="Sync Hud", accelerator="Ctrl+S")
hotkeys_menu.add_command(label="Show Menu", accelerator="F4")
hotkeys_menu.add_command(label="Browse Files", accelerator="F8")
hotkeys_menu.add_separator()
hotkeys_menu.add_command(label="In-Game")
hotkeys_menu.entryconfig("In-Game", state="disabled")
hotkeys_menu.add_separator()
hotkeys_menu.add_command(label="Load Dead Center finale", accelerator="O")
hotkeys_menu.add_command(label="Play credits (On a finale level)", accelerator="P")
hotkeys_menu.add_command(label="Noclip", accelerator="G")
hotkeys_menu.add_command(label="Pause", accelerator="F8")
hotkeys_menu.add_command(label="Admin system menu", accelerator="N")
hotkeys_menu.add_command(label="Slow-mo game speed", accelerator="F9")
hotkeys_menu.add_command(label="Default game speed", accelerator="F10")
hotkeys_menu.add_command(label="Last game cmd", accelerator="F11")

menu.add_cascade(label="Hotkeys", menu=hotkeys_menu)


root.mainloop()
