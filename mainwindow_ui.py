# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(398, 463)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.current = QtWidgets.QLabel(self.centralwidget)
        self.current.setObjectName("current")
        self.verticalLayout.addWidget(self.current)
        self.Vlayouy = QtWidgets.QVBoxLayout()
        self.Vlayouy.setObjectName("Vlayouy")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollWidget = QtWidgets.QWidget()
        self.scrollWidget.setGeometry(QtCore.QRect(0, 0, 374, 378))
        self.scrollWidget.setObjectName("scrollWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.weatherList = QtWidgets.QVBoxLayout()
        self.weatherList.setObjectName("weatherList")
        self.verticalLayout_2.addLayout(self.weatherList)
        self.scrollArea.setWidget(self.scrollWidget)
        self.Vlayouy.addWidget(self.scrollArea)
        self.verticalLayout.addLayout(self.Vlayouy)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 398, 20))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menu.addAction(self.action)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.current.setText(_translate("MainWindow", "Сейчас"))
        self.menu.setTitle(_translate("MainWindow", "настройки"))
        self.action.setText(_translate("MainWindow", "типо тут что то есть"))


