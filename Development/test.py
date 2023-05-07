from tkinter import Tk, Menu

root = Tk()
menu = Menu(root)
root.config(menu=menu)


self.hotkeys_menu = Menu(menu)
self.hotkeys_menu.add_command(label="Global")
self.hotkeys_menu.entryconfig("Global", state="disabled")
self.hotkeys_menu.add_separator()
self.hotkeys_menu.add_command(label="Sync Hud", accelerator="Ctrl+S")
self.hotkeys_menu.add_command(label="Show Menu", accelerator="F4")
self.hotkeys_menu.add_command(label="Browse Files", accelerator="F8")
self.hotkeys_menu.add_separator()
self.hotkeys_menu.add_command(label="In-Game")
self.hotkeys_menu.entryconfig("In-Game", state="disabled")
self.hotkeys_menu.add_separator()
self.hotkeys_menu.add_command(label="Load Dead Center finale", accelerator="O")
self.hotkeys_menu.add_command(label="Play credits (On a finale level)", accelerator="P")
self.hotkeys_menu.add_command(label="Noclip", accelerator="G")
self.hotkeys_menu.add_command(label="Pause", accelerator="F8")
self.hotkeys_menu.add_command(label="Admin system menu", accelerator="N")
self.hotkeys_menu.add_command(label="Slow-mo game speed", accelerator="F9")
self.hotkeys_menu.add_command(label="Default game speed", accelerator="F10")
self.hotkeys_menu.add_command(label="Last game cmd", accelerator="F11")

menu.add_cascade(label="Hotkeys", menu=self.hotkeys_menu)


root.mainloop()
