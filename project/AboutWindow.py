from PyQt5 import QtCore, QtWidgets
from AboutForm import Ui_Dialog
import os

class AboutWindows(QtWidgets.QDialog):

    def __init__(self):
        super(AboutWindows, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('О программе')
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.pushButton.clicked.connect(self.close)

