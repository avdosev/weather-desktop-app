from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

def showChangeLocationDialog():
   dialog = QDialog()
   dialog.setWindowTitle("Region setting")

   cityIDLineEdit = QLineEdit(parent=dialog)
   nameCityLineEdit = QLineEdit(parent=dialog)
   nameCountryLineEdit = QLineEdit(parent=dialog)
   
   layout = QFormLayout()
   
   layout.addRow("id твоего города:", cityIDLineEdit)
   layout.addRow('имя мухосранска:', nameCityLineEdit)
   layout.addRow('родина:', nameCountryLineEdit)

   
   buttonBox = QDialogButtonBox(QDialogButtonBox.Cancel | QDialogButtonBox.Save)
   buttonBox.accepted.connect(dialog.accept)
   buttonBox.rejected.connect(dialog.reject)

   centralLayout = QVBoxLayout(dialog)
   centralLayout.addLayout(layout)
   centralLayout.addWidget(buttonBox)

   code = dialog.exec_()
   return code, {
      'id': cityIDLineEdit.text,
      'name': nameCityLineEdit.text,
      'country': nameCountryLineEdit.text
   }