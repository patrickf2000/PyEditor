from PyQt5.QtWidgets import QPlainTextEdit
from PyQt5.QtGui import QFontMetrics
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtCore import Qt

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
		

