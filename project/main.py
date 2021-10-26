from PyQt5 import QtCore, QtWidgets
from MainForm import Ui_MainWindow
from PyQt5.QtWidgets import QFileDialog, QLabel, QTableWidgetItem, QHeaderView, QMessageBox
import sys
import os
from read_excel import Read


class MyWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.loadVipiski.clicked.connect(self.open_file)
        self.ui.loadPrilozhenya.clicked.connect(self.open_file)
        self.check_one = False
        self.check_two = False
        self.filename = ''
        self.filename_one = ''
        self.filename_two = ''

    def open_file(self):

        self.filename = QFileDialog.getOpenFileName(
            None, 'Открыть', os.path.join(os.path.join(
                os.environ['USERPROFILE']), 'Desktop'),
            'All Files(*.xlsx)')

        sender = self.sender()
        if str(self.filename) in "('', '')":
            self.ui.statusbar.showMessage('Файл не выбран')
        else:
            if sender.text() == 'ЗАГРУЗИТЬ ВЫПИСКИ':
                self.filename_one = self.filename
                self.check_one = True
                self.check_two = False
                self.new_thread()

            else:
                self.filename_two = self.filename
                self.check_one = False
                self.check_two = True
                self.new_thread()
    
    @QtCore.pyqtSlot(list)
    def appendText(self, list):
        for ls in list:
            self.ui.logger.append(str(ls.licevoy) + "   " + str(ls.summa))

    def new_thread(self):
        self.my_thread = Read(my_window=self)
        self.my_thread.appendText.connect(self.appendText)
        self.my_thread.start()



app = QtWidgets.QApplication([])
application = MyWindow()
application.setWindowTitle("Доходы 2")
application.show()

sys.exit(app.exec())
