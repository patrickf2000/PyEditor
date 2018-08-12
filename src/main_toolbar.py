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

 
