import Buy
import Customer
import Seller
import Product
import Shop
from DataBase import Customers, Sellers, Products, Shops #temp

Admin = Shop.shop("Admin", "12341234")

Arman = Customer.customer("Arman", "kianianarman@gmail.com", "12341234")
Iman = Seller.seller("Iman", "kianianiman@gmail.com", "12341234", 0)

CPU = Iman.ADD_Product("CPU","image", "This is a CPU")
GPU = Iman.ADD_Product("GPU","image", "This is a GPU")
Cpu_s = Iman.ADD_ITEM(CPU, 3, 30)  #3 CPU --- each 30$

Arman.ADD_TO_WALLET(100)         #arman wallet + 100$
Arman.CHANGE_USERNAME("Yes")     #arman user name changed to "Yes"
Arman.ADD_TO_CART(CPU, 1)        #arman add a item to cart

print(repr(Arman),end="\n\n")