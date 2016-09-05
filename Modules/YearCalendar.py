import sys
#sys.path.append("./Modules")
from PyQt4 import QtGui, Qt
from YearView import*
from Model import*
import datetime


class YearCalendar(QtGui.QWidget):
    def __init__(self, parent):
        QtGui.QWidget.__init__(self, parent)
        self.parent = parent
        self.resize(1341, 718)
        self.button_back = QtGui.QPushButton("<<")
        self.button_forward = QtGui.QPushButton(">>")
        self.button_test = QtGui.QPushButton("Test")
        self.button_layers = QtGui.QPushButton("Layers")
        self.label = QtGui.QLabel()
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.button_test)
        hbox.addWidget(self.button_back)
        hbox.addWidget(self.label)
        self.label.setAlignment(Qt.Qt.AlignCenter)
        hbox.addWidget(self.button_forward)
        hbox.addWidget(self.button_layers)
        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addLayout(hbox)
        self.setLayout(self.vbox)
        #self.show()

        #####################################################
        # Signals
        self.button_back.clicked.connect(self.year_back)
        self.button_forward.clicked.connect(self.year_forward)
        self.button_test.clicked.connect(self.test)
        #####################################################
        today = datetime.date.today()
        self.year = today.year
        self.add_view()
        self.init_calendar(self.year)


    def add_view(self):
        self.vbox.addWidget(self.parent.yearView)
        #self.yearView.setModel(self.parent.model)
        #self.yearView.set_selection_model(self.parent.model)

    def init_calendar(self, year):
        self.label.setText(str(self.year))
        #self.parent.model.set_year(year)
        
    def test(self):
        item = self.parent.model.item(0, 4)
        comment = QtGui.QStandardItem()
        activities = QtGui.QStandardItem()
        item.setChild(0, 1, comment)
        comment.setData("Comment")
        item.setChild(0, 2, activities)
        activities.setData("Activities")

    def year_back(self):
        self.year -= 1
        self.init_calendar(self.year)

    def year_forward(self):
        self.year += 1
        self.init_calendar(self.year)
