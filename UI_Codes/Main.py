from PyQt5 import QtCore, QtGui, QtWidgets

import sys
import pickle
class Main():
    def __init__(self):
        from Login import Ui_LoginPage
        app = QtWidgets.QApplication(sys.argv)
        Page = QtWidgets.QWidget()
        with open('../DataBase/logined.pkl', 'rb') as handle:
            logined_account = pickle.load(handle)
        if logined_account == 0:
            ui = Ui_LoginPage()
        elif 'customer' in str(type(logined_account)):
            from Customer_Main import Ui_Main_Customer
            ui = Ui_Main_Customer()
        elif 'seller' in str(type(logined_account)):
            from Seller_Main import Ui_Main_Seller
            ui = Ui_Main_Seller()
        elif 'shop' in str(type(logined_account)):
            from Operator_Main import Ui_Main_Operator
            ui = Ui_Main_Operator()
        
        ui.setupUi(Page)
        Page.show()
        sys.exit(app.exec_())
if __name__=='__main__':
    main = Main()