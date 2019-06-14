from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

def showdialog():
   d = QDialog()
   b1 = QPushButton("ok",d)
   b1.move(50,50)
   d.setWindowTitle("Dialog")
   d.exec_()