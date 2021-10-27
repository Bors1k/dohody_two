from PyQt5 import QtCore
import openpyxl
from PyQt5.QtCore import QThread, pyqtSignal
from openpyxl import Workbook
import re
from pojo import LS
import re


class Read(QThread):
    appendText = QtCore.pyqtSignal(list)
    def __init__(self, my_window, parent=None):
        super(Read, self).__init__()
        self.my_window = my_window
        self.filename = ''
        self.dict_lic_scheta = {}
        self.dict_summ = {}
        self.dict_LS = []
        
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
            if cell.value != None and cell.value != '█' and len(str(cell.value)) == 12 and str(cell.value).__contains__(",") != True and re.match(r"[а-я]", str(cell.value).lower()) == None:
                # print(str(cell.value) + ' ' + str(i))
                self.dict_lic_scheta[i] = str(cell.value)

        print(len(self.dict_lic_scheta))

        i = 0
        for cell in this_sheet['AC']:
            i = i + 1
            if 'Итого' in str(cell.value):
                # print(str(this_sheet['AG' + str(i)].value) + ' ' + str(i))
                self.dict_summ[i] = str(this_sheet['AG' + str(i)].value)
        
        print(len(self.dict_summ))

        firstLs = None
        SecondLs = None
        i = 1

        for k, v in self.dict_lic_scheta.items():
            if(firstLs == None):
                firstLs = LS(licevoy=v, rowNumber=k)
            elif(firstLs != None and SecondLs == None and i <= len(self.dict_lic_scheta)):
                SecondLs = LS(licevoy=v, rowNumber=k)
                if(i!=len(self.dict_lic_scheta)):
                    for key, value in self.dict_summ.items():
                        if(key > firstLs.rowNumber and key < SecondLs.rowNumber):
                            firstLs.SetSumma(value)

                    
                    self.dict_LS.append(firstLs)
                    firstLs = SecondLs
                    SecondLs = None

                else:
                    for key, value in self.dict_summ.items():
                            if(key > firstLs.rowNumber and key < SecondLs.rowNumber):
                                firstLs.SetSumma(value)

                            if(key > SecondLs.rowNumber):
                                SecondLs.SetSumma(value)
                    
                    self.dict_LS.append(firstLs)
                    self.dict_LS.append(SecondLs)

            i = i + 1

        print("count ls - ",len(self.dict_LS))

        self.appendText.emit(self.dict_LS)
