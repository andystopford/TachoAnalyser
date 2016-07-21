#!/usr/bin/python3.4
import sys
sys.path.append("./UI")
sys.path.append("./Modules")
sys.path.append("./Data")
from PyQt4 import  QtCore, QtGui
from UI import Ui_MainWindow
from TimePopup import TimePopup
from WorkDay import WorkDay
from TimeConvert import*
from Activities import*
from Driving import*
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
        #self.ui.buttonDriving.clicked.connect(self.driving)
        #self.ui.buttonWorking.clicked.connect(self.working)
        #self.ui.buttonBreak.clicked.connect(self.resting)
        self.ui.buttonCalc.clicked.connect(self.calc)
        self.ui.calendar.clicked.connect(self.set_day)
        self.ui.selectDriver.activated[str].connect(self.select_driver)
        ##################################################
        # Initialise
        header = self.ui.dayView.horizontalHeader()
        header.setResizeMode(QtGui.QHeaderView.Stretch)
        self.ui.buttonDriving.setEnabled(False)
        self.ui.buttonWorking.setEnabled(False)
        self.ui.buttonBreak.setEnabled(False)
        self.ui.selectDriver.addItems(self.drivers)
        # set to insert driver names alphabetically
        self.ui.selectDriver.setInsertPolicy(6)
        self.timeConvert = TimeConvert()

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
        working = re.findall(r'work, from (.*?) to (.*?) .*', text)
        for item in working:
            start = item[0]
            end = item[1]
            start = self.timeConvert.hrs_to_mins(start)
            end = self.timeConvert.hrs_to_mins(end)
            self.activity = Activity("Working", start, end)
            self.activity.calc_duration()
            self.workDay.activity_list.append(self.activity)
        driving = re.findall(r'driving, from (.*?) to (.*?) .*', text)
        for item in driving:
            start = item[0]
            end = item[1]
            start = self.timeConvert.hrs_to_mins(start)
            end = self.timeConvert.hrs_to_mins(end)
            self.activity = Activity("Driving", start, end)
            self.activity.calc_duration()
            self.workDay.activity_list.append(self.activity)
        break_rest = re.findall(r'break/rest, from (.*?) to (.*?) .*', text)
        for item in break_rest:
            start = item[0]
            end = item[1]
            start = self.timeConvert.hrs_to_mins(start)
            end = self.timeConvert.hrs_to_mins(end)
            self.activity = Activity("Break", start, end)
            self.activity.calc_duration()
            self.workDay.activity_list.append(self.activity)
        break_short = re.findall(r'short break, from (.*?) to (.*?) .*', text)
        for item in break_short:
            start = item[0]
            end = item[1]
            start = self.timeConvert.hrs_to_mins(start)
            end = self.timeConvert.hrs_to_mins(end)
            self.activity = Activity("Short Break", start, end)
            self.activity.calc_duration()
            self.workDay.activity_list.append(self.activity)
        self.workDay.sort()
        self.workDay.check_breaks()
        self.show_activities()


    def show_activities(self):
        self.ui.dayView.clear()
        for item in reversed(self.workDay.activity_list):
            item.duration = self.timeConvert.mins_to_hrs(item.duration)
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