import pickle
from Product import product
from Item import item
from Buy import buy
import random
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

open('../DataBase/Products.pkl', 'w')
listofproducts = []
for i in range(1,6):
    listofproducts.append(product(name=f"Huawei Mobile A{i}",description=f"Huawei Mobile A{i} description"))
with open('../DataBase/Products.pkl', 'wb') as handle:
    pickle.dump(listofproducts, handle)

with open('../DataBase/Sellers.pkl', 'rb') as handle:
    sellers_list = pickle.load(handle)

listofitems = []
for seller in sellers_list:
    for pr in listofproducts:
        listofitems.append(item(pr,seller,count=random.randint(1,10),cost=1))
open('../DataBase/Items.pkl', 'w')
with open('../DataBase/Items.pkl', 'wb') as handle:
    pickle.dump(listofitems, handle)




