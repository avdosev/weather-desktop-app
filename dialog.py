from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

def showChangeLocationDialog():
   dialog = QDialog()
   dialog.setWindowTitle("Region setting")
   dialog.set
   layout = QFormLayout(parent=dialog)
   
   layout.addRow("Имя пользователя:", QLineEdit())
   # layout.addRow("Электропочта:", eMail)
   # layout.addRow("Пароль:", passWord)
   # layout.addRow("Закрепим успех:", passWordAgain)
   buttonBox = QDialogButtonBox(QDialogButtonBox.Cancel | QDialogButtonBox.Save, parent=dialog)
   buttonBox.accepted.connect(dialog.accept)
   buttonBox.rejected.connect(dialog.reject)
   dialog.exec_()
   return dialog