"resource/hudlayout.res"
{
	overview
	{
		"visible"				"1"
		"fieldname"				"overview"
		"enabled"				"1"
		"xpos"					"0"
		"ypos"					"480"
		"wide"					"0"
		"tall"					"0"
	}

	// Tank approaching / Too far from Survivors
	HudZombiePanel
	{
		"fieldName" "HudZombiePanel"
		"visible" "1"
		"enabled" "1"
		"xpos"			"c-100"
		"ypos"			"c10"
		"wide"			"400"
		"tall"			"155"
		//"PaintBackgroundType"	"2"
		
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
			"xpos"	"c-100"
		}

		"if_split_screen_$WIN32" [$WIN32]
		{
			"xpos"	"c-360"
		}

		"if_split_screen_$X360" [$X360]
		{
			"xpos"	"c-360"
		}
		
		"if_split_screen_$X360GUEST" [$X360GUEST]
		{
			"xpos"	"c-460"
		}

		"if_split_screen_!$ENGLISH" [!$ENGLISH]
		{
			"xpos"	"c-560"
		}
	}
}
