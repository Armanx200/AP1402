from random import randint

class item():
    def __init__(self, product_id, seller_id, count, cost):
        self.ID = self.setid()
        self.Product_ID = product_id
        self.Seller_ID = seller_id
        self.Count = int(count)
        self.Cost = int(cost)   #cost per item
    def __repr__(self):
        return f"Product: {self.Product_ID.Name}\nID: {self.ID}\nPrice: {self.Cost}$\Seller: {self.Seller_ID.Name}\n"
    def setid(self):
        return "IM"+str(randint(99999,999999))
