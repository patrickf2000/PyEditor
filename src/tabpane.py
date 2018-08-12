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
	QFrame, 
	QVBoxLayout, 
	QTabWidget,
	QTextEdit
)
from PyQt5.QtCore import QFileInfo
from editor import Editor

class TabPane(QFrame):
	tabs = 0
	parent = 0

	def __init__(self, parentWindow): 
		super().__init__()
		self.parent = parentWindow
		
		layout = QVBoxLayout()
		layout.setContentsMargins(0,0,0,0)
		self.setLayout(layout)
		
		self.tabs = QTabWidget()
		layout.addWidget(self.tabs)
		
		self.tabs.setTabsClosable(True)
		self.tabs.setMovable(True)
		self.tabs.setTabBarAutoHide(True);
		
		self.addNewTab("untitled")
		
		self.tabs.tabCloseRequested.connect(self.onTabCloseRequested)
		self.tabs.currentChanged.connect(self.onCurrentChanged)
		
	def addNewTab(self,path):
		count = self.tabs.count()
		self.tabs.addTab(Editor(path,self.parent),QFileInfo(path).fileName())
		self.tabs.setCurrentIndex(count)
		self.parent.setSaved()
		
	def addNewUntitledTab(self):
		self.addNewTab("untitled")
		self.parent.setSaved()
		
	def getCurrentWidget(self):
		return self.tabs.currentWidget()
		
	def getParentWidget(self):
		return self.parent
		
	def setCurrentTabTitle(self, path):
		self.tabs.setTabText(self.tabs.currentIndex(),
				QFileInfo(path).fileName())
				
	def count(self):
		return self.tabs.count()
		
	def widgetAt(self,i):
		return self.tabs.widget(i)
				
	def onTabCloseRequested(self, index):
		if (self.tabs.count()==1):
			self.addNewUntitledTab()
		self.tabs.removeTab(index)
		
	def onCurrentChanged(self):
		self.parent.setPathLabel(self.tabs.currentWidget().getFilePath())
