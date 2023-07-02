from random import randint
import DataBase #temp
import Item
class customer(): #Customer
    def __init__(self, username, email, password):
        self.ID = self.setid()
        self.Name = username
        self.UserName = username
        self.Email = email
        self.Password = password
        self.Wallet = 0
        self.Cart = []            #List of Purchased items
        self.Cart_value = 0
        self.Wishlist = []
        DataBase.Customers.append(self.ID) #temp
        DataBase.Refresh()
    def __repr__(self):
        return f"Name: {self.Name}\nUserName: {self.UserName}\nEmail: {self.Email}\nPassword: {self.Password}\nID: {self.ID}\nWallet: {self.Wallet}$\nCart: {self.Cart}\nWishlist: {self.Wishlist}"
    def setid(self):
        return "CR"+str(randint(99999,999999))

    def ADD_TO_WALLET(self, amount):
        if amount >= 0:
            self.Wallet += amount
            return True
        return False

    def PAY(self, amount):
        if self.Wallet-amount >= 0:
            self.Wallet -= amount
            return True
        return False

    def ADD_TO_CART(self, item_ID, amount):
        if amount >= 0:
            self.Cart += [item_ID]*amount
            self.Cart_value += Item.item_ID.Cost
            return True
        return False
    
    def REMOVE_CART_ITEM(self, item):
        self.Cart.remove(item)

    def ADD_TO_WISHLIST(self, product):
        self.Wishlist.append(product)

    def REMOVE_WISHLIST(self, product):
        self.Wishlist.remove(product)

    def CHANGE_NAME(self, name):
        self.Name = name

    def CHANGE_USERNAME(self, username):
        self.UserName = username
    
    def CHANGE_Password(self, old_password, new_password):
        if old_password == self.Password:
            self.Password = new_password
            return True
        return False    
            