from random import randint
import DataBase #temp

class shop(): #Shop Admin
    def __init__(self, username, password):
        self.ID = self.setid()                                                                  
        self.UserName = username                                                                  
        self.Password = password
        self.LOC = [] #List of Customers
        self.LOS = [] #List of Sellers
        self.LOP = [] #List of Products
        DataBase.Shops.append(self)
        self.REFRESH
    def __repr__(self):
        return f"Shop: {self.ID}"
    def setid(self):
        return "SP"+str(randint(99999,999999))

    def REFRESH(self):
        self.LOC = DataBase.Customers
        self.LOS = DataBase.Sellers
        self.LOP = DataBase.Products

    def CHANGE_USERNAME(self, username):
        self.UserName = username
    
    def CHANGE_Password(self, old_password, new_password):
        if old_password == self.Password:
            self.Password = new_password
            return True
        return False  