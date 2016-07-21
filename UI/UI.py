# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TachoAnalyser.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(946, 571)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.selectDriver = QtGui.QComboBox(self.centralwidget)
        self.selectDriver.setEditable(True)
        self.selectDriver.setObjectName(_fromUtf8("selectDriver"))
        self.selectDriver.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.selectDriver)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.buttonDriving = QtGui.QPushButton(self.centralwidget)
        self.buttonDriving.setObjectName(_fromUtf8("buttonDriving"))
        self.horizontalLayout.addWidget(self.buttonDriving)
        self.buttonWorking = QtGui.QPushButton(self.centralwidget)
        self.buttonWorking.setObjectName(_fromUtf8("buttonWorking"))
        self.horizontalLayout.addWidget(self.buttonWorking)
        self.buttonBreak = QtGui.QPushButton(self.centralwidget)
        self.buttonBreak.setObjectName(_fromUtf8("buttonBreak"))
        self.horizontalLayout.addWidget(self.buttonBreak)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.textInput = QtGui.QTextEdit(self.centralwidget)
        self.textInput.setObjectName(_fromUtf8("textInput"))
        self.verticalLayout_2.addWidget(self.textInput)
        self.buttonCalc = QtGui.QPushButton(self.centralwidget)
        self.buttonCalc.setObjectName(_fromUtf8("buttonCalc"))
        self.verticalLayout_2.addWidget(self.buttonCalc)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.calendar = QtGui.QCalendarWidget(self.centralwidget)
        self.calendar.setObjectName(_fromUtf8("calendar"))
        self.verticalLayout_3.addWidget(self.calendar)
        self.dayView = QtGui.QTableWidget(self.centralwidget)
        self.dayView.setObjectName(_fromUtf8("dayView"))
        self.dayView.setColumnCount(3)
        self.dayView.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.dayView.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.dayView.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.dayView.setHorizontalHeaderItem(2, item)
        self.dayView.horizontalHeader().setStretchLastSection(True)
        self.dayView.verticalHeader().setSortIndicatorShown(True)
        self.verticalLayout_3.addWidget(self.dayView)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 1, 1, 1)
        self.synopsis = QtGui.QListWidget(self.centralwidget)
        self.synopsis.setObjectName(_fromUtf8("synopsis"))
        self.gridLayout.addWidget(self.synopsis, 0, 2, 1, 1)
        self.textInput.raise_()
        self.buttonCalc.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 946, 29))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.selectDriver.setProperty("currentText", _translate("MainWindow", "Select Driver...", None))
        self.selectDriver.setItemText(0, _translate("MainWindow", "Select Driver...", None))
        self.buttonDriving.setText(_translate("MainWindow", "Driving", None))
        self.buttonWorking.setText(_translate("MainWindow", "Working", None))
        self.buttonBreak.setText(_translate("MainWindow", "Break", None))
        self.buttonCalc.setText(_translate("MainWindow", "Calculate", None))
        item = self.dayView.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Time", None))
        item = self.dayView.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Activity", None))
        item = self.dayView.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Infringement", None))

