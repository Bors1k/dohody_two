import openpyxl
from PyQt5.QtCore import QThread, pyqtSignal
from openpyxl import Workbook
import re


class Read(QThread):
    def __init__(self, my_window, parent = None):
        super(Read, self).__init__()
        self.filename = ''

    def run(self):
        if self.my_window.check_one:
            self.filename = self.my_window.filename_one[0]
        else:
            self.filename = self.my_window.filename_two[0]

