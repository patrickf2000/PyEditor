from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon

from tabpane import TabPane
from main_toolbar import MainToolBar

from file_menu import FileMenu

class Window(QMainWindow):
	statusbar = 0
	savedLabel = 0
	pathLabel = 0
	tabs = 0

	def __init__(self):
		super().__init__()
		self.resize(600,500)
		self.setWindowTitle("PyEditor")
		self.setWindowIcon(QIcon.fromTheme("accessories-text-editor"))
		
		self.statusbar = self.statusBar()
		
		self.savedLabel = QLabel("saved")
		self.statusbar.addWidget(self.savedLabel)
		
		self.pathLabel = QLabel("untitled")
		self.statusbar.addWidget(self.pathLabel)
		
		self.tabs = TabPane(self)
		self.setCentralWidget(self.tabs)
		
		toolbar = MainToolBar(self.tabs)
		self.addToolBar(toolbar)
		
		fileMenu = self.menuBar().addMenu("File")
		FileMenu().initMenu(fileMenu,self.tabs)
		
	def setUnsaved(self):
		self.savedLabel.setText("unsaved")
		
	def setSaved(self):
		self.savedLabel.setText("saved")
		
	def setPathLabel(self,path):
		self.pathLabel.setText(path)
		
	def checkSave(self):
		ok = True
		details = list()
		for i in range(self.tabs.count()):
			current = self.tabs.widgetAt(i)
			if (current.isSaved() is False):
				ok = False
				details.append(current.getFilePath())
		if (not ok):
			msg = QMessageBox()
			msg.setWindowTitle("Warning!")
			msg.setText("You have unsaved documents!\n"
						"Do you wish to exit?")
			content = str("")
			for line in details:
				content+=str(line)+str("\n")
			msg.setDetailedText(str(content))
			msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
			msg.setDefaultButton(QMessageBox.No)
			msg.setIcon(QMessageBox.Warning)
			ret = msg.exec_()
			if (ret==QMessageBox.Yes):
				ok = True
			else:
				ok = False
		return ok
		
	def closeEvent(self,event):
		if self.checkSave():
			event.accept()
		else:
			event.ignore()
			

