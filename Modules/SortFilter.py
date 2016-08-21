from PyQt4 import QtCore, QtGui, Qt

class SortFilter(QtGui.QSortFilterProxyModel):
    def __init__(self, parent):
        QtGui.QSortFilterProxyModel.__init__(self)
