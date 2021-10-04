import openpyxl
from PyQt5.QtCore import QThread, pyqtSignal
from openpyxl import Workbook
import re
from pojo import LS

class Read(QThread):
    def __init__(self, my_window, parent=None):
        super(Read, self).__init__()
        self.my_window = my_window
        self.filename = ''
        self.dict_lic_scheta = {}
        self.dict_summ = {}

    def run(self):
        if self.my_window.check_one:
            self.filename = self.my_window.filename_one[0]
        else:
            self.filename = self.my_window.filename_two[0]

        wb = openpyxl.load_workbook(self.filename)
        sheet_one = wb.get_sheet_names()[0]
        this_sheet = wb[sheet_one]
        i = 0
        for cell in this_sheet['AH']:
            i = i + 1
            if cell.value != None and cell.value != '█' and len(str(cell.value)) == 12:
                # print(str(cell.value) + ' ' + str(i))
                self.dict_lic_scheta[str(cell.value)] = i

                
        
        i = 0 
        for cell in this_sheet['AC']:
            i = i + 1
            if 'Итого' in str(cell.value):
                # print(str(this_sheet['AG' + str(i)].value) + ' ' + str(i))
                self.dict_summ[str(this_sheet['AG' + str(i)].value)] = i
