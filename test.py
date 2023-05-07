import tkinter as tk


def EditorMenu_InspectHud():
    print("Inspect Hud")


def EditorMenu_ChatDebugSpamW():
    print("Chat Debug (WWWW)")


def EditorMenu_HideGameWorld():
    print("Hide World")


def ClipboardMenu():
    print("Copy Panel")


class SAVED_SETTINGS:
    Game_HideGameWorld = False


EDITORMENU_VGUIDRAWTREE = False

root = tk.Tk()

menubar = tk.Menu(root)
root.config(menu=menubar)

tools_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Tools", menu=tools_menu)

tools_menu.add_command(label="Inspect", command=EditorMenu_InspectHud)
tools_menu.add_command(label="Chat Debug (WWWW)", command=EditorMenu_ChatDebugSpamW)
tools_menu.add_command(label="Hide World", command=EditorMenu_HideGameWorld)
if SAVED_SETTINGS.Game_HideGameWorld:
    tools_menu.entryconfig("Hide World", state="disabled")
if EDITORMENU_VGUIDRAWTREE:
    tools_menu.entryconfig("Inspect Hud", state="disabled")

self.clipboard_menu = tk.Menu(tools_menu, tearoff=0)
self.clipboard_menu.add_command(label="Copy Panel", command=ClipboardMenu)
tools_menu.add_cascade(label="Copy Panel", menu=self.clipboard_menu)

root.mainloop()
