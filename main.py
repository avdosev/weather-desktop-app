import sys
from PyQt5 import QtWidgets
from mainwindow import MainWindow

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainWindow()
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение