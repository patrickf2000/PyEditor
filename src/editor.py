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
from PyQt5.QtWidgets import QPlainTextEdit
from PyQt5.QtGui import QFontMetrics
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtCore import Qt
from settings import Settings

class Editor(QPlainTextEdit):
	filePath = str("")
	parent = 0
	saved = True

	def __init__(self, path, parentWindow):
		super().__init__()
		self.filePath = path
		self.parent = parentWindow
		self.textChanged.connect(self.onTextChanged)
		
		width = (QFontMetrics(self.currentCharFormat().font()).averageCharWidth())*2;
		self.setTabStopWidth(width);
		
	def setFilePath(self,path):
		self.filePath = str(path)
		
	def getFilePath(self):
		return self.filePath
		
	def setText(self,content):
		self.setPlainText(content)
		
	def getText(self):
		return self.toPlainText()
		
	def isUntitled(self):
		if (self.filePath=="untitled"):
			return True
		else:
			return False
			
	def isSaved(self):
		return self.saved
		
	def setSaved(self,save):
		self.saved=save
		self.parent.setSaved()
		
	def keyPressEvent(self,event):
		setting = Settings()
		result = setting.getSetting("editor/autoindent","true")
		if (result=="true"):
			self.autoIndent(event)
		else:
			super().keyPressEvent(event)
		
	def autoIndent(self,event):
		if ((event.key()==Qt.Key_Enter)or(event.key()==Qt.Key_Return)):
			lastLine = self.document().findBlockByNumber(self.textCursor().blockNumber()).text();
			tabCount = 0
			for i in lastLine:
				if (i=="\t"):
					tabCount+=1
			if (tabCount>0):
				super().keyPressEvent(event)
				for i in range(tabCount):
					self.insertPlainText("\t")
			else:
				super().keyPressEvent(event)
		else:
			super().keyPressEvent(event)
		
	def onTextChanged(self):
		self.saved = False
		self.parent.setUnsaved()
		

