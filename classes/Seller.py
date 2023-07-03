from random import randint
import Product
import Item

class seller(): #Seller
    def __init__(self, username, email, password):
        self.ID = self.setid()                                
        self.Name = username                                   
        self.UserName = username                               
        self.Email = email                                     
        self.Password = password
        self.DFCS = 0         #Distance from centeral shop                               
        self.Wallet = 0
        self.Rating = 0
        self.Rates = 0          #how many people rated this
    def __repr__(self):
        return f"Name: {self.Name}\nEmail: {self.Email}\nWallet: {self.Wallet}$\nRating: {self.Rating}/5"
    def setid(self):
        return "SR"+str(randint(99999,999999))

    def ADD_TO_WALLET(self, amount):
        if amount >= 0:
            self.Wallet += amount
            return True
        return False

    def ADD_ITEM(self, product_id, count, cost):                      #  <================================================ Required
        return Item.item(product_id, self, count, cost)

    def ADD_Product(self, name, description="", image="Product.jpg"):
        return Product.product(name, description, image)

    def RATE(self, rate):  #CALCULATE_RATE
        self.Rates += 1
        self.Rating = ((self.Rating * (self.Rates-1)) / self.Rates) + (rate/self.Rates)

    def CHANGE_DFCS(self, dfcs):
        self.DFCS = dfcs

    def CHANGE_NAME(self, name):
        self.Name = name
    
    def CHANGE_USERNAME(self, username):
        self.UserName = username
    
    def CHANGE_Password(self, old_password, new_password):
        if old_password == self.Password:
            self.Password = new_password
            return True
        return False    