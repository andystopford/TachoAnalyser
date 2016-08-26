#!/usr/bin/env python
# coding=utf8
######################################################################

#Copyright (C)2015 Andy Stopford                                
#
#This is free software: you can redistribute it and/or modify 
#under the terms of the GNU General Public License
#as published by the Free Software Foundation; version 2.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, see <http://www.gnu.org/licenses/>.

#######################################################################
#import sip		# returns native Python types rather than QString, etc
#sip.setapi('QString', 2)
#sip.setapi('QVariant', 2)
import sys
sys.path.append("./modules")
sys.path.append("./UI")
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from almanac import*
#from EventPopup import*
from DateItem import*
from YearTable import*
import datetime


class YearPlanner(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.resize(1341, 718)
        self.button_back = QPushButton("<<")
        self.button_forward = QPushButton(">>")
        self.button_test = QPushButton("Test")
        self.button_layers = QPushButton("Layers")
        self.label = QLabel()
        hbox = QHBoxLayout()
        hbox.addWidget(self.button_test)
        hbox.addWidget(self.button_back)
        hbox.addWidget(self.label)
        self.label.setAlignment(Qt.AlignCenter)
        hbox.addWidget(self.button_forward)
        hbox.addWidget(self.button_layers)
        self.vbox = QVBoxLayout()
        self.vbox.addLayout(hbox)
        self.setLayout(self.vbox)
        self.show()

        #####################################################
        # Signals
        self.button_back.clicked.connect(self.year_back)
        self.button_forward.clicked.connect(self.year_forward)
        self.button_test.clicked.connect(self.test)
        #####################################################
        # Create dictionary to store table instances
        self.table_dict = {}
        today = datetime.date.today()
        self.year = today.year
        self.add_table()
        self.init_planner(self.year)

    def init_planner(self, year):
        self.label.setText(str(self.year))
        year_instance = Year(self, year)
        months = year_instance.get_months()
        for month in range(12):
            curr_month = month
            month = months[month]
            for date in range(len(month)):
                curr_date = date
                date = month[date]
                item = self.yearTable.item(curr_month, curr_date)
                item.setText(str(date))
                item.setTextAlignment(0x0020)
                item.setTextAlignment(0x0004)

    def add_table(self):
        # Create table instance for currently displayed year
        self.yearTable = YearTable()
        self.table_dict[str(self.year)] = self.yearTable
        self.vbox.addWidget(self.yearTable)
        self.yearTable.cellClicked.connect(self.event_edit)

    def event_edit(self, row, column):   
        # So we can get the Q.TW item at that cell. This item contains
        # events for that day, which can be set, edited, etc. via the popup.     
        item = self.yearTable.item(row, column)
        day = item.text()
        if day != '':
            print(day)
            print(row)
            #self.eventPopup = EventPopup(self, int(row), int(column), self.year)
            #self.eventPopup.show()
            #pos = QCursor.pos()
            #self.eventPopup.move(pos)
        
    def test(self):
        #date = [QDate(2016, 4, 1)]
        date = [(1, 4, 2016)]
        year_instance = Year(self, 2016)
        date_index = year_instance.get_indices(date)
        print(date_index)

        cell = self.yearTable.itemAt(5, 5)
        cell.setBackgroundColor(QColor(255, 0, 0))

    def year_back(self):
        self.year -= 1
        self.init_planner(self.year)

    def year_forward(self):
        self.year += 1
        self.init_planner(self.year)


if __name__=="__main__":

    app = QApplication(sys.argv)
    myapp = YearPlanner()
    myapp.show()
    myapp.raise_()
    sys.exit(app.exec_())