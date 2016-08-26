import sys
sys.path.append("./Modules")
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from itertools import cycle, islice
from DateItem import*


class YearTable(QTableWidget):
    def __init__(self, parent=None):    
        QTableWidget.__init__(self, parent)
        horiz_header = self.horizontalHeader()
        horiz_header.setResizeMode(QHeaderView.Stretch)
        vert_header = self.verticalHeader()
        vert_header.setResizeMode(QHeaderView.Stretch)
        self.setRowCount(12)    #Must be set for the following 
        self.setColumnCount(37) #to work
        # Label the horiz.header:
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        days_cycle = cycle(days)
        nth = lambda i, n, d=None: next(islice(i, n, None), d)
        day_labels = [nth(days_cycle, 0) for _ in range(37)]
        self.setHorizontalHeaderLabels(day_labels)

        # Colour weekends and weekdays differently:
        for row in range(12):
            for col in range(37):
                if (col % 7) - 6 == 0:
                    self.setItem(row, col, DateItem())
                    self.item(row, col).setBackground(QColor(100,250,213))
                elif (col % 7) - 5 == 0:
                    self.setItem(row, col, DateItem())
                    self.item(row, col).setBackground(QColor(100,250,213))
                else:
                    self.setItem(row, col, DateItem())
                    self.item(row, col).setBackground(QColor(188,250,213))



