"Resource/UI/InGameMainMenu.res"
{
	"InGameMainMenu"
	{
		"ControlName"			"Frame"
		"fieldName"				"InGameMainMenu"
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
		"ypos"		"20"
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
	
	"Custom_BtnReturnToGame"
	{
		"ControlName"			"L4D360HybridButton"
		"fieldName"				"Custom_BtnReturnToGame"
		"xpos"					"20"
		"ypos"					"125"
		"wide"					"120"
		"tall"					"15"	[$WIN32]
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"1"
		"navUp"					"Custom_BtnExitToMainMenu"
		"navDown"				"BtnGoIdle"
		"labelText"				"Resume" //#L4D360UI_InGameMainMenu_ReturnToGame
		"tooltiptext"			"#L4D360UI_InGameMainMenu_ReturnToGame_Tip"
		"style"					"MainMenuButton"
		"command"				"ReturnToGame"
		"ActivationType"		"1"
	}

	"BtnGoIdle"
	{
		"ControlName"			"L4D360HybridButton"
		"fieldName"				"BtnGoIdle"
		"xpos"					"20"
		"ypos"					"150"	[$WIN32]
		"wide"					"120"
		"tall"					"15"	[$WIN32]
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"1"
		"navUp"					"Custom_BtnReturnToGame"
		"navDown"				"BtnCallAVote"
		"labelText"				"AFK"
		"tooltiptext"			"#L4D360UI_InGameMainMenu_GoIdle_Tip"
		"disabled_tooltiptext"	"#L4D360UI_InGameMainMenu_GoIdle_Disabled"
		"style"					"MainMenuButton"
		"command"				"GoIdle"
		"ActivationType"		"1"
	}

	"BtnCallAVote"
	{
		"ControlName"			"L4D360HybridButton"
		"fieldName"				"BtnCallAVote"
		"xpos"					"20"
		"ypos"					"165"	[$WIN32]
		"wide"					"120"
		"tall"					"15"	[$WIN32]
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"0"
		"navUp"					"BtnGoIdle"
		"navDown"				"Custom_BtnVideo"
		"labelText"				"Vote"
		"tooltiptext"			"#L4D360UI_InGameMainMenu_CallAVote_Tip"
		"disabled_tooltiptext" "#L4D360UI_InGameMainMenu_CallAVote_Tip"
		"style"					"MainMenuButton"
		"command" 				"FlmVoteFlyout"
		"ActivationType"		"1"
	}

	"Custom_BtnVideo"
	{
		"ControlName"			"L4D360HybridButton"
		"fieldName"				"Custom_BtnVideo"
		"xpos"					"20"
		"ypos"					"190"	[$WIN32]
		"wide"					"120"
		"tall"					"15"	[$WIN32]
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"0"
		"navUp"					"BtnCallAVote"
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
		"xpos"					"20"
		"ypos"					"205"	[$WIN32]
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
		"xpos"					"20"
		"ypos"					"220"	[$WIN32]
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
		"xpos"					"20"
		"ypos"					"235"	[$WIN32]
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
		"xpos"					"20"
		"ypos"					"250"	[$WIN32]
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
		"xpos"					"20"
		"ypos"					"265"	[$WIN32]
		"wide"					"120"
		"tall"					"15"	[$WIN32]
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"0"
		"navUp"					"Custom_BtnMultiplayer"
		"navDown"				"Custom_BtnExitToMainMenu"
		"tooltiptext"			"#L4D_steamcloud_tip"
		"labelText"				"#L4D360UI_Cloud_Title"
		"style"					"MainMenuButton"
		"command"				"CloudSettings"
		"ActivationType"		"1"
	}

	"Custom_BtnExitToMainMenu"
	{
		"ControlName"			"L4D360HybridButton"
		"fieldName"				"Custom_BtnExitToMainMenu"
		"xpos"					"20"
		"ypos"					"290"	[$WIN32]
		"wide"					"120"
		"tall"					"15"	[$WIN32]
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"0"
		"navUp"					"Custom_BtnCloud"
		"navDown"				"Custom_BtnReturnToGame"
		"labelText"				"Disconnect" //#L4D360UI_InGameMainMenu_ExitToMainMenu
		"tooltiptext"			"#L4D360UI_InGameMainMenu_ExitToMainMenu_Tip"
		"style"					"MainMenuButton"
		"command"				"ExitToMainMenu"
		"ActivationType"		"1"
	}
	
	
	
	
	
	"BtnReturnToGame"
	{
		"ControlName"			"L4D360HybridButton"
		"fieldName"				"BtnReturnToGame"
		"xpos"					"100"
		"ypos"					"135"
		"wide"					"220"	[$WIN32]
		"wide"					"180"	[$X360]
		"tall"					"20"
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"0"
		"enabled"				"1"
		"tabPosition"			"1"
		"navUp"					"BtnExitToMainMenu"
		"navDown"				"BtnGoIdle"
		"labelText"				"#L4D360UI_InGameMainMenu_ReturnToGame"
		"tooltiptext"			"#L4D360UI_InGameMainMenu_ReturnToGame_Tip"
		"style"					"MainMenuButton"
		"command"				"ReturnToGame"
		"ActivationType"		"1"
	}

	"BtnInviteFriends"
	{
		"ControlName"			"L4D360HybridButton"
		"fieldName"				"BtnInviteFriends"
		"xpos"					"100"
		"ypos"					"210"
		"wide"					"220"	[$WIN32]
		"wide"					"180"	[$X360]
		"tall"					"20"
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"0"
		"enabled"				"1"
		"tabPosition"			"0"
		"navUp"					"BtnCallAVote"
		"navDown"				"BtnLeaderboard"
		"labelText"				"#L4D360UI_Lobby_InviteFriends"		[$WIN32]
		"tooltiptext"			"#L4D360UI_Lobby_InviteFriends_Tip"	[$WIN32]
		"labelText"				"#L4D360UI_InviteUIOptions"			[$X360]
		"tooltiptext"			"#L4D360UI_InviteUIOptions_Tip"		[$X360]
		"style"					"MainMenuButton"
		"ActivationType"		"1"
		"command"				"InviteUI_Steam"		[$WIN32]
		"command"				"FlmInviteFriends"		[$X360]
	}
	"FlmInviteFriends" [$X360]
	{
		"ControlName"			"FlyoutMenu"
		"fieldName"				"FlmInviteFriends"
		"visible"				"0"
		"wide"					"0"
		"tall"					"0"
		"zpos"					"3"
		"InitialFocus"			"BtnPlayers"
		"ResourceFile"			"resource/UI/L4D360UI/DropDownInviteLive.res"
	}
	
	"BtnLeaderboard"
	{
		"ControlName"			"L4D360HybridButton"
		"fieldName"				"BtnLeaderboard"
		"xpos"					"100"
		"ypos"					"235"
		"wide"					"220"	[$WIN32]
		"wide"					"180"	[$X360]
		"tall"					"20"	
		"autoResize"			"1"		
		"pinCorner"				"0"
		"visible"				"0"
		"enabled"				"1"
		"tabPosition"			"0"
		"navUp"					"BtnInviteFriends"
		"navDown"				"BtnStatsAndAchievements"
		"labelText"				"#L4D360UI_Leaderboard_Title"
		"tooltiptext"			"#L4D360UI_MainMenu_SurvivalLeaderboards_Tip"
		"style"					"MainMenuButton"
		"command"				"Leaderboards_"
		"ActivationType"		"1"
	}
	
	"BtnStatsAndAchievements"
	{
		"ControlName"			"L4D360HybridButton"
		"fieldName"				"BtnStatsAndAchievements"
		"xpos"					"100"
		"ypos"					"260"
		"wide"					"220"	[$WIN32]
		"wide"					"180"	[$X360]
		"tall"					"20"
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"0"
		"enabled"				"1"		[!$X360GUEST]
		"enabled"				"0"		[$X360GUEST]
		"tabPosition"			"0"
		"navUp"					"BtnLeaderboard"
		"navDown"				"BtnOptions"
		"labelText"				"#L4D360UI_MainMenu_StatsAndAchievements"
		"tooltiptext"			"#L4D360UI_MainMenu_PCStatsAndAchievements_Tip"	[$WIN32]
		"tooltiptext"			"#L4D360UI_MainMenu_StatsAndAchievements_Tip"	[$X360]
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
		"ypos"					"285"
		"wide"					"220"	[$WIN32]
		"wide"					"180"	[$X360]
		"tall"					"20"
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"0"
		"enabled"				"1"
		"tabPosition"			"0"
		"navUp"					"BtnStatsAndAchievements"
		"navDown"				"BtnExitToMainMenu"
		"labelText"				"#L4D360UI_MainMenu_Options"
		"tooltiptext"			"#L4D360UI_MainMenu_Options_Tip"
		"style"					"MainMenuButton"
		"command"				"FlmOptionsFlyout"
		"ActivationType"		"1"
	}

	"BtnExitToMainMenu"
	{
		"ControlName"			"L4D360HybridButton"
		"fieldName"				"BtnExitToMainMenu"
		"xpos"					"100"
		"ypos"					"322"
		"wide"					"220"	[$WIN32]
		"wide"					"180"	[$X360]
		"tall"					"20"
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"0"
		"enabled"				"1"
		"tabPosition"			"0"
		"navUp"					"BtnOptions"
		"navDown"				"BtnReturnToGame"
		"labelText"				"#L4D360UI_InGameMainMenu_ExitToMainMenu"
		"tooltiptext"			"#L4D360UI_InGameMainMenu_ExitToMainMenu_Tip"
		"style"					"MainMenuButton"
		"command"				"ExitToMainMenu"
		"ActivationType"		"1"
	}

	"FlmOptionsFlyout"
	{
		"ControlName"			"FlyoutMenu"
		"fieldName"				"FlmOptionsFlyout"
		"visible"				"0"
		"wide"					"0"
		"tall"					"0"
		"zpos"					"3"
		"InitialFocus"			"BtnVideo" [$WIN32]
		"InitialFocus"			"BtnAudioVideo" [$X360]
		"ResourceFile"			"resource/UI/L4D360UI/OptionsFlyout.res"		[$WIN32]
		"ResourceFile"			"resource/UI/L4D360UI/OptionsFlyoutIngame.res"	[$X360]
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

	"FlmVoteFlyout"
	{
		"ControlName"			"FlyoutMenu"
		"fieldName"				"FlmVoteFlyout"
		"visible"				"0"
		"wide"					"0"
		"tall"					"0"
		"zpos"					"3"
		"InitialFocus"			"BtnReturnToLobby"
		"ResourceFile"			"resource/UI/L4D360UI/InGameVoteFlyout.res"
	}
	
	"FlmVoteFlyoutVersus"
	{
		"ControlName"		"FlyoutMenu"
		"fieldName"			"FlmVoteFlyoutVersus"
		"visible"			"0"
		"wide"				"0"
		"tall"				"0"
		"zpos"				"3"
		"InitialFocus"		"BtnReturnToLobby"
		"ResourceFile"		"resource/UI/L4D360UI/InGameVoteFlyoutVersus.res"
	}
	
	"FlmVoteFlyoutSurvival"
	{
		"ControlName"		"FlyoutMenu"
		"fieldName"			"FlmVoteFlyoutSurvival"
		"visible"			"0"
		"wide"				"0"
		"tall"				"0"
		"zpos"				"3"
		"InitialFocus"		"BtnReturnToLobby"
		"ResourceFile"		"resource/UI/L4D360UI/InGameVoteFlyoutSurvival.res"
	}
}
