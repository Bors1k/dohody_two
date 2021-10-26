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
                self.dict_lic_scheta[str(cell.value)] = i

        print(len(self.dict_lic_scheta))

        i = 0
        for cell in this_sheet['AC']:
            i = i + 1
            if 'Итого' in str(cell.value):
                # print(str(this_sheet['AG' + str(i)].value) + ' ' + str(i))
                self.dict_summ[str(this_sheet['AG' + str(i)].value)] = i

        print(len(self.dict_summ))

        firstLs = None
        SecondLs = None
        i = 1

        for k, v in self.dict_lic_scheta.items():
            i = i + 1
            flag = True
            if(firstLs == None):
                firstLs = LS(licevoy=k, rowNumber=v)
            elif(firstLs != None and SecondLs == None and i != len(self.dict_lic_scheta)):
                SecondLs = LS(licevoy=k, rowNumber=v)

                for key, value in self.dict_summ.items():
                    if(flag):
                        if(value > firstLs.rowNumber and value < SecondLs.rowNumber):
                            firstLs.SetSumma(key)
                            self.dict_LS.append(firstLs)
                            flag = False

            else:
                for key, value in self.dict_summ.items():
                    if(flag):
                        if(value > firstLs.rowNumber):
                            firstLs.SetSumma(key)
                            self.dict_LS.append(firstLs)
                            flag = False

            # if(flag == True):
            #     firstLs.SetSumma(0)
            #     self.dict_LS.append(firstLs)

            firstLs = SecondLs
            SecondLs = None

        print(len(self.dict_LS))

        self.appendText.emit(self.dict_LS)
