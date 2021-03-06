# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.controlFrame = QtWidgets.QFrame(self.centralwidget)
        self.controlFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.controlFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.controlFrame.setLineWidth(2)
        self.controlFrame.setObjectName("controlFrame")
        self.widget = QtWidgets.QWidget(self.controlFrame)
        self.widget.setGeometry(QtCore.QRect(40, 220, 121, 141))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.paintButton = QtWidgets.QPushButton(self.widget)
        self.paintButton.setObjectName("paintButton")
        self.verticalLayout_2.addWidget(self.paintButton)
        self.clearButton = QtWidgets.QPushButton(self.widget)
        self.clearButton.setObjectName("clearButton")
        self.verticalLayout_2.addWidget(self.clearButton)
        self.timerButton = QtWidgets.QRadioButton(self.widget)
        self.timerButton.setObjectName("timerButton")
        self.verticalLayout_2.addWidget(self.timerButton)
        self.widget1 = QtWidgets.QWidget(self.controlFrame)
        self.widget1.setGeometry(QtCore.QRect(20, 100, 191, 91))
        self.widget1.setObjectName("widget1")
        self.gridLayout = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.periodEdit = QtWidgets.QLineEdit(self.widget1)
        self.periodEdit.setObjectName("periodEdit")
        self.gridLayout.addWidget(self.periodEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.hightEdit = QtWidgets.QLineEdit(self.widget1)
        self.hightEdit.setObjectName("hightEdit")
        self.gridLayout.addWidget(self.hightEdit, 1, 1, 1, 1)
        self.horizontalLayout_2.addWidget(self.controlFrame)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.totalFrame = QtWidgets.QFrame(self.centralwidget)
        self.totalFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.totalFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.totalFrame.setLineWidth(2)
        self.totalFrame.setObjectName("totalFrame")
        self.verticalLayout.addWidget(self.totalFrame)
        self.detailFrame = QtWidgets.QFrame(self.centralwidget)
        self.detailFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.detailFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.detailFrame.setLineWidth(2)
        self.detailFrame.setObjectName("detailFrame")
        self.verticalLayout.addWidget(self.detailFrame)
        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 7)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 7)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.paintAction = QtWidgets.QAction(MainWindow)
        self.paintAction.setObjectName("paintAction")
        self.clearAction = QtWidgets.QAction(MainWindow)
        self.clearAction.setObjectName("clearAction")
        self.menu.addAction(self.paintAction)
        self.menu.addAction(self.clearAction)
        self.menubar.addAction(self.menu.menuAction())
        self.toolBar.addAction(self.paintAction)
        self.toolBar.addAction(self.clearAction)

        self.retranslateUi(MainWindow)
        self.paintAction.triggered.connect(self.paintButton.click)
        self.clearAction.triggered.connect(self.clearButton.click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.paintButton.setText(_translate("MainWindow", "??????"))
        self.clearButton.setText(_translate("MainWindow", "??????"))
        self.timerButton.setText(_translate("MainWindow", "????????????"))
        self.label.setText(_translate("MainWindow", "??????"))
        self.periodEdit.setText(_translate("MainWindow", "0.1"))
        self.label_2.setText(_translate("MainWindow", "??????"))
        self.hightEdit.setText(_translate("MainWindow", "10"))
        self.menu.setTitle(_translate("MainWindow", "??????"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.paintAction.setText(_translate("MainWindow", "??????"))
        self.clearAction.setText(_translate("MainWindow", "??????"))
