
import pickle
with open('../DataBase/Customers.pkl', 'rb') as handle:
    customers_list = pickle.load(handle)

with open('../DataBase/Sellers.pkl', 'rb') as handle:
    sellers_list = pickle.load(handle)

with open('../DataBase/Operators.pkl', 'rb') as handle:
    operators_list = pickle.load(handle)

print("Customers: ",end=' ')
for i in customers_list:
    print(i.Email,end=' , ')
print()
print('Sellers: ',end=' ')
for i in sellers_list:
    print(i.Email,end=' , ')
print()
print('Shop admins: ',end=' ')
for i in operators_list:
    print(i.Email,end= ' , ')