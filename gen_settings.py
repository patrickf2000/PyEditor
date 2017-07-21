#!/usr/bin/python3
from os import getenv

def generate_settings():
	content = str("""<?xml version="1.0"?>
<settings>
	<subwindows>
		<char_selector>true</char_selector>
		<date_selector>true</date_selector>
		<console>true</console>
	</subwindows>
	<window css="default">
		<winX>700</winX>
		<winY>600</winY>
	</window>
	<toolbar css="default">
		<newFile>true</newFile>
		<openFile>true</openFile>
		<saveFile>true</saveFile>
		<saveFileAs>true</saveFileAs>
		<cut>true</cut>
		<copy>true</copy>
		<paste>true</paste>
		<undo>true</undo>
		<redo>true</redo>
		<webBrowser>true</webBrowser>
		<testFile>true</testFile>
		<syntaxmenu>true</syntaxmenu>
		<fontsize>true</fontsize>
	</toolbar>
	<menubar css="default" />
	<statusbar css="default" />
	<editor>
		<autoindent>true</autoindent>
		<line_color>#d9d9d9</line_color>
	</editor>
</settings>""")
	
	path = str(getenv("HOME"))
	path+=str("/.cpp-editor/settings.xml")
	
	with open(path,"w") as writer:
		writer.write(content)
		writer.close()
		
generate_settings()
