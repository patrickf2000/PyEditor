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
			
		
