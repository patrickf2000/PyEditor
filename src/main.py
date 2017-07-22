#!/usr/bin/python3
from PyQt5.QtWidgets import QApplication
from window import Window
import sys

if (__name__=="__main__"):
	app = QApplication(sys.argv)
	win = Window()
	win.show()
	sys.exit(app.exec_())
