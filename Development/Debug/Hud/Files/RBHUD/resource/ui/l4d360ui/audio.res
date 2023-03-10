"Resource/UI/Audio.res"
{
	"Audio"
	{
		"ControlName"		"Frame"
		"fieldName"			"Audio"
		"xpos"				"0"
		"ypos"				"0"
		"wide"				"f0"
		"tall"				"448"
		"autoResize"		"0"
		"pinCorner"			"0"
		"visible"			"1"
		"enabled"			"1"
		"tabPosition"		"0"
	}
	
	"ImgBackground"
	{
		"ControlName"			"L4DMenuBackground"
		"fieldName"				"ImgBackground"
		"xpos"				"0"
		"ypos"				"90"	//79
		"zpos"				"-1"
		"wide"				"f0"
		"tall"				"265"
		"autoResize"			"0"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"0"
		"fillColor"				"TransparentBlack"
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
	
	"BtnCancelCustom" [$WIN32]
	{
		"ControlName"			"L4D360HybridButton"
		"fieldName"				"BtnCancelCustom"
		"xpos"					"0"
		"ypos"					"68"
		"zpos"					"1"
		"wide"					"f0"
		"tall"					"15"
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"1"
		"wrap"					"1"
		"labelText"				""
		"tooltiptext"			""
		"style"					"MainMenuButton"
		"command"				"Back"
		"proportionalToParent"	"0"
		"usetitlesafe" 			"0"
		EnabledTextInsetX		"2"
		DisabledTextInsetX		"2"
		FocusTextInsetX			"2"
		OpenTextInsetX			"2"
		"allcaps"				"0"
	}
	
	"BtnCancelCustomText"
	{
		"ControlName"			"Label"
		"fieldName"				"BtnCancelCustomText"
		"xpos"					"0"
		"ypos"					"68"
		"zpos"					"1"
		"wide"					"f0"
		"tall"					"15"
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"0"
		"labelText"			"SAVE"
		"textAlignment"		"center"
		"font"				"MainBold"
	}
	
	"SldGameVolume"
	{
		"ControlName"			"SliderControl"
		"fieldName"				"SldGameVolume"
		"xpos"					"c-180"
		"ypos"					"95"
		"zpos"					"3"
		"wide"					"360"
		"tall"					"15"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"0"
		"minValue"				"0.0"
		"maxValue"				"1.0"
		"stepSize"				"0.05"
		"navUp"					"Btn3rdPartyCredits"
		"navDown"				"SldMusicVolume"
		"conCommand"			"volume"
		"inverseFill"			"0"
				
		//button and label
		"BtnDropButton"
		{
			"ControlName"			"L4D360HybridButton"
			"fieldName"				"BtnDropButton"
			"xpos"					"0"
			"ypos"					"0"
			"zpos"					"0"
			"wide"					"360"
			"wideatopen"			"260"	[$WIN32 && !$WIN32WIDE]
			"tall"					"15"
			"autoResize"			"1"
			"pinCorner"				"0"
			"visible"				"1"
			"enabled"				"1"
			"tabPosition"			"1"
			"AllCaps"				"1"
			"labelText"				"#GameUI_SoundEffectVolume"
			"tooltiptext"			"#L4D360UI_AudioOptions_Tooltip_Volume"
			"disabled_tooltiptext"	"#L4D360UI_AudioOptions_Tooltip_Volume_Disabled"
			"style"					"MainMenuButton"
			"command"				""
			"ActivationType"		"1"
			"OnlyActiveUser"		"1"
			"usablePlayerIndex"		"nobody"
		}
	}
	
	"SldMusicVolume"
	{
		"ControlName"			"SliderControl"
		"fieldName"				"SldMusicVolume"
		"xpos"					"c-180"
		"ypos"					"115"
		"zpos"					"3"
		"wide"					"360"
		"tall"					"15"
		"visible"				"1"
		"enabled"				"1"
		"usetitlesafe"			"0"
		"tabPosition"			"0"
		"minValue"				"0.0"
		"maxValue"				"1.0"
		"stepSize"				"0.05"
		"navUp"					"SldGameVolume"
		"navDown"				"DrpSpeakerConfiguration"
		"conCommand"			"snd_musicvolume"
		"inverseFill"			"0"
		
		//button and label
		"BtnDropButton"
		{
			"ControlName"			"L4D360HybridButton"
			"fieldName"				"BtnDropButton"
			"xpos"					"0"
			"ypos"					"0"
			"zpos"					"0"
			"wide"					"360"
			"wideatopen"			"260"	[$WIN32 && !$WIN32WIDE]
			"tall"					"15"
			"autoResize"			"1"
			"pinCorner"				"0"
			"visible"				"1"
			"enabled"				"1"
			"tabPosition"			"0"
			"AllCaps"				"1"
			"labelText"				"#GameUI_MusicVolume"
			"tooltiptext"			"#L4D360UI_AudioOptions_Tooltip_MusicVolume"
			"disabled_tooltiptext"	"#L4D360UI_AudioOptions_Tooltip_MusicVolume"
			"style"					"MainMenuButton"
			"command"				""
			"ActivationType"		"1"
			"OnlyActiveUser"		"1"
			"usablePlayerIndex"		"nobody"
		}
	}
	
	"DrpSpeakerConfiguration"
	{
		"ControlName"		"DropDownMenu"
		"fieldName"			"DrpSpeakerConfiguration"
		"xpos"				"c-180"
		"ypos"				"135"
		"zpos"				"3"
		"wide"				"360"
		"tall"				"15"
		"visible"			"1"
		"enabled"			"1"
		"usetitlesafe"		"0"
		"tabPosition"		"0"
		"navUp"				"SldMusicVolume"
		"navDown"			"DrpSoundQuality"
				
		//button and label
		"BtnDropButton"
		{
			"ControlName"				"L4D360HybridButton"
			"fieldName"					"BtnDropButton"
			"xpos"						"0"
			"ypos"						"0"
			"zpos"						"0"
			"wide"						"360"
			"wideatopen"				"260"	[$WIN32 && !$WIN32WIDE]
			"tall"						"15"
			"autoResize"				"1"
			"pinCorner"					"0"
			"visible"					"1"
			"enabled"					"1"
			"tabPosition"				"1"
			"AllCaps"					"1"
			"labelText"					"#GameUI_SpeakerConfiguration"
			"tooltiptext"				"#L4D_spkr_config_tip"
			"style"						"DropDownButton"
			"command"					"FlmSpeakerConfiguration"
			"ActivationType"			"1"
			"OnlyActiveUser"			"1"
		}
	}
	
	//flyouts		
	"FlmSpeakerConfiguration"
	{
		"ControlName"			"FlyoutMenu"
		"fieldName"				"FlmSpeakerConfiguration"
		"visible"				"0"
		"wide"					"0"
		"tall"					"0"
		"zpos"					"4"
		"InitialFocus"			"BtnHeadphones"
		"ResourceFile"			"resource/UI/L4D360UI/DropDownSpeakerConfiguration.res"
		"OnlyActiveUser"		"1"
	}
	
	"DrpSoundQuality"
	{
		"ControlName"		"DropDownMenu"
		"fieldName"			"DrpSoundQuality"
		"xpos"				"c-180"
		"ypos"				"155"
		"zpos"				"3"
		"wide"				"360"
		"tall"				"15"
		"visible"			"1"
		"enabled"			"1"
		"usetitlesafe"		"0"
		"tabPosition"		"0"
		"navUp"				"DrpSpeakerConfiguration"
		"navDown"			"DrpCaptioning"
				
		//button and label
		"BtnDropButton"
		{
			"ControlName"				"L4D360HybridButton"
			"fieldName"					"BtnDropButton"
			"xpos"						"0"
			"ypos"						"0"
			"zpos"						"0"
			"wide"						"360"
			"wideatopen"				"260"	[$WIN32 && !$WIN32WIDE]
			"tall"						"15"
			"autoResize"				"1"
			"pinCorner"					"0"
			"visible"					"1"
			"enabled"					"1"
			"tabPosition"				"1"
			"AllCaps"					"1"
			"labelText"					"#GameUI_SoundQuality"
			"tooltiptext"				"#L4D_sound_qual_tip"
			"style"						"DropDownButton"
			"command"					"FlmSoundQuality"
			"ActivationType"			"1"
			"OnlyActiveUser"			"1"
		}
	}
	
	//flyouts		
	"FlmSoundQuality"
	{
		"ControlName"			"FlyoutMenu"
		"fieldName"				"FlmSoundQuality"
		"visible"				"0"
		"wide"					"0"
		"tall"					"0"
		"zpos"					"4"
		"InitialFocus"			"BtnHigh"
		"ResourceFile"			"resource/UI/L4D360UI/DropDownSoundQuality.res"
		"OnlyActiveUser"		"1"
	}
	
	"DrpCaptioning"
	{
		"ControlName"		"DropDownMenu"
		"fieldName"			"DrpCaptioning"
		"xpos"				"c-180"
		"ypos"				"175"
		"zpos"				"3"
		"wide"				"360"
		"tall"				"15"
		"visible"			"1"
		"enabled"			"1"
		"usetitlesafe"		"0"
		"tabPosition"		"0"
		"navUp"				"DrpSoundQuality"
		"navDown"			"DrpVoiceCommunication"
				
		//button and label
		"BtnDropButton"
		{
			"ControlName"				"L4D360HybridButton"
			"fieldName"					"BtnDropButton"
			"xpos"						"0"
			"ypos"						"0"
			"zpos"						"0"
			"wide"						"360"
			"wideatopen"				"260"	[$WIN32 && !$WIN32WIDE]
			"tall"						"15"
			"autoResize"				"1"
			"pinCorner"					"0"
			"visible"					"1"
			"enabled"					"1"
			"tabPosition"				"1"
			"AllCaps"					"1"
			"labelText"					"#GameUI_Captioning"
			"tooltiptext"				"#L4D360UI_AudioOptions_Tooltip_Caption"
			"disabled_tooltiptext"		"#L4D360UI_AudioOptions_Tooltip_Caption_Disabled"
			"style"						"DropDownButton"
			"command"					"FlmCaption"
			"ActivationType"			"1"
			"OnlyActiveUser"			"1"
		}
	}
	
	//flyouts		
	"FlmCaption"
	{
		"ControlName"			"FlyoutMenu"
		"fieldName"				"FlmCaption"
		"visible"				"0"
		"wide"					"0"
		"tall"					"0"
		"zpos"					"4"
		"InitialFocus"			"BtnOff"
		"ResourceFile"			"resource/UI/L4D360UI/DropDownCaption.res"
		"OnlyActiveUser"		"1"
	}
	
	"DrpLanguage"
	{
		"ControlName"			"DropDownMenu"
		"fieldName"				"DrpLanguage"
		"xpos"					"c-180"
		"ypos"					"195"
		"zpos"					"3"
		"wide"					"360"
		"tall"					"15"
		"visible"				"0"
		"enabled"				"0"
		"usetitlesafe"			"0"
		"tabPosition"			"0"
		"navUp"					"DrpCaptioning"
		"navDown"				"DrpVoiceCommunication"
				
		//button and label
		"BtnDropButton"
		{
			"ControlName"				"L4D360HybridButton"
			"fieldName"					"BtnDropButton"
			"xpos"						"0"
			"ypos"						"0"
			"zpos"						"0"
			"wide"						"360"
			"wideatopen"				"260"	[$WIN32 && !$WIN32WIDE]
			"tall"						"15"
			"autoResize"				"1"
			"pinCorner"					"0"
			"visible"					"0"
			"enabled"					"0"
			"tabPosition"				"1"
			"AllCaps"					"1"
			"labelText"					"#GAMEUI_AudioSpokenLanguage"
			"tooltiptext"				"#L4D360UI_AudioOptions_Tooltip_Language"
			"disabled_tooltiptext"		"#L4D360UI_AudioOptions_Tooltip_Language_Disabled"
			"style"						"DropDownButton"
			"command"					"FlmLanguage"
			"ActivationType"			"1"
			"OnlyActiveUser"			"1"
		}
	}

	//flyouts		
	"FlmLanguage"
	{
		"ControlName"			"FlyoutMenu"
		"fieldName"				"FlmLanguage"
		"visible"				"0"
		"wide"					"0"
		"tall"					"0"
		"zpos"					"4"
		"InitialFocus"			"BtnOtherLanguage"
		"ResourceFile"			"resource/UI/L4D360UI/DropDownLanguagePC.res"
		"OnlyActiveUser"		"1"
	}
	
	"DrpVoiceCommunication"
	{
		"ControlName"		"DropDownMenu"
		"fieldName"			"DrpVoiceCommunication"
		"xpos"				"c-180"
		"ypos"				"215"
		"zpos"				"3"
		"wide"				"360"
		"tall"				"15"
		"visible"			"1"
		"enabled"			"1"
		"usetitlesafe"		"0"
		"tabPosition"		"0"
		"navUp"				"DrpCaptioning"
		"navDown"			"DrpVoiceCommunicationStyle"
				
		//button and label
		"BtnDropButton"
		{
			"ControlName"				"L4D360HybridButton"
			"fieldName"					"BtnDropButton"
			"xpos"						"0"
			"ypos"						"0"
			"zpos"						"0"
			"wide"						"360"
			"wideatopen"				"260"	[$WIN32 && !$WIN32WIDE]
			"tall"						"15"
			"autoResize"				"1"
			"pinCorner"					"0"
			"visible"					"1"
			"enabled"					"1"
			"tabPosition"				"1"
			"AllCaps"					"1"
			"labelText"					"#GameUI_EnableVoice"
			"tooltiptext"				"#L4D_enable_voice_tip"
			"style"						"DropDownButton"
			"command"					"FlmVoiceCommunication"
			"ActivationType"			"1"
			"OnlyActiveUser"			"1"
		}
	}
	
	//flyouts		
	"FlmVoiceCommunication"
	{
		"ControlName"			"FlyoutMenu"
		"fieldName"				"FlmVoiceCommunication"
		"visible"				"0"
		"wide"					"0"
		"tall"					"0"
		"zpos"					"4"
		"InitialFocus"			"BtnOn"
		"ResourceFile"			"resource/UI/L4D360UI/DropDownVoiceCommunication.res"
		"OnlyActiveUser"		"1"
	}
	
	"DrpVoiceCommunicationStyle"
	{
		"ControlName"		"DropDownMenu"
		"fieldName"			"DrpVoiceCommunicationStyle"
		"xpos"				"c-180"
		"ypos"				"235"
		"zpos"				"3"
		"wide"				"360"
		"tall"				"15"
		"visible"			"1"
		"enabled"			"1"
		"usetitlesafe"		"0"
		"tabPosition"		"0"
		"navUp"				"DrpVoiceCommunication"
		"navDown"			"SldVoiceVoxThreshold"
				
		//button and label
		"BtnDropButton"
		{
			"ControlName"				"L4D360HybridButton"
			"fieldName"					"BtnDropButton"
			"xpos"						"0"
			"ypos"						"0"
			"zpos"						"0"
			"wide"						"360"
			"wideatopen"				"260"	[$WIN32 && !$WIN32WIDE]
			"tall"						"15"
			"autoResize"				"1"
			"pinCorner"					"0"
			"visible"					"1"
			"enabled"					"1"
			"tabPosition"				"1"
			"AllCaps"					"1"
			"labelText"					"#GameUI_VoiceCommStyle"
			"tooltiptext"				"#L4D_voice_comm_tip"
			"disabled_tooltiptext"		"#L4D_disabled_voice_tip"
			"style"						"DropDownButton"
			"command"					"FlmVoiceCommunicationStyle"
			"ActivationType"			"1"
			"OnlyActiveUser"			"1"
		}
	}
	
	//flyouts		
	"FlmVoiceCommunicationStyle"
	{
		"ControlName"			"FlyoutMenu"
		"fieldName"				"FlmVoiceCommunicationStyle"
		"visible"				"0"
		"wide"					"0"
		"tall"					"0"
		"zpos"					"4"
		"InitialFocus"			"BtnOn"
		"ResourceFile"			"resource/UI/L4D360UI/DropDownVoiceCommunicationStyle.res"
		"OnlyActiveUser"		"1"
	}
	
	"SldVoiceVoxThreshold"
	{
		"ControlName"			"SliderControl"
		"fieldName"				"SldVoiceVoxThreshold"
		"xpos"					"c-180"
		"ypos"					"255"
		"zpos"					"3"
		"wide"					"360"
		"tall"					"15"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"0"
		"minValue"				"1.0"
		"maxValue"				"2000"
		"stepSize"				"100"
		"navUp"					"DrpVoiceCommunicationStyle"
		"navDown"				"SldVoiceTransmitVolume"
		"conCommand"				"voice_threshold"
		"inverseFill"				"1"
				
		//button and label
		"BtnDropButton"
		{
			"ControlName"			"L4D360HybridButton"
			"fieldName"				"BtnDropButton"
			"xpos"					"0"
			"ypos"					"0"
			"zpos"					"0"
			"wide"					"360"
			"wideatopen"			"260"	[$WIN32 && !$WIN32WIDE]
			"tall"					"15"
			"autoResize"			"1"
			"pinCorner"				"0"
			"visible"				"1"
			"enabled"				"1"
			"tabPosition"			"0"
			"AllCaps"				"1"
			"labelText"				"#GameUI_VoiceSensitivity"
			"tooltiptext"			"#L4D_mic_sens_tip"
			"disabled_tooltiptext"	"#L4D_disabled_threshold_tip"
			"style"					"MainMenuButton"
			"command"				""
			"ActivationType"		"1"
			"OnlyActiveUser"		"1"
			"usablePlayerIndex"		"nobody"
		}
	}

	"SldVoiceTransmitVolume"
	{
		"ControlName"			"SliderControl"
		"fieldName"				"SldVoiceTransmitVolume"
		"xpos"					"c-180"
		"ypos"					"275"
		"zpos"					"3"
		"wide"					"360"
		"tall"					"15"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"0"
		"minValue"				"0.0"
		"maxValue"				"100.0"
		"stepSize"				"10.0"
		"navUp"					"SldVoiceVoxThreshold"
		"navDown"				"SldVoiceReceiveVolume"
		"conCommand"			""
		"inverseFill"			"0"
				
		//button and label
		"BtnDropButton"
		{
			"ControlName"			"L4D360HybridButton"
			"fieldName"				"BtnDropButton"
			"xpos"					"0"
			"ypos"					"0"
			"zpos"					"0"
			"wide"					"360"
			"wideatopen"			"260"	[$WIN32 && !$WIN32WIDE]
			"tall"					"15"
			"autoResize"			"1"
			"pinCorner"				"0"
			"visible"				"1"
			"enabled"				"1"
			"tabPosition"			"0"
			"AllCaps"				"1"
			"labelText"				"#GameUI_VoiceTransmitVolume"
			"tooltiptext"			"#L4D_voice_transmit_tip"
			//"disabled_tooltiptext"	"#L4D_disabled_voice_transmit_tip"
			"style"					"MainMenuButton"
			"command"				""
			"ActivationType"		"1"
			"OnlyActiveUser"		"1"
			"usablePlayerIndex"		"nobody"
		}
	}
	
	"SldVoiceReceiveVolume"
	{
		"ControlName"			"SliderControl"
		"fieldName"				"SldVoiceReceiveVolume"
		"xpos"					"c-180"
		"ypos"					"295"
		"zpos"					"3"
		"wide"					"360"
		"tall"					"15"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"0"
		"minValue"				"0.0"
		"maxValue"				"1.0"
		"stepSize"				"0.05"
		"navUp"					"SldVoiceTransmitVolume"
		"navDown"				"DrpBoostMicrophone"
		"conCommand"			"voice_scale"
		"inverseFill"			"0"
				
		//button and label
		"BtnDropButton"
		{
			"ControlName"			"L4D360HybridButton"
			"fieldName"				"BtnDropButton"
			"xpos"					"0"
			"ypos"					"0"
			"zpos"					"0"
			"wide"					"360"
			"wideatopen"			"260"	[$WIN32 && !$WIN32WIDE]
			"tall"					"15"
			"autoResize"			"1"
			"pinCorner"				"0"
			"visible"				"1"
			"enabled"				"1"
			"tabPosition"			"0"
			"AllCaps"				"1"
			"labelText"				"#GameUI_VoiceReceiveVolume"
			"tooltiptext"			"#L4D_voice_receive_tip"
			"disabled_tooltiptext"	"#L4D_disabled_voice_tip"
			"style"					"MainMenuButton"
			"command"				""
			"ActivationType"		"1"
			"OnlyActiveUser"		"1"
			"usablePlayerIndex"		"nobody"
		}
	}
	
	"DrpBoostMicrophone"
	{
		"ControlName"		"DropDownMenu"
		"fieldName"			"DrpBoostMicrophone"
		"xpos"				"c-180"
		"ypos"				"315"
		"zpos"				"3"
		"wide"				"360"
		"tall"				"15"
		"visible"			"1" [!$OSX]
		"visible"			"0" [$OSX]
		"enabled"			"1"
		"usetitlesafe"		"0"
		"tabPosition"		"0"
		"navUp"				"SldVoiceReceiveVolume"
		"navDown"			"BtnTestMicrophone"
				
		//button and label
		"BtnDropButton"
		{
			"ControlName"				"L4D360HybridButton"
			"fieldName"					"BtnDropButton"
			"xpos"						"0"
			"ypos"						"0"
			"zpos"						"0"
			"wide"						"360"
			"wideatopen"				"260"	[$WIN32 && !$WIN32WIDE]
			"tall"						"15"
			"autoResize"				"1"
			"pinCorner"					"0"
			"visible"					"1"
			"enabled"					"1"
			"tabPosition"				"1"
			"AllCaps"					"1"
			"labelText"					"#GameUI_BoostMicrophone"
			"tooltiptext"				"#L4D_boost_mic_gain_tip"
			"disabled_tooltiptext"		"#L4D_disabled_voice_tip"
			"style"						"DropDownButton"
			"command"					"FlmBoostMicrophone"
			"ActivationType"			"1"
			"OnlyActiveUser"			"1"
		}
	}

	//flyouts		
	"FlmBoostMicrophone" 
	{
		"ControlName"			"FlyoutMenu"
		"fieldName"				"FlmBoostMicrophone"
		"visible"				"0"
		"wide"					"0"
		"tall"					"0"
		"zpos"					"4"
		"InitialFocus"			"BtnOn"
		"ResourceFile"			"resource/UI/L4D360UI/DropDownBoostMicrophone.res"
		"OnlyActiveUser"		"1"
	}
	
	"BtnTestMicrophone"
	{
		"ControlName"			"L4D360HybridButton"
		"fieldName"				"BtnTestMicrophone"
		"xpos"					"c-180"
		"ypos"					"335"
		"zpos"					"0"
		"wide"					"200"
		"tall"					"15"
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"1"
		"enabled"				"1"
		"tabPosition"			"0"
		"wrap"					"1"
		"navUp"					"DrpBoostMicrophone"
		"navDown"				"BtnCancel"
		"AllCaps"				"1"
		"labelText"				"#GameUI_TestMicrophone"
		"tooltiptext"			"#L4D_test_mic_tip"
		"disabled_tooltiptext"	"#L4D_disabled_voice_tip"
		"style"					"MainMenuButton"
		"command"				"TestMicrophone"
		EnabledTextInsetX		"2"
		DisabledTextInsetX		"2"
		FocusTextInsetX			"2"
		OpenTextInsetX			"2"
	}
	
	"MicMeter"
	{
		"ControlName"		"ImagePanel"
		"fieldName"			"MicMeter"
		"xpos"				"c107"
		"ypos"				"332"
		"wide"				"64"
		"tall"				"16"
		"autoResize"		"0"
		"pinCorner"			"0"
		"visible"			"1"
		"enabled"			"1"
		"tabPosition"		"0"
		"scaleImage"		"1"
		"image"				"resource/mic_meter_dead"
		"image2"			"resource/mic_meter_live"
		"barCount"			"19"
		"barSpacing"		"8"
	}
	
	"MicMeter2"
	{
		"ControlName"		"ImagePanel"
		"fieldName"			"MicMeter2"
		"xpos"				"c107"
		"ypos"				"332"
		"wide"				"64"
		"tall"				"16"
		"autoResize"		"0"
		"pinCorner"			"0"
		"visible"			"1"
		"enabled"			"1"
		"tabPosition"		"0"
		"scaleImage"		"1"
		"image"				"resource/mic_meter_live"
		"barCount"			"19"
		"barSpacing"		"8"
	}
	
	"MicMeterIndicator"
	{
		"ControlName"		"ImagePanel"
		"fieldName"			"MicMeterIndicator"
		"xpos"				"c107"
		"ypos"				"332"
		"wide"				"16"
		"tall"				"16"
		"autoResize"		"0"
		"pinCorner"			"0"
		"visible"			"1"
		"enabled"			"1"
		"tabPosition"		"0"
		"scaleImage"		"1"
		"image"				"resource/mic_meter_indicator"
		"barCount"			"19"
		"barSpacing"		"8"
	}
	
	"BtnCancel"
	{
		"ControlName"			"L4D360HybridButton"
		"fieldName"				"BtnCancel"
		"xpos"					"c-180"
		"ypos"					"355"
		"zpos"					"0"
		"wide"					"200"
		"tall"					"15"
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"0"
		"enabled"				"1"
		"tabPosition"			"0"
		"wrap"					"1"
		"navUp"					"BtnTestMicrophone"
		"navDown"				"Btn3rdPartyCredits"
		"AllCaps"				"1"
		"labelText"				"#L4D360UI_Done"
		"tooltiptext"			"#L4D360UI_Tooltip_Back"
		"style"					"MainMenuButton"
		"command"				"Back"
		EnabledTextInsetX		"2"
		DisabledTextInsetX		"2"
		FocusTextInsetX			"2"
		OpenTextInsetX			"2"
	}
		
	"Btn3rdPartyCredits"
	{
		"ControlName"			"L4D360HybridButton"
		"fieldName"				"Btn3rdPartyCredits"
		"xpos"					"c-140"
		"ypos"					"395"
		"zpos"					"0"
		"wide"					"280"
		"tall"					"15"
		"autoResize"			"1"
		"pinCorner"				"0"
		"visible"				"0"
		"enabled"				"1"
		"tabPosition"			"0"
		"wrap"					"1"
		"navUp"					"BtnCancel"
		"navDown"				"SldGameVolume"
		"AllCaps"				"1"
		"labelText"				"#GameUI_ThirdPartyAudio_Title"
		"tooltiptext"			"#GameUI_ThirdPartyTechCredits"
		"style"					"DialogButton"
		"command"				"3rdPartyCredits"
		EnabledTextInsetX		"2"
		DisabledTextInsetX		"2"
		FocusTextInsetX			"2"
		OpenTextInsetX			"2"
	}
}
