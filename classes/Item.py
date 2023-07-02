from random import randint

class item():
    def __init__(self, product_id, seller_id, count, cost):
        self.ID = self.setid()
        self.Product_ID = product_id
        self.Seller_ID = seller_id
        self.Count = count 
        self.Cost = cost    #cost per item
        self.Rating = 0
        self.Rates = 0
    def __repr__(self):
        return f"Product: {self.Name}\nID: {self.ID}\nPrice: {self.Cost}$\nDescription: {self.Description}\nrating: {self.Rating}/5"
    def setid(self):
        return "IM"+str(randint(99999,999999))

    def RATE(self, rate):    #CALCULATE_RATE
        self.Rates += 1
        self.Rating = ((self.Rating * (self.Rates-1)) / self.Rates) + (rate/self.Rates)
    