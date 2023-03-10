Scheme
{
	Fonts
	{
		// DEFAULT
		// fonts are used in order that they are listed
		// fonts listed later in the order will only be used if they fulfill a range not already filled
		// if a font fails to load then the subsequent fonts will replace
		"Default"
		{
			"1"
			{
				"name"			"Stubble bold"		[($WIN32 && $WIN32HIDEF) || ($X360 && ($X360WIDE && $X360HIDEF))]
				"name"			"Trade Gothic Bold" [($WIN32 && !$WIN32HIDEF) || ($X360 && !($X360WIDE && $X360HIDEF))]
				"tall"			"12"    [$WIN32]
				"tall"			"14"    [$X360]
				"weight"		"400"
				"range"			"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"antialias"		"1"
			}	
		}
		"DefaultDropShadow"
		{
			"1"
			{
				"name"			"Stubble bold"		[($WIN32 && $WIN32HIDEF) || ($X360 && ($X360WIDE && $X360HIDEF))]
				"name"			"Trade Gothic Bold" [($WIN32 && !$WIN32HIDEF) || ($X360 && !($X360WIDE && $X360HIDEF))]
				"tall"			"12"
				"weight"		"900"
				"range"			"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"dropshadow"	"1"
				"antialias"		"1"
			}
		}
		
		// Radial
		"DefaultDropShadowBold"
		{
			"1"
			{
				"name"		"Cerbetica"
				"tall"		"10"
				"weight"	"500"
				"dropshadow"	"1"
				"antialias"		"1"
			}
		}
		"DefaultSmall"
		{
			"1"
			{
				"name"			"Stubble bold"		[($WIN32 && $WIN32HIDEF) || ($X360 && ($X360WIDE && $X360HIDEF))]
				"name"			"Trade Gothic Bold" [($WIN32 && !$WIN32HIDEF) || ($X360 && !($X360WIDE && $X360HIDEF))]
				"tall"			"12"
				"weight"		"0"
				"range"			"0x0000 0x017F"
				"antialias"		"1"
			}
		}
		"DefaultVerySmall"
		{
			"1"
			{
				"name"			"Tahoma"
				"tall"			"12"
				"weight"		"0"
				"range"			"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"antialias"		"1"
			}
		}
		"DefaultLarge"
		{
			"1"
			{
				"name"			"Cerbetica"
				"tall"			"18"
				"weight"		"400"
				"antialias"		"1"
			}
		}
		"DefaultLargeDropShadow"
		{
			"1"
			{
				"name"			"Stubble bold"		[($WIN32 && $WIN32HIDEF) || ($X360 && ($X360WIDE && $X360HIDEF))]
				"name"			"Trade Gothic Bold" [($WIN32 && !$WIN32HIDEF) || ($X360 && !($X360WIDE && $X360HIDEF))]
				"tall"			"18"
				"weight"		"700"
				"antialias"		"1"
				"dropshadow"	"1"
			}
		}
		
		// Radial Select
		"DefaultLargeDropShadowBold"
		{
			"1"
			{
				"name"			"Cerbetica"
				"tall"			"12"
				"weight"		"900"
				"antialias"		"1"
				"dropshadow"	"1"
			}
		}
		"DefaultMedium"
		{
			"1"
			{
				"name"			"Stubble bold"		[($WIN32 && $WIN32HIDEF) || ($X360 && ($X360WIDE && $X360HIDEF))]
				"name"			"Trade Gothic Bold" [($WIN32 && !$WIN32HIDEF) || ($X360 && !($X360WIDE && $X360HIDEF))]
				"tall"			"12"
				"weight"		"400"
				"antialias"		"1"
			}
		}
		"FrameTitle"
		{
			"1"
			{
				"name"			"Stubble bold"		[($WIN32 && $WIN32HIDEF) || ($X360 && ($X360WIDE && $X360HIDEF))]
				"name"			"Trade Gothic Bold" [($WIN32 && !$WIN32HIDEF) || ($X360 && !($X360WIDE && $X360HIDEF))]
				"tall"			"18"				[$WIN32]
				"tall"			"24"				[$X360]
				"weight"		"700"
				"antialias"		"1"
			}
		}
		HudHintText
		{
			"1"
			{
				"name"			"Stubble bold"		[($WIN32 && $WIN32HIDEF) || ($X360 && ($X360WIDE && $X360HIDEF))]
				"name"			"Trade Gothic Bold" [($WIN32 && !$WIN32HIDEF) || ($X360 && !($X360WIDE && $X360HIDEF))]
				"tall"			"12"
				"weight"		"400"
				"antialias"		"1"
			}
		}
		AwardText
		{
			"1"
			{
				"name"			"Stubble bold"		[($WIN32 && $WIN32HIDEF) || ($X360 && ($X360WIDE && $X360HIDEF))]
				"name"			"Trade Gothic Bold" [($WIN32 && !$WIN32HIDEF) || ($X360 && !($X360WIDE && $X360HIDEF))]
				"tall"			"12"
				"weight"		"700"
				"dropshadow"	"1"
				"antialias"		"1"
			}
		}
		"MessageText"
		{
			"1"
			{
				"name"			"Stubble bold"		[($WIN32 && $WIN32HIDEF) || ($X360 && ($X360WIDE && $X360HIDEF))]
				"name"			"Trade Gothic Bold" [($WIN32 && !$WIN32HIDEF) || ($X360 && !($X360WIDE && $X360HIDEF))]
				"tall"			"10"
				"weight"		"400"
				"antialias"		"1"
			}
		}
		"OuttroStatsCrawl"
		{
			"1"
			{
				"name"			"Cerbetica"
				"tall"			"10"
				"weight"		"400"
				"antialias"		"1"
			}
		}
		"OuttroStatsCrawlUnderline"	
		{
			"1"
			{
				"name"			"Cerbetica"
				"tall"			"14"
				"weight"		"400"
				// "underline"	"1"
				"antialias"		"1"
			}
		}
		"OuttroStatsCrawlTitles"
		{
			"1"
			{
				"name"			"Cerbetica"
				"tall"			"18"
				"weight"		"400"
				"antialias"		"1"
			}
		}
		"PlayerDisplayName"	
		{
			"1"
			{
				"name"			"Stubble bold"		[($WIN32 && $WIN32HIDEF) || ($X360 && ($X360WIDE && $X360HIDEF))]
				"name"			"Trade Gothic Bold" [($WIN32 && !$WIN32HIDEF) || ($X360 && !($X360WIDE && $X360HIDEF))]
				"tall"			"14"
				"weight"		"400"
				"antialias"		"1"
			}
		}
		"PlayerDisplayNameSmall"	
		{
			"1"
			{
				"name"			"Stubble bold"		[($WIN32 && $WIN32HIDEF) || ($X360 && ($X360WIDE && $X360HIDEF))]
				"name"			"Trade Gothic Bold" [($WIN32 && !$WIN32HIDEF) || ($X360 && !($X360WIDE && $X360HIDEF))]
				"tall"			"12"
				"weight"		"400"
				"antialias"		"1"
			}
		}
		PlayerDisplayHealth
		{
			"1"
			{
				"name"			"Stubble bold"		[($WIN32 && $WIN32HIDEF) || ($X360 && ($X360WIDE && $X360HIDEF))]
				"name"			"Trade Gothic Bold" [($WIN32 && !$WIN32HIDEF) || ($X360 && !($X360WIDE && $X360HIDEF))]
				"tall"			"15"
				"weight"		"400"
				"antialias"		"1"
			}
		}
		HudNumbersSmall
		{
			"1"
			{
				"name"			"Stubble bold"		[($WIN32 && $WIN32HIDEF) || ($X360 && ($X360WIDE && $X360HIDEF))]
				"name"			"Trade Gothic Bold" [($WIN32 && !$WIN32HIDEF) || ($X360 && !($X360WIDE && $X360HIDEF))]
				"tall"			"16"
				"weight"		"1000"
				"additive"		"1"
				"antialias"		"1"
				"range"			"0x0000 0x017F"
			}
		}

		HudSelectionNumbers
		{
			"1"
			{
				"name"			"Stubble bold"		[($WIN32 && $WIN32HIDEF) || ($X360 && ($X360WIDE && $X360HIDEF))]
				"name"			"Trade Gothic Bold" [($WIN32 && !$WIN32HIDEF) || ($X360 && !($X360WIDE && $X360HIDEF))]
				"tall"			"11"
				"weight"		"700"
				"antialias"		"1"
				"additive"		"1"
				"range"			"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
			}
		}

		HudSelectionText
		{
			"1"
			{
				"name"			"Stubble bold"		[($WIN32 && $WIN32HIDEF) || ($X360 && ($X360WIDE && $X360HIDEF))]
				"name"			"Trade Gothic Bold" [($WIN32 && !$WIN32HIDEF) || ($X360 && !($X360WIDE && $X360HIDEF))]
				"tall"			"11"
				"weight"		"700"
				"antialias"		"1"
				"yres"			"1 599"				[$WIN32]
				"range"			"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"additive"		"1"
			}
			"2" [$WIN32]
			{
				"name"			"Stubble bold"		[($WIN32 && $WIN32HIDEF) || ($X360 && ($X360WIDE && $X360HIDEF))]
				"name"			"Trade Gothic Bold" [($WIN32 && !$WIN32HIDEF) || ($X360 && !($X360WIDE && $X360HIDEF))]
				"tall"			"11"
				"weight"		"700"
				"antialias"		"1"
				"yres"			"600 767"
				"range"			"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"additive"		"1"
			}
			"3" [$WIN32]
			{
				"name"			"Stubble bold"		[($WIN32 && $WIN32HIDEF) || ($X360 && ($X360WIDE && $X360HIDEF))]
				"name"			"Trade Gothic Bold" [($WIN32 && !$WIN32HIDEF) || ($X360 && !($X360WIDE && $X360HIDEF))]
				"tall"			"12"
				"weight"		"900"
				"antialias"		"1"
				"yres"			"768 1023"
				"range"			"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
			}
			"4" [$WIN32]
			{
				"name"			"Stubble bold"		[($WIN32 && $WIN32HIDEF) || ($X360 && ($X360WIDE && $X360HIDEF))]
				"name"			"Trade Gothic Bold" [($WIN32 && !$WIN32HIDEF) || ($X360 && !($X360WIDE && $X360HIDEF))]
				"tall"			"16"
				"weight"		"900"
				"antialias"		"1"
				"yres"			"1024 1199"
				"range"			"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
			}
			"5" [$WIN32]
			{
				"name"			"Stubble bold"		[($WIN32 && $WIN32HIDEF) || ($X360 && ($X360WIDE && $X360HIDEF))]
				"name"			"Trade Gothic Bold" [($WIN32 && !$WIN32HIDEF) || ($X360 && !($X360WIDE && $X360HIDEF))]
				"tall"			"17"
				"weight"		"1000"
				"antialias"		"1"
				"yres"			"1200 10000"
				"range"			"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
			}
		}
		
		DebugOverlay
		{
			"1"
			{
				"name"			"Courier New"
				"tall"			"14"		[$WIN32 || !($X360WIDE && $X360HIDEF)]
				"tall"			"20"		[$X360 && ($X360WIDE && $X360HIDEF)]
				"weight"		"400"		[$WIN32]
				"outline"		"1"			[$WIN32]
				"weight"		"700"		[$X360]
				"range"			"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
			}
		}

		ClientTitleFont
		{
			"1"
			{
				"name"		"Stubble bold"
				"tall"		"60"
				"weight"	"700"
				"antialias" "1"
			}
		}

		InstructorButtons
		{
			"1"
			{
				"bitmap"	"1"
				"name"		"Buttons"
				"scalex"	"0.8"
				"scaley"	"0.8"
			}
		}

		InstructorButtonsSteamController
		{
			"1"
			{
				"bitmap"	"1"
				"name"		"ButtonsSC"
				"scalex"	"0.5"
				"scaley"	"0.5"
			}
		}

		GameUIButtons
		{
			"1"
			{
				"bitmap"	"1"
				"name"		"Buttons"
				"scalex"	"0.5"
				"scaley"	"0.5"
			}
		}

		HudNumbers
		{
			"1"
			{
				"name"		"Stubble bold"
				"tall"		"28"
				"weight"	"400"
				"additive"	"1"
				"antialias" "1"
			}
		}

		SurvivalNumbers
		{
			"1"
			{
				"name"		"Stubble bold"
				"tall"		"38"
				"weight"	"400"
				"additive"	"1"
				"antialias" "1"
			}
		}

		HudAmmo
		{
			"1"
			{
				"name"		"Stubble bold"		[($WIN32 && $WIN32HIDEF) || ($X360 && ($X360WIDE && $X360HIDEF))]
				"name"		"Trade Gothic Bold" [($WIN32 && !$WIN32HIDEF) || ($X360 && !($X360WIDE && $X360HIDEF))]
				"tall"		"18"
				"weight"	"0"
				"additive"	"1"
				"antialias" "1"
			}
		}
		
		HudAmmoSmall
		{
			"1"
			{
				"name"			"Stubble bold"		[($WIN32 && $WIN32HIDEF) || ($X360 && ($X360WIDE && $X360HIDEF))]
				"name"			"Trade Gothic Bold" [($WIN32 && !$WIN32HIDEF) || ($X360 && !($X360WIDE && $X360HIDEF))]
				"tall"			"12"
				"weight"		"0"
				"additive"		"1"
				"antialias"		"1"
			}
		}
		
		HUDHealth
		{
			"1"
			{
				"name"			"Stubble bold"		[($WIN32 && $WIN32HIDEF) || ($X360 && ($X360WIDE && $X360HIDEF))]
				"name"			"Trade Gothic Bold" [($WIN32 && !$WIN32HIDEF) || ($X360 && !($X360WIDE && $X360HIDEF))]
				"tall"			"18"
				"weight"		"0"
				"additive"		"1"
				"antialias"		"1"
			}
		}

		SpectatorTarget
		{
			"1"
			{
				"name"			"Stubble bold"		[($WIN32 && $WIN32HIDEF) || ($X360 && ($X360WIDE && $X360HIDEF))]
				"name"			"Trade Gothic Bold" [($WIN32 && !$WIN32HIDEF) || ($X360 && !($X360WIDE && $X360HIDEF))]
				"tall"			"14"
				"weight"		"400"
				"additive"		"1"
				"antialias"		"1"
			}
		}

		"CloseCaption_Normal"
		{
			"1" [$WIN32]
			{
				"name"		"Cerbetica"
				"tall"		"18"
				"weight"	"500"
				"yres"		"1 600"
				"dropshadow"	"1"
				"antialias"		"1"
			}
			"2" [$WIN32]
			{
				"name"		"Cerbetica"	//Tahoma
				"tall"		"22"
				"weight"	"500"
				"yres"		"601 1199"
				"dropshadow"	"1"
				"antialias"		"1"
			}
			"3"
			{
				"name"		"Cerbetica"
				"tall"		"26"
				"weight"	"500"
				"yres"		"1200 10000"
				"dropshadow"	"1"
				"antialias"		"1"
			}
		}
		
		"CloseCaption_Italic"
		{
			"1" [$WIN32]
			{
				"name"		"Cerbetica"
				"tall"		"18"
				"weight"	"500"
				"yres"		"1 600"
				"dropshadow"	"1"
				"antialias"		"1"
				"italic"	"1"
			}
			"2" [$WIN32]
			{
				"name"		"Cerbetica"	//Tahoma
				"tall"		"22"
				"weight"	"500"
				"yres"		"601 1199"
				"dropshadow"	"1"
				"antialias"		"1"
				"italic"	"1"
			}
			"3"
			{
				"name"		"Cerbetica"
				"tall"		"26"
				"weight"	"500"
				"yres"		"1200 10000"
				"dropshadow"	"1"
				"antialias"		"1"
				"italic"	"1"
			}
		}
		"CloseCaption_Bold"
		{
			"1" [$WIN32]
			{
				"name"		"Cerbetica"
				"tall"		"18"
				"weight"	"900"
				"yres"		"1 600"
				"dropshadow"	"1"
				"antialias"		"1"
			}
			"2" [$WIN32]
			{
				"name"		"Cerbetica"	//Tahoma
				"tall"		"22"
				"weight"	"900"
				"yres"		"601 1199"
				"dropshadow"	"1"
				"antialias"		"1"
			}
			"3"
			{
				"name"		"Cerbetica"
				"tall"		"26"
				"weight"	"900"
				"yres"		"1200 10000"
				"dropshadow"	"1"
				"antialias"		"1"
			}
		}
		"CloseCaption_BoldItalic"
		{
			"1" [$WIN32]
			{
				"name"		"Cerbetica"
				"tall"		"18"
				"weight"	"900"
				"yres"		"1 600"
				"dropshadow"	"1"
				"antialias"		"1"
				"italic"	"1"
			}
			"2" [$WIN32]
			{
				"name"		"Cerbetica"	//Tahoma
				"tall"		"22"
				"weight"	"900"
				"yres"		"601 1199"
				"dropshadow"	"1"
				"antialias"		"1"
				"italic"	"1"
			}
			"3"
			{
				"name"		"Cerbetica"
				"tall"		"26"
				"weight"	"900"
				"yres"		"1200 10000"
				"dropshadow"	"1"
				"antialias"		"1"
				"italic"	"1"
			}
		}
		"CloseCaption_Small"
		{
			"1" [$WIN32]
			{
				"name"		"Cerbetica"
				"tall"		"12"
				"weight"	"500"
				"yres"		"1 600"
				"dropshadow"	"1"
				"antialias"		"1"
			}
			"2" [$WIN32]
			{
				"name"		"Cerbetica"	//Tahoma
				"tall"		"18"
				"weight"	"500"
				"yres"		"601 1199"
				"dropshadow"	"1"
				"antialias"		"1"
			}
			"3"
			{
				"name"		"Cerbetica"
				"tall"		"20"
				"weight"	"500"
				"yres"		"1200 10000"
				"dropshadow"	"1"
				"antialias"		"1"
			}
		}
		
		// this is the symbol font
		"Marlett"
		{
			"1"
			{
				"name"		"Marlett"
				"tall"		"11"
				"weight"	"0"
				"symbol"	"1"
				"range"		"0x0000 0x007F"	//	Basic Latin
			}
		}
		"TransitionTitle" //L4D: Transition screen, death screen
		{
			"1"
			{
				"name"			"Stubble bold"		[($WIN32 && $WIN32HIDEF) || ($X360 && ($X360WIDE && $X360HIDEF))]
				"name"			"Trade Gothic Bold" [($WIN32 && !$WIN32HIDEF) || ($X360 && !($X360WIDE && $X360HIDEF))]
				"tall"			"24"
				"weight"		"400"
				"antialias"		"1"
			}
		}
		"MenuTitle" //Left 4 Dead
		{
			"1"
			{
				"name"			"Stubble bold"		[($WIN32 && $WIN32HIDEF) || ($X360 && ($X360WIDE && $X360HIDEF))]
				"name"			"Trade Gothic Bold" [($WIN32 && !$WIN32HIDEF) || ($X360 && !($X360WIDE && $X360HIDEF))]
				"tall"			"18"
				"weight"		"400"
				"antialias"		"1"
			}
		}
		"MenuTitle_DropShadow" //Left 4 Dead
		{
			"1"
			{
				"name"			"Stubble bold"		[($WIN32 && $WIN32HIDEF) || ($X360 && ($X360WIDE && $X360HIDEF))]
				"name"			"Trade Gothic Bold" [($WIN32 && !$WIN32HIDEF) || ($X360 && !($X360WIDE && $X360HIDEF))]
				"tall"			"18"
				"weight"		"400"
				"antialias"		"1"
				"dropshadow"	"1"
			}
		}
		"MenuSubTitle" //Left 4 Dead
		{
			"1"
			{
				"name"			"Stubble bold"		[($WIN32 && $WIN32HIDEF) || ($X360 && ($X360WIDE && $X360HIDEF))]
				"name"			"Trade Gothic Bold" [($WIN32 && !$WIN32HIDEF) || ($X360 && !($X360WIDE && $X360HIDEF))]
				"tall"			"12"
				"weight"		"400"
				"antialias"		"1"
			}
		}
		"BodyText_medium" //Left 4 Dead
		{
			"1"
			{
				"name"			"Stubble bold"		[($WIN32 && $WIN32HIDEF) || ($X360 && ($X360WIDE && $X360HIDEF))]
				"name"			"Trade Gothic Bold" [($WIN32 && !$WIN32HIDEF) || ($X360 && !($X360WIDE && $X360HIDEF))]
				"tall"			"14"
				"weight"		"400"
				"antialias"		"1"
			}
		}
		"BodyText_small" //Left 4 Dead
		{
			"1"
			{
				"name"			"Stubble bold"		[($WIN32 && $WIN32HIDEF) || ($X360 && ($X360WIDE && $X360HIDEF))]
				"name"			"Trade Gothic Bold" [($WIN32 && !$WIN32HIDEF) || ($X360 && !($X360WIDE && $X360HIDEF))]
				"tall"			"11"
				"weight"		"500"
				"antialias"		"1"
			}
		}
		"InstructorTitle"  //Left 4 Dead
		{
			"1"
			{
				"name"			"Cerbetica"
				"tall"			"10"
				"weight"		"500"
				"antialias"		"1"
				"dropshadow"	"1"
			}
		}
		"InstructorTitle_ss"  //Left 4 Dead
		{
			"1"
			{
				"name"			"Stubble bold"		[($WIN32 && $WIN32HIDEF) || ($X360 && ($X360WIDE && $X360HIDEF))]
				"name"			"Trade Gothic Bold" [($WIN32 && !$WIN32HIDEF) || ($X360 && !($X360WIDE && $X360HIDEF))]
				"tall"			"14"
				"weight"		"400"
				"antialias"		"1"
				"dropshadow"	"1"
			}
		}

		// purposely NOT using resolution overrides
		"TargetID"
		{
			"1"
			{
				"name"			"Cerbetica"		
				"tall"			"10"
				"weight"		"500"
				"antialias"		"1"
				"dropshadow"	"0"	// already enabled by code
			}
		}

		"Credits"
		{
			"1"
			{
				"name"		"Stubble bold"
				"tall"		"30"
				"weight"	"400"
				"range"		"0x0000 0x007F"	//	Basic Latin
				"antialias" "1"
				"additive"	"1"
			}
		}
		
		HL2WeaponIcons [$WIN32]
		{
			"1"
			{
				"name"			"HalfLife2"
				"tall"			"64"
				"weight"		"0"
				"antialias"		"1"
				"additive"		"1"
				"custom"		"1"
			}
		}
		
		"L4D_Icons"
		{
			"1"
			{
				"name"		"ToolBox"
				"tall"		"16"
				"weight"	"400"
				"range"		"0x0000 0x007F"	//	Basic Latin
				"antialias" "1"
				"additive"	"1"
			}
		}
		
		"L4D_Icons_medium"
		{
			"1"
			{
				"name"		"ToolBox"
				"tall"		"18"
				"weight"	"400"
				"range"		"0x0000 0x007F"	//	Basic Latin
				"antialias" "1"
				"additive"	"1"
			}
		}
		
		"L4D_Icons_large"
		{
			"1"
			{
				"name"		"ToolBox"
				"tall"		"24"
				"weight"	"400"
				"range"		"0x0000 0x007F"	//	Basic Latin
				"antialias" "1"
				"additive"	"1"
			}
		}
		
		"L4D_Weapons"
		{
			"1"
			{
				"name"		"ToolBox"
				"tall"		"30"
				"weight"	"400"
				"range"		"0x0000 0x007F"	//	Basic Latin
				"antialias" "1"
				"additive"	"1"
			}
		}
		
		"L4D_WeaponsSmall"
		{
			"1"
			{
				"name"		"ToolBox"
				"tall"		"28"
				"weight"	"400"
				"range"		"0x0000 0x007F"	//	Basic Latin
				"antialias" "1"
				"additive"	"1"
			}
		}
		
		"CommentaryDefault"
		{
			"1" [$X360]
			{
				"name"		"Verdana"
				"tall"		"14"	[$X360LODEF]
				"tall"		"20"	[$X360HIDEF]
				"weight"	"900"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"antialias"	"1"
			}
		
			"1" [$WIN32]
			{
				"name"		"Verdana"
				"tall"		"12"
				"weight"	"900"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"yres"		"480 599"
				"antialias"	"1"
			}
			"2" [$WIN32]
			{
				"name"		"Verdana"
				"tall"		"13"
				"weight"	"900"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"yres"		"600 767"
				"antialias"	"1"
			}
			"3" [$WIN32]
			{
				"name"		"Verdana"
				"tall"		"14"
				"weight"	"900"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"yres"		"768 1023"
				"antialias"	"1"
			}
			"4" [$WIN32]
			{
				"name"		"Verdana"
				"tall"		"20"
				"weight"	"900"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"yres"		"1024 1199"
				"antialias"	"1"
			}
			"5" [$WIN32]
			{
				"name"		"Verdana"
				"tall"		"24"
				"weight"	"900"
				"range"		"0x0000 0x017F" //	Basic Latin, Latin-1 Supplement, Latin Extended-A
				"yres"		"1200 6000"
				"antialias"	"1"
			}
			"6" [$WIN32]
			{
				"name"		"Verdana"
				"tall"		"12"
				"range" 	"0x0000 0x00FF"
				"weight"	"900"
				"antialias"	"1"

			}
			"7" [$WIN32]
			{
				"name"		"Arial"
				"tall"		"12"
				"range" 	"0x0000 0x00FF"
				"weight"	"800"
				"antialias"	"1"
			}			
		}
		
		"MainBold"
		{
			"1"
			{
				"name"			"Stubble bold"		[($WIN32 && $WIN32HIDEF) || ($X360 && ($X360WIDE && $X360HIDEF))]
				"name"			"Trade Gothic Bold" [($WIN32 && !$WIN32HIDEF) || ($X360 && !($X360WIDE && $X360HIDEF))]
				"tall"			"20"
				"weight"		"800"
				"antialias"		"1"
			}
		}

		"MainBoldBlur"
		{
			"1"
			{
				"name"			"Stubble bold"		[($WIN32 && $WIN32HIDEF) || ($X360 && ($X360WIDE && $X360HIDEF))]
				"name"			"Trade Gothic Bold" [($WIN32 && !$WIN32HIDEF) || ($X360 && !($X360WIDE && $X360HIDEF))]
				"tall"			"20"
				"weight"		"800"
				"blur"			"3"
				"antialias"		"1"
			}
		}
	}

	BitmapFontFiles
	{
		// UI buttons, custom font, (256x64)
		"Buttons"		"materials/vgui/fonts/buttons_32.vbf"
		"ButtonsSC"		"materials/vgui/fonts/buttons_sc_32.vbf"
	}

	//////////////////////// CUSTOM FONT FILES /////////////////////////////
	//
	// specifies all the custom (non-system) font files that need to be loaded to service the above described fonts
	// Range specificies the characters to be used from the custom font before falling back to a default font
	// characters in the range not specificed in the font will appear empty
	CustomFontFiles
	{
		"1"		"resource/Futurot.vfont"
		"2"		"resource/Toolbox.vfont"
		"3"     "resource/TG.vfont"
		"4"     "resource/TGB.vfont"
		"5"		"resource/HALFLIFE2.vfont"
		"6"		"resource/Stubble-Bold.vfont"	
	}
}