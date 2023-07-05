# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Customer_Main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pickle
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

class Ui_Main_Customer(object):
    def setupUi(self, Main_Customer):
        
        self.page = Main_Customer
        Main_Customer.setObjectName("Main_Customer")
        Main_Customer.resize(1038, 570)
        Main_Customer.setMinimumSize(QtCore.QSize(1038, 570))
        Main_Customer.setMaximumSize(QtCore.QSize(1038, 570))
        self.verticalLayout = QtWidgets.QVBoxLayout(Main_Customer)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Header = QtWidgets.QHBoxLayout()
        self.Header.setObjectName("Header")
        self.Exit_PB = QtWidgets.QPushButton(Main_Customer)
        self.Exit_PB.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Images/Exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Exit_PB.setIcon(icon)
        self.Exit_PB.setIconSize(QtCore.QSize(60, 60))
        self.Exit_PB.setAutoDefault(False)
        self.Exit_PB.setDefault(False)
        self.Exit_PB.setFlat(False)
        self.Exit_PB.setObjectName("Exit_PB")
        
        self.Header.addWidget(self.Exit_PB)
        self.Cart_PB = QtWidgets.QPushButton(Main_Customer)
        self.Cart_PB.setMinimumSize(QtCore.QSize(73, 69))
        self.Cart_PB.setMaximumSize(QtCore.QSize(150, 69))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Cart_PB.setFont(font)
        self.Cart_PB.setStyleSheet("color: #f08804;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Images/Cart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Cart_PB.setIcon(icon1)
        self.Cart_PB.setIconSize(QtCore.QSize(60, 60))
        self.Cart_PB.setObjectName("Cart_PB")
        self.Header.addWidget(self.Cart_PB)
        self.Wishlist_PB = QtWidgets.QPushButton(Main_Customer)
        self.Wishlist_PB.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Images/WishList.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Wishlist_PB.setIcon(icon2)
        self.Wishlist_PB.setIconSize(QtCore.QSize(60, 60))
        self.Wishlist_PB.setObjectName("Wishlist_PB")
        self.Header.addWidget(self.Wishlist_PB)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Header.addItem(spacerItem)
        self.Specs_GL = QtWidgets.QGridLayout()
        self.Specs_GL.setObjectName("Specs_GL")
        self.Email_var = QtWidgets.QLabel(Main_Customer)
        self.Email_var.setObjectName("Email_var")
        
        self.Specs_GL.addWidget(self.Email_var, 1, 1, 1, 1)
        self.Email_LB = QtWidgets.QLabel(Main_Customer)
        self.Email_LB.setObjectName("Email_LB")
        self.Specs_GL.addWidget(self.Email_LB, 1, 2, 1, 1)
        self.ID_LB = QtWidgets.QLabel(Main_Customer)
        self.ID_LB.setObjectName("ID_LB")
        self.Specs_GL.addWidget(self.ID_LB, 2, 2, 1, 1)
        self.ID_var = QtWidgets.QLabel(Main_Customer)
        self.ID_var.setObjectName("ID_var")
        
        self.Specs_GL.addWidget(self.ID_var, 2, 1, 1, 1)
        self.Name_var = QtWidgets.QLabel(Main_Customer)
        self.Name_var.setObjectName("Name_var")
        
        self.Specs_GL.addWidget(self.Name_var, 0, 1, 1, 1)
        self.Name_LB = QtWidgets.QLabel(Main_Customer)
        self.Name_LB.setObjectName("Name_LB")
        self.Specs_GL.addWidget(self.Name_LB, 0, 2, 1, 1)
        self.Header.addLayout(self.Specs_GL)
        self.Header_HL = QtWidgets.QHBoxLayout()
        self.Header_HL.setObjectName("Header_HL")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Header_HL.addItem(spacerItem1)
        self.Unit_LB = QtWidgets.QLabel(Main_Customer)
        self.Unit_LB.setMaximumSize(QtCore.QSize(500, 50))
        self.Unit_LB.setObjectName("Unit_LB")
        self.Header_HL.addWidget(self.Unit_LB, 0, QtCore.Qt.AlignRight)
        self.Money_var = QtWidgets.QLabel(Main_Customer)
        self.Money_var.setMaximumSize(QtCore.QSize(500, 50))
        self.Money_var.setObjectName("Money_var")
        
        self.Header_HL.addWidget(self.Money_var, 0, QtCore.Qt.AlignLeft)
        self.Bal_LB = QtWidgets.QLabel(Main_Customer)
        self.Bal_LB.setMaximumSize(QtCore.QSize(500, 50))
        self.Bal_LB.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Bal_LB.setObjectName("Bal_LB")
        self.Header_HL.addWidget(self.Bal_LB, 0, QtCore.Qt.AlignRight)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Header_HL.addItem(spacerItem2)
        self.Shop_Name_LB = QtWidgets.QLabel(Main_Customer)
        self.Shop_Name_LB.setMaximumSize(QtCore.QSize(500, 50))
        self.Shop_Name_LB.setObjectName("Shop_Name_LB")
        self.Header_HL.addWidget(self.Shop_Name_LB)
        self.Header_HL.setStretch(0, 4)
        self.Header_HL.setStretch(4, 4)
        self.Header.addLayout(self.Header_HL)
        self.Header.setStretch(5, 1)
        self.verticalLayout.addLayout(self.Header)
        self.line = QtWidgets.QFrame(Main_Customer)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.Main = QtWidgets.QGridLayout()
        self.Main.setObjectName("Main")
        self.Main_HL = QtWidgets.QHBoxLayout()
        self.Main_HL.setContentsMargins(30, 30, 30, 30)
        self.Main_HL.setObjectName("Main_HL")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Main_HL.addItem(spacerItem3)
        self.Account_TB = QtWidgets.QToolButton(Main_Customer)
        self.Account_TB.setMinimumSize(QtCore.QSize(200, 200))
        self.Account_TB.setMaximumSize(QtCore.QSize(200, 200))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../Images/Acc.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Account_TB.setIcon(icon3)
        self.Account_TB.setIconSize(QtCore.QSize(125, 200))
        self.Account_TB.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.Account_TB.setObjectName("Account_TB")
        self.Main_HL.addWidget(self.Account_TB)
        self.List_TB = QtWidgets.QToolButton(Main_Customer)
        self.List_TB.setMinimumSize(QtCore.QSize(200, 200))
        self.List_TB.setMaximumSize(QtCore.QSize(200, 200))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../Images/list.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.List_TB.setIcon(icon4)
        self.List_TB.setIconSize(QtCore.QSize(200, 200))
        self.List_TB.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.List_TB.setObjectName("List_TB")
        self.Main_HL.addWidget(self.List_TB)
        self.Report_TB = QtWidgets.QToolButton(Main_Customer)
        self.Report_TB.setMinimumSize(QtCore.QSize(200, 200))
        self.Report_TB.setMaximumSize(QtCore.QSize(200, 200))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../Images/Report.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Report_TB.setIcon(icon5)
        self.Report_TB.setIconSize(QtCore.QSize(200, 200))
        self.Report_TB.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.Report_TB.setObjectName("Report_TB")
        self.Main_HL.addWidget(self.Report_TB)
        self.Product_TB = QtWidgets.QToolButton(Main_Customer)
        self.Product_TB.setMinimumSize(QtCore.QSize(200, 200))
        self.Product_TB.setMaximumSize(QtCore.QSize(200, 200))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../Images/Product.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Product_TB.setIcon(icon6)
        self.Product_TB.setIconSize(QtCore.QSize(200, 200))
        self.Product_TB.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.Product_TB.setObjectName("Product_TB")
        self.Main_HL.addWidget(self.Product_TB)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Main_HL.addItem(spacerItem4)
        self.Main_HL.setStretch(3, 1)
        self.Main.addLayout(self.Main_HL, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.Main)
        self.verticalLayout.setStretch(2, 1)

        ### Header ###
        with open('../DataBase/logined.pkl', 'rb') as handle:
            c = pickle.load(handle)
        self.c = c
        self.Exit_PB.clicked.connect(self.logout)
        self.Wishlist_PB.clicked.connect(self.wishlist)
        self.Cart_PB.clicked.connect(self.cart)
        self.Email_var.setText(c.Email)
        self.ID_var.setText(c.ID)
        self.Name_var.setText(c.Name)
        self.Money_var.setText(str(c.Wallet))
        self.Cart_PB.setText(str(self.sumofcart()))
        ### Main ###
        self.Account_TB.clicked.connect(self.account)
        self.Report_TB.clicked.connect(self.report)
        self.Product_TB.clicked.connect(self.product)
        self.List_TB.clicked.connect(self.list)

        self.retranslateUi(Main_Customer)
        QtCore.QMetaObject.connectSlotsByName(Main_Customer)


    def retranslateUi(self, Main_Customer):
        _translate = QtCore.QCoreApplication.translate
        Main_Customer.setWindowTitle(_translate("Main_Customer", "Main"))
        self.Email_LB.setText(_translate("Main_Customer", "ایمیل :"))
        self.ID_LB.setText(_translate("Main_Customer", "آیدی :"))
        self.Name_LB.setText(_translate("Main_Customer", "نام : "))
        self.Unit_LB.setText(_translate("Main_Customer", "ریال"))
        #self.Money_var.setText(_translate("Main_Customer", "<html><head/><body><p><span style=\" font-size:10pt;\">Money</span></p></body></html>"))
        self.Bal_LB.setText(_translate("Main_Customer", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt;\">: موجودی</span></p></body></html>"))
        self.Shop_Name_LB.setText(_translate("Main_Customer", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">فروشگاه من</span></p></body></html>"))
        self.Account_TB.setText(_translate("Main_Customer", "حساب کاربری"))
        self.List_TB.setText(_translate("Main_Customer", "لیست خرید"))
        self.Report_TB.setText(_translate("Main_Customer", "گزارشات مالی"))
        self.Product_TB.setText(_translate("Main_Customer", "محصولات"))
    
    ### Header ###
    def logout(self):
        with open('../DataBase/logined.pkl', 'wb') as handle:
            pickle.dump(0, handle)
        self.page.close()
        os.system('python Main.py')

    def wishlist(self):
        from Customer_WishList import Ui_Main_Customer
        self.WishListPage = QtWidgets.QWidget()
        self.ui = Ui_Main_Customer()
        self.ui.setupUi(self.WishListPage)
        
        self.page.hide()
        self.WishListPage.show()

    def cart(self):
        from Customer_Cart import Ui_Main_Customer
        self.CartPage = QtWidgets.QWidget()
        self.ui = Ui_Main_Customer()
        self.ui.setupUi(self.CartPage)
        
        self.page.hide()
        self.CartPage.show()
    
    ### Main ###
    def account(self):
        from Customer_Account import Ui_Main_Customer
        self.AccountPage = QtWidgets.QWidget()
        self.ui = Ui_Main_Customer()
        self.ui.setupUi(self.AccountPage)
        
        self.page.hide()
        self.AccountPage.show()

    def report(self):
        from Customer_Report import Ui_Main_Customer
        self.ReportPage = QtWidgets.QWidget()
        self.ui = Ui_Main_Customer()
        self.ui.setupUi(self.ReportPage)
        
        self.page.hide()
        self.ReportPage.show()
    def product(self):
        from Customer_Products import Ui_Main_Customer
        self.ProductsPage = QtWidgets.QWidget()
        self.ui = Ui_Main_Customer()
        self.ui.setupUi(self.ProductsPage)
        
        self.page.hide()
        self.ProductsPage.show()
    def list(self):
        from Customer_List import Ui_Main_Customer
        self.ListPage = QtWidgets.QWidget()
        self.ui = Ui_Main_Customer()
        self.ui.setupUi(self.ListPage)
        
        self.page.hide()
        self.ListPage.show()

    def sumofcart(self):
        sum = 0
        for By in self.c.Cart:
            sum += (By.Cost * By.Count)
        return sum
