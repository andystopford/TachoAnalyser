#!/usr/bin/python3.4
import sys
sys.path.append("./UI")
sys.path.append("./Modules")
sys.path.append("./Data")
from PyQt4 import QtCore, QtGui
from UI import Ui_MainWindow
from WorkDay import WorkDay
from TimeConvert import*
from Activities import*
from Break import*
from Driving import*
from Working import*
from TimeLine import*
from Calculator import*
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


class Mainwindow (QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        ##################################################
        self.curr_day = QtCore.QDate()
        self.drivers = ['a', 'b', 'c']
        ##################################################
        # Signals
        self.ui.buttonClear.clicked.connect(self.clear_input)
        self.ui.buttonCalc.clicked.connect(self.calc)
        self.ui.calendar.clicked.connect(self.set_day)
        self.ui.selectDriver.activated[str].connect(self.select_driver)
        ##################################################
        # Initialise
        header = self.ui.dayView.horizontalHeader()
        header.setResizeMode(QtGui.QHeaderView.Stretch)
        self.ui.selectDriver.addItems(self.drivers)
        # set to insert driver names alphabetically
        self.ui.selectDriver.setInsertPolicy(6)

        self.break_list = []
        self.driving_list = []
        self.work_list = []
        self.driving_block = 0
        self.activity_list = []

        self.TC = TimeConvert()
        self.timeLine = TimeLine(self)
        self.ui.workGraph.setScene(self.timeLine)
        self.calculator = Calculator(self)


    def clear_input(self):
        self.ui.textInput.clear()

    def select_driver(self, driver):
        self.driver = driver
        print (self.driver)

    def set_day(self, date):
        self.workDay = WorkDay(self, date)
        self.ui.buttonDriving.setEnabled(True)
        self.ui.buttonWorking.setEnabled(True)
        self.ui.buttonBreak.setEnabled(True)

    def calc(self):
        # Activity change info from readesm is pasted in and converted to
        # minutes for start, end and duration
        text = self.ui.textInput.toPlainText()
        text = str(text)
        # Open test file
        #text = open('./Data/testFile_2', 'r')
        #text = text.read()

        working = re.findall(r'work, from (.*?) to (.*?) .*', text)
        for item in working:
            start = item[0]
            end = item[1]
            start = self.TC.hrs_to_mins(start)
            end = self.TC.hrs_to_mins(end)
            duration = self.TC.calc_duration(start, end)
            self.workingClass = WorkingClass(self, start, end, duration)
            self.work_list.append(self.workingClass)
            activity = Activity("Working", start, end, duration)
            self.activity_list.append(activity)

        driving = re.findall(r'driving, from (.*?) to (.*?) .*', text)
        for item in driving:
            start = item[0]
            end = item[1]
            start = self.TC.hrs_to_mins(start)
            end = self.TC.hrs_to_mins(end)
            duration = self.TC.calc_duration(start, end)
            self.drivingClass = DrivingClass(self, start, end, duration)
            self.driving_list.append(self.drivingClass)
            activity = Activity("Driving", start, end, duration)
            self.activity_list.append(activity)

        break_rest = re.findall(r'break/rest, from (.*?) to (.*?) .*', text)
        b_r_index = 0
        for item in break_rest:
            start = item[0]
            end = item[1]
            start = self.TC.hrs_to_mins(start)
            end = self.TC.hrs_to_mins(end)
            duration = self.TC.calc_duration(start, end)
            self.breakClass = BreakClass(self, start, end, duration, b_r_index)
            self.break_list.append(self.breakClass)
            b_r_index += 1
            activity = Activity("Break", start, end, duration)
            self.activity_list.append(activity)

        break_short = re.findall(r'short break, from (.*?) to (.*?) .*', text)
        for item in break_short:
            start = item[0]
            end = item[1]
            start = self.TC.hrs_to_mins(start)
            end = self.TC.hrs_to_mins(end)
            self.activity = Activity("Short Break", start, end)
            self.activity.calc_duration()

        self.break_list[0].set_state(-1)
        self.timeLine.add_activities()
        self.activity_list.sort(key=lambda  x: x.start, reverse=False)
        self.calculator.timers()

    def show_activities(self):
        self.ui.dayView.clear()
        for item in reversed(self.workDay.activity_list):
            item.duration = self.TC.mins_to_hrs(item.duration)
            time = QtGui.QTableWidgetItem(str(item.duration))
            mode = QtGui.QTableWidgetItem(item.mode)
            self.ui.dayView.insertRow(0)
            self.ui.dayView.setItem(0, 0, time)
            self.ui.dayView.setItem(0, 1, mode)
        num = len(self.workDay.activity_list)
        self.ui.dayView.setRowCount(num)
        self.ui.dayView.setHorizontalHeaderLabels(['Time', 'Activity',
                                                   'Infringement'])


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Mainwindow()
    myapp.show()
    sys.exit(app.exec_())