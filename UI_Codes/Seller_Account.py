# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Seller_Account.ui'
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
        self.Main_SA = QtWidgets.QScrollArea(Main_Customer)
        self.Main_SA.setWidgetResizable(True)
        self.Main_SA.setObjectName("Main_SA")
        self.Main_SA_QW = QtWidgets.QWidget()
        self.Main_SA_QW.setGeometry(QtCore.QRect(0, 0, 1235, 646))
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
        Main_Customer.setWindowTitle(_translate("Main_Customer", "Form"))
        self.Wishlist_PB_2.setText(_translate("Main_Customer", "نظرات"))
        self.ID_LB_2.setText(_translate("Main_Customer", "آیدی :"))
        self.Email_LB_2.setText(_translate("Main_Customer", "ایمیل :"))
        self.Name_LB_2.setText(_translate("Main_Customer", "نام : "))
        self.label_5.setText(_translate("Main_Customer", "رضایت :"))
        self.Unit_LB_2.setText(_translate("Main_Customer", "ریال"))
        self.Bal_LB_2.setText(_translate("Main_Customer", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt;\">: موجودی</span></p></body></html>"))
        self.Shop_Name_LB_2.setText(_translate("Main_Customer", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">فروشگاه من</span></p></body></html>"))
        self.Pass_LB.setText(_translate("Main_Customer", "*******"))
        self.BIO_Email_LB.setText(_translate("Main_Customer", "Email"))
        self.DFSEdit_PB.setText(_translate("Main_Customer", "ویرایش"))
        self.NameEdit_PB.setText(_translate("Main_Customer", "ویرایش"))
        self.BIO_ID_LB.setText(_translate("Main_Customer", "ID"))
        self.BIO_LB_Text.setText(_translate("Main_Customer", "مشخصات کاربری: "))
        self.BIO_Name_LB.setText(_translate("Main_Customer", "Name"))
        self.PassEdit_PB.setText(_translate("Main_Customer", "ویرایش"))
        self.DFS_LB.setText(_translate("Main_Customer", "DFS"))
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

