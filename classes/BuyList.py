from random import randint
import datetime

class BuyList():
    def __init__(self):
        self.ID = self.setid()
        self.Buys = []
        self.count = 0
        self.totalcost = 0
        self.Date= datetime.datetime.now()

    def setid(self):
        return "BL"+str(randint(99999,999999))
    
    def AddBuy(self,buy):
        self.count += int(buy.Count)
        self.totalcost += int(buy.Count)*int(buy.Cost)
        self.Buys.append(buy)

    