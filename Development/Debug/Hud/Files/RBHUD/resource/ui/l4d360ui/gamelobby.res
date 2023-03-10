"Resource/UI/GameLobby.res"
{
	"GameLobby"
	{
		"ControlName"			"Frame"
		"fieldName"				"GameLobby"
		"xpos"					"0"
		"ypos"					"0"
		"wide"					"f0"
		"tall"					"440"		[$WIN32]
		"tall"					"380"		[$X360]
		"autoResize"			"0"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"0"
		"title_xpos"			"241"		[$WIN32]
	}

	"ImgBackground"
	{
		"ControlName"			"L4DMenuBackground"
		"fieldName"			"ImgBackground"
		"xpos"					"c-250"
		"ypos"					"90"
		"zpos"					"-1"
		"wide"					"280"
		"tall"					"150"
		"autoResize"			"0"
		"pinCorner"			"0"
		"visible"			"1"
		"enabled"			"1"
		"tabPosition"			"0"
		"fillColor"			"TransparentBlack"
	}

	"Background_Header"
	{
		"ControlName"	"Panel"
		"fieldName"		"Background_Header"
		"xpos"				"0"
		"ypos"				"20"
		"wide"			"f0"
		"tall"			"40"	//22
		"visible"		"1"
		"enabled"		"1"
		"zpos"			"-150033"
		"bgcolor_override"	"TransparentBlack"
	}

	"Background_ButtonSave"
	{
		"ControlName"	"Panel"
		"fieldName"		"Background_ButtonSave"
		"xpos"				"0"
		"ypos"				"65"
		"wide"			"f0"
		"tall"			"20"	//22
		"visible"		"1"
		"enabled"		"1"
		"zpos"			"-1500"
		"bgcolor_override"	"TransparentBlack"
	}

	"Background_Players"
	{
		"ControlName"	"Panel"
		"fieldName"		"Background_ButtonSave"
		"xpos"					"c35"
		"ypos"					"90"
		"zpos"					"-1"
		"wide"					"200"
		"tall"					"265"
		"visible"		"1"
		"enabled"		"1"
		"zpos"			"-1500"
		"bgcolor_override"	"TransparentBlack"
	}

	"Background_Chat"
	{
		"ControlName"	"Panel"
		"fieldName"		"Background_ButtonSave"
		"xpos"					"c-250"
		"ypos"					"245"
		"zpos"					"-1"
		"wide"					"280"
		"tall"					"110"
		"visible"		"1"
		"enabled"		"1"
		"zpos"			"-1500"
		"bgcolor_override"	"TransparentBlack"
	}

	"WorkingAnim"
	{
		"ControlName"			"ImagePanel"
		"fieldName"				"WorkingAnim"
		"xpos"					"c214"		[$WIN32]
		"xpos"					"r128"		[$X360]
		"ypos"					"27"
		"zpos"					"2"
		"wide"					"32"
		"tall"					"32"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"0"
		"scaleImage"			"1"
		"image"					"common/l4d_spinner"
	}

	"GplSurvivors"
	{
		"ControlName"			"GenericListPanel"
		"fieldName"				"GplSurvivors"
		"xpos"					"c32"
		"ypos"					"90"
		"zpos"					"2"
		"wide"					"200"
		"tall"					"f0"
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"0"
		"navLeft"				"BtnStartGame"
		"bcolor_override"		"blank"
		"NoDrawPanel"			"1"
		"arrowsVisible"			"0"
	}

	"LblNoLiveWarning"
	{
		"ControlName"			"Label"
		"fieldName"				"LblNoLiveWarning"
		"xpos"					"c107"
		"ypos"					"c50"
		"zpos"					"2"
		"wide"					"180"
		"tall"					"60"
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"0"
		"enabled"				"1"
		"tabPosition"			"0"
		"labelText"				"#L4D360UI_Lobby_Leaderboards_LIVE_Required"
		"Font"					"DefaultMedium" [!$ENGLISH]
		"textAlignment"			"center"
		"wrap"					"1"
		"fgcolor_override"		"TextYellow"
		"noshortcutsyntax"		"1"
	}

	"FlmPlayerFlyout"
	{
		"ControlName"			"FlyoutMenu"
		"fieldName"				"FlmPlayerFlyout"
		"visible"				"0"
		"wide"					"0"
		"tall"					"0"
		"zpos"					"3"
		"InitialFocus"			"BtnSendMessage"
		"ResourceFile"			"resource/UI/L4D360UI/DropDownLobbySteamPlayer.res"
	}

	"FlmPlayerFlyoutLeader"
	{
		"ControlName"			"FlyoutMenu"
		"fieldName"				"FlmPlayerFlyoutLeader"
		"visible"				"0"
		"wide"					"0"
		"tall"					"0"
		"zpos"					"3"
		"InitialFocus"			"BtnSendMessage"
		"ResourceFile"			"resource/UI/L4D360UI/DropDownLobbySteamPlayerLeader.res"
	}

	"LblLeaderLine"
	{
		"ControlName"			"Label"
		"fieldName"				"LblLeaderLine"
		"xpos"					"c-110"
		"ypos"					"36"
		"zpos"					"2"
		"wide"					"275"
		"tall"					"32"
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"0"
		"labelText"				""
		"Font"					"DefaultMedium" [$ENGLISH]
		"fgcolor_override"		"255 255 255 255"
		"noshortcutsyntax"		"1"
	}

	"ImgLevelImage"
	{
		"ControlName"			"ImagePanel"
		"fieldName"				"ImgLevelImage"
		"xpos"					"c-238"
		"ypos"					"102"
		"zpos"					"2"
		"wide"					"125"
		"tall"					"65"
		"scaleImage"			"1"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"0"
		"image"					"maps/any"
		"scaleImage"			"1"
	}
	"ImgLevelImageFrame"
	{
		"ControlName"			"ImagePanel"
		"fieldName"				"ImgLevelImageFrame"
		"xpos"					"c-250" [$WIN32 && $ENGLISH]
		"xpos"					"c-270" [$WIN32 && !$ENGLISH]
		"ypos"					"125"
		"xpos"					"c-260" [$X360]
		"wide"					"158"
		"tall"					"79"
		"scaleImage"			"1"
		"pinCorner"				"0"
		"visible"				"0"
		"enabled"				"1"
		"tabPosition"			"0"
		"image"					"campaignFrame"
		"scaleImage"			"1"
	}

	"LblSummaryLine1"
	{
		"ControlName"			"Label"
		"fieldName"				"LblSummaryLine1"
		"xpos"					"c-105"
		"ypos"					"100"
		"zpos"					"2"
		"wide"					"240"
		"tall"					"32"
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"0"
		"labelText"				""
		"Font"					"DefaultMedium"
		"textAlignment"			"north-west"
		"wrap"					"1"
		"fgcolor_override"		"TextYellow"
	}

	"LblSummaryLine2"
	{
		"ControlName"			"Label"
		"fieldName"				"LblSummaryLine2"
		"xpos"					"c-105"
		"ypos"					"115"
		"zpos"					"2"
		"wide"					"240"
		"tall"					"32"
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"0"
		"labelText"				""
		"Font"					"DefaultMedium"
		"textAlignment"			"north-west"
		"fgcolor_override"		"TextYellow"
	}

	"LblSummaryLine3"
	{
		"ControlName"			"Label"
		"fieldName"				"LblSummaryLine3"
		"xpos"					"c-105"
		"ypos"					"130"
		"zpos"					"2"
		"wide"					"240"
		"tall"					"32"
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"0"
		"labelText"				""
		"Font"					"DefaultMedium"
		"textAlignment"			"north-west"
		"fgcolor_override"		"TextYellow"
	}

	"LblSummaryLine4"
	{
		"ControlName"			"Label"
		"fieldName"				"LblSummaryLine4"
		"xpos"					"c-105"
		"ypos"					"145"
		"zpos"					"2"
		"wide"					"240"
		"tall"					"32"
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"0"
		"labelText"				""
		"Font"					"DefaultMedium"
		"textAlignment"			"north-west"
		"fgcolor_override"		"TextYellow"
	}

	"LblSummaryLine5"
	{
		"ControlName"			"Label"
		"fieldName"				"LblSummaryLine5"
		"xpos"					"c-105"
		"ypos"					"160"
		"zpos"					"2"
		"wide"					"240"
		"tall"					"32"
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"0"
		"labelText"				""
		"Font"					"DefaultMedium"
		"textAlignment"			"north-west"
		"fgcolor_override"		"TextYellow"
	}

	"BtnChangeGameSettings"
	{
		"ControlName"			"L4D360HybridButton"
		"fieldName"				"BtnChangeGameSettings"
		"command"				"ChangeGameSettings"
		"xpos"					"c-240"
		"ypos"					"175"
		"wide"					"180"
		"tall"					"15"
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"0"
		"navUp"					"BtnLeaveLobby"			[$WIN32]
		"navUp"					"BtnCancelDedicatedSearch"	[$X360]
		"navDown"				"DrpCharacter"
		"navRight"				"GplSurvivors"
		"tooltiptext"			"#L4D360UI_Lobby_Change_GameSettings_Tip"
		"disabled_tooltiptext"	"#L4D360UI_Lobby_Change_GameSettings_DisabledTip"
		"labelText"				"#L4D360UI_Lobby_Change_GameSettings"
		"style"					"MainMenuButton"
	}

	"DrpCharacter"
	{
		"ControlName"			"DropDownMenu"
		"fieldName"				"DrpCharacter"
		"xpos"					"c-240"
		"ypos"					"190"
		"wide"					"180"
		"tall"					"15"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"0"
		"navUp"					"BtnChangeGameSettings"
		"navDown"				"DrpVersusCharacter"
		"navRight"				"GplSurvivors"

		//button and label
		"BtnDropButton"
		{
			"ControlName"			"L4D360HybridButton"
			"fieldName"				"BtnDropButton"
			"xpos"					"0"
			"ypos"					"0"
			"wide"					"180"	[$WIN32 && $ENGLISH]
			"wide"					"260"	[$WIN32 && !$ENGLISH]
			"tall"					"15"	[$WIN32]
			"wide"					"180"	[$X360]
			"tall"					"20"	[$X360]
			"autoResize"			"1"
			"pinCorner"				"0"
			"visible"				"1"
			"enabled"				"1"
			"tabPosition"			"0"
			"labelText"				"#L4D360UI_Lobby_Character"
			"tooltiptext"			"#L4D360UI_GameSettings_Tooltip_Character"
			"disabled_tooltiptext"	"#L4D360UI_GameSettings_Tooltip_Character_Disabled"
			"style"					"DropDownButton"
			"command"				"FlmCharacterFlyout"
			"FocusButtonWidth"		"230"
			"OpenButtonWidth"		"230"
			"ActivationType"		"1" [$X360]
		}
	}

	"FlmCharacterFlyout"
	{
		"ControlName"			"FlyoutMenu"
		"fieldName"				"FlmCharacterFlyout"
		"visible"				"0"
		"wide"					"0"
		"tall"					"0"
		"zpos"					"3"
		"InitialFocus"			"BtnRandom"
		"ResourceFile"			"resource/UI/L4D360UI/DropDownCoopCharacters.res"
	}


	"DrpVersusCharacter"
	{
		"ControlName"			"DropDownMenu"
		"fieldName"				"DrpVersusCharacter"
		"xpos"					"c-240"
		"ypos"					"190"
		"wide"					"180"
		"tall"					"15"
		"visible"				"0"
		"enabled"				"1"
		"tabPosition"			"0"
		"navUp"					"DrpCharacter"
		"navDown"				"DrpGameAccess"
		"navRight"				"GplSurvivors"

		//button and label
		"BtnDropButton"
		{
			"ControlName"			"L4D360HybridButton"
			"fieldName"				"BtnDropButton"
			"xpos"					"0"
			"ypos"					"0"
			"wide"					"180"	[$WIN32 && $ENGLISH]
			"wide"					"260"	[$WIN32 && !$ENGLISH]
			"tall"					"15"	[$WIN32]
			"wide"					"180"	[$X360]
			"tall"					"20"	[$X360]
			"autoResize"			"1"
			"pinCorner"				"0"
			"visible"				"1"
			"enabled"				"1"
			"tabPosition"			"0"
			"labelText"				"#L4D360UI_Lobby_Character"
			"tooltiptext"			"#L4D360UI_GameSettings_Tooltip_Character"
			"disabled_tooltiptext"	"#L4D360UI_GameSettings_Tooltip_Character_Disabled"
			"style"					"DropDownButton"
			"command"				"FlmVersusCharacterFlyout"
			"FocusButtonWidth"		"230"
			"OpenButtonWidth"		"230"
			"ActivationType"		"1" [$X360]
		}
	}

	"FlmVersusCharacterFlyout"
	{
		"ControlName"			"FlyoutMenu"
		"fieldName"				"FlmVersusCharacterFlyout"
		"visible"				"0"
		"wide"					"0"
		"tall"					"0"
		"zpos"					"3"
		"InitialFocus"			"BtnRandom"
		"ResourceFile"			"resource/UI/L4D360UI/DropDownVersusCharacters.res"
	}


	"DrpGameAccess"
	{
		"ControlName"			"DropDownMenu"
		"fieldName"				"DrpGameAccess"
		"xpos"					"c-240"
		"ypos"					"205"
		"wide"					"180"
		"tall"					"15"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"0"
		"navUp"					"DrpVersusCharacter"
		"navDown"				"BtnStartGame" [$X360]
		"navDown"				"BtnInviteFriends" [$WIN32]
		"navRight"				"GplSurvivors"

		//button and label
		"BtnDropButton"
		{
			"ControlName"			"L4D360HybridButton"
			"fieldName"				"BtnDropButton"
			"xpos"					"0"
			"ypos"					"0"
			"wide"					"180"	[$WIN32 && $ENGLISH]
			"wide"					"260"	[$WIN32 && !$ENGLISH]
			"tall"					"15"	[$WIN32]
			"wide"					"180"	[$X360]
			"tall"					"20"	[$X360]
			"autoResize"			"1"
			"pinCorner"				"0"
			"visible"				"1"
			"enabled"				"1"
			"tabPosition"			"0"
			"labelText"				"#L4D360UI_Lobby_Change_GameAccess"
			"tooltiptext"			"#L4D360UI_Lobby_Change_GameAccess_Tip"
			"disabled_tooltiptext"	"#L4D360UI_Lobby_Change_GameAccess_Disabled_Tip"
			"style"					"DropDownButton"
			"command"				"FlmGameAccess"
			"FocusButtonWidth"		"230"
			"OpenButtonWidth"		"230"
			"ActivationType"		"1" [$X360]
		}
	}

	"BtnInviteFriends"
	{
		"ControlName"			"L4D360HybridButton"
		"fieldName"				"BtnInviteFriends"
		"command"				"InviteUI_Steam"
		"xpos"					"c-240"
		"ypos"					"220"
		"wide"					"180"
		"tall"					"15"
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"1"			[$WIN32]
		"visible"				"0"			[$X360]
		"enabled"				"1"
		"tabPosition"			"0"
		"navUp"					"DrpGameAccess"
		"navDown"				"ChatInputLine"
		"navRight"				"GplSurvivors"
		"tooltiptext"			"#L4D360UI_Lobby_InviteFriends_Tip"
		"disabled_tooltiptext"	"#L4D360UI_InGameMainMenu_InviteAFriend_Disabled"
		"labelText"				"#L4D360UI_Lobby_InviteFriends"
		"style"					"MainMenuButton"
	}

	"ChatInputLine" [$WIN32]
	{
		"ControlName"			"EditablePanel"
		"fieldName" 			"ChatInputLine"
		"visible" 				"1"
		"enabled" 				"1"
		"xpos"		       	"c-240"
		"ypos"			"338"
		"zpos"			"2"
		"wide"	 		"260"
		"tall"	 		"10"
		"PaintBackgroundType"	"0"
		"bgcolor_override"     	"blank"
		"navUp"					"BtnInviteFriends"
		"navDown"				"BtnStartGame"
	}

	"BtnStartGame"
	{
		"ControlName"			"L4D360HybridButton"
		"fieldName"				"BtnStartGame"
		"command"				"StartGame"
		"xpos"					"c35"
		"ypos"					"68"
		"wide"					"100"
		"tall"					"15"
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"0"
		"navUp"					"DrpGameAccess" [$X360]
		"navUp"					"ChatInputLine" [$WIN32]
		"navDown"				"BtnCancelDedicatedSearch" [$X360]
		"navDown"				"BtnCancelDedicatedSearch" [$WIN32]
		"navLeft"				"BtnCancelDedicatedSearch"
		"navRight"				"GplSurvivors"
		"tooltiptext"			"#L4D360UI_Lobby_StartMatchmacking_Tip"
		"disabled_tooltiptext"	"#L4D360UI_Lobby_StartMatchmacking_Disabled_Tip"
		"labelText"				"#L4D360UI_Lobby_StartMatchmacking"
		"style"					"MainMenuButton"
		"fgcolor_override"		"255 12 12 255" [$WIN32]
	}

	"BtnCancelDedicatedSearch"
	{
		"ControlName"			"L4D360HybridButton"
		"fieldName"				"BtnCancelDedicatedSearch"
		"command"				"CancelStartGame"
		"xpos"					"c35"
		"ypos"					"68"
		"wide"					"100"
		"tall"					"15"
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"0"
		"enabled"				"1"
		"tabPosition"			"0"
		"navUp"					"BtnStartGame"
		"navDown"				"BtnRequestStart"
		"navRight"				"GplSurvivors"
		"navLeft"				"BtnRequestStart"
		"tooltiptext"			"#L4D360UI_Lobby_CancelMatchmacking_Tip"
		"labelText"				"#L4D360UI_Lobby_CancelMatchmacking"
		"style"					"MainMenuButton"
	}

	"BtnRequestStart"
	{
		"ControlName"			"L4D360HybridButton"
		"fieldName"				"BtnRequestStart"
		"command"				"StartGame"
		"xpos"					"c35"
		"ypos"					"68"
		"wide"					"100"
		"tall"					"15"
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"0"
		"enabled"				"1"
		"tabPosition"			"0"
		"navUp"					"BtnCancelDedicatedSearch"
		"navDown"				"BtnCancelRequestStart"
		"navRight"				"GplSurvivors"
		"navLeft"				"BtnCancelRequestStart"
		"tooltiptext"			"#L4D360UI_Lobby_RequestStartMatchmacking_Tip"
		"labelText"				"#L4D360UI_Lobby_RequestStartMatchmacking"
		"style"					"MainMenuButton"
	}

	"BtnCancelRequestStart"
	{
		"ControlName"			"L4D360HybridButton"
		"fieldName"				"BtnCancelRequestStart"
		"command"				"CancelStartGame"
		"xpos"					"c35"
		"ypos"					"68"
		"wide"					"100"
		"tall"					"15"
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"0"
		"enabled"				"1"
		"tabPosition"			"0"
		"navUp"					"BtnRequestStart"
		"navDown"				"BtnVoiceButton" [$WIN32]
		"navDown"				"BtnChangeGameSettings" [$X360]
		"navRight"				"GplSurvivors"
		"tooltiptext"			"#L4D360UI_Lobby_CancelRequestStartMatchmacking_Tip"
		"labelText"				"#L4D360UI_Lobby_CancelRequestStartMatchmacking"
		"style"					"MainMenuButton"
	}

	"BtnVoiceButton" [$WIN32]
	{
		"ControlName"		"L4D360HybridButton"
		"fieldName"			"BtnVoiceButton"
		"command"			"ToggleVoice"
		"xpos"					"c-110"
		"ypos"					"68"
		"wide"					"100"
		"tall"					"15"
		"autoResize"		"1"
		"pinCorner"			"0"
		"visible"			"1"
		"enabled"			"1"
		"tabPosition"		"0"
 		"tooltiptext"		"#L4D360UI_Lobby_StartVoiceChat_Tip"
		"disabled_tooltiptext"	"#L4D360UI_Lobby_StartVoiceChat_Disabled_Tip"
		"labelText"			"#L4D360UI_Lobby_StartVoiceChat"
		"navUp"				"BtnRequestStart"
		"navDown"			"BtnLeaveLobby"
		"style"				"MainMenuButton"
	}
	
	"BtnLeaveLobby" [$WIN32]
	{
		"ControlName"			"L4D360HybridButton"
		"fieldName"				"BtnLeaveLobby"
		"command"				"LeaveLobby"
		"xpos"					"c-240"
		"ypos"					"68"
		"zpos"					"0"
		"wide"					"100"
		"tall"					"15"
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"0"
		"navUp"					"BtnVoiceButton"
		"navDown"				"BtnChangeGameSettings"
		"navRight"				"GplSurvivors"
		"tooltiptext"			"#L4D360UI_Lobby_LeaveLobby_Tip"
		"labelText"				"#L4D360UI_Lobby_LeaveLobby"
		"style"					"MainMenuButton"
	}

	"ChatBackground" [$WIN32]
	{
		"ControlName"			"ImagePanel"
		"fieldName"				"Divider1"
		"xpos"				  	"c-240" [$ENGLISH]
		"xpos"					"c-260" [!$ENGLISH]
		"ypos"					"326"
		"zpos"					"1"
		"wide"	 				"261"	[$ENGLISH]
		"wide"	 				"271"	[!$ENGLISH]
		"tall"	 				"70"
		"autoResize"			"0"
		"pinCorner"				"0"
		"visible"				"0"
		"enabled"				"1"
		"tabPosition"			"0"
		"image"					"divider_gradient"
		"scaleImage"			"1"
	}

	"LobbyChatHistory" [$WIN32]
	{
		"ControlName"			"RichText"
		"fieldName"				"LobbyChatHistory"
		"xpos"		       	"c-240"
		"ypos"			"250"
		"zpos"			"2"
		"wide"	 		"260"
		"tall"			"87"
		"wrap"					"1"
		"autoResize"			"1"
		"pinCorner"				"1"
		"visible"				"1"
		"enabled"				"1"
		"labelText"				""
		"textAlignment"			"south-west"
		"font"					"ChatFont"
		"maxchars"				"-1"
		"bgcolor_override"     	"blank"
	}

















	"IconSettings"
	{
		"ControlName"			"ImagePanel"
		"fieldName"				"IconSettings"
		"xpos"					"c-255"		[$WIN32 && $ENGLISH]
		"xpos"					"c-275"		[$WIN32 && !$ENGLISH]
		"ypos"					"206"		[$WIN32]
		"wide"					"15"		[$WIN32]
		"tall"					"15"		[$WIN32]
		"xpos"					"c-285"		[$X360]
		"ypos"					"210"		[$X360]
		"wide"					"20"		[$X360]
		"tall"					"20"		[$X360]
		"scaleImage"			"1"
		"pinCorner"				"0"
		"visible"				"0"
		"enabled"				"1"
		"tabPosition"			"0"
		"image"					"icon_button_settings"
		"scaleImage"			"1"
	}
	"IconCharacter"
	{
		"ControlName"			"ImagePanel"
		"fieldName"				"IconCharacter"
		"xpos"					"c-255"		[$WIN32 && $ENGLISH]
		"xpos"					"c-275"		[$WIN32 && !$ENGLISH]
		"ypos"					"226"		[$WIN32]
		"wide"					"15"		[$WIN32]
		"tall"					"15"		[$WIN32]
		"xpos"					"c-285"		[$X360]
		"ypos"					"235"		[$X360]
		"wide"					"20"		[$X360]
		"tall"					"20"		[$X360]
		"scaleImage"			"1"
		"pinCorner"				"0"
		"visible"				"0"
		"enabled"				"1"
		"tabPosition"			"0"
		"image"					"icon_button_character"
		"scaleImage"			"1"
	}
	    "IconCharacterVersus"
	{
		"ControlName"			"ImagePanel"
		"fieldName"				"IconCharacterVersus"
		"xpos"					"c-2559999"		[$WIN32 && $ENGLISH]
		"xpos"					"c-275"		[$WIN32 && !$ENGLISH]
		"ypos"					"226"		[$WIN32]
		"wide"					"15"		[$WIN32]
		"tall"					"15"		[$WIN32]
		"xpos"					"c-285"		[$X360]
		"ypos"					"235"		[$X360]
		"wide"					"20"		[$X360]
		"tall"					"20"		[$X360]
		"scaleImage"			"1"
		"pinCorner"				"0"
		"visible"				"0"
		"enabled"				"0"
		"tabPosition"			"0"
		"image"					"icon_button_character"
		"scaleImage"			"1"
	}

		"IconFriends"
	{
		"ControlName"			"ImagePanel"
		"fieldName"				"IconFriends"
		"xpos"					"c-255"		[$WIN32 && $ENGLISH]
		"xpos"					"c-275"		[$WIN32 && !$ENGLISH]
		"ypos"					"246"		[$WIN32]
		"wide"					"15"		[$WIN32]
		"tall"					"15"		[$WIN32]
		"xpos"					"c-285"		[$X360]
		"ypos"					"260"		[$X360]
		"wide"					"20"		[$X360]
		"tall"					"20"		[$X360]
		"scaleImage"			"1"
		"pinCorner"				"0"
		"visible"				"0"
		"enabled"				"1"
		"tabPosition"			"0"
		"image"					"icon_button_friends"
		"scaleImage"			"1"
	}

	    "IconPermissions"
	{
		"ControlName"			"ImagePanel"
		"fieldName"				"IconPermissions"
		"xpos"					"c-255"		[$WIN32 && $ENGLISH]
		"xpos"					"c-275"		[$WIN32 && !$ENGLISH]
		"ypos"					"266"		[$WIN32]
		"wide"					"15"		[$WIN32]
		"tall"					"15"		[$WIN32]
		"xpos"					"c-285"		[$X360]
		"ypos"					"285"		[$X360]
		"wide"					"20"		[$X360]
		"tall"					"20"		[$X360]
		"scaleImage"			"1"
		"pinCorner"				"0"
		"visible"				"0"
		"enabled"				"1"
		"tabPosition"			"0"
		"image"					"icon_button_permissions"
		"scaleImage"			"1"
	}

	   "IconForwardArrow"
	{
		"ControlName"			"ImagePanel"
		"fieldName"				"IconForwardArrow"
		"xpos"					"c-255"		[$WIN32 && $ENGLISH]
		"xpos"					"c-275"		[$WIN32 && !$ENGLISH]
		"ypos"					"306"		[$WIN32]
		"wide"					"15"		[$WIN32]
		"tall"					"15"		[$WIN32]
		"xpos"					"c-285"		[$X360]
		"ypos"					"310"		[$X360]
		"wide"					"20"		[$X360]
		"tall"					"20"		[$X360]
		"scaleImage"			"1"
		"pinCorner"				"0"
		"visible"				"0"
		"enabled"				"1"
		"tabPosition"			"0"
		"image"					"icon_button_arrow_right"
		"scaleImage"			"1"
	}

	"IconBackArrow" [$WIN32]
	{
		"ControlName"			"ImagePanel"
		"fieldName"				"IconBackArrow"
		"xpos"					"c-255999"		[$ENGLISH]
		"xpos"					"c-275"		[!$ENGLISH]
		"ypos"					"306"
		"wide"					"15"
		"tall"					"15"
		"scaleImage"			"1"
		"pinCorner"				"0"
		"visible"				"0"
		"enabled"				"0"
		"tabPosition"			"0"
		"image"					"icon_button_arrow_left"
		"scaleImage"			"1"
	}

	"IconBackArrow2" [$WIN32]
	{
		"ControlName"			"ImagePanel"
		"fieldName"				"IconBackArrow2"
		"xpos"					"c-255"		[$ENGLISH]
		"xpos"					"c-275"		[!$ENGLISH]
		"ypos"					"286"
		"wide"					"15"
		"tall"					"15"
		"scaleImage"			"1"
		"pinCorner"				"0"
		"visible"				"0"
		"enabled"				"1"
		"tabPosition"			"0"
		"image"					"icon_button_arrow_left"
		"scaleImage"			"1"
	}

	"DrpInviteFriends"
	{
		"ControlName"			"DropDownMenu"
		"fieldName"				"DrpInviteFriends"
		"xpos"					"c-240"		[$WIN32 && $ENGLISH]
		"xpos"					"c-260"		[$WIN32 && !$ENGLISH]
		"ypos"					"246"		[$WIN32]
		"wide"					"180"		[$WIN32 && $ENGLISH]
		"wide"					"260"		[$WIN32 && !$ENGLISH]
		"tall"					"15"		[$WIN32]
		"xpos"					"c-260"		[$X360]
		"ypos"					"260"		[$X360]
		"wide"					"180"		[$X360]
		"tall"					"20"		[$X360]
		"visible"				"0"			[$WIN32]
		"visible"				"1"			[$X360]
		"enabled"				"1"
		"tabPosition"			"0"
		"navUp"					"BtnInviteFriends"
		"navDown"				"DrpGameAccess"
		"navRight"				"GplSurvivors"

		//button and label
		"BtnDropButton"
		{
			"ControlName"			"L4D360HybridButton"
			"fieldName"				"BtnDropButton"
			"xpos"					"0"
			"ypos"					"0"
			"wide"					"180"	[$WIN32 && $ENGLISH]
			"wide"					"260"	[$WIN32 && !$ENGLISH]
			"tall"					"15"	[$WIN32]
			"wide"					"180"	[$X360]
			"tall"					"20"	[$X360]
			"autoResize"			"1"
			"pinCorner"				"0"
			"visible"				"1"
			"enabled"				"1"
			"tabPosition"			"0"
			"tooltiptext"			"#L4D360UI_InviteUIOptions_Tip"
			"disabled_tooltiptext"	"#L4D360UI_InviteUIOptions_Tip_Disabled"
			"labelText"				"#L4D360UI_InviteUIOptions"
			"style"					"DropDownButton"
			"command"				"FlmInviteFriends"
			"FocusButtonWidth"		"230"
			"OpenButtonWidth"		"230"
			"ActivationType"		"1" [$X360]
		}
	}
	"FlmInviteFriends"
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

	    "IconButtonVoice" [$WIN32]
	{
		"ControlName"			"ImagePanel"
		"fieldName"				"IconButtonVoice"
		"xpos"			        "c-255" [$ENGLISH]
		"xpos"			        "c-275" [!$ENGLISH]
		"ypos"			        "401"
		"wide"					"15"
		"tall"					"15"
		"scaleImage"			"1"
		"pinCorner"				"0"
		"visible"				"0"
		"enabled"				"1"
		"tabPosition"			"0"
		"image"					"icon_button_voice"
		"scaleImage"			"1"
	}
	
		
	"FlmGameAccess"
	{
		"ControlName"			"FlyoutMenu"
		"fieldName"				"FlmGameAccess"
		"visible"				"0"
		"wide"					"0"
		"tall"					"0"
		"zpos"					"3"
		"InitialFocus"			"BtnPublic"
		"ResourceFile"			"resource/UI/L4D360UI/DropDownLobbyGameAccess.res"
	}
}
