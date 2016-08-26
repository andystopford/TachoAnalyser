from PyQt4 import QtGui


class SortFilter(QtGui.QSortFilterProxyModel):
    def __init__(self, parent=None):
        super(SortFilter, self).__init__(parent)


