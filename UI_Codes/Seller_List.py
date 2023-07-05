# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Seller_List.ui'
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
        self.pushButton_3 = QtWidgets.QPushButton(Main_Customer)
        self.pushButton_3.setMinimumSize(QtCore.QSize(87, 87))
        self.pushButton_3.setMaximumSize(QtCore.QSize(9999, 9999))
        self.pushButton_3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Images/Back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(60, 60))
        self.pushButton_3.setObjectName("pushButton_3")
        self.Header_2.addWidget(self.pushButton_3)
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
        self.label_4 = QtWidgets.QLabel(Main_Customer)
        self.label_4.setObjectName("label_4")
        self.Specs_GL_2.addWidget(self.label_4, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(Main_Customer)
        self.label_5.setObjectName("label_5")
        self.Specs_GL_2.addWidget(self.label_5, 2, 2, 1, 1, QtCore.Qt.AlignRight)
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
        self.tableWidget = QtWidgets.QTableWidget(Main_Customer)
        self.tableWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.Main_VL.addWidget(self.tableWidget)
        self.Main.addLayout(self.Main_VL, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.Main)

        ### Header ###
        with open('../DataBase/logined.pkl', 'rb') as handle:
            c = pickle.load(handle)
        self.pushButton_3.clicked.connect(self.back)  #pushButton_2 = Back_PB
        self.Exit_PB_2.clicked.connect(self.logout)
        self.Wishlist_PB_2.clicked.connect(self.wishlist) #Comments
        self.Email_var_2.setText(c.Email)
        self.ID_var_2.setText(c.ID)
        self.Name_var_2.setText(c.Name)
        self.Money_var_2.setText(str(c.Wallet))
        self.label_4.setText(str(c.Rating))
        ### Main ###

        self.retranslateUi(Main_Customer)
        QtCore.QMetaObject.connectSlotsByName(Main_Customer)

    def retranslateUi(self, Main_Customer):
        _translate = QtCore.QCoreApplication.translate
        Main_Customer.setWindowTitle(_translate("Main_Customer", "List"))
        self.Wishlist_PB_2.setText(_translate("Main_Customer", "نظرات"))
        self.ID_LB_2.setText(_translate("Main_Customer", "آیدی :"))
        self.Email_LB_2.setText(_translate("Main_Customer", "ایمیل :"))
        self.Name_LB_2.setText(_translate("Main_Customer", "نام : "))
        self.label_5.setText(_translate("Main_Customer", "رضایت :"))
        self.Unit_LB_2.setText(_translate("Main_Customer", "ریال"))
        self.Bal_LB_2.setText(_translate("Main_Customer", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt;\">: موجودی</span></p></body></html>"))
        self.Shop_Name_LB_2.setText(_translate("Main_Customer", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">فروشگاه من</span></p></body></html>"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Main_Customer", "کد مرسوله"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Main_Customer", "قیمت"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Main_Customer", "تاریخ"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Main_Customer", "تعداد محصولات"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Main_Customer", "وضعیت"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Main_Customer", "بیشتر"))

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

