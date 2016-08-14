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
        MainWindow.resize(1020, 583)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.formLayout = QtGui.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.selectDriver = QtGui.QComboBox(self.centralwidget)
        self.selectDriver.setEditable(True)
        self.selectDriver.setObjectName(_fromUtf8("selectDriver"))
        self.selectDriver.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.selectDriver)
        self.textInput = QtGui.QTextEdit(self.centralwidget)
        self.textInput.setObjectName(_fromUtf8("textInput"))
        self.verticalLayout.addWidget(self.textInput)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.buttonCalc = QtGui.QPushButton(self.centralwidget)
        self.buttonCalc.setObjectName(_fromUtf8("buttonCalc"))
        self.horizontalLayout.addWidget(self.buttonCalc)
        self.buttonClear = QtGui.QPushButton(self.centralwidget)
        self.buttonClear.setObjectName(_fromUtf8("buttonClear"))
        self.horizontalLayout.addWidget(self.buttonClear)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.formLayout.setLayout(0, QtGui.QFormLayout.LabelRole, self.verticalLayout)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
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
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.synopsis = QtGui.QListWidget(self.centralwidget)
        self.synopsis.setObjectName(_fromUtf8("synopsis"))
        self.horizontalLayout_2.addWidget(self.synopsis)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.workGraph = QtGui.QGraphicsView(self.centralwidget)
        self.workGraph.setObjectName(_fromUtf8("workGraph"))
        self.verticalLayout_4.addWidget(self.workGraph)
        self.formLayout.setLayout(0, QtGui.QFormLayout.FieldRole, self.verticalLayout_4)
        self.buttonClear.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1020, 29))
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
        self.buttonCalc.setText(_translate("MainWindow", "Calculate", None))
        self.buttonClear.setText(_translate("MainWindow", "Clear", None))
        item = self.dayView.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Time", None))
        item = self.dayView.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Activity", None))
        item = self.dayView.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Infringement", None))

