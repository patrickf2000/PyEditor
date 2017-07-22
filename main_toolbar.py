from PyQt5.QtWidgets import (
	QToolBar,
	QToolButton)
from get_icon import GetIcon
from tabpane import TabPane
from file_actions import FileActions

class MainToolBar(QToolBar):
	tabs = 0
	
	def __init__(self, tabPane):
		super().__init__()
		
		self.tabs = tabPane
		
		newButton = QToolButton()
		openButton = QToolButton()
		saveButton = QToolButton()
		saveAsButton = QToolButton()
		cutButton = QToolButton()
		copyButton = QToolButton()
		pasteButton = QToolButton()
		undoButton = QToolButton()
		redoButton = QToolButton()
		
		newButton.setIcon(GetIcon.asQIcon("document-new"))
		openButton.setIcon(GetIcon.asQIcon("document-open"))
		saveButton.setIcon(GetIcon.asQIcon("document-save"))
		saveAsButton.setIcon(GetIcon.asQIcon("document-save-as"))
		cutButton.setIcon(GetIcon.asQIcon("edit-cut"))
		copyButton.setIcon(GetIcon.asQIcon("edit-copy"))
		pasteButton.setIcon(GetIcon.asQIcon("edit-paste"))
		undoButton.setIcon(GetIcon.asQIcon("edit-undo"))
		redoButton.setIcon(GetIcon.asQIcon("edit-redo"))
		
		newButton.setToolTip("New File")
		openButton.setToolTip("Open File")
		saveButton.setToolTip("Save File")
		saveAsButton.setToolTip("Save File As")
		cutButton.setToolTip("Cut")
		copyButton.setToolTip("Copy")
		pasteButton.setToolTip("Paste")
		undoButton.setToolTip("Undo")
		redoButton.setToolTip("Redo")
		
		newButton.clicked.connect(self.newButtonClicked)
		openButton.clicked.connect(self.openButtonClicked)
		saveButton.clicked.connect(self.saveButtonClicked)
		saveAsButton.clicked.connect(self.saveAsButtonClicked)
		cutButton.clicked.connect(self.cutButtonClicked)
		copyButton.clicked.connect(self.copyButtonClicked)
		pasteButton.clicked.connect(self.pasteButtonClicked)
		undoButton.clicked.connect(self.undoButtonClicked)
		redoButton.clicked.connect(self.redoButtonClicked)
		
		self.addWidget(newButton)
		self.addWidget(openButton)
		self.addWidget(saveButton)
		self.addWidget(saveAsButton)
		self.addSeparator()
		self.addWidget(cutButton)
		self.addWidget(copyButton)
		self.addWidget(pasteButton)
		self.addWidget(undoButton)
		self.addWidget(redoButton)
		
	def newButtonClicked(self):
		self.tabs.addNewUntitledTab()

	def openButtonClicked(self):
		FileActions.openFile(self.tabs)
		
	def saveButtonClicked(self):
		FileActions.saveFile(self.tabs)
		
	def saveAsButtonClicked(self):
		FileActions.saveFileAs(self.tabs)
		
	def cutButtonClicked(self):
		edit = self.tabs.getCurrentWidget()
		edit.cut()
		
	def copyButtonClicked(self):
		edit = self.tabs.getCurrentWidget()
		edit.copy()
		
	def pasteButtonClicked(self):
		edit = self.tabs.getCurrentWidget()
		edit.paste()
		
	def undoButtonClicked(self):
		edit = self.tabs.getCurrentWidget()
		edit.undo()
		
	def redoButtonClicked(self):
		edit = self.tabs.getCurrentWidget()
		edit.redo()

 
