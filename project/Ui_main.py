# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\github\League-of-Legends\project\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(876, 452)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 33, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.treeWidget.setFont(font)
        self.treeWidget.setMouseTracking(False)
        self.treeWidget.setTabletTracking(False)
        self.treeWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.treeWidget.setAutoFillBackground(False)
        self.treeWidget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.treeWidget.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.treeWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.treeWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setTextAlignment(0, QtCore.Qt.AlignCenter)
        self.treeWidget.headerItem().setTextAlignment(1, QtCore.Qt.AlignCenter)
        self.treeWidget.headerItem().setTextAlignment(2, QtCore.Qt.AlignCenter)
        self.treeWidget.headerItem().setTextAlignment(3, QtCore.Qt.AlignCenter)
        self.treeWidget.headerItem().setTextAlignment(4, QtCore.Qt.AlignCenter)
        self.treeWidget.headerItem().setTextAlignment(5, QtCore.Qt.AlignCenter)
        self.treeWidget.headerItem().setTextAlignment(6, QtCore.Qt.AlignCenter)
        self.treeWidget.headerItem().setTextAlignment(7, QtCore.Qt.AlignCenter)
        self.treeWidget.headerItem().setTextAlignment(8, QtCore.Qt.AlignCenter)
        self.treeWidget.headerItem().setTextAlignment(9, QtCore.Qt.AlignCenter)
        self.treeWidget.headerItem().setTextAlignment(10, QtCore.Qt.AlignCenter)
        self.treeWidget.headerItem().setTextAlignment(11, QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.treeWidget)
        spacerItem2 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout.addWidget(self.comboBox_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.horizontalLayout.addWidget(self.comboBox_3)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout.addWidget(self.pushButton_6)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 876, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_5 = QtWidgets.QMenu(self.menubar)
        self.menu_5.setObjectName("menu_5")
        MainWindow.setMenuBar(self.menubar)
        self.actionnew = QtWidgets.QAction(MainWindow)
        self.actionnew.setCheckable(True)
        self.actionnew.setChecked(False)
        self.actionnew.setObjectName("actionnew")
        self.actionb = QtWidgets.QAction(MainWindow)
        self.actionb.setCheckable(True)
        self.actionb.setChecked(False)
        self.actionb.setObjectName("actionb")
        self.menu.addAction(self.actionnew)
        self.menu_5.addAction(self.actionb)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())
        self.label.setBuddy(self.comboBox)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit, self.comboBox)
        MainWindow.setTabOrder(self.comboBox, self.pushButton_3)
        MainWindow.setTabOrder(self.pushButton_3, self.comboBox_2)
        MainWindow.setTabOrder(self.comboBox_2, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.pushButton_2)
        MainWindow.setTabOrder(self.pushButton_2, self.pushButton_4)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "项目管理系统"))
        self.pushButton_5.setText(_translate("MainWindow", "刷新"))
        self.label.setText(_translate("MainWindow", "按项查询："))
        self.comboBox.setItemText(0, _translate("MainWindow", "1.项目名称"))
        self.comboBox.setItemText(1, _translate("MainWindow", "2.设计阶段"))
        self.comboBox.setItemText(2, _translate("MainWindow", "3.设计人员"))
        self.comboBox.setItemText(3, _translate("MainWindow", "4.审核人员"))
        self.comboBox.setItemText(4, _translate("MainWindow", "5.超期项目"))
        self.comboBox.setItemText(5, _translate("MainWindow", "6.单位"))
        self.comboBox.setItemText(6, _translate("MainWindow", "7.地点"))
        self.label_2.setText(_translate("MainWindow", "查询内容："))
        self.pushButton_4.setText(_translate("MainWindow", "确定"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "项目id"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "项目名称"))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "设计阶段"))
        self.treeWidget.headerItem().setText(3, _translate("MainWindow", "立项日期"))
        self.treeWidget.headerItem().setText(4, _translate("MainWindow", "预期完成日期"))
        self.treeWidget.headerItem().setText(5, _translate("MainWindow", "实际完成日期"))
        self.treeWidget.headerItem().setText(6, _translate("MainWindow", "设计人员"))
        self.treeWidget.headerItem().setText(7, _translate("MainWindow", "审核人员"))
        self.treeWidget.headerItem().setText(8, _translate("MainWindow", "单位"))
        self.treeWidget.headerItem().setText(9, _translate("MainWindow", "电话"))
        self.treeWidget.headerItem().setText(10, _translate("MainWindow", "地点"))
        self.treeWidget.headerItem().setText(11, _translate("MainWindow", "工程概况"))
        self.label_3.setText(_translate("MainWindow", "增添设计阶段："))
        self.pushButton_3.setText(_translate("MainWindow", "搜索项目"))
        self.label_4.setText(_translate("MainWindow", "可添加阶段的项目："))
        self.pushButton.setText(_translate("MainWindow", "确定"))
        self.label_5.setText(_translate("MainWindow", "选择项目id进行附件下载："))
        self.pushButton_6.setText(_translate("MainWindow", "下载"))
        self.pushButton_2.setText(_translate("MainWindow", "退出"))
        self.menu.setTitle(_translate("MainWindow", "项目"))
        self.menu_5.setTitle(_translate("MainWindow", "关于"))
        self.actionnew.setText(_translate("MainWindow", "新建"))
        self.actionb.setText(_translate("MainWindow", "帮助"))