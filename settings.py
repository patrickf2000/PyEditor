#!/usr/bin/python3
from os import getenv
from os.path import exists
from gen_settings import generate_settings
from xml_parser import XmlParser

class Settings():
	settingsPath = str("")
	parser = 0
	
	def __init__(self):
		path = str(getenv("HOME"))
		path+=str("/.cpp-editor/settings.xml")
		self.settingsPath = path
		if (exists(path)==False):
			generate_settings()
		self.parser = XmlParser(path)
			
	def getSetting(self, ID, defaultSetting):
		setting = str("")
		try:
			setting = self.parser.getElementData(ID)
		except Exception:
			setting = defaultSetting
		return setting
		
	def getAttributeSetting(self, ID, attrID, defaultSetting):
		setting = str("")
		try:
			setting = self.parser.getElementAttribute(ID,attrID)
		except Exception:
			setting = defaultSetting
		if (setting==None):
			setting = defaultSetting
		return setting
		
	def writeSetting(self,ID,value):
		self.parser.setElementValue(ID,value)
		
	def writeAttributeSetting(self,ID,attr,attrValue):
		self.parser.setElementAttribute(ID,attr,attrValue)
