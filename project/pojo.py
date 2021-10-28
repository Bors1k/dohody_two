class LS():
    def __init__(self, licevoy, summa = "Отсутствует", rowNumber = "Отсутствует", vozvraty = "Отсутствует", zachety = "Отсутствует"):
       self.licevoy = licevoy
       self.summa = summa
       self.rowNumber = rowNumber
       self.vozvraty = vozvraty
       self.zachety = zachety
    
    def SetSumma(self,summa, vozvraty, zachety):
        self.summa = summa
        self.vozvraty = vozvraty
        self.zachety = zachety