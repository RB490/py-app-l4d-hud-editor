// Defines the positions of a variety of hud controls
"Resource/HudLayout.res"
{

	"AlignDebugPanel1080p"
	{
		"ControlName"	"EditablePanel"
		"fieldName"		"AlignDebugPanel1080p"
		"visible"		"0"
		"xpos"			"20"
		"ypos"			"20"
		"zpos"			"-100"
		"wide"			"813"
		"tall"			"440"
		"proportionaltoparent"	"1"
		//"border"		"CyanBorderThick"
		"bgcolor_override"	"255 255 255 50"	//TransparentLightBlack
		//"bgcolor_override"	"Blue"
	}
	

	"CustomCrosshair"  // Image Crosshair
	{
		"ControlName"	"ImagePanel"
		"fieldName"	    "CustomCrosshair"
		"xpos"		    "c-28"
		"ypos"		    "c-28"
		"wide"		    "56"
		"tall"		    "56"
		"visible"	    "1"			              // "1" to Enable, "0" to Disable
		"enabled"	    "1"
		"scaleImage"	"1"
		"autoResize"	"0"
		"pinCorner"	    "0"
		"image"		    "gfx\vgui\defaultweapon"
		"drawcolor"	    "255 255 255 255"
		"zpos"			"-1"
	}

	BuildableCostPanel
	{
		"fieldname"                 "BuildableCostPanel"
		"visible"                   "1"
		"enabled"                   "1"
		"xpos"                      "114"
		"ypos"                      "-100"
		"wide"                      "300"
		"tall"                      "80"
		"PaintBackgroundType"       "0"
		"PaintBackground"           "0"
	}

	CBudgetPanel
	{
		"fieldname"  "CBudgetPanel"
		"visible"    "1"
		"enabled"    "1"
		"wide"       "640"
		"tall"       "480"
	}

	// Local player Infected ability cooldown timer
	CHudAbilityTimer
	{
		"fieldname"                 "CHudAbilityTimer"
		"controlName"               "CHudAbilityTimer"
		"visible"                   "1"
		"enabled"                   "1"
		"xpos"                      "r72"
		"ypos"                      "r120"
		"wide"                      "80"
		"tall"                      "70"
		"usetitlesafe"              "1"
		"ability_charging_color"    "127 127 127 255"
		"ability_ready_color"       "255 255 255 255"
		"ability_surpressed_color"  "127 127 127 255"
	}

	// Local player health hud section
	CHudLocalPlayerDisplay
	{
		"fieldname"             "CHudLocalPlayerDisplay"
		"visible"               "1"
		"enabled"               "1"
		"xpos"                  "0"
		"ypos"                  "2"
		"wide"         "f0"
		"tall"         "f0"
		"usetitlesafe"          "1"
	}

	CHudSurvivorTeamStatus
	{
		"fieldname"            "CHudSurvivorTeamStatus"
		"controlName"          "CHudSurvivorTeamStatus"
		"visible"              "1"
		"enabled"              "1"
		"xpos"                 "r85"
		"ypos"                 "120"
		"wide"                 "80"
		"tall"                 "20"
		"PaintBackgroundType"  "2"
	}

	// Survivor teammate panels
	CHudTeamDisplay
	{
		"fieldname"                   "CHudTeamDisplay"
		"visible"                     "1"
		"enabled"                     "1"
		"xpos"                        "15"		//15	//c200
		"ypos"                        "r265"
		"wide"                        "f0"
		"tall"                        "500"
		"usetitlesafe"                "1"
	}

	CHudTeamMateInPerilNotice
	{
		"fieldname"  "CHudTeamMateInPerilNotice"
		"visible"    "1"
		"enabled"    "1"
		"ypos"       "50"
	}

	// Vote hud
	CHudVote
	{
		"fieldname"            "CHudVote"
		"visible"              "1"
		"enabled"              "1"
		"xpos"                 "c-150"	//c116		//r310 = rightaligned
		"ypos"                 "20"		// 70 = under scavenge timer
		"wide"                 "300"
		"tall"                 "200"
		"zpos"					"250"
		"usetitlesafe"         "1"
		"PaintBackgroundType"  "0"
		"bgcolor_override"     "0 0 0 0"
	}

	// Infected teammate panels
	CHudZombieTeamDisplay
	{
		"fieldname"                   "CHudZombieTeamDisplay"
		"visible"                     "1"
		"enabled"                     "1"
		"xpos"                        "0"
		"ypos"                        "r75"
		"wide"                        "f0"
		"tall"                        "100"
		"usetitlesafe"                "1"
		"HorizPanelSpacing"           "140"
		"VertPanelSpacing"            "45"
	}

	CItemPickupPanel
	{
		"fieldname"            "CItemPickupPanel"
		"visible"              "1"
		"enabled"              "1"
		"xpos"                 "0"
		"ypos"                 "0"
		"wide"                 "f0"
		"tall"                 "f0"
		"usetitlesafe"         "0"
		"PaintBackgroundType"  "2"
	}

	CTextureBudgetPanel
	{
		"fieldname"  "CTextureBudgetPanel"
		"visible"    "1"
		"enabled"    "1"
		"wide"       "640"
		"tall"       "480"
	}

	CVProfPanel
	{
		"fieldname"  "CVProfPanel"
		"visible"    "1"
		"enabled"    "1"
		"wide"       "640"
		"tall"       "480"
	}

	HudAccount
	{
		"fieldname"            "HudAccount"
		"visible"              "1"
		"enabled"              "1"
		"xpos"                 "r134"
		"ypos"                 "374"
		"wide"                 "116"
		"tall"                 "80"
		"PaintBackgroundType"  "2"
		"digit2_xpos"          "104"
		"digit2_ypos"          "2"
		"digit_xpos"           "104"
		"digit_ypos"           "36"
		"icon2_xpos"           "0"
		"icon2_ypos"           "2"
		"icon_xpos"            "0"
		"icon_ypos"            "36"
	}

	HudAnimationInfo
	{
		"fieldname"  "HudAnimationInfo"
		"visible"    "1"
		"enabled"    "1"
		"wide"       "640"
		"tall"       "480"
	}

	HudAnnouncement
	{
		"fieldname"            "HudAnnouncement"
		"visible"              "0"
		"enabled"              "1"
		"xpos"                 "c-150"
		"ypos"                 "300"
		"wide"                 "300"
		"tall"                 "15"
		"PaintBackgroundType"  "2"
	}

	HudArmor
	{
		"fieldname"            "HudArmor"
		"visible"              "1"
		"enabled"              "1"
		"xpos"                 "156"
		"ypos"                 "440"
		"wide"                 "132"
		"tall"                 "40"
		"PaintBackgroundType"  "2"
		"digit_xpos"           "34"
		"digit_ypos"           "2"
		"icon_xpos"            "0"
		"icon_ypos"            "2"
	}

	HudBiofeedback
	{
		"fieldname"     "HudBiofeedback"
		"visible"       "1"
		"enabled"       "1"
		"xpos"          "r128"
		"ypos"          "r479"
		"wide"          "128"
		"tall"          "64"
		"usetitlesafe"  "1"
	}

	HudBlood
	{
		"fieldname"  "HudBlood"
		"visible"    "1"
		"enabled"    "1"
		"wide"       "640"
		"tall"       "480"
	}

	HudC4
	{
		"fieldname"            "HudC4"
		"visible"              "1"
		"enabled"              "1"
		"xpos"                 "16"
		"ypos"                 "248"
		"wide"                 "40"
		"tall"                 "40"
		"PaintBackgroundType"  "2"
		"FlashColor"           "HudIcon_Red"
		"IconColor"            "HudIcon_Green"
	}

	HudChat
	{
		"fieldname"            "HudChat"
		"controlName"          "EditablePanel"
		"visible"              "1"
		"enabled"              "1"
		"xpos"                 "10"
		"ypos"                 "375"
		"wide"                 "320"
		"tall"                 "120"
		"usetitlesafe"         "1"
		"PaintBackgroundType"  "0"
		//"border"				"NoBorder"
	}

	// Closed captions
	HudCloseCaption
	{
		"fieldname"                   "HudCloseCaption"
		"visible"                     "1"
		"enabled"                     "1"
		"xpos"                        "135"	//c-150
		"ypos"                        "r135"
		"wide"                        "235"
		"tall"                        "125"
		"usetitlesafe"                "1"
		"BgAlpha"                     "00"
		"GrowTime"                    "0.20"
		"ItemFadeInTime"              "0.15"
		"ItemFadeOutTime"             "0.3"
		"ItemHiddenTime"              "0.2"
		"topoffset"                   "1"
		"bgcolor_override"			"TransparentLightBlack"
		"border" "BaseBorder"
	}
	
	HudCloseCaptionDebug
	{
		"controlName"				"panel"
		"fieldname"                   "HudCloseCaptionDebug"
		"visible"                     "0"
		"enabled"                     "1"
		"xpos"                        "c-300"	//c-150
		"ypos"                        "r140"
		"wide"                        "240"
		"tall"                        "130"
		"usetitlesafe"                "1"
		"BgAlpha"                     "128"
		"GrowTime"                    "0.20"
		"ItemFadeInTime"              "0.15"
		"ItemFadeOutTime"             "0.3"
		"ItemHiddenTime"              "0.2"
		"topoffset"                   "133"
		"bgcolor_override"			"blue"
		"border" "BaseBorder"
	}

	HudCommentary
	{
		"fieldname"              "HudCommentary"
		"visible"                "0"
		"enabled"                "1"
		"xpos"                   "c-190"
		"ypos"                   "350"
		"wide"                   "380"
		"tall"                   "40"
		"PaintBackgroundType"    "2"
		"alpha"                  "0"
		"bar_height"             "8"
		"bar_width"              "320"
		"bar_xpos"               "50"
		"bar_ypos"               "20"
		"count_xpos_from_right"  "10"
		"count_ypos"             "8"
		"icon_height"            "40"
		"icon_texture"           "vgui/hud/icon_commentary"
		"icon_width"             "40"
		"icon_xpos"              "0"
		"icon_ypos"              "0"
		"speaker_xpos"           "50"
		"speaker_ypos"           "8"
	}

	HudCredits
	{
		"fieldname"  "HudCredits"
		"visible"    "1"
		"enabled"    "1"
		"xpos"       "c-270"
		"ypos"       "c-190"
		"wide"       "540"
		"tall"       "380"
	}

	HudCrosshair
	{
		"fieldname"                 "HudCrosshair"
		"visible"                   "1"
		"enabled"                   "1"
		"wide"                      "640"
		"tall"                      "480"
		"ability_charging_color"    "127 127 127 255"
		"ability_ready_color"       "255 255 255 255"
		"ability_size"              "17"
		"ability_surpressed_color"  "127 127 127 255"
	}

	HudDamageIndicator
	{
		"fieldname"      "HudDamageIndicator"
		"visible"        "1"
		"enabled"        "1"
		"dmg_tall1"      "240"
		"dmg_tall2"      "200"
		"dmg_wide"       "36"
		"dmg_xpos"       "30"
		"dmg_ypos"       "100"
		"DmgColorLeft"   "255 0 0 0"
		"DmgColorRight"  "255 0 0 0"
		"EndRadius"      "80"
		"MaximumHeight"  "60"
		"MaximumWidth"   "80"
		"MinimumHeight"  "30"
		"MinimumTime"    "2"
		"MinimumWidth"   "40"
		"StartRadius"    "120"
	}

	HudDeathNotice
	{
		"fieldname"        "HudDeathNotice"
		"visible"          "1"
		"enabled"          "1"
		"xpos"             "0"
		"ypos"             "0"
		"wide"             "f0"
		"tall"             "480"
		"IconSize"         "16"
		"MaxDeathNotices"  "6"
		"TextFont"         "Default"
	}

	HudDefuser
	{
		"fieldname"            "HudDefuser"
		"visible"              "1"
		"enabled"              "1"
		"xpos"                 "16"
		"ypos"                 "248"
		"wide"                 "40"
		"tall"                 "40"
		"PaintBackgroundType"  "2"
		"IconColor"            "HudIcon_Green"
	}

	HudFinaleMeter
	{
		"fieldname"            "HudFinaleMeter"
		"visible"              "1"
		"enabled"              "1"
		"xpos"                 "c-100"
		"ypos"                 "-100"
		"wide"                 "200"
		"tall"                 "20"
		"PaintBackgroundType"  "2"
	}

	HudFlashbang
	{
	}

	HudFlashlight
	{
		"fieldname"            "HudFlashlight"
		"visible"              "1"
		"enabled"              "1"
		"xpos"                 "16"
		"ypos"                 "370"
		"wide"                 "102"
		"tall"                 "20"
		"PaintBackgroundType"  "2"
		"text_xpos"            "8"
		"text_ypos"            "6"
		"TextColor"            "255 170 0 220"
	}

	// Tank frustration meter
	HudFrustrationMeter
	{
		"fieldname"            "HudFrustrationMeter"
		"visible"              "1"
		"enabled"              "1"
		"xpos"                 "c-50"
		"ypos"                 "20"	//r24
		"wide"                 "100"
		"tall"                 "20"
		"usetitlesafe"         "2"
		"PaintBackgroundType"  "0"
	}

	HudGeiger
	{
		"fieldname"  "HudGeiger"
		"visible"    "1"
		"enabled"    "1"
		"wide"       "640"
		"tall"       "480"
	}

	// Local player infected spawn hud
	HudGhostPanel
	{
		"fieldname"                   "HudGhostPanel"
		"visible"                     "1"
		"enabled"                     "1"
		"xpos"                        "c-200"
		"ypos"                        "c80"
		"wide"                        "400"
		"tall"                        "65"
		"padding"                     "4"
		"RedText"                     "ColorOrange"
		"WhiteText"                   "200 200 200 255"
		"border"					"noborder"
	}

	HudHDRDemo
	{
		"fieldname"            "HudHDRDemo"
		"visible"              "0"
		"enabled"              "1"
		"xpos"                 "0"
		"ypos"                 "0"
		"wide"                 "640"
		"tall"                 "480"
		"PaintBackgroundType"  "2"
		"Alpha"                "255"
		"BorderBottom"         "64"
		"BorderCenter"         "0"
		"BorderColor"          "0 0 0 255"
		"BorderLeft"           "16"
		"BorderRight"          "16"
		"BorderTop"            "16"
		"LeftTitleY"           "422"
		"RightTitleY"          "422"
		"TextColor"            "255 255 255 255"
	}


	HudHistoryResource
	{
		"fieldname"    "HudHistoryResource"
		"visible"      "1"
		"enabled"      "1"
		"xpos"         "r640"
		"wide"         "640"
		"tall"         "330"
		"history_gap"  "55"
	}

	HudHostageRescueZone
	{
		"fieldname"            "HudHostageRescueZone"
		"visible"              "1"
		"enabled"              "1"
		"xpos"                 "16"
		"ypos"                 "248"
		"wide"                 "40"
		"tall"                 "40"
		"PaintBackgroundType"  "2"
		"FlashColor"           "HudIcon_Red"
		"IconColor"            "HudIcon_Green"
	}

	HudInfectedVOIP
	{
		"fieldname"            "HudInfectedVOIP"
		"visible"              "1"
		"enabled"              "1"
		"xpos"                 "r130"
		"ypos"                 "c100"
		"wide"                 "120"
		"tall"                 "84"
		"usetitlesafe"         "2"
		"PaintBackgroundType"  "0"
	}

	HudIntensityGraph
	{
		"fieldname"            "HudIntensityGraph"
		"visible"              "1"
		"enabled"              "1"
		"xpos"                 "c0"
		"ypos"                 "-100"
		"wide"                 "70"
		"tall"                 "100"
		"PaintBackgroundType"  "2"
	}

	// (by default red) 'Please wait for your teammates' panel that sometimes shows at the start of a map
	HudLeavingAreaWarning
	{
		"fieldname"            "HudLeavingAreaWarning"
		"visible"              "1"
		"enabled"              "1"
		"xpos"                 "c-100"
		"ypos"                 "20"
		"wide"                 "200"
		"tall"                 "15"
		"usetitlesafe"         "2"
		"PaintBackgroundType"  "2"
		"border"				"noborder"
	}

	HudMenu
	{
		"fieldname"        "HudMenu"
		"visible"          "1"
		"enabled"          "1"
		"zpos"             "1"
		"wide"             "640"
		"tall"             "480"
		"ItemFont"         "Default"
		"ItemFontPulsing"  "Default"
		"TextFont"         "Default"
	}

	HudMessage
	{
		"fieldname"  "HudMessage"
		"visible"    "1"
		"enabled"    "1"
		"wide"       "640"
		"tall"       "480"
	}

	HudMessagePanel
	{
		"fieldname"            "HudMessagePanel"
		"visible"              "0"
		"enabled"              "1"
		"xpos"                 "120"
		"ypos"                 "r235"
		"wide"                 "400"
		"tall"                 "180"
		"PaintBackgroundType"  "2"
		"text_spacing"         "1"
		"text_xpos"            "4"
		"text_ypos"            "4"
	}

	HudMOTD
	{
		"fieldname"  "HudMOTD"
		"visible"    "1"
		"enabled"    "1"
		"wide"       "640"
		"tall"       "480"
	}

	HudPredictionDump
	{
		"fieldname"  "HudPredictionDump"
		"visible"    "1"
		"enabled"    "1"
		"wide"       "640"
		"tall"       "480"
	}

	// Progress bar. Healing/being healed, starting generator etc
	HudProgressBar
	{
		"fieldName" 			"HudProgressBar"
		"xpos"					"c-100"
		"ypos"					"r38"
		"wide"					"200"
		"tall"  				"100"
		"visible" 				"1"
		"enabled" 				"1"
	}

	// Kill feed eg: Player X killed smoker
	HudPZDamageRecord
	{
		"fieldname"                   "HudPZDamageRecord"
		"visible"                     "1"
		"enabled"                     "1"
		"xpos"                        "20"
		"ypos"                        "20"
		"wide"                        "f0"
		"tall"                        "75"
		"usetitlesafe"                "1"
		"PaintBackgroundType"         "2"
		"label_textalign"             "west"
		"bgcolor_override"			"0 0 0 0"
	}

	HUDQuickInfo
	{
		"fieldname"  "HUDQuickInfo"
		"visible"    "1"
		"enabled"    "1"
		"wide"       "640"
		"tall"       "480"
	}

	HudRoundTimer
	{
		"fieldname"            "HudRoundTimer"
		"visible"              "1"
		"enabled"              "1"
		"xpos"                 "c-20"
		"ypos"                 "440"
		"wide"                 "120"
		"tall"                 "40"
		"PaintBackgroundType"  "2"
		"digit_xpos"           "34"
		"digit_ypos"           "2"
		"FlashColor"           "HudIcon_Red"
		"icon_xpos"            "0"
		"icon_ypos"            "2"
	}

	// Dead Center finale gascan hud
	HudScavengeProgress
	{
		"fieldname"        "HudScavengeProgress"
		"visible"          "1"
		"enabled"          "1"
		"xpos"             "r88"
		"ypos"             "20"
		"zpos"             "0"
		"wide"             "100"
		"tall"             "50"
		"NumberFont"       "HudNumbers"
		"PaintBackground"  "0"
		"border"			"noborder"
	}

	// Scavenge round timer
	HudScavengeTimer
	{
		"fieldname"        "HudScavengeTimer"
		"visible"          "1"
		"enabled"          "1"
		"xpos"             "r170"
		"ypos"             "20"
		"zpos"             "0"
		"wide"             "150"
		"tall"             "100"
		"NumberFont"       "HudNumbers"
		"PaintBackground"  "0"
		"border"			"noborder"
	}

	HudScenarioIcon
	{
		"fieldname"            "HudScenarioIcon"
		"visible"              "1"
		"enabled"              "1"
		"xpos"                 "c110"
		"ypos"                 "443"
		"wide"                 "40"
		"tall"                 "44"
		"PaintBackgroundType"  "2"
		"IconColor"            "Hostage_Yellow"
	}

	HudScope
	{
		"fieldname"  "HudZoom"
		"visible"    "1"
		"enabled"    "1"
		"wide"       "640"
		"tall"       "480"
	}

	HudScriptedMode
	{
		"fieldname"        "HudScriptedMode"
		"visible"          "1"
		"enabled"          "1"
		"xpos"             "c-320"
		"ypos"             "0"
		"zpos"             "0"
		"wide"             "640"
		"tall"             "480"
		"NumberFont"       "HudNumbers"
		"PaintBackground"  "0"
	}

	HudShoppingCart
	{
		"fieldname"            "HudShoppingCart"
		"visible"              "1"
		"enabled"              "1"
		"xpos"                 "16"
		"ypos"                 "200"
		"wide"                 "40"
		"tall"                 "40"
		"PaintBackgroundType"  "2"
		"IconColor"            "HudIcon_Green"
	}

	HudSuit
	{
		"fieldname"            "HudSuit"
		"visible"              "1"
		"enabled"              "1"
		"xpos"                 "140"
		"ypos"                 "432"
		"wide"                 "108"
		"tall"                 "36"
		"PaintBackgroundType"  "2"
		"digit_xpos"           "50"
		"digit_ypos"           "2"
		"text_xpos"            "8"
		"text_ypos"            "20"
	}

	// Survival round timer
	HudSurvivalTimer
	{
		"fieldname"        "HudSurvivalTimer"
		"visible"          "1"
		"enabled"          "1"
		"xpos"             "r185"
		"ypos"             "20"
		"zpos"             "0"
		"wide"             "165"
		"tall"             "100"
		"NumberFont"       "HudNumbers"
		"PaintBackground"  "0"
		"border"		"noborder"
	}

	HudTerritory
	{
		"fieldname"  "HudTerritory"
		"visible"    "1"
		"enabled"    "1"
		"xpos"       "240"
		"ypos"       "432"
		"wide"       "240"
		"tall"       "48"
	}

	HudTrain
	{
		"fieldname"  "HudTrain"
		"visible"    "1"
		"enabled"    "1"
		"wide"       "640"
		"tall"       "480"
	}

	HudVehicle
	{
		"fieldname"  "HudVehicle"
		"visible"    "1"
		"enabled"    "1"
		"wide"       "640"
		"tall"       "480"
	}

	// Local player voice chat icon
	HudVoiceSelfStatus
	{
		"fieldname"             "HudVoiceSelfStatus"
		"visible"               "1"
		"enabled"               "1"
		"xpos"                  "r35"
		"ypos"                  "r140"
		"wide"                  "24"
		"tall"                  "24"
		"usetitlesafe"          "1"
	}

	HudVoiceStatus
	{
		"fieldname"     "HudVoiceStatus"
		"visible"       "1"
		"enabled"       "1"
		"xpos"          "r130"
		"ypos"          "0"
		"wide"          "150"
		"tall"          "290"
		"icon_tall"     "16"
		"icon_wide"     "16"
		"icon_xpos"     "0"
		"icon_ypos"     "0"
		"inverted"      "0"
		"item_spacing"  "2"
		"item_tall"     "15"
		"item_wide"     "120"
		"text_font"     "DefaultDropShadow"
		"text_xpos"     "18"
	}

	HudWeapon
	{
		"fieldname"  "HudWeapon"
		"visible"    "1"
		"enabled"    "1"
		"wide"       "640"
		"tall"       "480"
	}

	// Local player weapon section
	HudWeaponSelection
	{
		"fieldName" "HudWeaponSelection"
		"xpos"	"r195"
		"ypos"	"r128"
		"wide"	"200"
		"tall"	"150"
		"visible" "1"
		"enabled" "1"
		"usetitlesafe" "1"
		
		"if_split_screen_horizontal"
		{
			"ypos"	"0"
		}

		"LargeBoxWide" "0"
		"LargeBoxTall" "0"
		"SmallBoxWide" "0"
		"SmallBoxTall" "0"
		"BoxGap" "0"
		"BoxDirection" "0"	// 0 is up, 1 is down, 2 is left, 3 is right

		"SelectionNumberXPos" "0"
		"SelectionNumberYPos" "0"
		"SelectionGrowTime"	"0"

		"Ammo1XPos"	"0"
		"Ammo1YPos"	"0"

		"Ammo2XPos"	"0"
		"Ammo2YPos"	"0"

		"IconXPos" "0"	// negative numbers mean right side
		"IconYPos" "0"
		"IconYPos_lodef" "0"

		"TextYPos" "0"	
		"TextColor" "0"
		"MaxSlots"	"0"
		"PlaySelectSounds"	"0"
			
		// primary weapon icon
		"PrimaryWeaponsYPos"	"10"
		"PrimaryWeaponWide"		"10"
		"PrimaryWeaponTall"		"0"
		"PrimaryWeaponsYPos"	"0"	
		"PrimaryBindingYPos"	"0"
		
		"PrimaryWeaponBoxWide"	"70"	//59
		"PrimaryWeaponBoxTall"	"31"
		"PistolBoxTall"	"15"	
		
		"IconSize"		"15"	// square weapon icon sizes		
		"RightSideIndent"	"25"
		
		// ammo numbers
		"PrimaryAmmoXPos"	"29"
		"PrimaryAmmoYPos"	"6"
		"ReserveAmmoXPos"	"58"
		"ReserveAmmoYPos"	"12"	
		
		"PrimaryAmmoFont"		"Cerbetica50Shadow"
		"ReserveAmmoFont"		"Cerbetica18Shadow"		
		"PistolAmmoFont"		"Cerbetica18Shadow"
	
		// ammo icons
		"AmmoIconXPos"	"964"	//64
		"AmmoIconYPos"	"16"
		"AmmoIconSize"	"15"	//10
		"SpecialAmmoXPos"	"35"
		"SpecialAmmoYPos"	"15"
				
		//melee weapons
		"MeleeWeaponX"		"-35"
		"MeleeWeaponY"		"-2"
		"MeleeWeaponWide"	"28"
		"MeleeWeaponTall"	"16"	
		
		//chainsaw
		"ChainsawX"			"-27"
		"ChainsawY"			"1"
		"ChainsawWide"		"24"	//25
		"ChainsawTall"		"12"	//12
		
		//chainsaw fuelbar
		"ChainsawBarX"		"-35"
		"ChainsawBarY"		"0"
		"ChainsawBarWide"	"4"
		"ChainsawBarTall"	"13"
			
		
		"SelectedItemColor"				"Ammo In Clip Low"
		"UnselectedItemColor"			"blue"
		"SelectedReserveAmmoColor"		"Ammo In Reserve"
		"UnselectedReserveAmmoColor"	"Ammo In Reserve"
		
		"InactiveItemColor"		"255 255 255 10"
		
		"SelectedScale"	"1.0"	// scale selected boxes by this much
		
		"PistolBoxWide"	"0"		//hardcoded,change PistolBoxTall instead
	}

	// Local player infected health section
	HudZombieHealth
	{
		"fieldname"             "HudZombieHealth"
		"visible"               "1"
		"enabled"               "1"
		"xpos"                  "r387"
		"ypos"                  "r100"
		"wide"                  "400"
		"tall"                  "100"
		"usetitlesafe"          "1"
	}

	// Infected Tank approaching / Too far from Survivors
	HudZombiePanel
	{
		"fieldname"                   "HudZombiePanel"
		"visible"                     "1"
		"enabled"                     "1"
		"xpos"                        "c-150"
		"ypos"                        "c80"
		"wide"                        "300"
		"tall"                        "155"
	}

	HudZoom
	{
		"fieldname"        "HudZoom"
		"visible"          "0"
		"enabled"          "1"
		"BorderThickness"  "88"
		"Circle1Radius"    "66"
		"Circle2Radius"    "74"
		"DashGap"          "16"
		"DashHeight"       "4"
	}

	overview
	{
		"fieldname"  "overview"
		"visible"    "1"
		"enabled"    "1"
		"xpos"       "0"
		"ypos"       "480"
		"wide"       "0"
		"tall"       "0"
	}

	PlayerLabel
	{
		"fieldname"  "PlayerLabel"
		"visible"    "1"
		"enabled"    "1"
		"xpos"       "c-320"
		"ypos"       "c-240"
		"wide"       "640"
		"tall"       "480"
	}

	// Infected rematch voting hud
	PZEndGamePanel
	{
		"fieldname"  "PZEndGamePanel"
		"visible"    "1"
		"enabled"    "1"
		"xpos"       "100"
		"ypos"       "100"
		"wide"       "354"
		"tall"       "200"
	}

	ScorePanel
	{
		"fieldname"  "ScorePanel"
		"visible"    "1"
		"enabled"    "1"
		"wide"       "640"
		"tall"       "480"
	}

	StatsCrawl
	{
		"fieldname"                "StatsCrawl"
		"visible"                  "1"
		"enabled"                  "1"
		"xpos"                     "0"
		"ypos"                     "0"
		"wide"                     "f0"
		"tall"                     "f0"
		"ButtonFont"               "GameUIButtons"
		"CreditsCrawlFont"         "Credits"
		"skip_legend_inset_x"      "10"
		"skip_legend_inset_y"      "25"
		"SkipLabelFont"            "DefaultLarge"
		"StatsCrawlFont"           "OuttroStatsCrawl"
		"StatsCrawlUnderlineFont"  "OuttroStatsCrawlUnderline"
		"vote_bot_inset_x"         "90"
		"vote_bot_inset_y"         "45"
		"votes"
		{
			"box_inset"                "1"
			"box_size"                 "16"
			"spacer"                   "4"
		}
	}

	TargetID
	{
		"fieldname"  "TargetID"
		"visible"    "1"
		"enabled"    "1"
		"xpos"       "c-320"
		"ypos"       "c-240"
		"wide"       "640"
		"tall"       "480"
	}

	TerritorySCore
	{
		"fieldname"  "TerritoryScore"
		"visible"    "0"
		"enabled"    "0"
		"xpos"       "240"
		"ypos"       "450"
		"wide"       "200"
		"tall"       "200"
		"text_xpos"  "8"
		"text_ypos"  "4"
	}
}
