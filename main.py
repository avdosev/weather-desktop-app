import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QCoreApplication
from mainwindow import MainWindow

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    appname = 'weather'
    organization = 'puk'
    QCoreApplication.setOrganizationDomain(organization)
    QCoreApplication.setApplicationName(appname)
    app = QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainWindow()
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение