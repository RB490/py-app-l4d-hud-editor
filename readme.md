# L4D Hud Editor Script

![](https://github.com/RB490/ahk-app-l4d-hud-editor/blob/master/Assets/Images/Readme.md/modifying.gif)

### What
Create & modify huds for both Left 4 Dead games without annoyances such as having to move files in and out the game folder or extracting all the pak01_dir.vpk's.

A menu containing variety of convenient commands. Eg: 'showpanel' which can show a lot of the game panels. For example the score interface at the end of a map

### How
1. The script creates a copy of the game folder and modifies it as needed.
2. Hud files are copied into it and removed when finished.
3. On saving changes in a text editor with CTRL+S the script moves any changed hud files into the game.

# Debugging
### Notes
* It's recommended to set HUD files to open in VSCode by default and install a Valve KeyValue Extension such as https://marketplace.visualstudio.com/items?itemName=GEEKiDoS.vdf
    > Opening the entire HUD folder in VSCode also makes for a convenient workflow

* After reloading fonts
    > Closed captions won't show fonts until the map is restarted

    > The options in the hud inspection debug tool (vgui_drawtree) will be invisible until the game is restarted. The most usefull option 'Highlight Selected' is the last option in the second row

* Text controls can't be centered while they have the 'wrap' property enabled
* Some changes require a full game restart before they take effect. Eg. deleting 'splatter' controls on some panels eg. the versus 'You will become the tank' panel
* Changes to 'scheme' files like clientscheme.res are only loaded when the game changes resolution
    > A few non-scheme files also require fonts to be reloaded for changes to take effect eg: 'Resource/UI/TransitionStatsSurvivorHighlight.res'
* Slowing down time is very usefull for debugging some panels that can't be shown using the 'showpanel' command
    > Panels will stay on the screen for a lot longer during slow motion

    > Some panels will be visible while hud_reloadscheme is working during slow motion
 
 * Addons: Having an addon's file name written in caps lock can cause unexpected behaviour. For example
crosshairs addons don't work with 'RBHUD' when the huds vpk file is titled 'RBHUD' but work fine with 'rbhud'

* Game menus aren't updated until they're reopened. Use click coordinates:
![](https://github.com/RB490/ahk-app-l4d-hud-editor/blob/master/Assets/Images/Readme.md/clickOnReload.png)

### Commands
* Sourcemod:              https://wiki.alliedmods.net/Admin_Commands_(SourceMod)
* Sourcemod funcommands:    https://forums.alliedmods.net/showthread.php?t=75520

> Sourcemod only works in 'insecure' mode

* Raymans admin system: https://steamcommunity.com/sharedfiles/filedetails/?id=213591107

### Hud elements

#### Scavenge tierbreaker
Debugging: copy paste the tiebreaker onto a visible panel eg: localplayerpanel.res

Positioning: host_timescale 50 or somewhere around there on the hud dev map to make rounds end quickly. then slow the time down again

#### Credits
Use hotkeys 'O' and 'P' to load dead center finale & teleport and finish finale, respectively

Slow time or pause while credits are playing

Reload changes with 'fonts'

#### Scavenge tiebreaker panel
Start scavenge round -> speed up the game using host_timescale -> when tiebreaker shows -> F9 to slow down

#### Multiplayer related panels
 Such as
- all 8 votes on the votehud
- infected teammate panels tab scoreboard
- infected teammate panels hud.

Run the game in insecure mode and join steam group with 15+ players. They usually have sv_consistency 0

When a good server is found, save the ip

#### Spectate
Take control of survivor bot -> spectate -> jointeam 2

#### Votehud
Set a panel to visible 1 ->  hud_reloadscheme with lower host_timescale -> pause game

#### Coop transition screen table
Requires font reloading which causes the background to turn black. To prevent this Enable 'reopen menu after reloading' option

Or

Manually enter 'hud_reloadscheme; ui_reloadscheme; mat_reloadallmaterials; mat_setvideomode 1 1 1 1;mat_setvideomode 1920 1080 1 1; wait; showpanel transition_stats'

#### pzdamagerecordpanel
Lower host_timescale