"resource/LoadingDiscPanel.res"
{
	CLoadingDiscPanel
	{
		"fieldName"	"CLoadingDiscPanel"
		"xpos"	"50"
		"ypos"	"40"
		"wide" 	"50"
		"tall"	"20"
		"PaintBackgroundType"	"0"
		
		"bgcolor_override"	"0 50 125 150"
		"border"			"noborder"
	}

	CLoadingDiscPanelCustom
	{
		"fieldName"	"CLoadingDiscPanelCustom"
		"xpos"	"50"
		"ypos"	"40"
		"wide" 	"50"
		"tall"	"20"
		"PaintBackgroundType"	"0"
		
		"bgcolor_override"	"0 50 125 150"
		"border"			"noborder"
	}

	LoadingLabel
	{
		"fieldName"	"LoadingLabel"
		"xpos" 	"0"
		"ypos"	"0999"
		"wide" 	"50"
		"tall"	"20"
		"labeltext"	"#GameUI_LoadingGame"
		"textAlignment"		"center"
		
		"fgcolor_override"		"125 100 50 255"
	}

	LoadingLabelCustom
	{
		"fieldname"      "LoadingLabelCustom"
		"controlName"    "Label"
		"xpos" 			"0"
		"ypos"			"0"
		"wide" 			"50"
		"tall"			"20"
		"font"           "Cerbetica10Shadow"
		"labelText"      "Paused"
		"textAlignment"  "center"
		//"border"			"baseborder"
	}

	LoadingProgress
	{
		"fieldName"	"LoadingProgress"
		"xpos" 	"430"
		"ypos"	"240"
		"wide"	"920"
		"tall"	"80"
	}
	
}
