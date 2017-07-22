from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtWidgets import QMessageBox, QAction
from PyQt5.QtWidgets import QMenu, qApp
from PyQt5.QtGui import QIcon

from get_icon import GetIcon
from tabpane import TabPane
from main_toolbar import MainToolBar
from file_actions import FileActions
from settings import Settings

class Window(QMainWindow):
	statusbar = 0
	savedLabel = 0
	pathLabel = 0
	tabs = 0
	setting = 0

	def __init__(self):
		super().__init__()
		self.setting = Settings()
		winX = self.setting.getSetting("window/winX","600")
		winY = self.setting.getSetting("window/winY","500")
		
		self.resize(int(winX),int(winY))
		self.setWindowTitle("PyEditor")
		self.setWindowIcon(GetIcon.asQIcon("text-editor"))
		
		self.statusbar = self.statusBar()
		
		self.savedLabel = QLabel("saved")
		self.statusbar.addWidget(self.savedLabel)
		
		self.pathLabel = QLabel("untitled")
		self.statusbar.addWidget(self.pathLabel)
		
		self.tabs = TabPane(self)
		self.setCentralWidget(self.tabs)
		
		toolbar = MainToolBar(self.tabs)
		self.addToolBar(toolbar)
		
		self.initMenus()
		
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
		
	def saveSettings(self):
		winX = self.width()
		winY = self.height()
		self.setting.writeSetting("window/winX",str(winX))
		self.setting.writeSetting("window/winY",str(winY))
		
	def closeEvent(self,event):
		if self.checkSave():
			self.saveSettings()
			event.accept()
		else:
			event.ignore()
			
	def exitProgram(self):
		if self.checkSave():
			self.saveSettings()
			qApp.exit()
			
##########################################
#			Menubar items                #
##########################################
	def initMenus(self):
		self.initFileMenu()
		self.initEditMenu()
		self.initViewMenu()
		self.initSettingsMenu()
		self.initHelpMenu()

###########FileMenu#######################
	def initFileMenu(self):
		fileMenu = self.menuBar().addMenu("File")
		
		newAction = QAction(GetIcon.asQIcon("document-new"),"New",fileMenu)
		openAction = QAction(GetIcon.asQIcon("document-open"),"Open",fileMenu)
		saveAction = QAction(GetIcon.asQIcon("document-save"),"Save",fileMenu)
		saveAsAction = QAction(GetIcon.asQIcon("document-save-as"),"Save As",fileMenu)
		quitAction = QAction(GetIcon.asQIcon("application-exit"),"Quit",fileMenu)
		
		newAction.triggered.connect(self.newActionClicked)
		openAction.triggered.connect(self.openActionClicked)
		saveAction.triggered.connect(self.saveActionClicked)
		saveAsAction.triggered.connect(self.saveAsActionClicked)
		quitAction.triggered.connect(self.exitProgram)
		
		fileMenu.addAction(newAction)
		fileMenu.addAction(openAction)
		fileMenu.addAction(saveAction)
		fileMenu.addAction(saveAsAction)
		fileMenu.addAction(quitAction)
		
	def newActionClicked(self):
		self.tabs.addNewUntitledTab()
		
	def openActionClicked(self):
		FileActions.openFile(self.tabs)
		
	def saveActionClicked(self):
		FileActions.saveFile(self.tabs)
		
	def saveAsActionClicked(self):
		FileActions.saveFileAs(self.tabs)

###########Edit Menu######################
	def initEditMenu(self):
		editMenu = self.menuBar().addMenu("Edit")
		
		cutAction = QAction(GetIcon.asQIcon("edit-cut"),"Cut",editMenu)
		copyAction = QAction(GetIcon.asQIcon("edit-copy"),"Copy",editMenu)
		pasteAction = QAction(GetIcon.asQIcon("edit-paste"),"Paste",editMenu)
		
		cutAction.triggered.connect(self.cutActionClicked)
		copyAction.triggered.connect(self.copyActionClicked)
		pasteAction.triggered.connect(self.pasteActionClicked)
		
		editMenu.addAction(cutAction)
		editMenu.addAction(copyAction)
		editMenu.addAction(pasteAction)
		
	def cutActionClicked(self):
		self.tabs.getCurrentWidget().cut()
		
	def copyActionClicked(self):
		self.tabs.getCurrentWidget().copy()
		
	def pasteActionClicked(self):
		self.tabs.getCurrentWidget().paste()
		
##########View Menu#######################
	def initViewMenu(self):
		viewMenu = self.menuBar().addMenu("View")
		
		fullscreenAction = QAction(GetIcon.asQIcon("view-fullscreen"),"Fullscreen",viewMenu)
		fullscreenAction.triggered.connect(self.fullscreenActionClicked)
		viewMenu.addAction(fullscreenAction)
		
	def fullscreenActionClicked(self):
		if (self.isFullScreen()):
			self.showNormal()
		else:
			self.showFullScreen()
			
#########Settings Menu####################
	def initSettingsMenu(self):
		settingsMenu = self.menuBar().addMenu("Settings")
		
		editorSub = settingsMenu.addMenu("Editor")
		
		autoIndent = QAction("Autoindent",editorSub)
		autoIndent.setCheckable(True)
		bool = self.setting.getSetting("editor/autoindent","true")
		if (bool=="true"):
			autoIndent.setChecked(True)
		else:
			autoIndent.setChecked(False)
		
		autoIndent.triggered.connect(self.autoIndentTriggered)
		
		editorSub.addAction(autoIndent)
		
	def autoIndentTriggered(self,checked):
		bool = str(checked).lower()
		self.setting.writeSetting("editor/autoindent",bool)

#########Help Menu########################
	def initHelpMenu(self):
		helpMenu = self.menuBar().addMenu("Help")
		
		aboutQt = QAction("About Qt",helpMenu)
		about = QAction(GetIcon.asQIcon("help-about"),"About",helpMenu)
		
		aboutQt.triggered.connect(qApp.aboutQt)
		about.triggered.connect(self.aboutActionClicked)
		
		helpMenu.addAction(aboutQt)
		helpMenu.addAction(about)
		
	def aboutActionClicked(self):
		QMessageBox.information(self,"About PyEditor",
			str("\tPyEditor\n\nPyEditor is a simple browser"+
				"written in Python. It uses Python 3 and PyQt5."),
			)



