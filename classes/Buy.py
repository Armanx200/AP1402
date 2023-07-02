import datetime
import Customer
import Item

class buy():
    def __init__(self, customer_id):
        self.Date = datetime.datetime.now()
        self.Customer_ID = customer_id
        self.Situiation = 0        #0:in progress       1:Done      -1:Failure
    def __repr__(self):
        return f"Customer_ID: {self.Customer_ID}\nItem_ID: {self.Item_ID}\nDate: {self.Date}"
    
    def purchase(self):
        s = self.Customer_ID
        if Customer.s.Wallet >= Customer.s.Cart_value:
            for item in Customer.s.Cart:
                Customer.s.PAY(item)
                Customer.s.REMOVE_CART_ITEM(item)
            return True
        return False


