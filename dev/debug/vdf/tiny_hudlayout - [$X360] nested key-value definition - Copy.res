//[$X360] nested key-value definition 'if_split_screen_top' under HudGhostPanel
"Resource/HudLayout.res"
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
		"xpos"			"c-190"
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
			"xpos"	"c-175"
		}
	}

 	HudGhostPanel
	{
		"fieldName"		"HudGhostPanel"
		"visible"		"1"
		"enabled"		"1"
		"xpos"			"c-180"
		"ypos"			"c10"
		"wide"			"400"
		"tall"			"155"
		"WhiteText"		"192 192 192 255"
		"RedText"		"246 5 5 255"
		"padding"		"4"
		
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
		
		"if_split_screen_top"	[$X360]
		{
			"ypos"	"c-70"
		}
	}
}
