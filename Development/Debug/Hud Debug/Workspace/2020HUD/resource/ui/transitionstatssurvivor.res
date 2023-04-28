// Coop end of round score screen
"Resource/UI/TransitionStatsSurvivor.res"
{

	CVersusModeResults
	{
		"fieldname"    "VersusModeResults"
		"controlName"  "CVersusModeResults"
		"visible"      "1"
		"enabled"      "1"
		"xpos"         "c-182"
		"ypos"         "95"
		"wide"         "364"
		"tall"         "120"
	}

	NextMap
	{
		"fieldname"         "NextMap"
		"controlName"       "Label"
		"visible"           "1"
		"enabled"           "1"
		"xpos"              "47"
		"ypos"              "21"
		"wide"              "f0"
		"tall"              "20"
		"usetitlesafe"      "1"
		"autoResize"        "0"
		"brighttext"        "0"
		"dulltext"          "0"
		"fgcolor_override"  ""
		"font"              "Cerbetica18Shadow"
		"pinCorner"         "0"
		"textAlignment"     "north-west"
		"wrap"              "0"
	}
	
	WorkingAnim
	{
		"fieldname"     "WorkingAnim"
		"controlName"   "ImagePanel"
		"visible"       "1"
		"enabled"       "1"
		"xpos"          "20"
		"ypos"          "20"
		"zpos"          "5"
		"wide"          "20"
		"tall"          "20"
		"usetitlesafe"  "1"
		"frame"         "0"
		"image"         "common/l4d_spinner"
		"scaleImage"    "1"
		"tabPosition"   "0"
	}
	
	WorkingAnimDebug
	{
		"fieldname"     "WorkingAnimDebug"
		"controlName"   "ImagePanel"
		"visible"       "0"
		"enabled"       "1"
		"xpos"          "20"
		"ypos"          "20"
		"zpos"          "5"
		"wide"          "20"
		"tall"          "20"
		"usetitlesafe"  "1"
		"frame"         "0"
		"image"         "common/l4d_spinner"
		"scaleImage"    "1"
		"tabPosition"   "0"
	}

	SurvivorHighlightStatsPanel
	{
		"fieldname"        "SurvivorHighlightStatsPanel"
		"controlName"      "DontAutoCreate"
		"visible"          "1"
		"enabled"          "1"
		"xpos"             "c-211"
		"ypos"             "122"
		"wide"             "440"
		"tall"             "190"
		"autoResize"       "0"
		"paintbackground"  "0"
		"pinCorner"        "0"
		"tabPosition"      "0"
	}

	transition_stats
	{
		"fieldname"              "transition_stats"
		"controlName"            "CTransitionStatsPanel"
		"visible"                "1"
		"enabled"                "1"
		"xpos"                   "0"
		"ypos"                   "0"
		"wide"                   "f0"
		"tall"                   "480"
		"autoResize"             "0"
		"pinCorner"              "0"
		"statpanel_y_in_vsmode"  "205"
		"tabPosition"            "0"
	}
	
	
	
	
	
	///////////////////////////////////////////////////////////////////
	
	CheckpointCleared
	{
		"fieldname"         "CheckpointCleared"
		"controlName"       "Label"
		"visible"           "0"
		"enabled"           "0"
		"xpos"              "45"
		"ypos"              "15"
		"wide"              "500"
		"tall"              "24"
		"usetitlesafe"      "1"
		"autoResize"        "0"
		"brighttext"        "0"
		"dulltext"          "0"
		"fgcolor_override"  "White"
		"font"              "TransitionTitle"
		"labelText"         "#L4D_ReportScreen_Title_Safe"
		"pinCorner"         "0"
		"textAlignment"     "north-west"
	}
	
	TipPanel
	{
		"fieldname"     "TipPanel"
		"visible"              "0"
		"enabled"              "0"
		"xpos"          "10"
		"ypos"          "r60"
		"zpos"          "50"
		"wide"          "400"
		"tall"          "100"
		"usetitlesafe"  "1"
		"autoResize"    "1"
		"scaleimage"    "1"
	}
	
	FooterBackground
	{
		"fieldname"         "FooterBackground"
		"controlName"       "Panel"
		"visible"              "0"
		"enabled"              "0"
		"xpos"              "0"
		"ypos"              "r90"
		"zpos"              "-2"
		"wide"              "f0"
		"tall"              "f0"
		"autoResize"        "0"
		"bgcolor_override"  "Black"
		"pinCorner"         "0"
		"tabPosition"       "0"
	}

	FooterBorder
	{
		"fieldname"         "FooterBorder"
		"controlName"       "Panel"
		"visible"              "0"
		"enabled"              "0"
		"xpos"              "0"
		"ypos"              "r90"
		"wide"              "f0"
		"tall"              "1"
		"autoResize"        "0"
		"bgcolor_override"  "100 100 100 255"
		"paintbackground"   "1"
		"pinCorner"         "0"
	}

	HeaderBackground
	{
		"fieldname"         "HeaderBackground"
		"controlName"       "Panel"
		"visible"              "0"
		"enabled"              "0"
		"xpos"              "0"
		"ypos"              "0"
		"zpos"              "-2"
		"wide"              "f0"
		"tall"              "80"
		"autoResize"        "0"
		"bgcolor_override"  "Black"
		"paintbackground"   "1"
		"pinCorner"         "0"
		"tabPosition"       "0"
	}

	HeaderBorder
	{
		"fieldname"         "HeaderBorder"
		"controlName"       "Panel"
		"visible"              "0"
		"enabled"              "0"
		"xpos"              "0"
		"ypos"              "80"
		"wide"              "f0"
		"tall"              "1"
		"autoResize"        "0"
		"bgcolor_override"  "100 100 100 255"
		"paintbackground"   "1"
		"pinCorner"         "0"
	}
	
	ClockIcon
	{
		"fieldname"            "ClockIcon"
		"controlName"          "CIconPanel"
		"visible"              "0"
		"enabled"              "0"
		"xpos"                 "10"
		"ypos"                 "15"
		"wide"                 "24"
		"tall"                 "24"
		"usetitlesafe"         "1"
		"PaintBackgroundType"  "0"
		"autoResize"           "0"
		"icon"                 "clock_1"
		"pinCorner"            "0"
		"scaleimage"           "1"
		"tabPosition"          "0"
	}
	
	LoadingText
	{
		"fieldname"      "LoadingText"
		"controlName"    "Label"
		"visible"              "0"
		"enabled"              "0"
		"xpos"           "r250"
		"ypos"           "20999"
		"zpos"           "5"
		"wide"           "200"
		"tall"           "20"
		"usetitlesafe"   "1"
		"autoResize"     "1"
		"Font"           "DefaultLarge"
		"labelText"      "#L4D360UI_Loading"
		"pinCorner"      "0"
		"tabPosition"    "0"
		"textAlignment"  "east"
		"border"			"cyanborder"
	}
}
