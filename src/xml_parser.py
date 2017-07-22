#!/usr/bin/python3
import sys
from xml.etree import ElementTree

class XmlParser():
	rootElement = 0
	xmlPath = str("")
	tree = 0
	
	def __init__(self, filePath):
		self.tree = ElementTree.parse(str(filePath))
		self.rootElement = self.tree.getroot()
		self.xmlPath = filePath
		
	def partNumber(self, name):
		no = 1
		for i in name:
			if (i=="/"):
				no=no+1
		return no
		
	def getParts(self, name):
		parts = list()
		current = str("")
		for i in name:
			if (i=="/"):
				parts.append(current)
				current = str("")
			else:
				current+=i
		parts.append(current)
		return parts
		
	def getElementData(self, name):
		content = str("")
		no = self.partNumber(name)
		if (no>1):
			parts = self.getParts(name)
			subElement = self.rootElement.find(parts[0])
			if (subElement==None):
				return content
			lastElement = 0
			for no in range(len(parts)):
				if (no==0):
					lastElement = subElement
				else:
					subElement = lastElement.find(parts[no])
					lastElement = subElement
			content = subElement.text
		else:
			sub = self.rootElement.find(name)
			if (sub!=None):
				content = sub.text
		return content
		
	def getElementAttribute(self, name, attrName):
		content = str("")
		no = self.partNumber(name)
		if (no>1):
			parts = self.getParts(name)
			subElement = self.rootElement.find(parts[0])
			if (subElement==None):
				return content
			lastElement = 0
			for no in range(len(parts)):
				if (no==0):
					lastElement = subElement
				else:
					subElement = lastElement.find(parts[no])
					lastElement = subElement
			content = subElement.get(attrName)
		else:
			sub = self.rootElement.find(name)
			if (sub!=None):
				content = sub.get(attrName)
		return content
		
	def setElementValue(self, name, value):
		no = self.partNumber(name)
		if (no>1):
			parts = self.getParts(name)
			subElement = self.rootElement.find(parts[0])
			if (subElement==None):
				return
			lastElement = 0
			for no in range(len(parts)):
				if (no==0):
					lastElement = subElement
				else:
					subElement = lastElement.find(parts[no])
					lastElement = subElement
			subElement.text = str(value)
		else:
			sub = self.rootElement.find(name)
			sub.text = str(value)
		self.tree.write(self.xmlPath)
		
	def setElementAttribute(self, name, attrName, value):
		no = self.partNumber(name)
		if (no>1):
			parts = self.getParts(name)
			subElement = self.rootElement.find(parts[0])
			if (subElement==None):
				return
			lastElement = 0
			for no in range(len(parts)):
				if (no==0):
					lastElement = subElement
				else:
					subElement = lastElement.find(parts[no])
					lastElement = subElement
			subElement.set(attrName,value)
		else:
			sub = self.rootElement.find(name)
			sub.set(attrName,value)
		self.tree.write(self.xmlPath)
