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
        MainWindow.resize(1052, 721)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter_4 = QtGui.QSplitter(self.centralwidget)
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName(_fromUtf8("splitter_4"))
        self.splitter_3 = QtGui.QSplitter(self.splitter_4)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName(_fromUtf8("splitter_3"))
        self.layoutWidget = QtGui.QWidget(self.splitter_3)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.buttonSave = QtGui.QPushButton(self.layoutWidget)
        self.buttonSave.setObjectName(_fromUtf8("buttonSave"))
        self.verticalLayout_3.addWidget(self.buttonSave)
        self.selectDriver = QtGui.QComboBox(self.layoutWidget)
        self.selectDriver.setEditable(True)
        self.selectDriver.setObjectName(_fromUtf8("selectDriver"))
        self.selectDriver.addItem(_fromUtf8(""))
        self.verticalLayout_3.addWidget(self.selectDriver)
        self.splitter = QtGui.QSplitter(self.splitter_3)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.textInput = QtGui.QTextEdit(self.splitter)
        self.textInput.setObjectName(_fromUtf8("textInput"))
        self.layoutWidget1 = QtGui.QWidget(self.splitter)
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.buttonCalc = QtGui.QPushButton(self.layoutWidget1)
        self.buttonCalc.setObjectName(_fromUtf8("buttonCalc"))
        self.horizontalLayout.addWidget(self.buttonCalc)
        self.buttonClear = QtGui.QPushButton(self.layoutWidget1)
        self.buttonClear.setObjectName(_fromUtf8("buttonClear"))
        self.horizontalLayout.addWidget(self.buttonClear)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.dayView = QtGui.QTableWidget(self.layoutWidget1)
        self.dayView.setObjectName(_fromUtf8("dayView"))
        self.dayView.setColumnCount(3)
        self.dayView.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.dayView.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.dayView.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.dayView.setHorizontalHeaderItem(2, item)
        self.dayView.horizontalHeader().setStretchLastSection(True)
        self.dayView.verticalHeader().setSortIndicatorShown(True)
        self.verticalLayout.addWidget(self.dayView)
        self.layoutWidget2 = QtGui.QWidget(self.splitter_3)
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.splitter_2 = QtGui.QSplitter(self.layoutWidget2)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.calendar = QtGui.QCalendarWidget(self.splitter_2)
        self.calendar.setObjectName(_fromUtf8("calendar"))
        self.commentsBox = QtGui.QTextEdit(self.splitter_2)
        self.commentsBox.setObjectName(_fromUtf8("commentsBox"))
        self.verticalLayout_2.addWidget(self.splitter_2)
        self.buttonAdd = QtGui.QPushButton(self.layoutWidget2)
        self.buttonAdd.setObjectName(_fromUtf8("buttonAdd"))
        self.verticalLayout_2.addWidget(self.buttonAdd)
        self.workGraph = QtGui.QGraphicsView(self.splitter_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.workGraph.sizePolicy().hasHeightForWidth())
        self.workGraph.setSizePolicy(sizePolicy)
        self.workGraph.setMinimumSize(QtCore.QSize(0, 150))
        self.workGraph.setObjectName(_fromUtf8("workGraph"))
        self.gridLayout.addWidget(self.splitter_4, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1052, 29))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.buttonSave.setText(_translate("MainWindow", "Save", None))
        self.selectDriver.setProperty("currentText", _translate("MainWindow", "Select Driver...", None))
        self.selectDriver.setItemText(0, _translate("MainWindow", "Select Driver...", None))
        self.buttonCalc.setText(_translate("MainWindow", "Calculate", None))
        self.buttonClear.setText(_translate("MainWindow", "Clear", None))
        item = self.dayView.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Hours", None))
        item = self.dayView.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Activity", None))
        item = self.dayView.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Infringement", None))
        self.buttonAdd.setText(_translate("MainWindow", "Add", None))

