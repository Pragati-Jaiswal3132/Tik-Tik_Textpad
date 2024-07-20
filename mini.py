# importing Modules
import sys

from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initializeUI()
		self.attempts = 0

	def initializeUI(self):
		self.setWindowTitle("Tik-Tik Textpad :)")
		self.MainwindowUI()
		self.createAction()
		self.createMenu()
		self.createToolbar()
		self.show()

	def MainwindowUI(self):
		self.textEdit_obj = QTextEdit(self)
		self.textEdit_obj.move(300,300)

		vLayout_obj = QVBoxLayout()
		vLayout_obj.addWidget(self.textEdit_obj)
		
		container_obj = QWidget()
		container_obj.setLayout(vLayout_obj)
		self.setCentralWidget(container_obj)
		
		self.setStatusBar(QStatusBar())

	def createAction(self):
		#Create File Menu

		#Save
		self.save_obj = QAction(QIcon("ToolBarImages/save_file.png"),"&Save")
		self.save_obj.setShortcut("Ctrl+S")
		self.save_obj.setStatusTip("Saves your File (Ctrl+S)")
		self.save_obj.triggered.connect(self.saveFile)

		#Clear
		self.clear_obj = QAction(QIcon("ToolBarImages/clear.png"),"&Clear")
		self.clear_obj.setShortcut("Ctrl+E")
		self.clear_obj.setStatusTip("Clears all Text (Ctrl+E)")
		self.clear_obj.triggered.connect(self.textEdit_obj.clear)

		#Exit
		self.exit_obj =QAction(QIcon("ToolBarImages/exit.png"),"&Exit")
		self.exit_obj.setShortcut("Ctrl+Q")
		self.exit_obj.setStatusTip("Close the Application (Ctrl+Q)")
		self.exit_obj.triggered.connect(self.close)


		#Create Edit menu

		#Cut
		self.cut_obj = QAction(QIcon("ToolBarImages/cut.png"),"&Cut")
		self.cut_obj.setShortcut("Ctrl+X")
		self.cut_obj.setStatusTip("Cuts the selected text (Ctrl+X)")
		self.cut_obj.triggered.connect(self.textEdit_obj.cut)

		#Copy
		self.copy_obj = QAction(QIcon("ToolBarImages/copy.png"),"&Copy")
		self.copy_obj.setShortcut("Ctrl+C")
		self.copy_obj.setStatusTip("Copy the selected text (Ctrl+C)")
		self.copy_obj.triggered.connect(self.textEdit_obj.copy)

		#Paste
		self.paste_obj = QAction(QIcon("ToolBarImages/paste.png"),"&Paste")
		self.paste_obj.setShortcut("Ctrl+V")
		self.paste_obj.setStatusTip("Paste the text from the clipboard (Ctrl+V)")
		self.paste_obj.triggered.connect(self.textEdit_obj.paste)


		#Create Format menu

		#Font
		self.font_obj = QAction(QIcon("ToolBarImages/font.png"),"&Font")
		self.font_obj.setShortcut("Ctrl+F")
		self.font_obj.setStatusTip("Select text Font style (Ctrl+F)")
		self.font_obj.triggered.connect(self.fontStyle)

		#Colour
		self.colour_obj = QAction(QIcon("ToolBarImages/color.png"),"&Colour")
		self.colour_obj.setShortcut("Ctrl+L")
		self.colour_obj.setStatusTip("Select text colour (Ctrl+L)")
		self.colour_obj.triggered.connect(self.fontColour)

		#Create Help menu

		#About
		self.about_obj = QAction("About")
		self.about_obj.setStatusTip("Information about Tik-Tik Textpad:) Application")
		self.about_obj.triggered.connect(self.aboutDialog)

	def createMenu(self):
		self.menuBar().setNativeMenuBar(False)

		fileMenu_obj = self.menuBar().addMenu("File")
		fileMenu_obj.addAction(self.save_obj)
		fileMenu_obj.addAction(self.clear_obj)
		fileMenu_obj.addAction(self.exit_obj)

		editMenu_obj =self.menuBar().addMenu("Edit")
		editMenu_obj.addAction(self.cut_obj)
		editMenu_obj.addAction(self.copy_obj)
		editMenu_obj.addAction(self.paste_obj)

		formatMenu_obj =self.menuBar().addMenu("Format")
		formatMenu_obj.addAction(self.font_obj)
		formatMenu_obj.addAction(self.colour_obj)

		helpMenu_obj =self.menuBar().addMenu("Help")
		helpMenu_obj.addAction(self.about_obj)

	def createToolbar(self):
		toolbar =QToolBar("Toolbar", self)
		toolbar.setIconSize(QSize(20,20))
		self.addToolBar(toolbar)
		toolbar.addAction(self.save_obj)
		toolbar.addAction(self.clear_obj)
		toolbar.addAction(self.cut_obj)
		toolbar.addAction(self.copy_obj)
		toolbar.addAction(self.paste_obj)
		toolbar.addAction(self.font_obj)
		toolbar.addAction(self.colour_obj)
		toolbar.addAction(self.exit_obj)

	def saveFile(self):
		file_name,_=QFileDialog.getSaveFileName(self, "Save File","","HTML Files (*.html);;Text Files (*.txt)")
		
		if file_name.endswith(".txt"):
			notepad_text = self.textEdit_obj.toPlainText()
			with open(file_name, "w") as f:
				f.write(notepad_text)
		elif file_name.endwith(".html"):
			notepad_html =self.textEdit_obj.toHtml()
			with open(file_name, "w") as f:
				f.write(notepad_html)
		else:
			QMessageBox.information(self, "NOt Saved", "Text not saved.",QMessageBox.StandardButton.Ok)
	
	def fontStyle(self):
		currentFont= self.textEdit_obj.currentFont()
		font_val, ok = QFontDialog.getFont()
		if ok:
			self.textEdit_obj.setCurrentFont(font_val)

	def fontColour(self):
		colour =QColorDialog.getColor()
		if colour.isValid():
			self.textEdit_obj.setTextColor(colour)
	
	def aboutDialog(self):
		QMessageBox.about(self, "About Notepad", """<p>Tik-Tik Textpad :) version 1.0<br> Author: Pragati Jaiswal<br> For any queries contact: <br> pragatijaiswal3132@gmail.com </p>""")

if __name__=='__main__':
	app = QApplication(sys.argv)
	window = MainWindow()
	
	#To exit
	sys.exit(app.exec())
