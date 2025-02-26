# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgba(85, 85, 127, 100);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget#widget{background-color: rgba(85, 85, 127, 50);};\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setStyleSheet("QWidget#widget{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 170, 255, 246), stop:1 rgba(85, 170, 127, 255));};")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.loadVipiski = QtWidgets.QPushButton(self.widget)
        self.loadVipiski.setMinimumSize(QtCore.QSize(0, 30))
        self.loadVipiski.setStyleSheet("QPushButton{\n"
"background-color: rgba(85, 85, 127, 100);\n"
"font: 75 12pt \"Times New Roman\";\n"
"color: rgb(170, 255, 127);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(85, 85, 127, 150);\n"
"font: 75 12pt \"Times New Roman\";\n"
"color: rgb(0, 255, 255);\n"
"border-radius: 5px;\n"
"}")
        self.loadVipiski.setObjectName("loadVipiski")
        self.horizontalLayout.addWidget(self.loadVipiski)
        self.loadPrilozhenya = QtWidgets.QPushButton(self.widget)
        self.loadPrilozhenya.setMinimumSize(QtCore.QSize(0, 30))
        self.loadPrilozhenya.setStyleSheet("QPushButton{\n"
"background-color: rgba(85, 85, 127, 100);\n"
"font: 75 12pt \"Times New Roman\";\n"
"color: rgb(170, 255, 127);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(85, 85, 127, 150);\n"
"font: 75 12pt \"Times New Roman\";\n"
"color: rgb(0, 255, 255);\n"
"border-radius: 5px;\n"
"}")
        self.loadPrilozhenya.setObjectName("loadPrilozhenya")
        self.horizontalLayout.addWidget(self.loadPrilozhenya)
        self.sverka = QtWidgets.QPushButton(self.widget)
        self.sverka.setMinimumSize(QtCore.QSize(0, 30))
        self.sverka.setStyleSheet("QPushButton{\n"
"background-color: rgba(85, 85, 127, 100);\n"
"font: 75 12pt \"Times New Roman\";\n"
"color: rgb(170, 255, 127);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(85, 85, 127, 150);\n"
"font: 75 12pt \"Times New Roman\";\n"
"color: rgb(0, 255, 255);\n"
"border-radius: 5px;\n"
"}")
        self.sverka.setObjectName("sverka")
        self.horizontalLayout.addWidget(self.sverka)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setStyleSheet("border-radius: 15px")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.verticalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setStyleSheet("color: rgb(255, 255, 255);")
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menu_2 = QtWidgets.QAction(MainWindow)
        self.menu_2.setObjectName("menu_2")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_Excel = QtWidgets.QAction(MainWindow)
        self.action_Excel.setObjectName("action_Excel")
        self.menu.addAction(self.menu_2)
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_Excel)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loadVipiski.setText(_translate("MainWindow", "ЗАГРУЗИТЬ ВЫПИСКИ"))
        self.loadPrilozhenya.setText(_translate("MainWindow", "ЗАГРУЗИТЬ ПРИЛОЖЕНИЯ"))
        self.sverka.setText(_translate("MainWindow", "ПРИСТУПИТЬ К СВЕРКЕ"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.menu_2.setText(_translate("MainWindow", "О программе"))
        self.action.setText(_translate("MainWindow", "Сброс"))
        self.action_Excel.setText(_translate("MainWindow", "Выгрузить в Excel"))
