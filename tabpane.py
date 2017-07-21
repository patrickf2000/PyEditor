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
