class LS():
    def __init__(self, licevoy, summa = 0, rowNumber = 0, vozvraty = 0, zachety = 0):
       self.licevoy = licevoy
       self.summa = summa
       self.rowNumber = rowNumber
       self.vozvraty = vozvraty
       self.zachety = zachety
    
    def SetSumma(self,summa, vozvraty, zachety):
        self.summa = summa
        self.vozvraty = vozvraty
        self.zachety = zachety