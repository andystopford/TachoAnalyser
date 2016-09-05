from PyQt4 import QtGui, Qt, QtCore
from itertools import cycle, islice
from Year import*


class Model(QtGui.QStandardItemModel):
    def __init__(self, parent=None):
        super(Model, self).__init__(parent)
        self.setRowCount(12)
        self.setColumnCount(37)
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        self.setVerticalHeaderLabels(months)
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        days_cycle = cycle(days)
        nth = lambda i, n, d=None: next(islice(i, n, None), d)
        day_labels = [nth(days_cycle, 0) for _ in range(37)]
        self.setHorizontalHeaderLabels(day_labels)
        # Colour weekends and weekdays differently and insert QStandardItems in each:
        for row in range(12):
            for col in range(37):
                if (col % 7) - 6 == 0 or (col % 7) - 5 == 0:
                    day = QtGui.QStandardItem()
                    self.setItem(row, col, day)
                    self.item(row, col).setBackground(QtGui.QColor(160, 195, 255))
                else:
                    day = QtGui.QStandardItem()
                    self.setItem(row, col, day)
                    self.item(row, col).setBackground(QtGui.QColor(195, 218, 255))

    def set_year(self, year):
        # fill in the appropriate dates, e.g. 1st, 2nd, etc
        year_instance = Year(self, year)
        months = year_instance.get_months()
        for month_num in range(12):
            curr_month = month_num
            month = months[month_num]
            for date in range(len(month)):
                curr_date = date
                date = month[date]
                item = self.item(curr_month, curr_date)
                item_text = str(date)
                if item is not None:
                    # Set text in calendar
                    item.setText(item_text)
                    item.setTextAlignment(Qt.Qt.AlignCenter)
                    # Make the QDate a child of the day
                    if date is not '':
                        date = int(date)
                        today = QtCore.QDate(year, curr_month + 1, date)
                        date = QtGui.QStandardItem()
                        item.setChild(0, 1, date)
                        date.setData(today)


    """
    def data(self, index, role):
        # Colour weekends and weekdays differently:
        if not index.isValid():
            return QtCore.QVariant()
        elif role == QtCore.Qt.BackgroundRole:
            for row in range(12):
                for col in range(37):
                    if index.column() % 7 -6 == 0:
                        return QtGui.QBrush(QtGui.QColor(100, 250, 213))
                    elif index.column() % 7 - 5 == 0:
                        return QtGui.QBrush(QtGui.QColor(100, 250, 213))
                    else:
                        return QtGui.QBrush(QtGui.QColor(188, 250, 213))
        if role == QtCore.Qt.DisplayRole:
            label = QtGui.QLabel()
            label.setText("test")
            #return label
    """


