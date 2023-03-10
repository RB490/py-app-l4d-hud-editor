// Parsed on 2021.09.17 by https://github.com/RB490/ahk-app-l4d-hud-editor

// Defines the positions of a variety of hud controls

"scripts/hudlayout.res"
{

	"overview"
	{
		"fieldname"     "overview"
		"visible"       "1"
		"enabled"       "1"
		"xpos"          "0"
		"ypos"          "480"
		"wide"          "0"
		"tall"          "0"
	}

	"HudCommentary"
	{
		"fieldname"                 "HudCommentary"
		"visible"                   "0"
		"enabled"                   "1"
		"xpos"                      "c-190"
		"ypos"                      "350"
		"wide"                      "380"
		"tall"                      "40"
		"PaintBackgroundType"       "2"
		"icon_ypos"                 "0"
		"icon_xpos"                 "0"

		//Uncommon
		"alpha"                     "0"
		"bar_height"                "8"
		"bar_width"                 "320"
		"bar_xpos"                  "50"
		"bar_ypos"                  "20"
		"count_xpos_from_right"     "10"
		"count_ypos"                "8"
		"icon_height"               "40"
		"icon_texture"              "vgui/hud/icon_commentary"
		"icon_width"                "40"
		"speaker_xpos"              "50"
		"speaker_ypos"              "8"
	}

	"HudHDRDemo"
	{
		"fieldname"               "HudHDRDemo"
		"visible"                 "0"
		"enabled"                 "1"
		"xpos"                    "0"
		"ypos"                    "0"
		"wide"                    "640"
		"tall"                    "480"
		"PaintBackgroundType"     "2"

		//Uncommon
		"Alpha"                   "255"
		"BorderBottom"            "64"
		"BorderCenter"            "0"
		"BorderColor"             "0 0 0 255"
		"BorderLeft"              "16"
		"BorderRight"             "16"
		"BorderTop"               "16"
		"LeftTitleY"              "422"
		"RightTitleY"             "422"
		"TextColor"               "255 255 255 255"
	}

	// Survival round timer
	"HudSurvivalTimer"
	{
		"fieldname"           "HudSurvivalTimer"
		"visible"             "1"
		"enabled"             "1"
		"xpos"                "c-220"
		"ypos"                "-10"
		"zpos"                "0"
		"wide"                "440"
		"tall"                "100"
		"PaintBackground"     "0"
		"NumberFont"          "HudNumbers"
	}

	"HudScriptedMode"
	{
		"fieldname"           "HudScriptedMode"
		"visible"             "1"
		"enabled"             "1"
		"xpos"                "c-320"
		"ypos"                "0"
		"zpos"                "0"
		"wide"                "640"
		"tall"                "480"
		"PaintBackground"     "0"
		"NumberFont"          "HudNumbers"
	}

	// Scavenge round timer
	"HudScavengeTimer"
	{
		"fieldname"           "HudScavengeTimer"
		"visible"             "1"
		"enabled"             "1"
		"xpos"                "c-220"
		"ypos"                "15"
		"zpos"                "0"
		"wide"                "440"
		"tall"                "100"
		"PaintBackground"     "0"
		"NumberFont"          "HudNumbers"
	}

	// Scavenge gascan hud
	"HudScavengeProgress"
	{
		"fieldname"           "HudScavengeProgress"
		"visible"             "1"
		"enabled"             "1"
		"xpos"                "c-42"
		"ypos"                "23"
		"zpos"                "0"
		"wide"                "85"
		"tall"                "43"
		"PaintBackground"     "0"
		"NumberFont"          "HudNumbers"
	}

	"TargetID"
	{
		"fieldname"     "TargetID"
		"visible"       "1"
		"enabled"       "1"
		"xpos"          "c-320"
		"ypos"          "c-240"
		"wide"          "640"
		"tall"          "480"
	}

	"PlayerLabel"
	{
		"fieldname"     "PlayerLabel"
		"visible"       "1"
		"enabled"       "1"
		"xpos"          "c-320"
		"ypos"          "c-240"
		"wide"          "640"
		"tall"          "480"
	}

	"HudArmor"
	{
		"fieldname"               "HudArmor"
		"visible"                 "1"
		"enabled"                 "1"
		"xpos"                    "156"
		"ypos"                    "440"
		"wide"                    "132"
		"tall"                    "40"
		"PaintBackgroundType"     "2"
		"digit_xpos"              "34"
		"digit_ypos"              "2"
		"icon_ypos"               "2"
		"icon_xpos"               "0"
	}

	"HudSuit"
	{
		"fieldname"               "HudSuit"
		"visible"                 "1"
		"enabled"                 "1"
		"xpos"                    "140"
		"ypos"                    "432"
		"wide"                    "108"
		"tall"                    "36"
		"PaintBackgroundType"     "2"
		"digit_xpos"              "50"
		"digit_ypos"              "2"
		"text_xpos"               "8"
		"text_ypos"               "20"
	}

	// Progress bar. Healing/being healed, starting generator etc
	"HudProgressBar"
	{
		"fieldname"                    "HudProgressBar"
		"visible"                      "1"
		"enabled"                      "1"
		"xpos"                         "c-114"
		"ypos"                         "c10"
		"wide"                         "300"
		"tall"                         "80"
		"PaintBackground"              "0"
		"PaintBackgroundType"          "0"

		//Uncommon
		"if_split_screen_vertical"
		{
			"ypos"     "c-10"
		}
	}

	// Progressbar looking panel. Unused but does show during hud_reloadscheme with lower host_timescale. Can be moved offscreen
	"BuildableCostPanel"
	{
		"fieldname"                    "BuildableCostPanel"
		"visible"                      "1"
		"enabled"                      "1"
		"xpos"                         "c-114"
		"ypos"                         "c10"
		"wide"                         "300"
		"tall"                         "80"
		"PaintBackground"              "0"
		"PaintBackgroundType"          "0"

		//Uncommon
		"if_split_screen_vertical"
		{
			"ypos"     "c-10"
		}
	}

	"HudRoundTimer"
	{
		"fieldname"               "HudRoundTimer"
		"visible"                 "1"
		"enabled"                 "1"
		"xpos"                    "c-20"
		"ypos"                    "440"
		"wide"                    "120"
		"tall"                    "40"
		"PaintBackgroundType"     "2"
		"digit_xpos"              "34"
		"digit_ypos"              "2"
		"icon_ypos"               "2"
		"icon_xpos"               "0"
		"FlashColor"              "HudIcon_Red"
	}

	"HudAccount"
	{
		"fieldname"               "HudAccount"
		"visible"                 "1"
		"enabled"                 "1"
		"xpos"                    "r134"
		"ypos"                    "374"
		"wide"                    "116"
		"tall"                    "80"
		"PaintBackgroundType"     "2"
		"digit_xpos"              "104"
		"digit_ypos"              "36"
		"icon_ypos"               "36"
		"icon_xpos"               "0"

		//Uncommon
		"digit2_xpos"             "104"
		"digit2_ypos"             "2"
		"icon2_xpos"              "0"
		"icon2_ypos"              "2"
	}

	"HudShoppingCart"
	{
		"fieldname"               "HudShoppingCart"
		"visible"                 "1"
		"enabled"                 "1"
		"xpos"                    "16"
		"ypos"                    "200"
		"wide"                    "40"
		"tall"                    "40"
		"PaintBackgroundType"     "2"
		"IconColor"               "HudIcon_Green"
	}

	"HudC4"
	{
		"fieldname"               "HudC4"
		"visible"                 "1"
		"enabled"                 "1"
		"xpos"                    "16"
		"ypos"                    "248"
		"wide"                    "40"
		"tall"                    "40"
		"PaintBackgroundType"     "2"
		"IconColor"               "HudIcon_Green"
		"FlashColor"              "HudIcon_Red"
	}

	"HudDefuser"
	{
		"fieldname"               "HudDefuser"
		"visible"                 "1"
		"enabled"                 "1"
		"xpos"                    "16"
		"ypos"                    "248"
		"wide"                    "40"
		"tall"                    "40"
		"PaintBackgroundType"     "2"
		"IconColor"               "HudIcon_Green"
	}

	"HudHostageRescueZone"
	{
		"fieldname"               "HudHostageRescueZone"
		"visible"                 "1"
		"enabled"                 "1"
		"xpos"                    "16"
		"ypos"                    "248"
		"wide"                    "40"
		"tall"                    "40"
		"PaintBackgroundType"     "2"
		"IconColor"               "HudIcon_Green"
		"FlashColor"              "HudIcon_Red"
	}

	"HudScenarioIcon"
	{
		"fieldname"               "HudScenarioIcon"
		"visible"                 "1"
		"enabled"                 "1"
		"xpos"                    "c110"
		"ypos"                    "443"
		"wide"                    "40"
		"tall"                    "44"
		"PaintBackgroundType"     "2"
		"IconColor"               "Hostage_Yellow"
	}

	"HudFlashlight"
	{
		"fieldname"               "HudFlashlight"
		"visible"                 "1"
		"enabled"                 "1"
		"xpos"                    "16"
		"ypos"                    "370"
		"wide"                    "102"
		"tall"                    "20"
		"PaintBackgroundType"     "2"
		"text_xpos"               "8"
		"text_ypos"               "6"

		//Uncommon
		"TextColor"               "255 170 0 220"
	}

	"HudDamageIndicator"
	{
		"fieldname"         "HudDamageIndicator"
		"visible"           "1"
		"enabled"           "1"

		//Uncommon
		"dmg_tall1"         "240"
		"dmg_tall2"         "200"
		"dmg_wide"          "36"
		"dmg_xpos"          "30"
		"dmg_ypos"          "100"
		"DmgColorLeft"      "255 0 0 0"
		"DmgColorRight"     "255 0 0 0"
		"EndRadius"         "80"
		"MaximumHeight"     "60"
		"MaximumWidth"      "80"
		"MinimumHeight"     "30"
		"MinimumTime"       "2"
		"MinimumWidth"      "40"
		"StartRadius"       "120"
	}

	// Sniper zoom hud. Unused since its now hardcoded but does show during hud_reloadscheme with lower host_timescale. Can be moved offscreen
	"HudZoom"
	{
		"fieldname"           "HudZoom"
		"visible"             "1"
		"enabled"             "1"

		//Uncommon
		"BorderThickness"     "88"
		"Circle1Radius"       "66"
		"Circle2Radius"       "74"
		"DashGap"             "16"
		"DashHeight"          "4"
	}

	"HudWeaponSelection"
	{
		"fieldname"                      "HudWeaponSelection"
		"visible"                        "1"
		"enabled"                        "1"
		"xpos"                           "r105"
		"ypos"                           "c-90"
		"wide"                           "100"
		"tall"                           "175"
		"usetitlesafe"                   "1"

		//Uncommon
		"Ammo1XPos"                      "55"
		"Ammo1YPos"                      "4"
		"Ammo2XPos"                      "58"
		"Ammo2YPos"                      "5"
		"AmmoIconSize"                   "22"
		"AmmoIconXPos"                   "20"
		"AmmoIconYPos"                   "3"
		"BoxDirection"                   "0"
		"BoxGap"                         "1"
		"ChainsawBarTall"                "19"
		"ChainsawBarWide"                "5"
		"ChainsawBarX"                   "45"
		"ChainsawBarY"                   "2"
		"ChainsawTall"                   "19"
		"ChainsawWide"                   "41"
		"ChainsawX"                      "2"
		"ChainsawY"                      "2"
		"IconSize"                       "24"
		"IconXPos"                       "-55"
		"IconYPos"                       "-5"
		"IconYPos_lodef"                 "2"
		"InactiveItemColor"              "90 90 90 255"
		"LargeBoxTall"                   "32"
		"LargeBoxWide"                   "150"
		"MaxSlots"                       "5"
		"MeleeWeaponTall"                "22"
		"MeleeWeaponWide"                "49"
		"MeleeWeaponX"                   "2"
		"MeleeWeaponY"                   "0"
		"PistolAmmoFont"                 "HudAmmo"
		"PistolBoxTall"                  "24"
		"PistolBoxWide"                  "53"
		"PlaySelectSounds"               "0"
		"PrimaryAmmoFont"                "HudAmmo"
		"PrimaryAmmoXPos"                "22"
		"PrimaryAmmoYPos"                "0"
		"PrimaryBindingYPos"             "38"
		"PrimaryWeaponBoxTall"           "28"
		"PrimaryWeaponBoxWide"           "53"
		"PrimaryWeaponsYPos"             "10"
		"PrimaryWeaponTall"              "20"
		"PrimaryWeaponWide"              "60"
		"ReserveAmmoFont"                "HudAmmoSmall"
		"ReserveAmmoXPos"                "22"
		"ReserveAmmoYPos"                "14"
		"RightSideIndent"                "10"
		"SelectedItemColor"              "142 214 57 255"
		"SelectedReserveAmmoColor"       "93 142 32 255"
		"SelectedScale"                  "1.0"
		"SelectionGrowTime"              "0.4"
		"SelectionNumberXPos"            "4"
		"SelectionNumberYPos"            "4"
		"SmallBoxTall"                   "24"
		"SmallBoxWide"                   "150"
		"SpecialAmmoXPos"                "18"
		"SpecialAmmoYPos"                "6"
		"TextColor"                      "SelectionTextFg"
		"TextYPos"                       "68"
		"UnselectedItemColor"            "White"
		"UnselectedReserveAmmoColor"     "169 169 169 255"
		"if_split_screen_horizontal"
		{
			"ypos"     "0"
		}
	}

	// Infected crosshair properties
	"HudCrosshair"
	{
		"fieldname"                    "HudCrosshair"
		"visible"                      "1"
		"enabled"                      "1"
		"wide"                         "640"
		"tall"                         "480"

		//Uncommon
		"ability_charging_color"       "127 127 127 255"
		"ability_ready_color"          "255 255 255 255"
		"ability_size"                 "17"
		"ability_surpressed_color"     "127 127 127 255"
	}

	"HudDeathNotice"
	{
		"fieldname"           "HudDeathNotice"
		"visible"             "1"
		"enabled"             "1"
		"xpos"                "0"
		"ypos"                "0"
		"wide"                "f0"
		"tall"                "480"

		//Uncommon
		"IconSize"            "16"
		"MaxDeathNotices"     "6"
		"TextFont"            "Default"
	}

	"HudVehicle"
	{
		"fieldname"     "HudVehicle"
		"visible"       "1"
		"enabled"       "1"
		"wide"          "640"
		"tall"          "480"
	}

	"CVProfPanel"
	{
		"fieldname"     "CVProfPanel"
		"visible"       "1"
		"enabled"       "1"
		"wide"          "640"
		"tall"          "480"
	}

	"ScorePanel"
	{
		"fieldname"     "ScorePanel"
		"visible"       "1"
		"enabled"       "1"
		"wide"          "640"
		"tall"          "480"
	}

	"HudTrain"
	{
		"fieldname"     "HudTrain"
		"visible"       "1"
		"enabled"       "1"
		"wide"          "640"
		"tall"          "480"
	}

	"HudMOTD"
	{
		"fieldname"     "HudMOTD"
		"visible"       "1"
		"enabled"       "1"
		"wide"          "640"
		"tall"          "480"
	}

	"HudMessage"
	{
		"fieldname"     "HudMessage"
		"visible"       "1"
		"enabled"       "1"
		"wide"          "640"
		"tall"          "480"
	}

	"HudMenu"
	{
		"fieldname"           "HudMenu"
		"visible"             "1"
		"enabled"             "1"
		"zpos"                "1"
		"wide"                "640"
		"tall"                "480"

		//Uncommon
		"ItemFont"            "Default"
		"ItemFontPulsing"     "Default"
		"TextFont"            "Default"
	}

	// Closed captions
	"HudCloseCaption"
	{
		"fieldname"                      "HudCloseCaption"
		"visible"                        "1"
		"enabled"                        "1"
		"xpos"                           "c-150"
		"ypos"                           "r220"
		"wide"                           "300"
		"tall"                           "135"
		"usetitlesafe"                   "1"

		//Uncommon
		"BgAlpha"                        "128"
		"GrowTime"                       "0.25"
		"ItemFadeInTime"                 "0.15"
		"ItemFadeOutTime"                "0.3"
		"ItemHiddenTime"                 "0.2"
		"topoffset"                      "0"
		"if_split_screen_horizontal"
		{
			"xpos"     "0"
			"ypos"     "r220"
			"wide"     "275"
			"tall"     "108"
		}
		"if_split_screen_vertical"
		{
			"ypos"     "r160"
			"tall"     "108"
		}
	}

	"HudHistoryResource"
	{
		"fieldname"       "HudHistoryResource"
		"visible"         "1"
		"enabled"         "1"
		"xpos"            "r640"
		"wide"            "640"
		"tall"            "330"

		//Uncommon
		"history_gap"     "55"
	}

	"HudGeiger"
	{
		"fieldname"     "HudGeiger"
		"visible"       "1"
		"enabled"       "1"
		"wide"          "640"
		"tall"          "480"
	}

	"HUDQuickInfo"
	{
		"fieldname"     "HUDQuickInfo"
		"visible"       "1"
		"enabled"       "1"
		"wide"          "640"
		"tall"          "480"
	}

	"HudWeapon"
	{
		"fieldname"     "HudWeapon"
		"visible"       "1"
		"enabled"       "1"
		"wide"          "640"
		"tall"          "480"
	}

	"HudAnimationInfo"
	{
		"fieldname"     "HudAnimationInfo"
		"visible"       "1"
		"enabled"       "1"
		"wide"          "640"
		"tall"          "480"
	}

	// Vote hud
	"CHudVote"
	{
		"fieldname"               "CHudVote"
		"visible"                 "1"
		"enabled"                 "1"
		"xpos"                    "10"
		"ypos"                    "c-80"
		"wide"                    "210"
		"tall"                    "200"
		"bgcolor_override"        "0 0 0 0"
		"PaintBackgroundType"     "0"
		"usetitlesafe"            "1"
	}

	// Infected local player ability cooldown timer
	"CHudAbilityTimer"
	{
		"fieldname"                    "CHudAbilityTimer"
		"controlName"                  "CHudAbilityTimer"
		"visible"                      "1"
		"enabled"                      "1"
		"xpos"                         "r72"
		"ypos"                         "r120"
		"wide"                         "80"
		"tall"                         "70"
		"usetitlesafe"                 "1"

		//Uncommon
		"ability_charging_color"       "127 127 127 255"
		"ability_ready_color"          "255 255 255 255"
		"ability_surpressed_color"     "127 127 127 255"
		"if_split_screen_left"
		{
			"xpos"     "-8"
		}
	}

	// Local player infected health section
	"HudZombieHealth"
	{
		"fieldname"                "HudZombieHealth"
		"visible"                  "1"
		"enabled"                  "1"
		"xpos"                     "r387"
		"ypos"                     "r100"
		"wide"                     "400"
		"tall"                     "100"
		"usetitlesafe"             "1"

		//Uncommon
		"if_split_screen_left"
		{
			"xpos"     "1"
		}
	}

	"CBudgetPanel"
	{
		"fieldname"     "CBudgetPanel"
		"visible"       "1"
		"enabled"       "1"
		"wide"          "640"
		"tall"          "480"
	}

	"CTextureBudgetPanel"
	{
		"fieldname"     "CTextureBudgetPanel"
		"visible"       "1"
		"enabled"       "1"
		"wide"          "640"
		"tall"          "480"
	}

	"HudPredictionDump"
	{
		"fieldname"     "HudPredictionDump"
		"visible"       "1"
		"enabled"       "1"
		"wide"          "640"
		"tall"          "480"
	}

	"HudScope"
	{
		"fieldname"     "HudZoom"
		"visible"       "1"
		"enabled"       "1"
		"wide"          "640"
		"tall"          "480"
	}

	// Local player voice chat icon
	"HudVoiceSelfStatus"
	{
		"fieldname"                "HudVoiceSelfStatus"
		"visible"                  "1"
		"enabled"                  "1"
		"xpos"                     "r132"
		"ypos"                     "r78"
		"wide"                     "24"
		"tall"                     "24"
		"usetitlesafe"             "1"

		//Uncommon
		"if_split_screen_left"
		{
			"xpos"     "100"
		}
	}

	"HudBiofeedback"
	{
		"fieldname"        "HudBiofeedback"
		"visible"          "1"
		"enabled"          "1"
		"xpos"             "r128"
		"ypos"             "r479"
		"wide"             "128"
		"tall"             "64"
		"usetitlesafe"     "1"
	}

	"HudVoiceStatus"
	{
		"fieldname"        "HudVoiceStatus"
		"visible"          "1"
		"enabled"          "1"
		"xpos"             "r130"
		"ypos"             "0"
		"wide"             "150"
		"tall"             "290"
		"text_font"        "DefaultDropShadow"
		"text_xpos"        "18"
		"icon_ypos"        "0"
		"icon_xpos"        "0"
		"icon_tall"        "16"
		"icon_wide"        "16"
		"inverted"         "0"

		//Uncommon
		"item_spacing"     "2"
		"item_tall"        "15"
		"item_wide"        "120"
	}

	"HudFlashbang"
	{
	}

	// Game instructor. But is hard coded. Font: InstructorTitle
	"HudHintDisplay"
	{
		"fieldname"     "HudHintDisplay"
		"visible"       "0"
		"enabled"       "1"
		"xpos"          "c-200"
		"ypos"          "294"
		"wide"          "400"
		"tall"          "50"
		"text_xpos"     "8"
		"text_ypos"     "8"

		//Uncommon
		"center_x"      "0"
		"center_y"      "-1"
	}

	// Game instructor. But is hard coded. Font: InstructorTitle
	"HudHintKeyDisplay"
	{
		"fieldname"               "HudHintKeyDisplay"
		"visible"                 "0"
		"enabled"                 "1"
		"xpos"                    "r120"
		"ypos"                    "r340"
		"wide"                    "100"
		"tall"                    "200"
		"PaintBackgroundType"     "2"
		"text_xpos"               "8"
		"text_ypos"               "8"

		//Uncommon
		"text_xgap"               "8"
		"text_ygap"               "8"
		"TextColor"               "255 170 0 220"
	}

	"HudTerritory"
	{
		"fieldname"     "HudTerritory"
		"visible"       "1"
		"enabled"       "1"
		"xpos"          "240"
		"ypos"          "432"
		"wide"          "240"
		"tall"          "48"
	}

	"TerritorySCore"
	{
		"fieldname"     "TerritoryScore"
		"visible"       "0"
		"enabled"       "0"
		"xpos"          "240"
		"ypos"          "450"
		"wide"          "200"
		"tall"          "200"
		"text_xpos"     "8"
		"text_ypos"     "4"
	}

	"HudChat"
	{
		"fieldname"               "HudChat"
		"controlName"             "EditablePanel"
		"visible"                 "1"
		"enabled"                 "1"
		"xpos"                    "10"
		"ypos"                    "275"
		"wide"                    "320"
		"tall"                    "120"
		"PaintBackgroundType"     "2"
		"usetitlesafe"            "1"
	}

	"HudMessagePanel"
	{
		"fieldname"               "HudMessagePanel"
		"visible"                 "0"
		"enabled"                 "1"
		"xpos"                    "120"
		"ypos"                    "r235"
		"wide"                    "400"
		"tall"                    "180"
		"PaintBackgroundType"     "2"
		"text_xpos"               "4"
		"text_ypos"               "4"

		//Uncommon
		"text_spacing"            "1"
	}

	"HudBlood"
	{
		"fieldname"     "HudBlood"
		"visible"       "1"
		"enabled"       "1"
		"wide"          "640"
		"tall"          "480"
	}

	"CHudSurvivorTeamStatus"
	{
		"fieldname"               "CHudSurvivorTeamStatus"
		"controlName"             "CHudSurvivorTeamStatus"
		"visible"                 "1"
		"enabled"                 "1"
		"xpos"                    "r85"
		"ypos"                    "120"
		"wide"                    "80"
		"tall"                    "20"
		"PaintBackgroundType"     "2"
	}

	// Local player health hud section
	"CHudLocalPlayerDisplay"
	{
		"fieldname"                "CHudLocalPlayerDisplay"
		"visible"                  "1"
		"enabled"                  "1"
		"xpos"                     "r160"
		"ypos"                     "r91"
		"wide"                     "160"
		"tall"                     "320"
		"usetitlesafe"             "1"

		//Uncommon
		"if_split_screen_left"
		{
			"xpos"     "0"
		}
		"if_split_screen_top"
		{
			"ypos"     "r90"
		}
	}

	// Survivor teammate panels
	"CHudTeamDisplay"
	{
		"fieldname"                      "CHudTeamDisplay"
		"visible"                        "1"
		"enabled"                        "1"
		"xpos"                           "5"
		"ypos"                           "r80"
		"wide"                           "f0"
		"tall"                           "100"
		"usetitlesafe"                   "1"

		//Uncommon
		"if_split_screen_horizontal"
		{
			"ypos"     "c-59"
		}
		"if_split_screen_vertical"
		{
			"xpos"             "c-300"
			"wide"             "600"
			"tall"             "100"
			"usetitlesafe"     "1"
		}
	}

	// 'Rescue countdown' Unused panel but does show during hud_reloadscheme with lower host_timescale. Can be moved offscreen
	"HudFinaleMeter"
	{
		"fieldname"               "HudFinaleMeter"
		"visible"                 "1"
		"enabled"                 "1"
		"xpos"                    "c-100"
		"ypos"                    "12"
		"wide"                    "200"
		"tall"                    "20"
		"PaintBackgroundType"     "2"
	}

	// Tank frustration meter
	"HudFrustrationMeter"
	{
		"fieldname"               "HudFrustrationMeter"
		"visible"                 "1"
		"enabled"                 "1"
		"xpos"                    "10"
		"ypos"                    "c0"
		"wide"                    "300"
		"tall"                    "84"
		"PaintBackgroundType"     "0"
		"usetitlesafe"            "2"
	}

	"HudInfectedVOIP"
	{
		"fieldname"               "HudInfectedVOIP"
		"visible"                 "1"
		"enabled"                 "1"
		"xpos"                    "r130"
		"ypos"                    "c100"
		"wide"                    "120"
		"tall"                    "84"
		"PaintBackgroundType"     "0"
		"usetitlesafe"            "2"
	}

	// Infected Tank approaching / Too far from Survivors
	"HudZombiePanel"
	{
		"fieldname"                      "HudZombiePanel"
		"visible"                        "1"
		"enabled"                        "1"
		"xpos"                           "c-190"
		"ypos"                           "c10"
		"wide"                           "400"
		"tall"                           "155"

		//Uncommon
		"if_split_screen_horizontal"
		{
			"ypos"     "c-45"
		}
		"if_split_screen_left"
		{
			"xpos"     "c-145"
		}
		"if_split_screen_right"
		{
			"xpos"     "c-175"
		}
	}

	"HudGhostPanel"
	{
		"fieldname"                      "HudGhostPanel"
		"visible"                        "1"
		"enabled"                        "1"
		"xpos"                           "c-180"
		"ypos"                           "c10"
		"wide"                           "400"
		"tall"                           "155"

		//Uncommon
		"padding"                        "4"
		"RedText"                        "246 5 5 255"
		"WhiteText"                      "192 192 192 255"
		"if_split_screen_horizontal"
		{
			"ypos"     "c-45"
		}
		"if_split_screen_left"
		{
			"xpos"     "c-145"
		}
		"if_split_screen_right"
		{
			"xpos"     "c-205"
		}
	}

	"HudCredits"
	{
		"fieldname"     "HudCredits"
		"visible"       "1"
		"enabled"       "1"
		"xpos"          "c-270"
		"ypos"          "c-190"
		"wide"          "540"
		"tall"          "380"
	}

	"HudAnnouncement"
	{
		"fieldname"               "HudAnnouncement"
		"visible"                 "0"
		"enabled"                 "1"
		"xpos"                    "c-150"
		"ypos"                    "300"
		"wide"                    "300"
		"tall"                    "15"
		"PaintBackgroundType"     "2"
	}

	"CHudTeamMateInPerilNotice"
	{
		"fieldname"     "CHudTeamMateInPerilNotice"
		"visible"       "1"
		"enabled"       "1"
		"ypos"          "50"
	}

	// 'Build_up' survivor meter Unused panel but does show during hud_reloadscheme with lower host_timescale. Can be moved offscreen
	"HudIntensityGraph"
	{
		"fieldname"               "HudIntensityGraph"
		"visible"                 "1"
		"enabled"                 "1"
		"xpos"                    "r75"
		"ypos"                    "190"
		"wide"                    "70"
		"tall"                    "100"
		"PaintBackgroundType"     "2"
	}

	// (by default red) 'Please wait for your teammates' panel that sometimes shows at the start of a map
	"HudLeavingAreaWarning"
	{
		"fieldname"               "HudLeavingAreaWarning"
		"visible"                 "1"
		"enabled"                 "1"
		"xpos"                    "10"
		"ypos"                    "c26"
		"wide"                    "200"
		"tall"                    "14"
		"PaintBackgroundType"     "2"
		"usetitlesafe"            "2"
	}

	"CItemPickupPanel"
	{
		"fieldname"               "CItemPickupPanel"
		"visible"                 "1"
		"enabled"                 "1"
		"xpos"                    "0"
		"ypos"                    "0"
		"wide"                    "f0"
		"tall"                    "f0"
		"PaintBackgroundType"     "2"
		"usetitlesafe"            "0"
	}

	// Kill feed eg: Player X killed smoker
	"HudPZDamageRecord"
	{
		"fieldname"                      "HudPZDamageRecord"
		"visible"                        "1"
		"enabled"                        "1"
		"xpos"                           "0"
		"ypos"                           "170"
		"wide"                           "f0"
		"tall"                           "75"
		"PaintBackgroundType"            "2"
		"usetitlesafe"                   "1"

		//Uncommon
		"label_textalign"                "west"
		"if_split_screen_horizontal"
		{
			"ypos"                "55"
			"label_textalign"     "west"
		}
		"if_split_screen_vertical"
		{
			"ypos"                "55"
			"label_textalign"     "center"
		}
	}

	"StatsCrawl"
	{
		"fieldname"                   "StatsCrawl"
		"visible"                     "1"
		"enabled"                     "1"
		"xpos"                        "0"
		"ypos"                        "0"
		"wide"                        "f0"
		"tall"                        "f0"

		//Uncommon
		"ButtonFont"                  "GameUIButtons"
		"CreditsCrawlFont"            "Credits"
		"skip_legend_inset_x"         "10"
		"skip_legend_inset_y"         "25"
		"SkipLabelFont"               "DefaultLarge"
		"StatsCrawlFont"              "OuttroStatsCrawl"
		"StatsCrawlUnderlineFont"     "OuttroStatsCrawlUnderline"
		"vote_bot_inset_x"            "90"
		"vote_bot_inset_y"            "45"
		"votes"
		{
			"box_inset"     "1"
			"box_size"      "16"
			"spacer"        "4"
		}
	}

	// Infected rematch voting hud
	"PZEndGamePanel"
	{
		"fieldname"     "PZEndGamePanel"
		"visible"       "1"
		"enabled"       "1"
		"xpos"          "c-177"
		"ypos"          "c10"
		"wide"          "354"
		"tall"          "200"
	}

	// Infected teammate panels
	"CHudZombieTeamDisplay"
	{
		"fieldname"                      "CHudZombieTeamDisplay"
		"visible"                        "1"
		"enabled"                        "1"
		"xpos"                           "0"
		"ypos"                           "r75"
		"wide"                           "f0"
		"tall"                           "100"
		"usetitlesafe"                   "1"

		//Uncommon
		"HorizPanelSpacing"              "140"
		"VertPanelSpacing"               "45"
		"if_split_screen_horizontal"
		{
			"ypos"     "c-59"
		}
		"if_split_screen_vertical"
		{
			"xpos"     "c-140"
		}
	}

}