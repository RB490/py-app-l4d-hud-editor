"Resource/UI/MainMenu.res"
{
	"MainMenu"
	{
		"ControlName"			"Frame"
		"fieldName"				"MainMenu"
		"xpos"					"0"
		"ypos"					"0"
		"wide"					"f0"
		"tall"					"f0"
		"autoResize"			"0"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"0"
		"PaintBackgroundType"	"0"
	}
	
	"PnlBackground"
	{
		"ControlName"		"L4DMenuBackground"
		"fieldName"			"PnlBackground"
		"xpos"				"10"
		"ypos"				"0"
		"zpos"				"-1"
		"wide"				"140"
		"tall"				"f0"
		"visible"			"1"
		"enabled"			"1"
		"fillColor"			"TransparentBlack"
	}
	
	GameHeaderImage
	{
		"ControlName"	"ImagePanel"
		"fieldName"	"GameHeaderImage"
		"xpos"		"60"
		"ypos"		"15"
		"wide"		"40"
		"tall"		"40"
		"zpos"		"-1"
		"visible"	"1"
		"enabled"	"1"
		"scaleImage"	"1"
		"image"		"../vui/l4d2header"
		
	}
	
	"TextVersion"
	{
		"ControlName"			"Label"
		"fieldName"				"TextVersion"
		"xpos"					"10"
		"ypos"					"60"
		"wide"					"140"
		"tall"					"15"
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"0"
		"labelText"			"RBHUD"
		"textAlignment"		"center"
		"font"				"MainBold"
	}
	
	"Custom_BtnSingleplayer"
	{
		"ControlName"			"L4D360HybridButton"
		"fieldName"				"Custom_BtnSingleplayer"
		"xpos"					"15"
		"ypos"					"85"	[$WIN32]
		"wide"					"120"	[$WIN32]
		"tall"					"15"	[$WIN32]
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"1"
		"navUp"					"PnlQuickJoinGroups" [$WIN32]
		"navDown"				"Custom_BtnCoOp"
		"labelText"				"Singleplayer" //#L4D360UI_MainMenu_CoOp
		"tooltiptext"			"#L4D360UI_MainMenu_CoOp_Tip"
		"style"					"MainMenuButton"
		"command"				"SoloPlay"
		"ActivationType"		"1"
	}
	
	"Custom_BtnCoOp"
	{
		"ControlName"			"L4D360HybridButton"
		"fieldName"				"Custom_BtnCoOp"
		"xpos"					"15"
		"ypos"					"100"	[$WIN32]
		"wide"					"120"	[$WIN32]
		"tall"					"15"	[$WIN32]
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"1"
		"navUp"					"Custom_BtnSingleplayer" [$WIN32]
		"navDown"				"Custom_BtnCoOpReaslism"
		"labelText"				"Campaign" //#L4D360UI_MainMenu_CoOp
		"tooltiptext"			"#L4D360UI_MainMenu_CoOp_Tip"
		"style"					"MainMenuButton"
		"command"				"CustomMatch_coop"
		"ActivationType"		"1"
	}
	
	"Custom_BtnCoOpReaslism"
	{
		"ControlName"			"L4D360HybridButton"
		"fieldName"				"Custom_BtnCoOpReaslism"
		"xpos"					"15"
		"ypos"					"115"	[$WIN32]
		"wide"					"120"	[$WIN32]
		"tall"					"15"	[$WIN32]
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"1"
		"navUp"					"Custom_BtnCoOp" [$WIN32]
		"navDown"				"Custom_BtnVersus"
		"labelText"				"Realism Campaign" //#L4D360UI_MainMenu_CoOp
		"tooltiptext"			"#L4D360UI_MainMenu_CoOp_Tip"
		"style"					"MainMenuButton"
		"command"				"CustomMatch_realism"
		"ActivationType"		"1"
	}
	
	"Custom_BtnVersus"
	{
		"ControlName"			"L4D360HybridButton"
		"fieldName"				"Custom_BtnVersus"
		"xpos"					"15"
		"ypos"					"130"	[$WIN32]
		"wide"					"120"	[$WIN32]
		"tall"					"15"	[$WIN32]
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"0"
		"navUp"					"Custom_BtnCoOpReaslism"
		"navDown"				"Custom_BtnVersusRealism"
		"labelText"				"Versus" 
		"tooltiptext"			"#L4D360UI_MainMenu_Versus_Tip"
		"disabled_tooltiptext"	"#L4D360UI_MainMenu_Versus_Tip_Disabled"
		"style"					"MainMenuButton"
		"command"				"CustomMatch_versus"
		"ActivationType"		"1"
		"FocusDisabledBorderSize" "1"
	}
	
	"Custom_BtnVersusRealism"
	{
		"ControlName"			"L4D360HybridButton"
		"fieldName"				"Custom_BtnVersusRealism"
		"xpos"					"15"
		"ypos"					"145"	[$WIN32]
		"wide"					"120"	[$WIN32]
		"tall"					"15"	[$WIN32]
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"0"
		"navUp"					"Custom_BtnVersus"
		"navDown"				"Custom_BtnScavenge"
		"labelText"				"Realism Versus" 
		"tooltiptext"			"#L4D360UI_MainMenu_Versus_Tip"
		"disabled_tooltiptext"	"#L4D360UI_MainMenu_Versus_Tip_Disabled"
		"style"					"MainMenuButton"
		"command"				"CustomMatch_mutation12"
		"ActivationType"		"1"
		"FocusDisabledBorderSize" "1"
	}
	
	"Custom_BtnScavenge"
	{
		"ControlName"			"L4D360HybridButton"
		"fieldName"				"Custom_BtnScavenge"
		"xpos"					"15"
		"ypos"					"160"	[$WIN32]
		"wide"					"120"	[$WIN32]
		"tall"					"15"	[$WIN32]
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"0"
		"navUp"					"Custom_BtnVersusRealism"
		"navDown"				"Custom_BtnSurvival"
		"labelText"				"Scavenge" 
		"tooltiptext"			"#L4D360UI_MainMenu_Versus_Tip"
		"disabled_tooltiptext"	"#L4D360UI_MainMenu_Versus_Tip_Disabled"
		"style"					"MainMenuButton"
		"command"				"CustomMatch_scavenge"
		"ActivationType"		"1"
		"FocusDisabledBorderSize" "1"
	}
	
	"Custom_BtnSurvival"
	{
		"ControlName"			"L4D360HybridButton"
		"fieldName"				"Custom_BtnSurvival"
		"xpos"					"15"
		"ypos"					"175"	[$WIN32]
		"wide"					"120"	[$WIN32]
		"tall"					"15"	[$WIN32]
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"0"
		"navUp"					"Custom_BtnScavenge"
		"navDown"				"Custom_BtnMutation"
		"labelText"				"Survival" 
		"tooltiptext"			"#L4D360UI_MainMenu_Versus_Tip"
		"disabled_tooltiptext"	"#L4D360UI_MainMenu_Versus_Tip_Disabled"
		"style"					"MainMenuButton"
		"command"				"CustomMatch_survival"
		"ActivationType"		"1"
		"FocusDisabledBorderSize" "1"
	}
	
	"Custom_BtnMutation"
	{
		"ControlName"			"L4D360HybridButton"
		"fieldName"				"Custom_BtnMutation"
		"xpos"					"15"
		"ypos"					"190"	[$WIN32]
		"wide"					"120"	[$WIN32]
		"tall"					"15"	[$WIN32]
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"0"
		"navUp"					"Custom_BtnSurvival"
		"navDown"				"Custom_BtnChangeMutation"
		"labelText"				"Mutation" 
		"tooltiptext"			"#L4D360UI_MainMenu_Versus_Tip"
		"disabled_tooltiptext"	"#L4D360UI_MainMenu_Versus_Tip_Disabled"
		"style"					"MainMenuButton"
		"command"				"CustomMatch_challenge"
		"ActivationType"		"1"
		"FocusDisabledBorderSize" "1"
	}
	
	"Custom_BtnChangeMutation"
	{
		"ControlName"			"L4D360HybridButton"
		"fieldName"				"Custom_BtnChangeMutation"
		"xpos"					"15"
		"ypos"					"205"	[$WIN32]
		"wide"					"120"	[$WIN32]
		"tall"					"15"	[$WIN32]
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"0"
		"navUp"					"Custom_BtnMutation"
		"navDown"				"Custom_BtnServerBrowser"
		"labelText"				"Change Mutation" 
		"tooltiptext"			"#L4D360UI_MainMenu_Versus_Tip"
		"disabled_tooltiptext"	"#L4D360UI_MainMenu_Versus_Tip_Disabled"
		"style"					"MainMenuButton"
		"command"				"ChooseChallengeMode"
		"ActivationType"		"1"
		"FocusDisabledBorderSize" "1"
	}

	"Custom_BtnServerBrowser"
	{
		"ControlName"				"L4D360HybridButton"
		"fieldName"					"Custom_BtnServerBrowser"
		"xpos"						"15"
		"ypos"						"235"
		"wide"						"120"
		"tall"						"15"
		"autoResize"				"1"
		"pinCorner"					"0"
		"visible"					"1"
		"enabled"					"1"
		"tabPosition"				"0"
		"navUp"						"Custom_BtnChangeMutation"
		"navDown"					"Custom_BtnAddons"
		"labelText"					"Servers"
		"tooltiptext"				"#L4D360UI_MainMenu_PlaySolo_Tip"
		"disabled_tooltiptext"		"#L4D360UI_MainMenu_PlaySolo_Tip_Disabled"
		"style"						"MainMenuButton"
		"command"					"OpenServerBrowser"
		"ActivationType"			"1"
		"FocusDisabledBorderSize"	"1"
	}
	
	"Custom_BtnAddons"
	{
		"ControlName"				"L4D360HybridButton"
		"fieldName"					"Custom_BtnAddons"
		"xpos"						"15"
		"ypos"						"265"
		"wide"						"120"
		"tall"						"15"
		"autoResize"				"1"
		"pinCorner"					"0"
		"visible"					"1"
		"enabled"					"1"
		"tabPosition"				"0"
		"navUp"						"Custom_BtnServerBrowser"
		"navDown"					"Custom_BtnStatsAndAchievements"
		"labelText"					"Addons" //#L4D360UI_MainMenu_PlaySolo
		"tooltiptext"				"#L4D360UI_MainMenu_PlaySolo_Tip"
		"disabled_tooltiptext"		"#L4D360UI_MainMenu_PlaySolo_Tip_Disabled"
		"style"						"MainMenuButton"
		"command"					"Addons"
		"ActivationType"			"1"
		"FocusDisabledBorderSize"	"1"
	}
	
	"Custom_BtnStatsAndAchievements"
	{
		"ControlName"			"L4D360HybridButton"
		"fieldName"				"Custom_BtnStatsAndAchievements"
		"xpos"					"15"
		"ypos"					"280"	[$WIN32]
		"wide"					"120"	[$WIN32]
		"tall"					"15"	[$WIN32]
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"0"
		"navUp"					"Custom_BtnAddons"
		"navDown"				"Custom_BtnPlaySurvivalLeaderboards"
		"labelText"				"Achievements" //#L4D360UI_MainMenu_StatsAndAchievements
		"tooltiptext"			"#L4D360UI_MainMenu_PCStatsAndAchievements_Tip"	[$WIN32]
		"style"					"MainMenuButton"
		"command"				"StatsAndAchievements"
		"ActivationType"		"1"
	}
	
	"Custom_BtnPlaySurvivalLeaderboards"
	{
		"ControlName"				"L4D360HybridButton"
		"fieldName"					"Custom_BtnPlaySurvivalLeaderboards"
		"xpos"						"15"
		"ypos"						"295"
		"wide"						"120"
		"tall"						"15"
		"autoResize"				"1"
		"pinCorner"					"0"
		"visible"					"1"
		"enabled"					"1"
		"tabPosition"				"0"
		"navUp"						"Custom_BtnStatsAndAchievements"
		"navDown"					"Custom_BtnCommentary"
		"labelText"					"Leaderboards" //#L4D360UI_MainMenu_PlaySolo
		"tooltiptext"				"#L4D360UI_MainMenu_PlaySolo_Tip"
		"disabled_tooltiptext"		"#L4D360UI_MainMenu_PlaySolo_Tip_Disabled"
		"style"						"MainMenuButton"
		"command"					"Leaderboards_survival"
		"ActivationType"			"1"
		"FocusDisabledBorderSize"	"1"
	}
	
	"Custom_BtnCommentary"
	{
		"ControlName"			"L4D360HybridButton"
		"fieldName"				"Custom_BtnCommentary"
		"xpos"					"15"
		"ypos"					"310"	[$WIN32]
		"wide"					"120"	[$WIN32]
		"tall"					"15"	[$WIN32]
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"0"
		"navUp"					"Custom_BtnPlaySurvivalLeaderboards"
		"navDown"				"Custom_BtnVideo"
		"labelText"				"Developer Commentary" //#L4D360UI_MainMenu_StatsAndAchievements
		"tooltiptext"			"#L4D360UI_MainMenu_PCStatsAndAchievements_Tip"	[$WIN32]
		"style"					"MainMenuButton"
		"command"				"DeveloperCommentary"
		"ActivationType"		"1"
	}
	
	"Custom_BtnVideo"
	{
		"ControlName"			"L4D360HybridButton"
		"fieldName"				"Custom_BtnVideo"
		"xpos"					"15"
		"ypos"					"340"	[$WIN32]
		"wide"					"120"
		"tall"					"15"	[$WIN32]
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"0"
		"navUp"					"Custom_BtnCommentary"
		"navDown"				"Custom_BtnBrightness"
		"tooltiptext"			"#L4D_video_tip"
		"labelText"				"#GameUI_Video"
		"style"					"MainMenuButton"
		"command"				"Video"
		"ActivationType"		"1"
	}

	"Custom_BtnBrightness"
	{
		"ControlName"			"L4D360HybridButton"
		"fieldName"				"Custom_BtnBrightness"
		"xpos"					"15"
		"ypos"					"355"	[$WIN32]
		"wide"					"120"
		"tall"					"15"	[$WIN32]
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"0"
		"navUp"					"Custom_BtnVideo"
		"navDown"				"Custom_BtnAudio"
		"tooltiptext"			"#GameUI_AdjustGamma"
		"labelText"				"#GameUI_Brightness"
		"style"					"MainMenuButton"
		"command"				"Brightness"
		"ActivationType"		"1"
	}

	"Custom_BtnAudio"
	{
		"ControlName"			"L4D360HybridButton"
		"fieldName"				"Custom_BtnAudio"
		"xpos"					"15"
		"ypos"					"370"	[$WIN32]
		"wide"					"120"
		"tall"					"15"	[$WIN32]
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"0"
		"navUp"					"Custom_BtnBrightness"
		"navDown"				"Custom_BtnController"
		"tooltiptext"			"#L4D_audio_tip"
		"labelText"				"#GameUI_Audio"
		"style"					"MainMenuButton"
		"command"				"Audio"
		"ActivationType"		"1"
	}

	"Custom_BtnController"
	{
		"ControlName"			"L4D360HybridButton"
		"fieldName"				"Custom_BtnController"
		"xpos"					"15"
		"ypos"					"385"	[$WIN32]
		"wide"					"120"
		"tall"					"15"	[$WIN32]
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"0"
		"navUp"					"Custom_BtnAudio"
		"navDown"				"Custom_BtnMultiplayer"
		"tooltiptext"			"#L4D_keyboard_tip"
		"labelText"				"#L4D360UI_KeyboardMouse"
		"style"					"MainMenuButton"
		"command"				"KeyboardMouse"
		"ActivationType"		"1"
	}

	"Custom_BtnMultiplayer"
	{
		"ControlName"			"L4D360HybridButton"
		"fieldName"				"Custom_BtnMultiplayer"
		"xpos"					"15"
		"ypos"					"400"	[$WIN32]
		"wide"					"120"
		"tall"					"15"	[$WIN32]
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"0"
		"navUp"					"Custom_BtnController"
		"navDown"				"Custom_BtnCloud"
		"tooltiptext"			"#L4D_multiplayer_tip"
		"labelText"				"#GameUI_Multiplayer"
		"style"					"MainMenuButton"
		"command"				"MultiplayerSettings"
		"ActivationType"		"1"
	}

	"Custom_BtnCloud"
	{
		"ControlName"			"L4D360HybridButton"
		"fieldName"				"Custom_BtnCloud"
		"xpos"					"15"
		"ypos"					"415"	[$WIN32]
		"wide"					"120"
		"tall"					"15"	[$WIN32]
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"0"
		"navUp"					"Custom_BtnMultiplayer"
		"navDown"				"Custom_BtnQuit"
		"tooltiptext"			"#L4D_steamcloud_tip"
		"labelText"				"#L4D360UI_Cloud_Title"
		"style"					"MainMenuButton"
		"command"				"CloudSettings"
		"ActivationType"		"1"
	}
	
	"Custom_BtnQuit" [$WIN32]
	{
		"ControlName"			"L4D360HybridButton"
		"fieldName"				"Custom_BtnQuit"
		"xpos"					"15"
		"ypos"					"445"
		"wide"					"120"
		"tall"					"15"
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"0"
		"navUp"					"Custom_BtnCloud"
		"navDown"				"PnlQuickJoin"
		"labelText"				"Quit" //#L4D360UI_MainMenu_Quit
		"tooltiptext"			"#L4D360UI_MainMenu_Quit_Tip"
		"style"					"MainMenuButton"
		"command"				"QuitGame"
		"ActivationType"		"1"
	}
	
	"PnlQuickJoin"
	{
		"ControlName"			"QuickJoinPanel"
		"fieldName"				"PnlQuickJoin"
		"ResourceFile"			"resource/UI/L4D360UI/QuickJoin.res"
		"visible"				"0"
		"wide"					"240"	[$WIN32]
		"tall"					"300"
		"xpos"					"160"
		"ypos"					"r75"	[$WIN32]
		"navUp"					"Custom_BtnQuit"
		"navDown"				"PnlQuickJoinGroups"
	}
	
	"PnlQuickJoinGroups"	[$WIN32]
	{
		"ControlName"			"QuickJoinGroupsPanel"
		"fieldName"				"PnlQuickJoinGroups"
		"ResourceFile"			"resource/UI/L4D360UI/QuickJoinGroups.res"
		"visible"				"0"
		"wide"					"500"
		"tall"					"300"
		"xpos"					"c0"
		"ypos"					"r75"
		"navUp"					"PnlQuickJoin"
		"navDown"				"Custom_BtnSingleplayer"
	}
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	"BtnStatsAndAchievements"
	{
		"ControlName"			"L4D360HybridButton"
		"fieldName"				"BtnStatsAndAchievements"
		"xpos"					"100"
		"ypos"					"255"
		"wide"					"180"
		"tall"					"20"
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"0"		[$X360GUEST]
		"enabled"				"0"		[$X360GUEST]
		"visible"				"0"		[!$X360GUEST]
		"enabled"				"1"		[!$X360GUEST]
		"tabPosition"			"0"
		"navUp"					"BtnChangeGamers"
		"navDown"				"BtnOptions"
		"labelText"				"#L4D360UI_MainMenu_StatsAndAchievements"
		"tooltiptext"			"#L4D360UI_MainMenu_StatsAndAchievements_Tip"	[$X360]
		"tooltiptext"			"#L4D360UI_MainMenu_PCStatsAndAchievements_Tip"	[$WIN32]
		"style"					"MainMenuButton"
		"command"				"StatsAndAchievements"
		"ActivationType"		"1"
		"EnableCondition"		"Never" [$DEMO]
	}
	
	"BtnOptions"
	{
		"ControlName"			"L4D360HybridButton"
		"fieldName"				"BtnOptions"
		"xpos"					"100"
		"ypos"					"275"
		"wide"					"180"
		"tall"					"20"
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"0"
		"enabled"				"1"
		"tabPosition"			"0"
		"navUp"					"BtnStatsAndAchievements"
		"navDown"				"BtnAddons"
		"labelText"				"#L4D360UI_MainMenu_Options"
		"tooltiptext"			"#L4D360UI_MainMenu_Options_Tip"
		"style"					"MainMenuButton"
		"command"				"FlmOptionsFlyout"			[!$X360GUEST]
		"command"				"FlmOptionsGuestFlyout"		[$X360GUEST]	
		"ActivationType"		"1"
	}
	
	"IconAddons"
	{
		"ControlName"			"ImagePanel"
		"fieldName"				"IconAddons"
		"xpos"					"110"
		"ypos"					"262"
		"wide"					"20"
		"tall"					"20"
		"scaleImage"			"1"
		"pinCorner"				"0"
		"visible"				"0"
		"enabled"				"1"
		"tabPosition"			"0"
		"image"					"common/l4d_spinner"
		"frame"					"0"
		"scaleImage"			"1"
	}	

	"IconAddons_Bg"
	{
		"ControlName"	"Panel"
		"fieldName"	"IconAddons_Bg"
		"xpos"					"110"
		"ypos"					"262"
		"wide"					"20"
		"tall"					"20"
		"zpos"		"9999"
		"visible"		"0"
		"enabled"		"1"
		"scaleImage"	"0"
		"bgcolor_override"	"255 255 255 255"
	}
	
	"BtnAddons"
	{
		"ControlName"			"L4D360HybridButton"
		"fieldName"				"BtnAddons"
		"xpos"					"100"
		"ypos"					"295"
		"wide"					"180"
		"tall"					"20"
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"0"
		"enabled"				"1"
		"tabPosition"			"0"
		"navUp"					"BtnOptions"
		"navDown"				"BtnExtras"
		"labelText"				"#L4D360UI_Extras_Addons"
		"tooltiptext"			"#L4D360UI_Extras_Addons_Tip"
		"style"					"MainMenuButton"
		"command"				"Addons"			[!$X360GUEST]
		"command"				"Addons"		[$X360GUEST]	
		"ActivationType"		"1"
	}

	"BtnExtras"
	{
		"ControlName"			"L4D360HybridButton"
		"fieldName"				"BtnExtras"
		"xpos"					"100"
		"ypos"					"315"
		"wide"					"180"
		"tall"					"20"
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"0"
		"enabled"				"1"
		"tabPosition"			"0"
		"navUp"					"BtnAddons"
		"navDown"				"BtnBlogPost"
		"labelText"				"#L4D360UI_MainMenu_Extras"
		"tooltiptext"			"#L4D360UI_MainMenu_Extras_Tip"
		"style"					"MainMenuButton"
		"command"				"FlmExtrasFlyoutCheck"
		"ActivationType"		"1"
		"EnableCondition"					"Never" [$DEMO]
	}

	"IconBlogPost"
	{
		"ControlName"			"ImagePanel"
		"fieldName"				"IconBlogPost"
		"xpos"					"75"
		"ypos"					"335"
		"wide"					"20"
		"tall"					"20"
		"scaleImage"			"1"
		"pinCorner"				"0"
		"visible"				"0"
		"enabled"				"1"
		"tabPosition"			"0"
		"image"					"rssfeed"
		"frame"					"0"
		"scaleImage"			"1"
	}	
	
	"BtnBlogPost"
	{
		"ControlName"			"L4D360HybridButton"
		"fieldName"				"BtnBlogPost"
		"xpos"					"100"
		"ypos"					"3359999"	//335
		"wide"					"180"
		"tall"					"20"
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"0"
		"enabled"				"0"
		"tabPosition"			"0"
		"navUp"					"BtnExtras"
		"navDown"				"BtnQuit" [$WIN32]
		"navDown"				"BtnGameModes" [$X360]
		"labelText"				"#L4D360UI_MainMenu_BlogPost"
		"tooltiptext"			""
		"style"					"MainMenuButton"
		"command"				"ShowBlogPost"
		"ActivationType"		"1"
		"EnableCondition"					"Never" [$DEMO]
	}
	
	"BtnQuit"
	{
		"ControlName"			"L4D360HybridButton"
		"fieldName"				"BtnQuit"
		"xpos"					"100"
		"ypos"					"355"
		"wide"					"180"
		"tall"					"20"
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"0" [$X360]
		"visible"				"0" [$WIN32]
		"enabled"				"1"
		"tabPosition"			"0"
		"navUp"					"BtnBlogPost"
		"navDown"				"PnlQuickJoin"
		"labelText"				"#L4D360UI_MainMenu_Quit"
		"tooltiptext"			"#L4D360UI_MainMenu_Quit_Tip"
		"style"					"MainMenuButton"
		"command"				"QuitGame"
		"ActivationType"		"1"
	}

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	"LblPlayer1GamerTag"	[$X360]
	{
		"ControlName"			"Label"
		"fieldName"				"LblPlayer1GamerTag"
		"xpos"					"100"
		"ypos"					"r120"
		"wide"					"300"
		"tall"					"16"
		"autoResize"			"0"
		"pinCorner"				"0"
		"visible"				"0"
		"enabled"				"1"
		"tabPosition"			"0"
		"Font"					"DefaultMedium"
		"fgcolor_override"		"125 125 125 255"
		"noshortcutsyntax"		"1"
	}
	
	// either this or the enable
	"LblPlayer2GamerTag"	[$X360]
	{
		"ControlName"			"Label"
		"fieldName"				"LblPlayer2GamerTag"
		"xpos"					"100"
		"ypos"					"r100"
		"wide"					"300"
		"tall"					"16"
		"autoResize"			"0"
		"pinCorner"				"0"
		"visible"				"0"
		"enabled"				"1"
		"tabPosition"			"0"
		"Font"					"DefaultMedium"
		"fgcolor_override"		"125 125 125 255"
		"noshortcutsyntax"		"1"
	}
	
	"LblPlayer2Enable"	[$X360]
	{
		"ControlName"			"Label"
		"fieldName"				"LblPlayer2Enable"
		"xpos"					"100"
		"ypos"					"r100"
		"wide"					"300"
		"tall"					"16"
		"autoResize"			"0"
		"pinCorner"				"0"
		"visible"				"0"
		"enabled"				"1"
		"tabPosition"			"0"
		"labelText"				"#L4D360UI_MainMenu_SignInMessageSsStart2"
		"Font"					"DefaultMedium"
		"fgcolor_override"		"125 125 125 255"
	}
	
	"LblPlayer2DisableIcon"		[$X360]
	{
		"ControlName"			"Label"
		"fieldName"				"LblPlayer2DisableIcon"
		"xpos"					"100"
		"ypos"					"r140"
		"wide"					"30"
		"tall"					"16"
		"autoResize"			"0"
		"pinCorner"				"0"
		"visible"				"0"
		"enabled"				"1"
		"tabPosition"			"0"
		"Font"					"GameUIButtonsMini"
		"labelText"				"#GameUI_Icons_BACK"
	}
	
	"LblPlayer2Disable"		[$X360]
	{
		"ControlName"			"Label"
		"fieldName"				"LblPlayer2Disable"
		"xpos"					"125"
		"ypos"					"r140"
		"wide"					"300"
		"tall"					"16"
		"autoResize"			"0"
		"pinCorner"				"0"
		"visible"				"0"
		"enabled"				"1"
		"tabPosition"			"0"
		"Font"					"DefaultMedium"
		"labelText"				"#L4D360UI_MainMenu_SignInMessageSsDisable"
		"fgcolor_override"		"125 125 125 255"
	}
	
	"BtnGameModes"
	{
		"ControlName"			"GameModes"
		"fieldName"				"BtnGameModes"

		"tabPosition"			"1"
		"navUp"					"BtnBlogPost"			[$X360]
		"navUp"					"PnlQuickJoin"		[$WIN32]
		"navDown"				"BtnChangeGamers"	[$X360]
		"navDown"				"BtnStatsAndAchievements"	[$WIN32]

		"visible"					"0"
		"xpos"					"0"
		"ypos"					"35"	//35
		
		// needed to push the game modes carousel behind the other main menu buttons
		// that overlap into the carousel rect (which needs be oversized due to flyouts)
		// and would not get mouse hittests
		"zpos"					-10				[$WIN32]
		
		"borderimage"			"vgui/menu_mode_border"	

		"leftarrow"				"vgui/arrow_left"	
		"rightarrow"			"vgui/arrow_right"	
		"arrowwidth"			21
		"arrowheight"			21
		"arrowoffsety"			-3
		"rightarrowoffsetx"		7		[$WIN32]

		// main pic, vertically centered
		"picoffsetx"			100
		"picwidth"				153
		"picheight"				153

		// menu text, underneath pic
		"menutitlex"			100
		"menutitley"			16
		// the 360 doesn't clip text, these can be more exact to the fat main menu button
		"menutitlewide"			180	[$X360 && (!$GERMAN && !$FRENCH && !$POLISH)]
		"menutitlewide"			230	[$X360 && ($GERMAN || $FRENCH)]
		"menutitlewide"			240	[$X360 && $POLISH]
		// the pc clips text, these need to be wider for the hint, but then use wideatopen to foreshorten the flyout
		"menutitlewide"			500	[$WIN32]
		"wideatopen"			180	[$WIN32 && (!$GERMAN && !$FRENCH && !$POLISH)]
		"wideatopen"			230	[$WIN32 && ($GERMAN || $FRENCH)]
		"wideatopen"			240	[$WIN32 && $POLISH]
		"menutitletall"			80

		// small pics, vertically centered, to the right of the main pic
		"subpics"				5		[$X360WIDE || $WIN32WIDE]
		"subpics"				3		[!($X360WIDE || $WIN32WIDE)]
		"subpicgap"				6		// between pics
		"subpicoffsetx"			20		[$X360]
		"subpicoffsetx"			50		[$WIN32]
		"subpicoffsety"			-10
		"subpicwidth"			86	
		"subpicheight"			86
		"subpicnamefont"		"Default"
		"hidelabels"			"1"		[!$ENGLISH]			

		"mode" [!$X360GUEST]
		{
			"id"				"BtnCoOp"
			"name"				"#L4D360UI_ModeCaps_COOP"
			"image"				"vgui/menu_mode_campaign"
			"command"			"FlmCampaignFlyout"
			"menutitle"			"#L4D360UI_MainMenu_CoOp"
			"menuhint"			"#L4D360UI_MainMenu_CoOp_Tip"
		}
		
		"mode" [!$X360GUEST]
		{
			"id"				"BtnPlayChallenge"
			"name"				"#L4D360UI_ModeCaps_CHALLENGE"
			"image"				"vgui/menu_mode_mutation"
			"command"			"PlayChallenge"
			"menutitle"			"#L4D360UI_MainMenu_PlayChallenge"
			"menuhint"			" "
			"menuhintdisabled"	"#L4D360UI_MainMenu_DemoVersion"	[$DEMO]
			"custommode"		"1" // mutation
			"enabled"			"0"									[$DEMO]
		}

		"mode" [!$X360GUEST]
		{
			"id"				"BtnPlayRealism"
			"name"				"#L4D360UI_ModeCaps_REALISM"
			"image"				"vgui/menu_mode_realism"
			"command"			"FlmRealismFlyout"
			"menutitle"			"#L4D360UI_MainMenu_Realism"
			"menuhint"			"#L4D360UI_MainMenu_Realism_Tip"
			"menuhintdisabled"	"#L4D360UI_MainMenu_DemoVersion"	[$DEMO]
			"enabled"			"0"									[$DEMO]
		}

		"mode" [!$X360GUEST]
		{
			"id"				"BtnVersus"
			"name"				"#L4D360UI_ModeCaps_VERSUS"
			"image"				"vgui/menu_mode_versus"
			"command"			"VersusSoftLock"
			"menutitle"			"#L4D360UI_MainMenu_Versus"
			"menuhint"			"#L4D360UI_MainMenu_Versus_Tip"
			"menuhintdisabled"	"#L4D360UI_MainMenu_DemoVersion"	[$DEMO]
			"enabled"			"0"									[$DEMO]
		}

		"mode" [!$X360GUEST]
		{
			"id"				"BtnRealismVersus"
			"name"				"#L4D360UI_ModeCaps_mutation12_short"
			"image"				"vgui/menu_mode_realismversus"
			"command"			"FlmRealismVersusFlyout"						
			"menutitle"			"#L4D360UI_ModeCaps_mutation12"
			"menuhint"			"#L4D360UI_MainMenu_PlayChallenge_Tip_mutation12"			
			"menuhintdisabled"	"#L4D360UI_MainMenu_DemoVersion"	[$DEMO]
			"enabled"			"0"									[$DEMO]
		}

		"mode" [!$X360GUEST]
		{
			"id"				"BtnSurvival"
			"name"				"#L4D360UI_ModeCaps_SURVIVAL"
			"image"				"vgui/menu_mode_survival"
			"command"			"SurvivalCheck"
			"menutitle"			"#L4D360UI_MainMenu_Survival"
			"menuhint"			"#L4D360UI_MainMenu_Survival_Tip"
			"menuhintdisabled"	"#L4D360UI_MainMenu_DemoVersion"	[$DEMO]
			"enabled"			"0"									[$DEMO]
		}

		"mode" [!$X360GUEST]
		{
			"id"				"BtnScavenge"
			"name"				"#L4D360UI_ModeCaps_SCAVENGE"
			"image"				"vgui/menu_mode_scavenge"
			"command"			"ScavengeCheck"
			"menutitle"			"#L4D360UI_MainMenu_Scavenge"
			"menuhint"			"#L4D360UI_MainMenu_Scavenge_Tip"
			"menuhintdisabled"	"#L4D360UI_MainMenu_DemoVersion"	[$DEMO]
			"enabled"			"0"									[$DEMO]
		}
		
		"mode" [!$X360SPLITSCREEN]
		{
			"id"				"BtnPlaySolo"
			"name"				"#L4D360UI_ModeCaps_offline_SP"
			"image"				"vgui/menu_mode_singleplayer"
			"command"			"SoloPlay"
			"menutitle"			"#L4D360UI_MainMenu_PlaySolo"
			"menuhint"			"#L4D360UI_MainMenu_PlaySolo_Tip"
		}	
		"mode" [$X360SPLITSCREEN]
		{
			"id"				"BtnPlaySolo"
			"name"				"#L4D360UI_ModeCaps_offline_SS"
			"image"				"vgui/menu_mode_offline_coop"
			"command"			"SoloPlay"
			"menutitle"			"#L4D360UI_MainMenu_PlaySplitscreen"
			"menuhint"			"#L4D360UI_MainMenu_OfflineCoOp_Tip"
		}
	}
	
	"BtnChangeGamers"
	{
		"ControlName"			"L4D360HybridButton"
		"fieldName"				"BtnChangeGamers"
		"xpos"					"100"
		"ypos"					"255"
		"wide"					"180"
		"tall"					"20"
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"0"		[!$X360GUEST]
		"enabled"				"0"		[!$X360GUEST]
		"visible"				"1"		[$X360GUEST]
		"enabled"				"1"		[$X360GUEST]
		"tabPosition"			"0"
		"navUp"					"BtnGameModes"
		"navDown"				"BtnStatsAndAchievements"
		"labelText"				"#L4D360UI_MainMenu_SignIn"
		"tooltiptext"			"#L4D360UI_MainMenu_ChangeGamers_Tip"
		"style"					"MainMenuButton"
		"command"				"ChangeGamers"
		"ActivationType"		"1"
	}
	
	
	"FlmCampaignFlyout"
	{
		"ControlName"			"FlyoutMenu"
		"fieldName"				"FlmCampaignFlyout"
		"visible"				"0"
		"wide"					"0"
		"tall"					"0"
		"zpos"					"3"
		"InitialFocus"			"BtnQuickMatch"
		"ResourceFile"			"resource/UI/L4D360UI/CampaignFlyout.res"
	}

	"FlmRealismFlyout"
	{
		"ControlName"			"FlyoutMenu"
		"fieldName"				"FlmRealismFlyout"
		"visible"				"0"
		"wide"					"0"
		"tall"					"0"
		"zpos"					"3"
		"InitialFocus"			"BtnQuickMatch"
		"ResourceFile"			"resource/UI/L4D360UI/RealismFlyout.res"
	}
	
	"FlmSurvivalFlyout"
	{
		"ControlName"			"FlyoutMenu"
		"fieldName"				"FlmSurvivalFlyout"
		"visible"				"0"
		"wide"					"0"
		"tall"					"0"
		"zpos"					"3"
		"InitialFocus"			"BtnQuickMatch"
		"ResourceFile"			"resource/UI/L4D360UI/SurvivalFlyout.res"
	}

	"FlmScavengeFlyout"
	{
		"ControlName"			"FlyoutMenu"
		"fieldName"				"FlmScavengeFlyout"
		"visible"				"0"
		"wide"					"0"
		"tall"					"0"
		"zpos"					"3"
		"InitialFocus"			"BtnQuickMatch"
		"ResourceFile"			"resource/UI/L4D360UI/ScavengeFlyout.res"
	}

	"FlmVersusFlyout"
	{
		"ControlName"			"FlyoutMenu"
		"fieldName"				"FlmVersusFlyout"
		"visible"				"0"
		"wide"					"0"
		"tall"					"0"
		"zpos"					"3"
		"InitialFocus"			"BtnQuickMatch"
		"ResourceFile"			"resource/UI/L4D360UI/VersusFlyout.res"
	}

	"FlmRealismVersusFlyout"
	{
		"ControlName"			"FlyoutMenu"
		"fieldName"				"FlmRealismVersusFlyout"
		"visible"				"0"
		"wide"					"0"
		"tall"					"0"
		"zpos"					"3"
		"InitialFocus"			"BtnQuickMatch"
		"ResourceFile"			"resource/UI/L4D360UI/RealismVersusFlyout.res"
	}
	
	"FlmMutationCategories"
	{
		"ControlName"			"FlyoutMenu"
		"fieldName"				"FlmMutationCategories"
		"visible"				"0"
		"wide"					"0"
		"tall"					"0"
		"zpos"					"3"
		"InitialFocus"			"BtnQuickMatch"
		"ResourceFile"			"resource/UI/L4D360UI/MutationCategoriesFlyout.res"
	}

	"FlmMutationSolo"
	{
		"ControlName"			"FlyoutMenu"
		"fieldName"				"FlmMutationSolo"
		"visible"				"0"
		"wide"					"0"
		"tall"					"0"
		"zpos"					"3"
		"InitialFocus"			"BtnQuickMatch"
		"ResourceFile"			"resource/UI/L4D360UI/MutationSoloFlyout.res"
	}

	"FlmMutationCoop"
	{
		"ControlName"			"FlyoutMenu"
		"fieldName"				"FlmMutationCoop"
		"visible"				"0"
		"wide"					"0"
		"tall"					"0"
		"zpos"					"3"
		"InitialFocus"			"BtnQuickMatch"
		"ResourceFile"			"resource/UI/L4D360UI/MutationCoopFlyout.res"
	}

	"FlmMutationVersus"
	{
		"ControlName"			"FlyoutMenu"
		"fieldName"				"FlmMutationVersus"
		"visible"				"0"
		"wide"					"0"
		"tall"					"0"
		"zpos"					"3"
		"InitialFocus"			"BtnQuickMatch"
		"ResourceFile"			"resource/UI/L4D360UI/MutationVersusFlyout.res"
	}

	"FlmChallengeFlyout1"
	{
		"ControlName"			"FlyoutMenu"
		"fieldName"				"FlmChallengeFlyout1"
		"visible"				"0"
		"wide"					"0"
		"tall"					"0"
		"zpos"					"3"
		"InitialFocus"			"BtnQuickMatch"
		"ResourceFile"			"resource/UI/L4D360UI/mainmenu_flyout_challenge1.res"
	}

	"FlmChallengeFlyout4"
	{
		"ControlName"			"FlyoutMenu"
		"fieldName"				"FlmChallengeFlyout4"
		"visible"				"0"
		"wide"					"0"
		"tall"					"0"
		"zpos"					"3"
		"InitialFocus"			"BtnQuickMatch"
		"ResourceFile"			"resource/UI/L4D360UI/mainmenu_flyout_challenge4.res"
	}

	"FlmChallengeFlyout8"
	{
		"ControlName"			"FlyoutMenu"
		"fieldName"				"FlmChallengeFlyout8"
		"visible"				"0"
		"wide"					"0"
		"tall"					"0"
		"zpos"					"3"
		"InitialFocus"			"BtnQuickMatch"
		"ResourceFile"			"resource/UI/L4D360UI/mainmenu_flyout_challenge8.res"
	}
		
	"FlmOptionsFlyout"
	{
		"ControlName"			"FlyoutMenu"
		"fieldName"				"FlmOptionsFlyout"
		"visible"				"0"
		"wide"					"0"
		"tall"					"0"
		"zpos"					"3"
		"InitialFocus"			"BtnAudioVideo"	[$X360]
		"InitialFocus"			"BtnVideo"	[$WIN32]
		"ResourceFile"			"resource/UI/L4D360UI/OptionsFlyout.res"
	}
	
	"FlmOptionsGuestFlyout"
	{
		"ControlName"			"FlyoutMenu"
		"fieldName"				"FlmOptionsGuestFlyout"
		"visible"				"0"
		"wide"					"0"
		"tall"					"0"
		"zpos"					"3"
		"InitialFocus"			"BtnAudioVideo"
		"ResourceFile"			"resource/UI/L4D360UI/OptionsGuestFlyout.res"
	}

	"FlmExtrasFlyout_Simple"
	{
		"ControlName"			"FlyoutMenu"
		"fieldName"				"FlmExtrasFlyout_Simple"
		"visible"				"0"
		"wide"					"0"
		"tall"					"0"
		"zpos"					"3"
		"InitialFocus"			"BtnCommentary"
		"ResourceFile"			"resource/UI/L4D360UI/ExtrasFlyout.res"
	}

	"FlmExtrasFlyout_Live"
	{
		"ControlName"			"FlyoutMenu"
		"fieldName"				"FlmExtrasFlyout_Live"
		"visible"				"0"
		"wide"					"0"
		"tall"					"0"
		"zpos"					"3"
		"InitialFocus"			"BtnCommunity"
		"ResourceFile"			"resource/UI/L4D360UI/ExtrasFlyoutLive.res"
	}
}
