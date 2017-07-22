try:
	import resources
except Exception:
	print("Error: Could not find resources file.")
	print("Please regenerate.")
	exit(1)
	
from PyQt5.QtGui import QPixmap, QIcon

class GetIcon():
	@staticmethod
	def fromRsc(name):
		pixmap = QPixmap(str(":/icons/")+str(name)+str(".png"))
		return pixmap
		
	@staticmethod
	def asQIcon(name):
		pix = GetIcon.fromRsc(name)
		return QIcon(pix)
