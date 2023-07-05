# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Seller_Main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pickle
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

class Ui_Main_Seller(object):
    def setupUi(self, Main_Seller):

        self.page = Main_Seller
        Main_Seller.setObjectName("Main_Seller")
        Main_Seller.resize(1280, 720)
        Main_Seller.setMinimumSize(QtCore.QSize(1280, 720))
        Main_Seller.setMaximumSize(QtCore.QSize(1280, 720))
        self.verticalLayout = QtWidgets.QVBoxLayout(Main_Seller)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Header = QtWidgets.QHBoxLayout()
        self.Header.setObjectName("Header")
        self.Exit_PB = QtWidgets.QPushButton(Main_Seller)
        self.Exit_PB.setMinimumSize(QtCore.QSize(87, 87))
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
        self.Wishlist_PB = QtWidgets.QPushButton(Main_Seller)
        self.Wishlist_PB.setMinimumSize(QtCore.QSize(150, 0))
        self.Wishlist_PB.setMaximumSize(QtCore.QSize(200, 999))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Images/Comment.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Wishlist_PB.setIcon(icon1)
        self.Wishlist_PB.setIconSize(QtCore.QSize(60, 60))
        self.Wishlist_PB.setObjectName("Wishlist_PB")
        self.Header.addWidget(self.Wishlist_PB)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Header.addItem(spacerItem)
        self.Specs_GL = QtWidgets.QGridLayout()
        self.Specs_GL.setObjectName("Specs_GL")
        self.ID_LB = QtWidgets.QLabel(Main_Seller)
        self.ID_LB.setObjectName("ID_LB")
        self.Specs_GL.addWidget(self.ID_LB, 3, 2, 1, 1)
        self.ID_var = QtWidgets.QLabel(Main_Seller)
        self.ID_var.setObjectName("ID_var")
        self.Specs_GL.addWidget(self.ID_var, 3, 1, 1, 1)
        self.Email_var = QtWidgets.QLabel(Main_Seller)
        self.Email_var.setObjectName("Email_var")
        self.Specs_GL.addWidget(self.Email_var, 1, 1, 1, 1)
        self.Email_LB = QtWidgets.QLabel(Main_Seller)
        self.Email_LB.setObjectName("Email_LB")
        self.Specs_GL.addWidget(self.Email_LB, 1, 2, 1, 1)
        self.Name_var = QtWidgets.QLabel(Main_Seller)
        self.Name_var.setObjectName("Name_var")
        self.Specs_GL.addWidget(self.Name_var, 0, 1, 1, 1)
        self.Name_LB = QtWidgets.QLabel(Main_Seller)
        self.Name_LB.setObjectName("Name_LB")
        self.Specs_GL.addWidget(self.Name_LB, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(Main_Seller)
        self.label_2.setObjectName("label_2")
        self.Specs_GL.addWidget(self.label_2, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(Main_Seller)
        self.label.setObjectName("label")
        self.Specs_GL.addWidget(self.label, 2, 2, 1, 1, QtCore.Qt.AlignRight)
        self.Header.addLayout(self.Specs_GL)
        self.Header_HL = QtWidgets.QHBoxLayout()
        self.Header_HL.setObjectName("Header_HL")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Header_HL.addItem(spacerItem1)
        self.Unit_LB = QtWidgets.QLabel(Main_Seller)
        self.Unit_LB.setMaximumSize(QtCore.QSize(500, 50))
        self.Unit_LB.setObjectName("Unit_LB")
        self.Header_HL.addWidget(self.Unit_LB, 0, QtCore.Qt.AlignRight)
        self.Money_var = QtWidgets.QLabel(Main_Seller)
        self.Money_var.setMaximumSize(QtCore.QSize(500, 50))
        self.Money_var.setObjectName("Money_var")
        self.Header_HL.addWidget(self.Money_var, 0, QtCore.Qt.AlignLeft)
        self.Bal_LB = QtWidgets.QLabel(Main_Seller)
        self.Bal_LB.setMaximumSize(QtCore.QSize(500, 50))
        self.Bal_LB.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Bal_LB.setObjectName("Bal_LB")
        self.Header_HL.addWidget(self.Bal_LB, 0, QtCore.Qt.AlignRight)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Header_HL.addItem(spacerItem2)
        self.Shop_Name_LB = QtWidgets.QLabel(Main_Seller)
        self.Shop_Name_LB.setMaximumSize(QtCore.QSize(500, 50))
        self.Shop_Name_LB.setObjectName("Shop_Name_LB")
        self.Header_HL.addWidget(self.Shop_Name_LB)
        self.Header_HL.setStretch(0, 4)
        self.Header_HL.setStretch(4, 4)
        self.Header.addLayout(self.Header_HL)
        self.Header.setStretch(4, 1)
        self.verticalLayout.addLayout(self.Header)
        self.line = QtWidgets.QFrame(Main_Seller)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(30, 30, 30, 30)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Main_HL = QtWidgets.QHBoxLayout()
        self.Main_HL.setContentsMargins(30, 30, 30, 30)
        self.Main_HL.setObjectName("Main_HL")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Main_HL.addItem(spacerItem3)
        self.Account_TB = QtWidgets.QToolButton(Main_Seller)
        self.Account_TB.setMinimumSize(QtCore.QSize(200, 200))
        self.Account_TB.setMaximumSize(QtCore.QSize(200, 200))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Images/Acc.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Account_TB.setIcon(icon2)
        self.Account_TB.setIconSize(QtCore.QSize(125, 200))
        self.Account_TB.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.Account_TB.setObjectName("Account_TB")
        self.Main_HL.addWidget(self.Account_TB)
        self.toolButton = QtWidgets.QToolButton(Main_Seller)
        self.toolButton.setMinimumSize(QtCore.QSize(200, 200))
        self.toolButton.setMaximumSize(QtCore.QSize(200, 200))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../Images/list.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon3)
        self.toolButton.setIconSize(QtCore.QSize(200, 200))
        self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton.setObjectName("toolButton")
        self.Main_HL.addWidget(self.toolButton)
        self.Report_TB = QtWidgets.QToolButton(Main_Seller)
        self.Report_TB.setMinimumSize(QtCore.QSize(200, 200))
        self.Report_TB.setMaximumSize(QtCore.QSize(200, 200))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../Images/Report.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Report_TB.setIcon(icon4)
        self.Report_TB.setIconSize(QtCore.QSize(200, 200))
        self.Report_TB.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.Report_TB.setObjectName("Report_TB")
        self.Main_HL.addWidget(self.Report_TB)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Main_HL.addItem(spacerItem4)
        self.Main_HL.setStretch(3, 1)
        self.verticalLayout_4.addLayout(self.Main_HL)
        self.Main_HL_6 = QtWidgets.QHBoxLayout()
        self.Main_HL_6.setContentsMargins(30, 30, 30, 30)
        self.Main_HL_6.setObjectName("Main_HL_6")
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Main_HL_6.addItem(spacerItem5)
        self.Cart_PB = QtWidgets.QToolButton(Main_Seller)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(200)
        sizePolicy.setHeightForWidth(self.Cart_PB.sizePolicy().hasHeightForWidth())
        self.Cart_PB.setSizePolicy(sizePolicy)
        self.Cart_PB.setMinimumSize(QtCore.QSize(200, 200))
        self.Cart_PB.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Cart_PB.setFont(font)
        self.Cart_PB.setStyleSheet("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../Images/Cart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Cart_PB.setIcon(icon5)
        self.Cart_PB.setIconSize(QtCore.QSize(200, 150))
        self.Cart_PB.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.Cart_PB.setObjectName("Cart_PB")
        self.Main_HL_6.addWidget(self.Cart_PB)
        self.Product_TB_6 = QtWidgets.QToolButton(Main_Seller)
        self.Product_TB_6.setMinimumSize(QtCore.QSize(200, 200))
        self.Product_TB_6.setMaximumSize(QtCore.QSize(200, 200))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../Images/Product.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Product_TB_6.setIcon(icon6)
        self.Product_TB_6.setIconSize(QtCore.QSize(200, 200))
        self.Product_TB_6.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.Product_TB_6.setObjectName("Product_TB_6")
        self.Main_HL_6.addWidget(self.Product_TB_6)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.Main_HL_6.addItem(spacerItem6)
        self.verticalLayout_4.addLayout(self.Main_HL_6)
        self.verticalLayout.addLayout(self.verticalLayout_4)

        ### Header ###
        with open('../DataBase/logined.pkl', 'rb') as handle:
            c = pickle.load(handle)
        self.Exit_PB.clicked.connect(self.logout)
        self.Wishlist_PB.clicked.connect(self.wishlist) #Comments
        self.Email_var.setText(c.Email)
        self.ID_var.setText(c.ID)
        self.Name_var.setText(c.Name)
        self.Money_var.setText(str(c.Wallet))
        self.label_2.setText(str(c.Rating))
        ### Main ###
        self.Account_TB.clicked.connect(self.account)
        self.Report_TB.clicked.connect(self.report)
        self.Product_TB_6.clicked.connect(self.product)
        self.toolButton.clicked.connect(self.list)  #List
        self.Cart_PB.clicked.connect(self.cart)

        self.retranslateUi(Main_Seller)
        QtCore.QMetaObject.connectSlotsByName(Main_Seller)

    def retranslateUi(self, Main_Seller):
        _translate = QtCore.QCoreApplication.translate
        Main_Seller.setWindowTitle(_translate("Main_Seller", "Main"))
        self.Wishlist_PB.setText(_translate("Main_Seller", "نظرات"))
        self.ID_LB.setText(_translate("Main_Seller", "آیدی :"))
        self.Email_LB.setText(_translate("Main_Seller", "ایمیل :"))
        self.Name_LB.setText(_translate("Main_Seller", "نام : "))
        self.label.setText(_translate("Main_Seller", "رضایت :"))
        self.Unit_LB.setText(_translate("Main_Seller", "ریال"))
        self.Bal_LB.setText(_translate("Main_Seller", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt;\">: موجودی</span></p></body></html>"))
        self.Shop_Name_LB.setText(_translate("Main_Seller", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">فروشگاه من</span></p></body></html>"))
        self.Account_TB.setText(_translate("Main_Seller", "حساب کاربری"))
        self.toolButton.setText(_translate("Main_Seller", "لیست فروش"))
        self.Report_TB.setText(_translate("Main_Seller", "گزارشات مالی"))
        self.Cart_PB.setText(_translate("Main_Seller", "اضافه کردن محصول"))
        self.Product_TB_6.setText(_translate("Main_Seller", "محصولات من"))


### Header ###
    def logout(self):
        with open('../DataBase/logined.pkl', 'wb') as handle:
            pickle.dump(0, handle)
        self.page.close()
        os.system('python Main.py')

    def wishlist(self):
        from Seller_Comment import Ui_Main_Customer
        self.Page = QtWidgets.QWidget()
        self.ui = Ui_Main_Customer()
        self.ui.setupUi(self.Page)
        
        self.page.hide()
        self.Page.show()


    def cart(self):
        from Seller_Add import Ui_Main_Customer
        self.Page = QtWidgets.QWidget()
        self.ui = Ui_Main_Customer()
        self.ui.setupUi(self.Page)
        
        self.page.hide()
        self.Page.show()

    ### Main ###
    def account(self):
        from Seller_Account import Ui_Main_Customer
        self.AccountPage = QtWidgets.QWidget()
        self.ui = Ui_Main_Customer()
        self.ui.setupUi(self.AccountPage)
        
        self.page.hide()
        self.AccountPage.show()

    def report(self):
        from Seller_Report import Ui_Main_Customer
        self.ReportPage = QtWidgets.QWidget()
        self.ui = Ui_Main_Customer()
        self.ui.setupUi(self.ReportPage)
        
        self.page.hide()
        self.ReportPage.show()

    def product(self):
        from Seller_Products import Ui_Main_Customer
        self.ProductsPage = QtWidgets.QWidget()
        self.ui = Ui_Main_Customer()
        self.ui.setupUi(self.ProductsPage)
        
        self.page.hide()
        self.ProductsPage.show()
    def list(self):
        from Seller_List import Ui_Main_Customer
        self.ListPage = QtWidgets.QWidget()
        self.ui = Ui_Main_Customer()
        self.ui.setupUi(self.ListPage)
        
        self.page.hide()
        self.ListPage.show()


