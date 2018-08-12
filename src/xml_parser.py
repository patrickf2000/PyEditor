#!/usr/bin/python3
# Copyright 2018 Patrick Flynn
#
# Redistribution and use in source and binary forms, with or without modification, 
# are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, 
#	this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice, this 
#	list of conditions and the following disclaimer in the documentation and/or 
#	other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its contributors may 
#	be used to endorse or promote products derived from this software 
#	without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND 
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED 
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. 
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, 
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT 
# NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR 
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, 
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, 
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
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
