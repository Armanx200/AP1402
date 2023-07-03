import os
import pickle
from Shop import shop
import hashlib
def reset():
    # try:
    #     os.mkdir('../DataBase/')
    # except:
    #     pass
    # open('../DataBase/Customers.pkl', 'w')
    # with open('../DataBase/Customers.pkl', 'wb') as handle:
    #     pickle.dump([], handle)

    # open('../DataBase/Sellers.pkl', 'w')
    # with open('../DataBase/Sellers.pkl', 'wb') as handle:
    #     pickle.dump([], handle)

    # open('../DataBase/Operators.pkl', 'w')
    # with open('../DataBase/Operators.pkl', 'wb') as handle:
    #     pickle.dump([shop('admin',hashlib.sha256(bytes('admin', encoding='utf-8')).hexdigest(),'admin@gmail.com')], handle)

    open('../DataBase/logined.pkl', 'w')
    with open('../DataBase/logined.pkl', 'wb') as handle:
        pickle.dump(0, handle)
reset()