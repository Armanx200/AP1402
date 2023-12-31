# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Customer_Account.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pickle
import sys,os
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)
sys.path.append('../classes/')
sys.path.append('../DataBase/')

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
        self.Back_PB = QtWidgets.QPushButton(Main_Customer)
        self.Back_PB.setMinimumSize(QtCore.QSize(73, 69))
        self.Back_PB.setMaximumSize(QtCore.QSize(73, 69))
        self.Back_PB.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Images/Back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Back_PB.setIcon(icon)
        self.Back_PB.setIconSize(QtCore.QSize(60, 60))
        self.Back_PB.setObjectName("Back_PB")
        self.Header.addWidget(self.Back_PB)
        self.Exit_PB = QtWidgets.QPushButton(Main_Customer)
        self.Exit_PB.setMinimumSize(QtCore.QSize(73, 69))
        self.Exit_PB.setMaximumSize(QtCore.QSize(73, 69))
        self.Exit_PB.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Images/Exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Exit_PB.setIcon(icon1)
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Images/Cart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Cart_PB.setIcon(icon2)
        self.Cart_PB.setIconSize(QtCore.QSize(60, 60))
        self.Cart_PB.setObjectName("Cart_PB")
        self.Header.addWidget(self.Cart_PB)
        self.Wishlist_PB = QtWidgets.QPushButton(Main_Customer)
        self.Wishlist_PB.setMinimumSize(QtCore.QSize(73, 69))
        self.Wishlist_PB.setMaximumSize(QtCore.QSize(73, 69))
        self.Wishlist_PB.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../Images/WishList.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Wishlist_PB.setIcon(icon3)
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
        self.Header.setStretch(6, 1)
        self.verticalLayout.addLayout(self.Header)
        self.line = QtWidgets.QFrame(Main_Customer)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.Main_SA = QtWidgets.QScrollArea(Main_Customer)
        self.Main_SA.setWidgetResizable(True)
        self.Main_SA.setObjectName("Main_SA")
        self.Main_SA_QW = QtWidgets.QWidget()
        self.Main_SA_QW.setGeometry(QtCore.QRect(0, 0, 993, 646))
        self.Main_SA_QW.setObjectName("Main_SA_QW")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.Main_SA_QW)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget = QtWidgets.QWidget(self.Main_SA_QW)
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.BIO_GL = QtWidgets.QGridLayout(self.widget)
        self.BIO_GL.setContentsMargins(20, 30, 20, 30)
        self.BIO_GL.setObjectName("BIO_GL")
        self.Pass_LB = QtWidgets.QLabel(self.widget)
        self.Pass_LB.setObjectName("Pass_LB")
        self.BIO_GL.addWidget(self.Pass_LB, 5, 1, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.BIO_Email_LB = QtWidgets.QLabel(self.widget)
        self.BIO_Email_LB.setObjectName("BIO_Email_LB")
        self.BIO_GL.addWidget(self.BIO_Email_LB, 3, 1, 1, 1, QtCore.Qt.AlignRight)
        self.DFSEdit_PB = QtWidgets.QPushButton(self.widget)
        self.DFSEdit_PB.setObjectName("DFSEdit_PB")
        self.BIO_GL.addWidget(self.DFSEdit_PB, 4, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.NameEdit_PB = QtWidgets.QPushButton(self.widget)
        self.NameEdit_PB.setObjectName("NameEdit_PB")
        self.BIO_GL.addWidget(self.NameEdit_PB, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.BIO_ID_LB = QtWidgets.QLabel(self.widget)
        self.BIO_ID_LB.setObjectName("BIO_ID_LB")
        self.BIO_GL.addWidget(self.BIO_ID_LB, 2, 1, 1, 1, QtCore.Qt.AlignRight)
        self.BIO_LB_Text = QtWidgets.QLabel(self.widget)
        self.BIO_LB_Text.setObjectName("BIO_LB_Text")
        self.BIO_GL.addWidget(self.BIO_LB_Text, 0, 3, 1, 1)
        self.BIO_Name_LB = QtWidgets.QLabel(self.widget)
        self.BIO_Name_LB.setObjectName("BIO_Name_LB")
        self.BIO_GL.addWidget(self.BIO_Name_LB, 1, 1, 1, 1, QtCore.Qt.AlignRight)
        self.PassEdit_PB = QtWidgets.QPushButton(self.widget)
        self.PassEdit_PB.setObjectName("PassEdit_PB")
        self.BIO_GL.addWidget(self.PassEdit_PB, 5, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.DFS_LB = QtWidgets.QLabel(self.widget)
        self.DFS_LB.setObjectName("DFS_LB")
        self.BIO_GL.addWidget(self.DFS_LB, 4, 1, 1, 1, QtCore.Qt.AlignRight)
        self.DFS_LB_Text = QtWidgets.QLabel(self.widget)
        self.DFS_LB_Text.setObjectName("DFS_LB_Text")
        self.BIO_GL.addWidget(self.DFS_LB_Text, 4, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.BIO_GL.addItem(spacerItem3, 0, 2, 1, 1)
        self.BIO_Email_LB_Text = QtWidgets.QLabel(self.widget)
        self.BIO_Email_LB_Text.setObjectName("BIO_Email_LB_Text")
        self.BIO_GL.addWidget(self.BIO_Email_LB_Text, 3, 3, 1, 1)
        self.BIO_Name_LB_Text = QtWidgets.QLabel(self.widget)
        self.BIO_Name_LB_Text.setObjectName("BIO_Name_LB_Text")
        self.BIO_GL.addWidget(self.BIO_Name_LB_Text, 1, 3, 1, 1)
        self.BIO_ID_LB_Text = QtWidgets.QLabel(self.widget)
        self.BIO_ID_LB_Text.setObjectName("BIO_ID_LB_Text")
        self.BIO_GL.addWidget(self.BIO_ID_LB_Text, 2, 3, 1, 1)
        self.Pass_LB_Text = QtWidgets.QLabel(self.widget)
        self.Pass_LB_Text.setObjectName("Pass_LB_Text")
        self.BIO_GL.addWidget(self.Pass_LB_Text, 5, 3, 1, 1)
        self.BIO_GL.setColumnStretch(0, 1)
        self.verticalLayout_5.addWidget(self.widget)
        self.widget1 = QtWidgets.QWidget(self.Main_SA_QW)
        self.widget1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget1.setObjectName("widget1")
        self.Name_Edit_VL = QtWidgets.QVBoxLayout(self.widget1)
        self.Name_Edit_VL.setContentsMargins(30, 20, 30, 20)
        self.Name_Edit_VL.setObjectName("Name_Edit_VL")
        self.Name_Edit_GL = QtWidgets.QGridLayout()
        self.Name_Edit_GL.setObjectName("Name_Edit_GL")
        self.New_Name_LB_Text = QtWidgets.QLabel(self.widget1)
        self.New_Name_LB_Text.setObjectName("New_Name_LB_Text")
        self.Name_Edit_GL.addWidget(self.New_Name_LB_Text, 1, 2, 1, 1, QtCore.Qt.AlignRight)
        self.Edit_Name_LB_Text = QtWidgets.QLabel(self.widget1)
        self.Edit_Name_LB_Text.setObjectName("Edit_Name_LB_Text")
        self.Name_Edit_GL.addWidget(self.Edit_Name_LB_Text, 0, 2, 1, 1, QtCore.Qt.AlignRight)
        self.Edit_Name_LB = QtWidgets.QLabel(self.widget1)
        self.Edit_Name_LB.setObjectName("Edit_Name_LB")
        self.Name_Edit_GL.addWidget(self.Edit_Name_LB, 0, 1, 1, 1, QtCore.Qt.AlignRight)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Name_Edit_GL.addItem(spacerItem4, 1, 0, 1, 1)
        self.New_Name_LE = QtWidgets.QLineEdit(self.widget1)
        self.New_Name_LE.setObjectName("New_Name_LE")
        self.Name_Edit_GL.addWidget(self.New_Name_LE, 1, 1, 1, 1)
        self.Name_Edit_VL.addLayout(self.Name_Edit_GL)
        self.Name_Edit_PB = QtWidgets.QPushButton(self.widget1)
        self.Name_Edit_PB.setObjectName("Name_Edit_PB")
        self.Name_Edit_VL.addWidget(self.Name_Edit_PB, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_5.addWidget(self.widget1)
        self.widget2 = QtWidgets.QWidget(self.Main_SA_QW)
        self.widget2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget2.setObjectName("widget2")
        self.DFS_VL = QtWidgets.QVBoxLayout(self.widget2)
        self.DFS_VL.setContentsMargins(30, 20, 30, 20)
        self.DFS_VL.setObjectName("DFS_VL")
        self.DFS_GL = QtWidgets.QGridLayout()
        self.DFS_GL.setObjectName("DFS_GL")
        self.New_DFS_LB_Text = QtWidgets.QLabel(self.widget2)
        self.New_DFS_LB_Text.setObjectName("New_DFS_LB_Text")
        self.DFS_GL.addWidget(self.New_DFS_LB_Text, 1, 2, 1, 1, QtCore.Qt.AlignRight)
        self.Edit_DFS_LB_Text = QtWidgets.QLabel(self.widget2)
        self.Edit_DFS_LB_Text.setObjectName("Edit_DFS_LB_Text")
        self.DFS_GL.addWidget(self.Edit_DFS_LB_Text, 0, 2, 1, 1, QtCore.Qt.AlignRight)
        self.Edit_DFS_LB = QtWidgets.QLabel(self.widget2)
        self.Edit_DFS_LB.setObjectName("Edit_DFS_LB")
        self.DFS_GL.addWidget(self.Edit_DFS_LB, 0, 1, 1, 1, QtCore.Qt.AlignRight)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.DFS_GL.addItem(spacerItem5, 1, 0, 1, 1)
        self.New_DFS_LE = QtWidgets.QLineEdit(self.widget2)
        self.New_DFS_LE.setObjectName("New_DFS_LE")
        self.DFS_GL.addWidget(self.New_DFS_LE, 1, 1, 1, 1)
        self.DFS_VL.addLayout(self.DFS_GL)
        self.Edit_DFS_PB = QtWidgets.QPushButton(self.widget2)
        self.Edit_DFS_PB.setObjectName("Edit_DFS_PB")
        self.DFS_VL.addWidget(self.Edit_DFS_PB, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_5.addWidget(self.widget2)
        self.widget3 = QtWidgets.QWidget(self.Main_SA_QW)
        self.widget3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget3.setObjectName("widget3")
        self.Pass_VL = QtWidgets.QVBoxLayout(self.widget3)
        self.Pass_VL.setContentsMargins(30, 20, 30, 20)
        self.Pass_VL.setObjectName("Pass_VL")
        self.Pass_GL = QtWidgets.QGridLayout()
        self.Pass_GL.setObjectName("Pass_GL")
        self.New_Pass_LB_Text = QtWidgets.QLabel(self.widget3)
        self.New_Pass_LB_Text.setObjectName("New_Pass_LB_Text")
        self.Pass_GL.addWidget(self.New_Pass_LB_Text, 1, 2, 1, 1, QtCore.Qt.AlignRight)
        self.Edit_Pass_LB_Text = QtWidgets.QLabel(self.widget3)
        self.Edit_Pass_LB_Text.setObjectName("Edit_Pass_LB_Text")
        self.Pass_GL.addWidget(self.Edit_Pass_LB_Text, 0, 2, 1, 1, QtCore.Qt.AlignRight)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Pass_GL.addItem(spacerItem6, 1, 0, 1, 1)
        self.New_Pass_LE = QtWidgets.QLineEdit(self.widget3)
        self.New_Pass_LE.setObjectName("New_Pass_LE")
        self.Pass_GL.addWidget(self.New_Pass_LE, 1, 1, 1, 1)
        self.Edit_Pass_LE = QtWidgets.QLineEdit(self.widget3)
        self.Edit_Pass_LE.setObjectName("Edit_Pass_LE")
        self.Pass_GL.addWidget(self.Edit_Pass_LE, 0, 1, 1, 1)
        self.Pass_VL.addLayout(self.Pass_GL)
        self.Edit_Pass_PB = QtWidgets.QPushButton(self.widget3)
        self.Edit_Pass_PB.setObjectName("Edit_Pass_PB")
        self.Pass_VL.addWidget(self.Edit_Pass_PB, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_5.addWidget(self.widget3)
        self.Main_SA.setWidget(self.Main_SA_QW)
        self.verticalLayout.addWidget(self.Main_SA)

        ### Header ###
        with open('../DataBase/logined.pkl', 'rb') as handle:
            c = pickle.load(handle)
        self.c = c
        self.Back_PB.clicked.connect(self.back)
        self.Exit_PB.clicked.connect(self.logout)
        self.Wishlist_PB.clicked.connect(self.wishlist)
        self.Cart_PB.clicked.connect(self.cart)
        self.Email_var.setText(c.Email)
        self.ID_var.setText(c.ID)
        self.Name_var.setText(c.Name)
        self.Money_var.setText(str(c.Wallet))
        self.Cart_PB.setText(str(self.sumofcart()))
        ### Main ###
        self.widget1.setVisible(False)
        self.widget2.setVisible(False)
        self.widget3.setVisible(False)
        self.NameEdit_PB.clicked.connect(self.name_edit)
        self.DFSEdit_PB.clicked.connect(self.dfs_edit)
        self.PassEdit_PB.clicked.connect(self.pass_edit)
        self.Name_Edit_PB.clicked.connect(self.change_name)
        self.Edit_DFS_PB.clicked.connect(self.change_dfs)
        self.Edit_Pass_PB.clicked.connect(self.change_pass)
        self.Edit_Pass_LE.setEchoMode(QtWidgets.QLineEdit.Password)
        self.New_Pass_LE.setEchoMode(QtWidgets.QLineEdit.Password)
        self.BIO_Email_LB.setText(c.Email)
        self.BIO_Name_LB.setText(c.Name)
        self.BIO_ID_LB.setText(c.ID)
        self.DFS_LB.setText(c.DFCS)

        self.retranslateUi(Main_Customer)
        QtCore.QMetaObject.connectSlotsByName(Main_Customer)

    def retranslateUi(self, Main_Customer):
        _translate = QtCore.QCoreApplication.translate
        Main_Customer.setWindowTitle(_translate("Main_Customer", "Account"))
        self.Email_LB.setText(_translate("Main_Customer", "ایمیل :"))
        self.ID_LB.setText(_translate("Main_Customer", "آیدی :"))
        self.Name_LB.setText(_translate("Main_Customer", "نام : "))
        self.Unit_LB.setText(_translate("Main_Customer", "ریال"))
        self.Bal_LB.setText(_translate("Main_Customer", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt;\">: موجودی</span></p></body></html>"))
        self.Shop_Name_LB.setText(_translate("Main_Customer", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">فروشگاه من</span></p></body></html>"))
        self.Pass_LB.setText(_translate("Main_Customer", "*******"))
        self.DFSEdit_PB.setText(_translate("Main_Customer", "ویرایش"))
        self.NameEdit_PB.setText(_translate("Main_Customer", "ویرایش"))
        self.BIO_LB_Text.setText(_translate("Main_Customer", "مشخصات کاربری: "))
        self.PassEdit_PB.setText(_translate("Main_Customer", "ویرایش"))
        self.DFS_LB_Text.setText(_translate("Main_Customer", "فاصله از مرکز: "))
        self.BIO_Email_LB_Text.setText(_translate("Main_Customer", "ایمیل: "))
        self.BIO_Name_LB_Text.setText(_translate("Main_Customer", "نام: "))
        self.BIO_ID_LB_Text.setText(_translate("Main_Customer", "مشخصه: "))
        self.Pass_LB_Text.setText(_translate("Main_Customer", "رمز: "))
        self.New_Name_LB_Text.setText(_translate("Main_Customer", "نام جدید :"))
        self.Edit_Name_LB_Text.setText(_translate("Main_Customer", "نام قدیمی :"))
        self.Edit_Name_LB.setText(_translate("Main_Customer", "Name"))
        self.New_Name_LE.setPlaceholderText(_translate("Main_Customer", "نام خود را وارد کنید."))
        self.Name_Edit_PB.setText(_translate("Main_Customer", "تغییر نام"))
        self.New_DFS_LB_Text.setText(_translate("Main_Customer", "فاصله جدید :"))
        self.Edit_DFS_LB_Text.setText(_translate("Main_Customer", "فاصله قدیمی :"))
        self.Edit_DFS_LB.setText(_translate("Main_Customer", "DFS"))
        self.New_DFS_LE.setPlaceholderText(_translate("Main_Customer", "فاصله خود از فروشگاه مرکزی وارد کنید."))
        self.Edit_DFS_PB.setText(_translate("Main_Customer", "تغییر فاصله"))
        self.New_Pass_LB_Text.setText(_translate("Main_Customer", "رمز جدید :"))
        self.Edit_Pass_LB_Text.setText(_translate("Main_Customer", "رمز قدیمی :"))
        self.New_Pass_LE.setPlaceholderText(_translate("Main_Customer", "رمز جدید خود را وارد کنید."))
        self.Edit_Pass_LE.setPlaceholderText(_translate("Main_Customer", "رمز قدیمی خود را وارد کنید."))
        self.Edit_Pass_PB.setText(_translate("Main_Customer", "تغییر رمز"))

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
    
    def back(self):
        from Customer_Main import Ui_Main_Customer
        self.MainPage = QtWidgets.QWidget()
        self.ui = Ui_Main_Customer()
        self.ui.setupUi(self.MainPage)
        
        self.page.hide()
        self.MainPage.show()
        
    ### Main ###
    def name_edit(self):
        self.widget1.setVisible(True) #name
        self.widget2.setVisible(False) #dfs
        self.widget3.setVisible(False) #pass
    
    def dfs_edit(self):
        self.widget1.setVisible(False) #name
        self.widget2.setVisible(True) #dfs
        self.widget3.setVisible(False) #pass
    
    def pass_edit(self):
        self.widget1.setVisible(False) #name
        self.widget2.setVisible(False) #dfs
        self.widget3.setVisible(True) #pass

    def refresh(self):
        self.Page = QtWidgets.QWidget()
        self.ui = Ui_Main_Customer()
        self.ui.setupUi(self.Page)
        
        self.page.hide()
        self.Page.show()

    def change_name(self):
        name = self.New_Name_LE.text()
        from Customer import customer
        with open('../DataBase/logined.pkl', 'rb') as handle:
                        obj = pickle.load(handle)
        if len(name) >= 0: 
            with open('../DataBase/Customers.pkl', 'rb') as handle:
                customers_list = pickle.load(handle)
            for c in customers_list:
                if c.Email == obj.Email:
                    c.CHANGE_NAME(name)
            with open('../DataBase/Customers.pkl', 'wb') as handle:
                        pickle.dump(customers_list, handle)
            with open('../DataBase/logined.pkl', 'wb') as handle:
                        pickle.dump(c, handle)   
        self.refresh()
    
    def change_dfs(self):
        dfs = self.New_DFS_LE.text()
        from Customer import customer
        with open('../DataBase/logined.pkl', 'rb') as handle:
                        obj = pickle.load(handle)
        with open('../DataBase/Customers.pkl', 'rb') as handle:
                customers_list = pickle.load(handle)
        for c in customers_list:
            if c.Email == obj.Email:
                c.DFCS = dfs
        with open('../DataBase/Customers.pkl', 'wb') as handle:
                    pickle.dump(customers_list, handle)
        with open('../DataBase/logined.pkl', 'wb') as handle:
                    pickle.dump(c, handle)
        self.refresh()

    def change_pass(self):
        old_pass = self.Edit_Pass_LE.text()
        new_pass = self.New_Pass_LE.text()
        import hashlib
        from Customer import customer
        with open('../DataBase/logined.pkl', 'rb') as handle:
                        obj = pickle.load(handle)
        if hashlib.sha256(bytes(old_pass, encoding='utf-8')).hexdigest() == obj.Password:
            #obj.Password = hashlib.sha256(bytes(new_pass, encoding='utf-8')).hexdigest()
            with open('../DataBase/Customers.pkl', 'rb') as handle:
                customers_list = pickle.load(handle)
            for c in customers_list:
                if c.Email == obj.Email:
                    c.Password = hashlib.sha256(bytes(new_pass, encoding='utf-8')).hexdigest()
            with open('../DataBase/Customers.pkl', 'wb') as handle:
                        pickle.dump(customers_list, handle)    
        
            
        self.refresh()
    
    def sumofcart(self):
        sum = 0
        for By in self.c.Cart:
            sum += (By.Cost * By.Count)
        return sum


        


    
        
        
