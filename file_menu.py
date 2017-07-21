from PyQt5.QtWidgets import QMenu, QAction, qApp
from PyQt5.QtGui import QIcon
from file_actions import FileActions

class FileMenu():
	tabs = 0

	def initMenu(self,menu,tabpane):
		self.tabs = tabpane
	
		newAction = QAction(QIcon.fromTheme("document-new"),str("New"),menu)
		openAction = QAction(QIcon.fromTheme("document-open"),str("Open"),menu)
		saveAction = QAction(QIcon.fromTheme("document-save"),str("Save"),menu)
		saveAsAction = QAction(QIcon.fromTheme("document-save-as"),str("Save As"),menu)
		quit = QAction(QIcon.fromTheme("application-exit"),str("Quit"),menu)
		
		newAction.triggered.connect(self.newActionTriggered)
		openAction.triggered.connect(self.openActionTriggered)
		saveAction.triggered.connect(self.saveActionTriggered)
		saveAsAction.triggered.connect(self.saveAsActionTriggered)
		quit.triggered.connect(qApp.quit)
		
		menu.addAction(newAction)
		menu.addAction(openAction)
		menu.addAction(saveAction)
		menu.addAction(saveAsAction)
		menu.addAction(quit)
		
	def newActionTriggered(self):
		pass
		
	def openActionTriggered(self):
		print("Open")
		FileActions.openFile(self.tabs)
		
	def saveActionTriggered(self):
		FileActions.saveFile(self.tabs)
		
	def saveAsActionTriggered(self):
		FileActions.saveFileAs(self.tabs)
