from PyQt5.QtWidgets import QFileDialog
from tabpane import TabPane
from editor import Editor

class FileActions():
	@staticmethod
	def openFile(tabpane):
		chooser = QFileDialog()
		chooser.setAcceptMode(QFileDialog.AcceptOpen)
		if (not chooser.exec_()):
			return
		if (len(chooser.selectedFiles())==0):
			return
		path = chooser.selectedFiles()[0]
		content = str("")
		with open(path) as reader:
			for line in reader:
				content+=str(line)
		
		edit = tabpane.getCurrentWidget()
		if (edit.isUntitled()):
			if (edit.isSaved()):
				tabpane.getCurrentWidget().setText(content)
				tabpane.getCurrentWidget().setFilePath(path)
				tabpane.setCurrentTabTitle(path)
		else:
			tabpane.addNewTab(path)
			tabpane.getCurrentWidget().setText(content)
		tabpane.getCurrentWidget().setSaved(True)
		tabpane.getParentWidget().setPathLabel(path)
		
	@staticmethod
	def saveFile(tabpane):
		edit = tabpane.getCurrentWidget()
		if (edit.isUntitled()):
			FileActions.saveFileAs(tabpane)
		else:
			path = edit.getFilePath()
			txt = edit.getText()
			with open(path,"w") as writer:
				writer.write(txt)
			tabpane.getParentWidget().setSaved()
			edit.setSaved(True)
		
	@staticmethod
	def saveFileAs(tabpane):
		chooser = QFileDialog()
		chooser.setAcceptMode(QFileDialog.AcceptSave)
		if (chooser.exec_()):
			if (len(chooser.selectedFiles())==0):
				return
			path = chooser.selectedFiles()[0]
			tabpane.getCurrentWidget().setFilePath(path)
			tabpane.setCurrentTabTitle(path)
			tabpane.getParentWidget().setSaved()
			tabpane.getParentWidget().setPathLabel(path)
			FileActions.saveFile(tabpane)
			
		
