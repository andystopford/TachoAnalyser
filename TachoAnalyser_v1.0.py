#!/usr/bin/python3.4
import sys

sys.path.append("./UI")
sys.path.append("./Modules")
sys.path.append("./Data")
from PyQt4 import QtCore, QtGui
from UI import Ui_MainWindow
from TimeConvert import *
from Activities import *
from TimeLine import *
from Calculator import *
from IO import *
from DataModel import *
from TreeView import *
from SortFilter import*
import re

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


####################################################################################


class Mainwindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        ##################################################
        self.curr_day = QtCore.QDate()
        self.drivers = ['Andy', 'Chris', 'Dan', 'Richard']
        self.months = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 'Jul': '07',
                       'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
        ##################################################
        # Signals
        self.ui.buttonClear.clicked.connect(self.clear_input)
        self.ui.buttonCalc.clicked.connect(self.read_input)
        self.ui.selectDriver.activated[str].connect(self.select_driver)
        self.ui.buttonAdd.clicked.connect(self.add)
        self.ui.buttonSave.clicked.connect(self.save)
        ##################################################
        # Initialise
        header = self.ui.dayView.horizontalHeader()
        header.setResizeMode(QtGui.QHeaderView.Stretch)
        self.ui.selectDriver.addItems(self.drivers)
        # set to insert driver names alphabetically
        self.ui.selectDriver.setInsertPolicy(6)
        self.activity_list = []
        self.TC = TimeConvert()
        self.timeLine = TimeLine(self)
        self.ui.workGraph.setScene(self.timeLine)
        self.calculator = Calculator(self)
        self.treeView = TreeView(self)
        self.ui.verticalLayout_3.addWidget(self.treeView)
        # Data model
        self.model = DataModel(self)
        self.sortFilter = SortFilter(self)
        self.sortFilter.setSourceModel(self.model)
        self.treeView.setModel(self.sortFilter)
        #self.treeView.setSortingEnabled(True)

    def clear_input(self):
        self.ui.textInput.clear()
        self.activity_list = []
        self.timeLine.clear_timeline()
        self.ui.dayView.clear()
        self.calculator.clear()

    def select_driver(self, driver):
        # TODO Clear previous driver
        path = './Data/' + driver + '.xml'
        self.data_file = DataIO(self, path)
        self.data_file.open()
        #for item in self.model.findItems('15.07.2016:'):
        #    print(item.text())
        self.model.sort(0, 1)

    def read_input(self):
        # Activity change info from readesm is pasted in and converted to
        # minutes for start, end and duration
        text = self.ui.textInput.toPlainText()
        text = str(text)
        # Open test file
        # text = open('./Data/testFile_2', 'r')
        # text = text.read()
        # Get date
        date_line = re.search(r'Activities on (.*?) .*', text)
        date = (date_line.group())
        day = (date[22:24])
        day = day.strip()
        day = day.zfill(2)
        month_str = (date[18:21])
        month = self.months[month_str]
        year = (date[-5:])
        self.date = str(day + '.' + month + '.' +year)   # TODO highlight in calendar

        # Get Activities
        working = re.findall(r'work, from (.*?) to (.*?) .*', text)
        for item in working:
            start = item[0]
            end = item[1]
            start = self.TC.hrs_to_mins(start)
            end = self.TC.hrs_to_mins(end)
            duration = self.TC.calc_duration(start, end)
            activity = Activity("Working", start, end, duration, "")
            self.activity_list.append(activity)

        driving = re.findall(r'driving, from (.*?) to (.*?) .*', text)
        for item in driving:
            start = item[0]
            end = item[1]
            start = self.TC.hrs_to_mins(start)
            end = self.TC.hrs_to_mins(end)
            duration = self.TC.calc_duration(start, end)
            activity = Activity("Driving", start, end, duration, "")
            self.activity_list.append(activity)

        break_rest = re.findall(r'break/rest, from (.*?) to (.*?) .*', text)
        for item in break_rest:
            start = item[0]
            end = item[1]
            start = self.TC.hrs_to_mins(start)
            end = self.TC.hrs_to_mins(end)
            duration = self.TC.calc_duration(start, end)
            activity = Activity("Break", start, end, duration, "")
            self.activity_list.append(activity)

        self.timeLine.add_activities()
        self.activity_list.sort(key=lambda x: x.start, reverse=False)
        self.calculator.timers()
        self.show_activities()

    def show_activities(self):
        self.ui.dayView.clear()
        for item in reversed(self.activity_list):
            item.duration = self.TC.mins_to_hrs(item.duration)
            hours = QtGui.QTableWidgetItem(item.duration)
            mode = QtGui.QTableWidgetItem(item.mode)
            infr = QtGui.QTableWidgetItem(item.infr)
            self.ui.dayView.insertRow(0)
            self.ui.dayView.setItem(0, 0, hours)
            self.ui.dayView.setItem(0, 1, mode)
            self.ui.dayView.setItem(0, 2, infr)
        num = len(self.activity_list)
        self.ui.dayView.setRowCount(num)
        self.ui.dayView.setHorizontalHeaderLabels(['Hours', 'Activity',
                                                   'Infringement'])

    def add(self):
        self.data_file.add_day()

    def save(self):
        #path = './Data/' + self.driver + '.xml'
        # data_file = DataIO(self, path)
        self.data_file.save()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Mainwindow()
    myapp.show()
    sys.exit(app.exec_())
