
import pickle
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

with open('../DataBase/Customers.pkl', 'rb') as handle:
    customers_list = pickle.load(handle)

with open('../DataBase/Sellers.pkl', 'rb') as handle:
    sellers_list = pickle.load(handle)

with open('../DataBase/Operators.pkl', 'rb') as handle:
    operators_list = pickle.load(handle)

with open('../DataBase/Products.pkl', 'rb') as handle:
    products_list = pickle.load(handle)

with open('../DataBase/Items.pkl', 'rb') as handle:
    items_list = pickle.load(handle)

print("Customers: ",end=' ')
for i in customers_list:
    print(i,end=' , ')
print()
print('Sellers: ',end=' ')
for i in sellers_list:
    print(i.Email,end=' , ')
print()
print('Shop admins: ',end=' ')
for i in operators_list:
    print(i.Email,end= ' , ')

# print()
# print('Products: ',end=' ')
# for i in products_list:
#     print(i,end= ' , ')

# print()
# print('Items: ',end=' ')
# for i in items_list:
#     print(i,end= ' , ')