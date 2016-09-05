#!/usr/bin/python3.4
import sys

# sys.path.append("./UI")
sys.path.append("./Modules")
sys.path.append("./Data")
from PyQt4 import QtCore, QtGui
from Activities import *
from Calculator import *
from IO import *
from Model import *
from TableView import *
from TimeConvert import *
from TimeLine import *
from Year import *
from YearView import *
import datetime
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


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.centralWidget = QtGui.QWidget()
        self.setCentralWidget(self.centralWidget)
        self.buttonSave = QtGui.QPushButton("Save")
        self.buttonBack = QtGui.QPushButton("<<")
        self.buttonForward = QtGui.QPushButton(">>")
        self.selectDriver = QtGui.QComboBox()
        self.selectDriver.setInsertPolicy(6)
        self.label = QtGui.QLabel()
        self.textInput = QtGui.QTextEdit()
        self.buttonClear = QtGui.QPushButton("Clear")
        self.buttonCalc = QtGui.QPushButton("Calculate")
        self.commentsBox = QtGui.QTextEdit()
        self.dayView = QtGui.QTableWidget()
        header = self.dayView.horizontalHeader()
        header.setResizeMode(QtGui.QHeaderView.Stretch)
        self.dayView.setColumnCount(3)
        self.dayView.setHorizontalHeaderLabels(['Hours', 'Activity',
                                                'Infringement'])
        self.buttonAdd = QtGui.QPushButton("Add")
        self.workGraph = QtGui.QGraphicsView()
        self.workGraph.setMinimumHeight(195)
        self.calculator = Calculator(self)
        self.TC = TimeConvert()
        self.timeLine = TimeLine(self)
        self.workGraph.setScene(self.timeLine)
        self.yearView = YearView(self)
        self.yearView.setMinimumHeight(330)

        # the basic layout:
        box = QtGui.QGridLayout()
        # Top button bar
        top_button_widget = QtGui.QWidget()
        top_button_layout = QtGui.QHBoxLayout()
        top_button_widget.setLayout(top_button_layout)
        top_button_layout.addWidget(self.buttonSave)
        top_button_layout.addWidget(self.buttonBack)
        top_button_layout.addWidget(self.label)
        top_button_layout.addWidget(self.buttonForward)
        top_button_layout.addWidget(self.selectDriver)
        self.label.setAlignment(Qt.Qt.AlignCenter)
        # Calendar secn
        top_box = QtGui.QWidget()
        top_box_layout = QtGui.QVBoxLayout()
        top_box.setLayout(top_box_layout)
        top_box_layout.addWidget(top_button_widget)
        top_box_layout.addWidget(self.yearView)
        # Calc buttons
        calc_box = QtGui.QWidget()
        calc_box_layout = QtGui.QHBoxLayout()
        calc_box.setLayout(calc_box_layout)
        calc_box_layout.addWidget(self.buttonClear)
        calc_box_layout.addWidget(self.buttonCalc)
        # Left mid top
        textInput_box = QtGui.QWidget()
        textInput_layout = QtGui.QVBoxLayout()
        textInput_box.setLayout(textInput_layout)
        textInput_layout.addWidget(self.textInput)
        # Left mid box
        left_mid_box = QtGui.QWidget()
        left_mid_layout = QtGui.QVBoxLayout()
        left_mid_box.setLayout(left_mid_layout)
        left_mid_layout.addWidget(textInput_box)
        left_mid_layout.addWidget(calc_box)
        # Right mid bottom
        add_box = QtGui.QWidget()
        add_layout = QtGui.QVBoxLayout()
        add_box.setLayout(add_layout)
        add_layout.addWidget(self.commentsBox)
        add_layout.addWidget(self.buttonAdd)
        # Right mid top
        dayView_box = QtGui.QWidget()
        textInput_layout = QtGui.QVBoxLayout()
        dayView_box.setLayout(textInput_layout)
        textInput_layout.addWidget(self.dayView)
        # Right mid
        splitter_R_mid = QtGui.QSplitter(Qt.Qt.Vertical)
        splitter_R_mid.addWidget(dayView_box)
        splitter_R_mid.addWidget(add_box)
        # Middle
        splitter_central = QtGui.QSplitter(Qt.Qt.Horizontal)
        splitter_central.addWidget(left_mid_box)
        splitter_central.addWidget(splitter_R_mid)
        # Top and middle
        splitter_top = QtGui.QSplitter(Qt.Qt.Vertical)
        splitter_top.addWidget(top_box)
        splitter_top.addWidget(splitter_central)
        # Bottom
        splitter_bottom = QtGui.QSplitter(Qt.Qt.Vertical)
        splitter_bottom.addWidget(splitter_top)
        splitter_bottom.addWidget(self.workGraph)
        box.addWidget(splitter_bottom)
        self.centralWidget.setLayout(box)
        # QtGui.QApplication.setStyle(Qt.QStyleFactory.create('cleanlooks'))
        self.resize(1125, 702)
        self.setWindowTitle("TachoAnalyser v 1.0")
        ##################################################
        # Signals
        self.buttonBack.clicked.connect(self.year_back)
        self.buttonForward.clicked.connect(self.year_forward)
        self.buttonClear.clicked.connect(self.clear_input)
        self.buttonCalc.clicked.connect(self.read_input)
        self.selectDriver.activated[str].connect(self.select_driver)
        self.buttonAdd.clicked.connect(self.add)
        self.buttonSave.clicked.connect(self.save)
        ##################################################
        # Initialise
        self.drivers = ['', 'Andy', 'Chris', 'Dan', 'Richard', 'DriverX']
        self.months = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 'Jul': '07',
                       'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
        self.selectDriver.addItems(self.drivers)
        # set to insert driver names alphabetically
        self.driver = ""
        self.key_list = []  # temp store for model_dict keys
        self.model_dict = {}
        self.infringements = ""
        today = datetime.date.today()
        self.year = today.year
        self.init_model()

    def init_model(self):
        # Placeholder model - called at startup or if no driver selected
        # so that the calendar dates can be filled in
        model = Model()
        model.set_year(self.year)
        self.yearView.setModel(model)
        self.yearView.set_selection_model(model)
        self.label.setText(str(self.year))
        self.clear_input()

    def year_back(self):
        self.year -= 1
        if str(self.year) not in self.model_dict:
            self.init_model()
        else:
            self.label.setText(str(self.year))
            self.clear_input()
            self.set_model()

    def year_forward(self):
        self.year += 1
        if str(self.year) not in self.model_dict:
            self.init_model()
        else:
            self.label.setText(str(self.year))
            self.clear_input()
            self.set_model()

    def clear_input(self):
        self.textInput.clear()
        # self.activity_list = []
        self.timeLine.clear_timeline()
        self.dayView.clearContents()
        self.commentsBox.clear()
        self.calculator.clear()

    def select_driver(self, driver):
        self.init_model()
        self.clear_input()
        self.driver = driver
        path = './Data/' + self.driver + '.xml'  # Test Path
        dataIO = DataIO(self, path)
        dataIO.get_years()
        for year in self.key_list:
            model = Model()
            self.model_dict[year] = model
        dataIO.open()
        self.set_model()

    def set_model(self):
        # print(self.model_dict)
        self.model = self.model_dict[str(self.year)]  # does this need to be global model?
        self.model.set_year(self.year)
        self.yearView.setModel(self.model)
        self.yearView.set_selection_model(self.model)
        self.label.setText(str(self.year))

    def read_input(self):
        # Activity change info from readesm is pasted in and converted to
        # minutes for start, end and duration
        activity_list = []
        text = self.textInput.toPlainText()
        text = str(text)
        date_line = re.search(r'Activities on (.*?) .*', text)
        date = (date_line.group())
        day = (date[22:24])
        day = day.strip()
        day = day.zfill(2)
        day = int(day)
        month_str = (date[18:21])
        month = self.months[month_str]
        month = int(month)
        year = (date[-5:-1])
        year = int(year)
        self.date = QtCore.QDate(year, month, day)

        # Get Activities
        working = re.findall(r'work, from (.*?) to (.*?) .*', text)
        for item in working:
            start = item[0]
            end = item[1]
            start = self.TC.hrs_to_mins(start)
            end = self.TC.hrs_to_mins(end)
            duration = self.TC.calc_duration(start, end)
            activity = Activity("Working", start, end, duration, "")
            activity_list.append(activity)

        driving = re.findall(r'driving, from (.*?) to (.*?) .*', text)
        for item in driving:
            start = item[0]
            end = item[1]
            start = self.TC.hrs_to_mins(start)
            end = self.TC.hrs_to_mins(end)
            duration = self.TC.calc_duration(start, end)
            activity = Activity("Driving", start, end, duration, "")
            activity_list.append(activity)

        break_rest = re.findall(r'break/rest, from (.*?) to (.*?) .*', text)
        for item in break_rest:
            start = item[0]
            end = item[1]
            start = self.TC.hrs_to_mins(start)
            end = self.TC.hrs_to_mins(end)
            duration = self.TC.calc_duration(start, end)
            activity = Activity("Break", start, end, duration, "")
            activity_list.append(activity)

        self.timeLine.add_activities(activity_list)
        activity_list.sort(key=lambda x: x.start, reverse=False)
        #for item in activity_list:
        self.calculator.timers(activity_list)
        self.show_activities(activity_list)

    def show_activities(self, activity_list):
        self.dayView.clearContents()
        for item in reversed(activity_list):
            item.duration = self.TC.mins_to_hrs(item.duration)
            hours = QtGui.QTableWidgetItem(item.duration)
            mode = QtGui.QTableWidgetItem(item.mode)
            infr = QtGui.QTableWidgetItem(item.infr)
            self.dayView.insertRow(0)
            self.dayView.setItem(0, 0, hours)
            self.dayView.setItem(0, 1, mode)
            self.dayView.setItem(0, 2, infr)
        num = len(activity_list)
        self.dayView.setRowCount(num)

    def add(self):
        # Invoked when add button pressed
        date = QtCore.QDate(self.date)
        activities = self.textInput.toPlainText()
        comments = self.commentsBox.toPlainText()
        # TODO Method specially for this

        year = date.year()
        month = date.month()
        day = date.day()
        year_instance = Year(self, year)
        col = year_instance.get_column(month, day)
        row = month - 1
        current_model = self.model_dict[str(year)]
        item = current_model.item(row, col)
        comment = QtGui.QStandardItem()
        activity = QtGui.QStandardItem()
        item.setChild(0, 2, comment)
        item.setChild(0, 3, activity)
        comment.setData(comments)
        activity.setData(activities)
        item.setBackground(QtGui.QColor(255, 158, 158))
        if self.infringements != "":
            item.setBackground(QtGui.QColor(255, 0, 0))

    def add_day(self, date, comments, activities):
        # Invoked from DataIO when it opens a file
        if date is not None:
            year = date[0:4]
            month = date[5:7]
            day = date[8:10]
            month = int(month)
            day = int(day)
            year_instance = Year(self, year)
            col = year_instance.get_column(month, day)
            row = month - 1
            current_model = self.model_dict[year]
            item = current_model.item(row, col)
            comment = QtGui.QStandardItem()
            activity = QtGui.QStandardItem()
            item.setChild(0, 2, comment)
            item.setChild(0, 3, activity)
            comment.setData(comments)
            activity.setData(activities)
            item.setBackground(QtGui.QColor(255, 158, 158))
            if self.infringements != "":
                item.setBackground(QtGui.QColor(255, 0, 0))
            self.infringements = ""

    def save(self):
        print(self.model_dict)
        for key in self.model_dict:
            model = self.model_dict[key]
            # Seems like year needs to be switched to add other years to model_dict
            data = []
            for row in range(model.rowCount()):
                data.append([])
                for column in range(model.columnCount()):
                    # index = model.index(row, column)
                    item = model.item(row, column)
                    # date = model(index)
                    if item.child(0, 3) is not None:
                        date = item.child(0, 1)  # Qdate
                        comm = item.child(0, 2)  # Comments
                        act = item.child(0, 3)  # Activities
                        date = date.data()
                        date = date.toString()
                        comment = comm.data()
                        activity = act.data()

                        data[row].append(date)
                        print(date)
                        print(comment)

            # path = './Data/' + self.driver + '.xml'  # Test path
            # dataIO = DataIO(self, path)
            # dataIO.save()

            # TODO add infringement highlighting


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())
