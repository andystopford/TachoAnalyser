from PyQt4 import QtGui


class DataModel(QtGui.QStandardItemModel):
    def __init__(self, parent):
        QtGui.QStandardItemModel.__init__(self)
        self.parent = parent

    def add_date(self, date, activities, comment):
        date = QtGui.QStandardItem(date)
        comment = QtGui.QStandardItem(comment)
        activities = QtGui.QStandardItem(activities)
        self.appendRow(date)
        date.appendRow(comment)
        comment.appendRow(activities)
        # TODO add sort by date function



