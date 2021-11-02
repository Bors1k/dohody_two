import os
from PyQt5 import QtCore
import openpyxl
from PyQt5.QtCore import QThread, pyqtSignal
from openpyxl import Workbook
import re

import pyexcel
from pojo import LS
import re


class Read(QThread):
    appendText = QtCore.pyqtSignal(list,bool)
    
    def __init__(self, my_window, parent=None):
        super(Read, self).__init__()
        self.my_window = my_window
        self.filename = ''
        self.dict_lic_scheta = {}
        self.dict_summ = {}
        self.dict_vozvraty = {}
        self.dict_zachety = {}
        self.dict_LS = []
        self.check_one = self.my_window.check_one
        self.delete_file = True


    def write_dicts(self, wb, sheet_one, this_sheet, lic, itogo, summ, vozvr, zach, check_A_operacii, check_A_neispoln):
        i = 0
        for cell in this_sheet[lic]:
            i = i + 1
            if cell.value != None and cell.value != '█' and len(str(cell.value)) == 12 and str(cell.value).__contains__(",") != True and re.match(r"[а-я]", str(cell.value).lower()) == None:
                # print(str(cell.value) + ' ' + str(i))
                self.dict_lic_scheta[i] = str(cell.value)

        print(len(self.dict_lic_scheta))
        operacii = False
        i = 0
        for cell in this_sheet[itogo]:
            i = i + 1
            if this_sheet['A' + str(i)].value == check_A_operacii:
                operacii = True
            if this_sheet['A' + str(i)].value == check_A_neispoln:
                operacii = False
            if 'Итого' in str(cell.value) and operacii:
                # print(str(this_sheet['AG' + str(i)].value) + ' ' + str(i))
                self.dict_summ[i] = str(this_sheet[summ + str(i)].value)
                self.dict_vozvraty[i] = str(this_sheet[vozvr + str(i)].value)
                self.dict_zachety[i] = str(this_sheet[zach + str(i)].value)
        
        print(len(self.dict_summ))

    def motor(self):
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
                            firstLs.SetSumma(value, self.dict_vozvraty[key], self.dict_zachety[key])

                    
                    self.dict_LS.append(firstLs)
                    firstLs = SecondLs
                    SecondLs = None

                else:
                    for key, value in self.dict_summ.items():
                            if(key > firstLs.rowNumber and key < SecondLs.rowNumber):
                                firstLs.SetSumma(value, self.dict_vozvraty[key], self.dict_zachety[key])

                            if(key > SecondLs.rowNumber):
                                SecondLs.SetSumma(value, self.dict_vozvraty[key], self.dict_zachety[key])
                    
                    self.dict_LS.append(firstLs)
                    self.dict_LS.append(SecondLs)

            i = i + 1

        print("count ls - ",len(self.dict_LS))
        
    def run(self):
        if self.check_one:
            self.filename = self.my_window.filename_one[0]
            if self.filename.__contains__('.xlsx'):
                self.delete_file = False
            else:
                pyexcel.save_book_as(file_name=self.filename,dest_file_name=self.filename.replace('.xls','.xlsx'))
                self.filename = self.filename.replace('.xls','.xlsx')
        else:
            self.filename = self.my_window.filename_two[0]
            if self.filename.__contains__('.xlsx'):
                self.delete_file = False
            else:
                pyexcel.save_book_as(file_name=self.filename,dest_file_name=self.filename.replace('.xls','.xlsx'))
                self.filename = self.filename.replace('.xls','.xlsx')
        wb = openpyxl.load_workbook(self.filename)
        sheet_one = wb.get_sheet_names()[0]
        this_sheet = wb[sheet_one]

        if self.check_one:
            self.write_dicts(wb, sheet_one, this_sheet,'AH', 'AC', 'AG', 'AL', 'AQ', '2. Операции с бюджетными средствами', '3. Неисполненные поручения администратора доходов')
            self.motor()
            if self.delete_file:
                os.remove(self.filename)
            self.appendText.emit(self.dict_LS,self.check_one)
        else:
            self.write_dicts(wb, sheet_one, this_sheet,'AC', 'F', 'K', 'Q', 'W', '1. Операции со средствами', '2. Неисполненные поручения администратора доходов')
            self.motor()
            if self.delete_file:
                os.remove(self.filename)
            self.appendText.emit(self.dict_LS,self.check_one)
