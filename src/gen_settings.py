#!/usr/bin/python3
from os import getenv, makedirs
import platform
import os.path

def genWindows(content):
	print("Generating for Windows...")
	
	path = str(getenv("USERPROFILE"))
	path+=str("\.py-editor\settings.xml")
	
	makedirs(os.path.dirname(path),exist_ok=True)
	
	with open(path,"w") as writer:
		writer.write(content)
		
	print("Done")

def genLinux(content):
	print("Generating for Linux...")

	path = str(getenv("HOME"))
	path+=str("/.py-editor/settings.xml")
	
	with open(path,"w") as writer:
		writer.write(content)
		
	print("Done")
	
def generate_settings():
	content = str("""<?xml version="1.0"?>
<settings>
	<window css="default">
		<winX>700</winX>
		<winY>600</winY>
	</window>
	<editor>
		<autoindent>true</autoindent>
	</editor>
</settings>""")
	
	if (platform.system()=="Windows"):
		genWindows(content)
	else:
		genLinux(content)
		
generate_settings()
