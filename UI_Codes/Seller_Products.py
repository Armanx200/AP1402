# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Seller_Products.ui'
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
        Main_Customer.resize(1280, 720)
        Main_Customer.setMinimumSize(QtCore.QSize(1280, 720))
        Main_Customer.setMaximumSize(QtCore.QSize(1280, 720))
        self.verticalLayout = QtWidgets.QVBoxLayout(Main_Customer)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Header_2 = QtWidgets.QHBoxLayout()
        self.Header_2.setObjectName("Header_2")
        self.pushButton_2 = QtWidgets.QPushButton(Main_Customer)
        self.pushButton_2.setMinimumSize(QtCore.QSize(87, 87))
        self.pushButton_2.setMaximumSize(QtCore.QSize(9999, 9999))
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Images/Back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(60, 60))
        self.pushButton_2.setObjectName("pushButton_2")
        self.Header_2.addWidget(self.pushButton_2)
        self.Exit_PB_2 = QtWidgets.QPushButton(Main_Customer)
        self.Exit_PB_2.setMinimumSize(QtCore.QSize(87, 87))
        self.Exit_PB_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Images/Exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Exit_PB_2.setIcon(icon1)
        self.Exit_PB_2.setIconSize(QtCore.QSize(60, 60))
        self.Exit_PB_2.setAutoDefault(False)
        self.Exit_PB_2.setDefault(False)
        self.Exit_PB_2.setFlat(False)
        self.Exit_PB_2.setObjectName("Exit_PB_2")
        self.Header_2.addWidget(self.Exit_PB_2)
        self.Wishlist_PB_2 = QtWidgets.QPushButton(Main_Customer)
        self.Wishlist_PB_2.setMinimumSize(QtCore.QSize(150, 0))
        self.Wishlist_PB_2.setMaximumSize(QtCore.QSize(200, 999))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Images/Comment.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Wishlist_PB_2.setIcon(icon2)
        self.Wishlist_PB_2.setIconSize(QtCore.QSize(60, 60))
        self.Wishlist_PB_2.setObjectName("Wishlist_PB_2")
        self.Header_2.addWidget(self.Wishlist_PB_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Header_2.addItem(spacerItem)
        self.Specs_GL_2 = QtWidgets.QGridLayout()
        self.Specs_GL_2.setObjectName("Specs_GL_2")
        self.ID_LB_2 = QtWidgets.QLabel(Main_Customer)
        self.ID_LB_2.setObjectName("ID_LB_2")
        self.Specs_GL_2.addWidget(self.ID_LB_2, 3, 2, 1, 1)
        self.ID_var_2 = QtWidgets.QLabel(Main_Customer)
        self.ID_var_2.setObjectName("ID_var_2")
        self.Specs_GL_2.addWidget(self.ID_var_2, 3, 1, 1, 1)
        self.Email_var_2 = QtWidgets.QLabel(Main_Customer)
        self.Email_var_2.setObjectName("Email_var_2")
        self.Specs_GL_2.addWidget(self.Email_var_2, 1, 1, 1, 1)
        self.Email_LB_2 = QtWidgets.QLabel(Main_Customer)
        self.Email_LB_2.setObjectName("Email_LB_2")
        self.Specs_GL_2.addWidget(self.Email_LB_2, 1, 2, 1, 1)
        self.Name_var_2 = QtWidgets.QLabel(Main_Customer)
        self.Name_var_2.setObjectName("Name_var_2")
        self.Specs_GL_2.addWidget(self.Name_var_2, 0, 1, 1, 1)
        self.Name_LB_2 = QtWidgets.QLabel(Main_Customer)
        self.Name_LB_2.setObjectName("Name_LB_2")
        self.Specs_GL_2.addWidget(self.Name_LB_2, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(Main_Customer)
        self.label_2.setObjectName("label_2")
        self.Specs_GL_2.addWidget(self.label_2, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(Main_Customer)
        self.label.setObjectName("label")
        self.Specs_GL_2.addWidget(self.label, 2, 2, 1, 1, QtCore.Qt.AlignRight)
        self.Header_2.addLayout(self.Specs_GL_2)
        self.Header_HL_2 = QtWidgets.QHBoxLayout()
        self.Header_HL_2.setObjectName("Header_HL_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Header_HL_2.addItem(spacerItem1)
        self.Unit_LB_2 = QtWidgets.QLabel(Main_Customer)
        self.Unit_LB_2.setMaximumSize(QtCore.QSize(500, 50))
        self.Unit_LB_2.setObjectName("Unit_LB_2")
        self.Header_HL_2.addWidget(self.Unit_LB_2, 0, QtCore.Qt.AlignRight)
        self.Money_var_2 = QtWidgets.QLabel(Main_Customer)
        self.Money_var_2.setMaximumSize(QtCore.QSize(500, 50))
        self.Money_var_2.setObjectName("Money_var_2")
        self.Header_HL_2.addWidget(self.Money_var_2, 0, QtCore.Qt.AlignLeft)
        self.Bal_LB_2 = QtWidgets.QLabel(Main_Customer)
        self.Bal_LB_2.setMaximumSize(QtCore.QSize(500, 50))
        self.Bal_LB_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Bal_LB_2.setObjectName("Bal_LB_2")
        self.Header_HL_2.addWidget(self.Bal_LB_2, 0, QtCore.Qt.AlignRight)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Header_HL_2.addItem(spacerItem2)
        self.Shop_Name_LB_2 = QtWidgets.QLabel(Main_Customer)
        self.Shop_Name_LB_2.setMaximumSize(QtCore.QSize(500, 50))
        self.Shop_Name_LB_2.setObjectName("Shop_Name_LB_2")
        self.Header_HL_2.addWidget(self.Shop_Name_LB_2)
        self.Header_HL_2.setStretch(0, 4)
        self.Header_HL_2.setStretch(4, 4)
        self.Header_2.addLayout(self.Header_HL_2)
        self.Header_2.setStretch(5, 1)
        self.verticalLayout.addLayout(self.Header_2)
        self.line = QtWidgets.QFrame(Main_Customer)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.Main = QtWidgets.QGridLayout()
        self.Main.setObjectName("Main")
        self.Main_VL = QtWidgets.QVBoxLayout()
        self.Main_VL.setObjectName("Main_VL")
        self.Main_SA = QtWidgets.QScrollArea(Main_Customer)
        self.Main_SA.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Main_SA.setWidgetResizable(True)
        self.Main_SA.setObjectName("Main_SA")
        self.Main_QW = QtWidgets.QWidget()
        self.Main_QW.setGeometry(QtCore.QRect(0, 0, 1231, 766))
        self.Main_QW.setObjectName("Main_QW")
        self.gridLayout = QtWidgets.QGridLayout(self.Main_QW)
        self.gridLayout.setObjectName("gridLayout")
        self.Main_Line = QtWidgets.QFrame(self.Main_QW)
        self.Main_Line.setFrameShape(QtWidgets.QFrame.HLine)
        self.Main_Line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Main_Line.setObjectName("Main_Line")
        self.gridLayout.addWidget(self.Main_Line, 2, 0, 1, 1)
        self.Top_Line = QtWidgets.QFrame(self.Main_QW)
        self.Top_Line.setFrameShape(QtWidgets.QFrame.HLine)
        self.Top_Line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Top_Line.setObjectName("Top_Line")
        self.gridLayout.addWidget(self.Top_Line, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 4, 0, 1, 1)
        self.Item_GL_2 = QtWidgets.QWidget(self.Main_QW)
        self.Item_GL_2.setMinimumSize(QtCore.QSize(900, 350))
        self.Item_GL_2.setMaximumSize(QtCore.QSize(1000, 350))
        self.Item_GL_2.setStyleSheet("background-color:White;")
        self.Item_GL_2.setObjectName("Item_GL_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.Item_GL_2)
        self.gridLayout_8.setContentsMargins(30, 30, 30, 30)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.Picture_6 = QtWidgets.QToolButton(self.Item_GL_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Picture_6.sizePolicy().hasHeightForWidth())
        self.Picture_6.setSizePolicy(sizePolicy)
        self.Picture_6.setMinimumSize(QtCore.QSize(800, 150))
        self.Picture_6.setMaximumSize(QtCore.QSize(1000, 150))
        self.Picture_6.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Picture_6.setAutoFillBackground(False)
        self.Picture_6.setStyleSheet("background-color:rgb(0,0,0,0);")
        self.Picture_6.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../Images/UserUploaded imgs/Product.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Picture_6.setIcon(icon3)
        self.Picture_6.setIconSize(QtCore.QSize(200, 200))
        self.Picture_6.setObjectName("Picture_6")
        self.gridLayout_8.addWidget(self.Picture_6, 0, 1, 1, 1)
        self.Description_6 = QtWidgets.QWidget(self.Item_GL_2)
        self.Description_6.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"")
        self.Description_6.setObjectName("Description_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.Description_6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.Name_6 = QtWidgets.QToolButton(self.Description_6)
        self.Name_6.setMinimumSize(QtCore.QSize(719, 0))
        self.Name_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Name_6.setStyleSheet("background-color:rgb(0,0,0,0);")
        self.Name_6.setObjectName("Name_6")
        self.verticalLayout_7.addWidget(self.Name_6, 0, QtCore.Qt.AlignHCenter)
        self.Rate_6 = QtWidgets.QToolButton(self.Description_6)
        self.Rate_6.setMinimumSize(QtCore.QSize(90, 0))
        self.Rate_6.setStyleSheet("background-color: rgb(0,0,0,0)")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../Images/WishList.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Rate_6.setIcon(icon4)
        self.Rate_6.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.Rate_6.setObjectName("Rate_6")
        self.verticalLayout_7.addWidget(self.Rate_6, 0, QtCore.Qt.AlignHCenter)
        self.Amount_6 = QtWidgets.QLabel(self.Description_6)
        self.Amount_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Amount_6.setObjectName("Amount_6")
        self.verticalLayout_7.addWidget(self.Amount_6, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout_8.addWidget(self.Description_6, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.Item_GL_2, 3, 0, 1, 1, QtCore.Qt.AlignTop)
        self.Item_GL_1 = QtWidgets.QWidget(self.Main_QW)
        self.Item_GL_1.setMinimumSize(QtCore.QSize(900, 350))
        self.Item_GL_1.setMaximumSize(QtCore.QSize(1000, 350))
        self.Item_GL_1.setStyleSheet("background-color:White;")
        self.Item_GL_1.setObjectName("Item_GL_1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Item_GL_1)
        self.gridLayout_2.setContentsMargins(30, 30, 30, 30)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Picture_1 = QtWidgets.QToolButton(self.Item_GL_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Picture_1.sizePolicy().hasHeightForWidth())
        self.Picture_1.setSizePolicy(sizePolicy)
        self.Picture_1.setMinimumSize(QtCore.QSize(800, 150))
        self.Picture_1.setMaximumSize(QtCore.QSize(1000, 150))
        self.Picture_1.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Picture_1.setAutoFillBackground(False)
        self.Picture_1.setStyleSheet("background-color:rgb(0,0,0,0);")
        self.Picture_1.setText("")
        self.Picture_1.setIcon(icon3)
        self.Picture_1.setIconSize(QtCore.QSize(200, 200))
        self.Picture_1.setObjectName("Picture_1")
        self.gridLayout_2.addWidget(self.Picture_1, 0, 1, 1, 1)
        self.Description = QtWidgets.QWidget(self.Item_GL_1)
        self.Description.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"")
        self.Description.setObjectName("Description")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Description)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Name = QtWidgets.QToolButton(self.Description)
        self.Name.setMinimumSize(QtCore.QSize(719, 0))
        self.Name.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Name.setStyleSheet("background-color:rgb(0,0,0,0);")
        self.Name.setObjectName("Name")
        self.verticalLayout_2.addWidget(self.Name, 0, QtCore.Qt.AlignHCenter)
        self.Rate = QtWidgets.QToolButton(self.Description)
        self.Rate.setMinimumSize(QtCore.QSize(90, 0))
        self.Rate.setStyleSheet("background-color: rgb(0,0,0,0)")
        self.Rate.setIcon(icon4)
        self.Rate.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.Rate.setObjectName("Rate")
        self.verticalLayout_2.addWidget(self.Rate, 0, QtCore.Qt.AlignHCenter)
        self.Amount = QtWidgets.QLabel(self.Description)
        self.Amount.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Amount.setObjectName("Amount")
        self.verticalLayout_2.addWidget(self.Amount, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout_2.addWidget(self.Description, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.Item_GL_1, 1, 0, 1, 1)
        self.Main_Line_3 = QtWidgets.QFrame(self.Main_QW)
        self.Main_Line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.Main_Line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Main_Line_3.setObjectName("Main_Line_3")
        self.gridLayout.addWidget(self.Main_Line_3, 5, 0, 1, 1)
        self.Main_SA.setWidget(self.Main_QW)
        self.Main_VL.addWidget(self.Main_SA)
        self.Main.addLayout(self.Main_VL, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.Main)

        ### Header ###
        with open('../DataBase/logined.pkl', 'rb') as handle:
            c = pickle.load(handle)
        self.pushButton_2.clicked.connect(self.back)  #pushButton_2 = Back_PB
        self.Exit_PB_2.clicked.connect(self.logout)
        self.Wishlist_PB_2.clicked.connect(self.wishlist) #Comments
        self.Email_var_2.setText(c.Email)
        self.ID_var_2.setText(c.ID)
        self.Name_var_2.setText(c.Name)
        self.Money_var_2.setText(str(c.Wallet))
        self.label_2.setText(str(c.Rating))
        ### Main ###

        self.retranslateUi(Main_Customer)
        QtCore.QMetaObject.connectSlotsByName(Main_Customer)

    def retranslateUi(self, Main_Customer):
        _translate = QtCore.QCoreApplication.translate
        Main_Customer.setWindowTitle(_translate("Main_Customer", "Form"))
        self.Wishlist_PB_2.setText(_translate("Main_Customer", "نظرات"))
        self.ID_LB_2.setText(_translate("Main_Customer", "آیدی :"))
        self.Email_LB_2.setText(_translate("Main_Customer", "ایمیل :"))
        self.Name_LB_2.setText(_translate("Main_Customer", "نام : "))
        self.label.setText(_translate("Main_Customer", "رضایت :"))
        self.Unit_LB_2.setText(_translate("Main_Customer", "ریال"))
        self.Bal_LB_2.setText(_translate("Main_Customer", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt;\">: موجودی</span></p></body></html>"))
        self.Shop_Name_LB_2.setText(_translate("Main_Customer", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">فروشگاه من</span></p></body></html>"))
        self.Name_6.setText(_translate("Main_Customer", "Name"))
        self.Rate_6.setText(_translate("Main_Customer", "Rate / 5"))
        self.Amount_6.setText(_translate("Main_Customer", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt;\">ریال</span><span style=\" font-size:12pt; font-weight:600;\"> Amount</span></p></body></html>"))
        self.Name.setText(_translate("Main_Customer", "Name"))
        self.Rate.setText(_translate("Main_Customer", "Rate / 5"))
        self.Amount.setText(_translate("Main_Customer", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt;\">ریال</span><span style=\" font-size:12pt; font-weight:600;\"> Amount</span></p></body></html>"))


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
    
    def back(self):
        from Seller_Main import Ui_Main_Seller
        self.MainPage = QtWidgets.QWidget()
        self.ui = Ui_Main_Seller()
        self.ui.setupUi(self.MainPage)
        
        self.page.hide()
        self.MainPage.show()

    ### Main ###

