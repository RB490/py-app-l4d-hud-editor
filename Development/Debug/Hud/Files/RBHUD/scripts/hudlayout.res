"Resource/HudLayout.res"
{
	"CustomCrosshair"
	{
		"ControlName"	"ImagePanel"
		"fieldName"	"CustomCrosshair"
		"xpos"		"c-8"
		"ypos"		"c-8"
		"wide"		"16"
		"tall"		"16"
		"visible"	"1"
		"enabled"	"1"
		"scaleImage"	"0"
		"image"		"_crosshair\crosshair"
		"zpos"		"-100" //zpos -2 and under hides crosshair behind credits
	}
	"CrosshairDebugBackground"
	{
		"ControlName"	"Panel"
		"fieldName"		"CrosshairDebugBackground"
		"xpos"			"c-32"
		"ypos"          "c-32"
		"wide"			"64"
		"tall"			"64"
		"visible"		"0"
		"enabled"		"1"
		"zpos"			"-2000"
		"bgcolor_override"	"TransparentLightBlack"
	}
	
	"CenterDebugBackground"
	{
		"ControlName"	"Panel"
		"fieldName"		"CenterDebugBackground"
		"xpos"			"c-125"	//c-125		//c-170
		"ypos"          "c0"
		"wide"			"250"	//250		//340
		"tall"			"147"	//122		//322
		"visible"		"0"
		"enabled"		"1"
		"zpos"			"-2000"
		"bgcolor_override"	"TransparentLightBlack"
	}
	
	"CenterDebugBackgroundWide"
	{
		"ControlName"	"Panel"
		"fieldName"		"CenterDebugBackgroundWide"
		"xpos"			"0"
		"ypos"          "c10"
		"wide"			"f0"
		"tall"			"100"
		"visible"		"0"
		"enabled"		"1"
		"zpos"			"-2000"
		"bgcolor_override"	"TransparentLightBlack"
	}
	
	//ink TWEAKED////////////////////////////////////////////////////
	HudWeaponSelection
	{
		"fieldName" "HudWeaponSelection"
		"xpos"	"c60"
		"ypos"	"c84"
		"wide"	"130"
		"tall"	"100"
		"visible" "1"
		"enabled" "1"
		"usetitlesafe" "1"
		
		"if_split_screen_horizontal"
		{
			"ypos"	"0"
		}

		"LargeBoxWide" "150"
		"LargeBoxTall" "32"
		"SmallBoxWide" "150"
		"SmallBoxTall" "24"
		"BoxGap" "1"
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
		
		"PrimaryWeaponsYPos"	"10"	
		"PrimaryWeaponBoxWide"	"70"
		"PrimaryWeaponBoxTall"	"34"
		"PrimaryBindingYPos"	"10"
		
		//melee weapons
		"MeleeWeaponX"		"-31"
		"MeleeWeaponY"		"-7"
		"MeleeWeaponWide"	"25"
		"MeleeWeaponTall"	"11"	
		
		//chainsaw
		"ChainsawX"			"-31"
		"ChainsawY"			"-7"
		"ChainsawWide"		"25"
		"ChainsawTall"		"12"	
		
		//chainsaw fuelbar
		"ChainsawBarX"		"-3"
		"ChainsawBarY"		"-7"
		"ChainsawBarWide"	"4"
		"ChainsawBarTall"	"12"		
		
		// ammo numbers
		"PrimaryAmmoXPos"	"35"
		"PrimaryAmmoYPos"	"7"
		"ReserveAmmoXPos"	"65"
		"ReserveAmmoYPos"	"12"	
		
		"PrimaryAmmoFont"		"TradeGothicShadow42"
		"ReserveAmmoFont"		"TradeGothicShadow19"		
		"PistolAmmoFont"		"TradeGothicShadow19"
	
		// ammo icons
		"AmmoIconXPos"	"964"	//64
		"AmmoIconYPos"	"16"
		"AmmoIconSize"	"10"	//10
		"SpecialAmmoXPos"	"37"
		"SpecialAmmoYPos"	"15"
				
		"PistolBoxWide"	"0"		//hardcoded,change PistolBoxTall instead
		"PistolBoxTall"	"0"
				
		"RightSideIndent"	"15"
		"IconSize"		"0"	// square weapon icon sizes			
		
		"SelectedItemColor"				"white"
		"UnselectedItemColor"			"white"
		"SelectedReserveAmmoColor"		"0 250 154 255"
		"UnselectedReserveAmmoColor"	"0 250 154 255"
		
		"InactiveItemColor"		"90 90 90 255"		[$WIN32]
		
		"SelectedScale"	"1.0"	// scale selected boxes by this much
	}

	CHudLocalPlayerDisplay
	{
		"fieldName" 	"CHudLocalPlayerDisplay"
		"visible"	"1"
		"enabled" 	"1"
		"usetitlesafe"	"1"
		"xpos"		"0"
		"ypos"		"0"
		"wide"		"f0"
		"tall"		"f0"
		"if_split_screen_left"
		{
			"xpos"	"0"
		}
		
		"if_split_screen_top"
		{
			"ypos"	"r90"
		}
	}

	"HudChat"
	{
		"ControlName"		"EditablePanel"
		"fieldName" 		"HudChat"
		"visible" 		"1"
		"enabled" 		"1"
		"xpos"			"0"
		"ypos"			"275"
		"wide"	 		"320"
		"tall"	 		"120"
		"PaintBackgroundType"	"0"
		"usetitlesafe"	"1"
		"bgcolor_override"		"blank"
	}
	
	HudFrustrationMeter
	{
		"fieldName"				"HudFrustrationMeter"
		"xpos"					"c-80"
		"ypos"					"10"
		"wide"					"200"
		"tall"					"84"
		"visible"				"1"
		"enabled"				"1"
		"PaintBackgroundType"	"0"
		"usetitlesafe"			"2"
	}
	
	// Tank approaching / Too far from Survivors
	HudZombiePanel
	{
		"fieldName" "HudZombiePanel"
		"visible" "1"
		"enabled" "1"
		"xpos"	"0"
		"ypos"	"c30"
		"wide"	"f0"
		"tall"	"155"
		"PaintBackgroundType"	"2"
		"if_split_screen_horizontal"
 		{
 			"ypos"	"c-45"			
  		}
  		"if_split_screen_left"
		{
			"xpos"	"c-145"
		}
		"if_split_screen_right"
		{
			"xpos"	"c-175"
		}
	}
	"CHudAbilityTimer"
	{
		"ControlName"	"CHudAbilityTimer"
		"fieldName"	"CHudAbilityTimer"
		"xpos"		"r95"
		"ypos"		"r83"
		"wide"		"80"
		"tall"		"80"
		"visible"	"1"
		"enabled"	"1"
		"ability_surpressed_color" "127 127 127 255"
		"ability_charging_color" "127 127 127 255"
		"ability_ready_color" "255 255 255 255"
		"usetitlesafe"	"1"
		
  		"if_split_screen_left"
		{
			"xpos"	"-8"
		}
	}
	"HudZombieHealth"
	{
		"fieldName"		"HudZombieHealth"
		"xpos"		"r95"
		"ypos"		"r83"
		"wide"		"400"
		"tall"		"150"
		"visible"		"1"
		"enabled"		"1"
		"usetitlesafe"	"1"
		  		
  		"if_split_screen_left"
		{
			"xpos"	"1"
		}
	}
	CHudZombieTeamDisplay
	{
		"fieldName" "CHudZombieTeamDisplay"
		"visible" "1"
		"enabled" "1"
		"usetitlesafe"	"1"
		"xpos"		"10"	//-15
		"ypos"		"r85"
		"wide"		"f0"
		"tall"		"75"
		"zpos"	"50000"
		"VertPanelSpacing"   "0"	//useless
		"HorizPanelSpacing"   "98"
		"bgcolor_override"	"blank"
		"if_split_screen_horizontal"
		{
			"ypos"	"c-59"
		}
		"if_split_screen_vertical"
		{
			"xpos"	"c-140"
		}
	}
	HudGhostPanel
	{
		"fieldName"	"HudGhostPanel"
		"visible"	"1"
		"enabled"	"1"
		"xpos"		"0"		//c-180
		"ypos"		"c30"
		"wide"		"f0"	//350
		"tall"		"155"
		"WhiteText"	"192 192 192 255"
		"RedText"	"246 5 5 255"
		"padding"	"4"
 		"if_split_screen_horizontal"
 		{
			"ypos"	"c-45"			
  		}
  		"if_split_screen_left"
		{
			"xpos"	"c-145"
		}
		"if_split_screen_right"
		{
			"xpos"	"c-205"
		}
	}

	HudPZDamageRecord
	{
		"fieldName" "HudPZDamageRecord"
		"xpos"	"0"
		"ypos"	"0"
		"wide"	"f0"
		"tall"  "f0"
		"visible" "1"
		"enabled" "1"
		"PaintBackgroundType"	"0"
		"usetitlesafe" "1"
		"label_textalign"		"west"
		"if_split_screen_horizontal"
 		{
			"ypos"	"20"
			"label_textalign"		"west"
  		}
  		"if_split_screen_vertical"
 		{
			"ypos"	"20"
			"label_textalign"		"center"
  		}
		
		"bgcolor_override"		""
	}
	
	CHudTeamDisplay
	{
		"fieldName" "CHudTeamDisplay"
		"visible" "1"
		"enabled" "1"
		"usetitlesafe"	"1"
		"xpos"			"0"
		"ypos"			"0"
		"wide"			"f0"
		"tall"			"f0"
		"if_split_screen_horizontal"
		{
			"ypos"	"c-59"
		}
		"if_split_screen_vertical"
		{
			"xpos"			"c-300"
			"wide"			"600"
			"tall"			"100"
			"usetitlesafe"	"1"
		}
	}
	
	PZEndGamePanel
	{
		"fieldName" "PZEndGamePanel"
		"visible" "1"
		"enabled" "1"
		"xpos"	"0"
		"ypos"	"0"
		"wide"	"f0"
		"tall"	"f0"
	}
	
	"CHudVote"
	{
		"fieldName"		"CHudVote"
		"xpos"			"0"
		"ypos"			"0"
		"wide"			"f0"
		"tall"			"f0"
		"visible"		"1"
		"enabled"		"1"
		"PaintBackgroundType"	"0"
		"usetitlesafe"	"1"
	}
	
	HudScavengeProgress
	{
		"fieldName" "HudScavengeProgress"
		"visible" "1"
		"enabled" "1"
		"xpos"		"c-37"	
		"ypos"		"5"	
		"zpos"		"0"
		"wide"	 "85"
		"tall"	 "43"
		"PaintBackground"	"0"
	
		"NumberFont"		"HudNumbers"
	}
	
	HudSurvivalTimer
	{
		"fieldName" "HudSurvivalTimer"
		"visible"			"1"
		"enabled"			"1"
		"xpos"				"0"
		"ypos"				"0"
		"zpos"				"0"
		"wide"				"f0"
		"tall"				"f0"
		"PaintBackground"	"0"
		"NumberFont"		"HudNumbers"
	}

	HudScavengeTimer
	{
		"fieldName" "HudScavengeTimer"
		"visible" "1"
		"enabled" "1"
		"xpos"		"0"
		"ypos"		"0"
		"zpos"		"0"
		"wide"	 "f0"
		"tall"	 "f0"
		"PaintBackground"	"0"
	
		"NumberFont"		"HudNumbers"
	}
	//ink END ///////////////////////////////////////////////////////
	overview
	{
		"fieldname"				"overview"
		"visible"				"1"
		"enabled"				"1"
		"xpos"					"0"
		"ypos"					"480"
		"wide"					"0"
		"tall"					"0"
	}

	HudCommentary
	{
		"fieldName" "HudCommentary"
		"xpos"	"c-190"
		"ypos"	"350"
		"wide"	"380"
		"tall"  "40"
		"visible" "0"
		"enabled" "1"
		
		"alpha"		"0"
		
		"PaintBackgroundType"	"2"
		
		"bar_xpos"		"50"
		"bar_ypos"		"20"
		"bar_height"	"8"
		"bar_width"		"320"
		"speaker_xpos"	"50"
		"speaker_ypos"	"8"
		"count_xpos_from_right"	"10"	// Counts from the right side
		"count_ypos"	"8"
		
		"icon_texture"	"vgui/hud/icon_commentary"
		"icon_xpos"		"0"
		"icon_ypos"		"0"		
		"icon_width"	"40"
		"icon_height"	"40"
	}
	
	HudHDRDemo
	{
		"fieldName" "HudHDRDemo"
		"xpos"	"0"
		"ypos"	"0"
		"wide"	"640"
		"tall"  "480"
		"visible" "0"
		"enabled" "1"
		
		"Alpha"	"255"
		"PaintBackgroundType"	"2"
		
		"BorderColor"	"0 0 0 255"
		"BorderLeft"	"16"
		"BorderRight"	"16"
		"BorderTop"		"16"
		"BorderBottom"	"64"
		"BorderCenter"	"0"
		
		"TextColor"		"255 255 255 255"
		"LeftTitleY"	"422"
		"RightTitleY"	"422"
	}





	TargetID
	{
		"fieldName" "TargetID"
		"visible" "1"
		"enabled" "1"
		"xpos"		"c-320"
		"ypos"		"c-240"
		"wide"	 "640"
		"tall"	 "480"
	}

	PlayerLabel
	{
		"fieldName" "PlayerLabel"
		"visible" "1"
		"enabled" "1"
		"xpos"		"c-320"
		"ypos"		"c-240"
		"wide"	 "640"
		"tall"	 "480"
	}

	HudArmor
	{
		"fieldName"		"HudArmor"
		"xpos"	"156"
		"ypos"	"440"
		"wide"	"132"
		"tall"  "40"
		"visible" "1"
		"enabled" "1"

		"PaintBackgroundType"	"2"
		
		"icon_xpos"	"0"
		"icon_ypos"	"2"
		"digit_xpos" "34"
		"digit_ypos" "2"
	}
	
	HudSuit
	{
		"fieldName"		"HudSuit"
		"xpos"	"140"
		"ypos"	"432"
		"wide"	"108"
		"tall"  "36"
		"visible" "1"
		"enabled" "1"

		"PaintBackgroundType"	"2"

		
		"text_xpos" "8"
		"text_ypos" "20"
		"digit_xpos" "50"
		"digit_ypos" "2"
	}

	HudProgressBar
	{
		"fieldName" "HudProgressBar"
		"xpos"	"c-85"
		"ypos"	"c107"
		"if_split_screen_active"
		{
			"ypos"	"c-10"
		}
		"wide"	"175"
		"tall"  "45"
		"visible" "1"
		"enabled" "1"
		"PaintBackgroundType"	"0"
		"PaintBackground"	"0"
	}

	HudRoundTimer
	{
		"fieldName" "HudRoundTimer"
		"xpos"	"c-20"
		"ypos"	"440"
		"wide"	"120"
		"tall"  "40"
		"visible" "1"
		"enabled" "1"
		
		"PaintBackgroundType"	"2"

		"FlashColor" "HudIcon_Red"		

		"icon_xpos"		"0"
		"icon_ypos"		"2"
		"digit_xpos"	"34"
		"digit_ypos"	"2"
	}

	HudAccount
	{
		"fieldName" "HudAccount"
		"xpos"	"r134"
		"ypos"	"374"
		"wide"	"116"
		"tall"  "80"
		"visible" "1"
		"enabled" "1"

		"PaintBackgroundType"	"2"

		"icon_xpos"	"0"
		"icon_ypos"	"36"
		"digit_xpos" "104"
		"digit_ypos" "36"
		"icon2_xpos"	"0"
		"icon2_ypos"	"2"
		"digit2_xpos"	"104"
		"digit2_ypos"	"2"
	}

	HudShoppingCart
	{
		"fieldName" "HudShoppingCart"
		"xpos"	"16"
		"ypos"	"200"
		"wide"	"40"
		"tall"  "40"
		"visible" "1"
		"enabled" "1"

		"PaintBackgroundType"	"2"
		"IconColor"			"HudIcon_Green"

	}

	HudC4
	{
		"fieldName" "HudC4"
		"xpos"	"16"
		"ypos" 	"248"
		"wide"	"40"
		"tall"  "40"
		"visible" "1"
		"enabled" "1"
	

		"PaintBackgroundType"	"2"
		"IconColor"			"HudIcon_Green"
		"FlashColor"		"HudIcon_Red"

	}

	HudDefuser
	{
		"fieldName" "HudDefuser"
		"xpos"	"16"
		"ypos" 	"248"
		"wide"	"40"
		"tall"  "40"
		"visible" "1"
		"enabled" "1"

		"PaintBackgroundType"	"2"

		"IconColor"				"HudIcon_Green"

	}

	HudHostageRescueZone
	{
		"fieldName" "HudHostageRescueZone"
		"xpos"	"16"
		"ypos" 	"248"
		"wide"	"40"
		"tall"  "40"
		"visible" "1"
		"enabled" "1"
	

		"PaintBackgroundType"	"2"
		"IconColor"			"HudIcon_Green"
		"FlashColor"		"HudIcon_Red"
	}

	HudScenarioIcon 
	{
		"fieldName" "HudScenarioIcon"
		"xpos"	"c110"
		"ypos"	"443"
		"wide"	"40"
		"tall"  "44"
		"visible" "1"
		"enabled" "1"

		"PaintBackgroundType"	"2"

		"IconColor"				"Hostage_Yellow"	
	}

	HudFlashlight
	{
		"fieldName" "HudFlashlight"
		"visible" "1"
		"enabled" "1"
		"xpos"	"16"
		"ypos"	"370"
		"wide"	"102"
		"tall"	"20"
		
		"text_xpos" "8"
		"text_ypos" "6"
		"TextColor"	"255 170 0 220"

		"PaintBackgroundType"	"2"
	}
	
	HudDamageIndicator
	{
		"fieldName" "HudDamageIndicator"
		"visible" "1"
		"enabled" "1"

		// TF Damage Indicator vars
		"MinimumWidth" "40"
		"MaximumWidth" "80"
		"StartRadius" "120"
		"EndRadius" "80"
		"MinimumHeight" "30"
		"MaximumHeight" "60"
		"MinimumTime" "2"

		// CS Damage Indicator vars
		"DmgColorLeft" "255 0 0 0"
		"DmgColorRight" "255 0 0 0"
		
		"dmg_xpos" "30"
		"dmg_ypos" "100"
		"dmg_wide" "36"
		"dmg_tall1" "240"
		"dmg_tall2" "200"
	}

	HudZoom
	{
		"fieldName" "HudZoom"
		"visible" "1"
		"enabled" "1"
		"Circle1Radius" "66"
		"Circle2Radius"	"74"
		"DashGap"	"16"
		"DashHeight" "4"
		"BorderThickness" "88"
	}

	HudCrosshair
	{
		"fieldName" "HudCrosshair"
		"visible" "1"
		"enabled" "1"
		"wide"	 "640"
		"tall"	 "480"

		"ability_size"	"17"
		"ability_surpressed_color" "127 127 127 255"
		"ability_charging_color" "127 127 127 255"
		"ability_ready_color" "255 255 255 255"
	}

	HudDeathNotice
	{
		"fieldName" "HudDeathNotice"
		"visible" "1"
		"enabled" "1"
		"xpos"	 "0"
		"ypos"	 "0"
		"wide"	 "f0"
		"tall"	 "480"

		"MaxDeathNotices" "6"
		"IconSize"		"16"
		"TextFont"				"Default"
	}

	HudVehicle
	{
		"fieldName" "HudVehicle"
		"visible" "1"
		"enabled" "1"
		"wide"	 "640"
		"tall"	 "480"
	}


	CVProfPanel
	{
		"fieldName" "CVProfPanel"
		"visible" "1"
		"enabled" "1"
		"wide"	 "640"
		"tall"	 "480"
	}

	ScorePanel
	{
		"fieldName" "ScorePanel"
		"visible" "1"
		"enabled" "1"
		"wide"	 "640"
		"tall"	 "480"
	}

	HudTrain
	{
		"fieldName" "HudTrain"
		"visible" "1"
		"enabled" "1"
		"wide"	 "640"
		"tall"	 "480"
	}

	HudMOTD
	{
		"fieldName" "HudMOTD"
		"visible" "1"
		"enabled" "1"
		"wide"	 "640"
		"tall"	 "480"
	}

	HudMessage
	{
		"fieldName" "HudMessage"
		"visible" "1"
		"enabled" "1"
		"wide"	 "640"
		"tall"	 "480"
	}

	HudMenu
	{
		"fieldName" "HudMenu"
		"visible" "1"
		"enabled" "1"
		"wide"	 "640"
		"tall"	 "480"
		"zpos" "1"

		"TextFont"				"Default"
		"ItemFont"				"Default"
		"ItemFontPulsing"		"Default"
	}

	HudCloseCaption
	{
		"fieldName" "HudCloseCaption"
		"visible"	"1"
		"enabled"	"1"
		"xpos"			"c-100"
		"ypos"			"r95"
		"wide"			"200"
		"tall"			"85"
		"usetitlesafe"	"1"
		"if_split_screen_vertical"
		{
			"ypos"		"r160"
			"tall"		"108"
		}
		"if_split_screen_horizontal"
		{
			"xpos"		"0"
			"ypos"		"r220"
			"wide"		"275"
			"tall"		"108"
		}
		"BgAlpha"	"50"
		"GrowTime"		"0.10"
		"ItemHiddenTime"	"0.10"
		"ItemFadeInTime"	"0.10"
		"ItemFadeOutTime"	"0.10"
		"topoffset"		"0"
		"bgcolor_override"	""
		"zpos"	"-50000"
	}

	HudHistoryResource 
	{
		"fieldName" "HudHistoryResource"
		"visible" "1"
		"enabled" "1"
		"xpos"	 "r640"
		"wide"	 "640"
		"tall"	 "330"
		"history_gap" "55"
	}

	HudGeiger
	{
		"fieldName" "HudGeiger"
		"visible" "1"
		"enabled" "1"
		"wide"	 "640"
		"tall"	 "480"
	}

	HUDQuickInfo
	{
		"fieldName" "HUDQuickInfo"
		"visible" "1"
		"enabled" "1"
		"wide"	 "640"
		"tall"	 "480"
	}

	HudWeapon
	{
		"fieldName" "HudWeapon"
		"visible" "1"
		"enabled" "1"
		"wide"	 "640"
		"tall"	 "480"
	}
	HudAnimationInfo
	{
		"fieldName" "HudAnimationInfo"
		"visible" "1"
		"enabled" "1"
		"wide"	 "640"
		"tall"	 "480"
	}
	CBudgetPanel
	{
		"fieldName" "CBudgetPanel"
		"visible" "1"
		"enabled" "1"
		"wide"	 "640"
		"tall"	 "480"
	}
	CTextureBudgetPanel
	{
		"fieldName" "CTextureBudgetPanel"
		"visible" "1"
		"enabled" "1"
		"wide"	 "640"
		"tall"	 "480"
	}

	HudPredictionDump
	{
		"fieldName" "HudPredictionDump"
		"visible" "1"
		"enabled" "1"
		"wide"	 "640"
		"tall"	 "480"
	}

	HudScope
	{
		"fieldName" "HudZoom"
		"visible" "1"
		"enabled" "1"
		"wide"	 "640"
		"tall"	 "480"
	}

	HudVoiceSelfStatus
	{
		"fieldName" "HudVoiceSelfStatus"
		"visible" "1"
		"enabled" "1"
		"xpos"			"r25"
		"ypos"			"r105"
		"wide" 			"20"
		"tall" 			"20"
		
		"usetitlesafe"	"1"
		
		"if_split_screen_left"
		{
			"xpos"	"100"
		}
	}
	
	HudBiofeedback
	{
		"fieldName" "HudBiofeedback"
		"visible" "1"
		"enabled" "1"
		"xpos" "r128"
		"ypos" "r479"
		"wide" "128"
		"tall" "64"
				
		"usetitlesafe"	"1"
	}

	HudVoiceStatus
	{
		"fieldName" "HudVoiceStatus"
		"visible" "1"
		"enabled" "1"
		"xpos" "r130"
		"ypos" "0"
		"wide" "150"
		"tall" "290"

		"item_tall"	"15"
		"item_wide"	"120"

		"item_spacing" "2"

		"icon_ypos"	"0"
		"icon_xpos"	"0"
		"icon_tall"	"16"
		"icon_wide"	"16"

		"text_xpos"	"18"
		"text_font"	"DefaultDropShadow"
		
		"inverted"	"0"	// draws text in player color, no background
	}

	HudFlashbang
	{
	}

	HudTerritory
	{
		"fieldName" "HudTerritory"
		"visible" "1"
		"enabled" "1"
		"xpos"	"240"
	    	"ypos"	"432"
	    	"wide" "240"
	    	"tall" "48"
	}

	TerritorySCore
	{
	    "fieldName" "TerritoryScore"
	    "visible" "0"
	    "enabled" "0"
	    "xpos"	"240"
	    "ypos"	"450"
	    "wide" "200"
	    "tall" "200"
	    "text_xpos" "8"
	    "text_ypos" "4"
	}

	// TERROR:
	HudMessagePanel	// HudMessage is already taken :P
	{
		"fieldName"	"HudMessagePanel"
		"visible"	"0"
		"enabled" "1"
		"xpos"	"120"
		"ypos"	"r235"
		"wide"	"400"
		"tall"	"180"
		"PaintBackgroundType"	"2"
		"text_xpos"	"4"
		"text_ypos"	"4"
		"text_spacing"	"1"
	}

	HudBlood
	{
		"fieldName" "HudBlood"
		"visible" "1"
		"enabled" "1"
		"wide"	 "640"
		"tall"	 "480"
	}

	"CHudSurvivorTeamStatus"
	{
		"ControlName"		"CHudSurvivorTeamStatus"
		"fieldName"		"CHudSurvivorTeamStatus"
		"xpos"			"r85"
		"ypos"			"120"
		"wide"			"80"
		"tall"			"20"
		"visible"		"1"
		"enabled"		"1"
		"PaintBackgroundType"	"2"
	}

	HudFinaleMeter
	{
		"fieldName" "HudFinaleMeter"
		"visible" "1"
		"enabled" "1"
		"xpos"	"c-100"
		"ypos"	"12"
		"wide"	 "200"
		"tall"	 "20"
		"PaintBackgroundType"	"2" // rounded corners
	}
	
	HudInfectedVOIP
	{
		"fieldName"				"HudInfectedVOIP"
		"xpos"					"r130"
		"ypos"					"c100"
		"wide"					"120"
		"tall"					"84"
		"visible"				"1"
		"enabled"				"1"
		"PaintBackgroundType"	"0"
		"usetitlesafe"			"2"
	}

	HudCredits
	{
		"fieldName" "HudCredits"
		"visible" "1"
		"enabled" "1"
		"xpos"		"c-270"
		"ypos"		"c-190"
		"wide"	 "540"
		"tall"	 "380"
	}

	HudAnnouncement
	{
		"fieldName" "HudAnnouncement"
		"xpos"	"c-150"
		"ypos"	"300"
		"wide"	"300"
		"tall"  "15"
		"visible" "0"
		"enabled" "1"
		"PaintBackgroundType"	"2"
	}

	CHudTeamMateInPerilNotice
	{
		"fieldName" "CHudTeamMateInPerilNotice"
		"ypos"	"50"
		"visible" "1"
		"enabled" "1"
	}

	HudIntensityGraph
	{
		"fieldName" "HudIntensityGraph"
		"xpos"	"r75"
		"ypos"	"190"
		"wide"	"70"
		"tall"  "100"
		"visible" "1"
		"enabled" "1"
		"PaintBackgroundType"	"2"
	}
	
	HudLeavingAreaWarning
	{
		"fieldName" "HudLeavingAreaWarning"
		"xpos"	"10"
		"ypos"	"c26"
		"wide"	"200"
		"tall"  "14"
		"visible" "1"
		"enabled" "1"
		"PaintBackgroundType"	"2"
		"usetitlesafe"	"2"
	}
	
	CItemPickupPanel
	{
		"fieldName" "CItemPickupPanel"
		"xpos"	"0"
		"ypos"	"0"
		"wide"	"f0"
		"tall"  "f0"
		"visible" "1"
		"enabled" "1"
		"PaintBackgroundType"	"2"
		
		"usetitlesafe"	"0"
	}
	
	StatsCrawl
	{
		"fieldName" "StatsCrawl"
		"visible" "1"
		"enabled" "1"
		
		"xpos"	"0"			
		"ypos"	"0"			
		"wide"	"f0"
		"tall"  "f0"
		
		"vote_bot_inset_x" "150"	[$X360]
		"vote_bot_inset_y" "75"		[$X360]

		"skip_legend_inset_x"	"70"	[$X360]
		"skip_legend_inset_y"	"55"	[$X360]
		
		"vote_bot_inset_x" "90"		[$WIN32]
		"vote_bot_inset_y" "45"		[$WIN32]
		
		"skip_legend_inset_x"	"10"	[$WIN32]
		"skip_legend_inset_y"	"25"	[$WIN32]
		
		"SkipLabelFont"	"DefaultLarge"
		"ButtonFont"	"GameUIButtons"

		"StatsCrawlFont"	"OuttroStatsCrawl"
		"StatsCrawlUnderlineFont" "OuttroStatsCrawlUnderline"

		"CreditsCrawlFont"	"Credits"
		
		"votes"
		{
			"box_size"		"16"
			"spacer"		"4"
			"box_inset"		"1"
		}
	}
	
	HudHintDisplay	[$WIN32]
	{
		"fieldName"	"HudHintDisplay"
		"visible"	"0"
		"enabled" "1"
		"xpos"	"c-200"
		"ypos"	"294"
		"wide"	"400"
		"tall"	"50"
		"text_xpos"	"8"
		"text_ypos"	"8"
		"center_x"	"0"	// center text horizontally
		"center_y"	"-1"	// align text on the bottom
		
		"bgcolor_override"	"blank"
	}

	HudHintKeyDisplay
	{
		"fieldName"	"HudHintKeyDisplay"
		"visible"	"0"
		"enabled" 	"1"
		"xpos"		"r120"
		"ypos"		"r340"
		"wide"		"100"
		"tall"		"200"
		"text_xpos"	"8"
		"text_ypos"	"8"
		"text_xgap"	"8"
		"text_ygap"	"8"
		"TextColor"	"255 170 0 220"

		"PaintBackgroundType"	"2"
	}
}
