# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(820, 520)
        Form.setMinimumSize(QtCore.QSize(820, 520))
        Form.setMaximumSize(QtCore.QSize(820, 520))
        Form.setMouseTracking(False)
        Form.setTabletTracking(False)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(8, 10, 801, 381))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(730, 480, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.radioButton1 = QtWidgets.QRadioButton(Form)
        self.radioButton1.setGeometry(QtCore.QRect(10, 408, 141, 17))
        self.radioButton1.setObjectName("radioButton1")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(10, 428, 121, 31))
        self.radioButton.setObjectName("radioButton")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(130, 435, 241, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(410, 406, 111, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(519, 430, 271, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(445, 484, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(598, 485, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(410, 486, 31, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(563, 487, 31, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(444, 430, 71, 20))
        self.label_3.setObjectName("label_3")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(540, 406, 181, 17))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(Form)
        self.checkBox_2.setGeometry(QtCore.QRect(132, 409, 101, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(10, 481, 361, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(650, 455, 101, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(580, 456, 61, 20))
        self.label_4.setObjectName("label_4")
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(718, 404, 71, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(Form)
        self.lineEdit_7.setGeometry(QtCore.QRect(462, 458, 113, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(410, 464, 54, 12))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "数据清洗辅助工具"))
        self.pushButton.setText(_translate("Form", "运行"))
        self.radioButton1.setText(_translate("Form", "1-数据分析与拆分"))
        self.radioButton.setText(_translate("Form", "2-提取关键字数据"))
        self.lineEdit.setText(_translate("Form", ".*姓名;.*电话"))
        self.radioButton_2.setText(_translate("Form", "excel导入数据库"))
        self.lineEdit_2.setText(_translate("Form", "127.0.0.1:3306"))
        self.lineEdit_3.setText(_translate("Form", "root"))
        self.lineEdit_4.setText(_translate("Form", "123456"))
        self.label.setText(_translate("Form", "账号"))
        self.label_2.setText(_translate("Form", "密码"))
        self.label_3.setText(_translate("Form", "数据库:端口"))
        self.checkBox.setText(_translate("Form", "导入文件名称(需要注明行数)"))
        self.checkBox_2.setText(_translate("Form", "进行数据拆分"))
        self.lineEdit_5.setText(_translate("Form", "my_table"))
        self.label_4.setText(_translate("Form", "数据库表名"))
        self.lineEdit_7.setText(_translate("Form", "mydatabase"))
        self.label_5.setText(_translate("Form", "数据库名"))
