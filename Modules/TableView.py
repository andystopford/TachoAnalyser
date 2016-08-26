from PyQt4 import QtGui, QtCore


class TableView(QtGui.QTableView):
    """
    Overrides QTreeView to handle selection events
    """
    def __init__(self, parent):
        super(TableView, self).__init__(parent)
        self.parent = parent
        self.set_pos()
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.connect(self, QtCore.SIGNAL("customContextMenuRequested(QPoint)"), self.right_click)

    def set_pos(self):
        self.setGeometry(QtCore.QRect(1, 38, 340, 414))

    def setModel(self, model):
        """
        Set up a QItemSelectionModel - sends the current and previous selection
        - we want the current ([0]) selection
        """
        super(TableView, self).setModel(self.parent.model)
        self.connect(self.selectionModel(),
                     QtCore.SIGNAL("selectionChanged(QItemSelection, QItemSelection)"),
                     self.get_selection)
        self.setColumnHidden(2, True)
        header = self.horizontalHeader()
        header.setResizeMode(1)

    def get_selection(self):
        index = self.selectedIndexes()[0]
        date = self.parent.model.itemFromIndex(index)
        row = date.row()
        comment = self.parent.model.item(row, 1)
        activities = self.parent.model.item(row, 2)
        self.parent.clear_input()
        self.parent.ui.commentsBox.setText(comment.text())
        self.parent.ui.textInput.setText(activities.text())
        self.parent.read_input()

    def right_click(self):
        menu = QtGui.QMenu(self)
        delete = QtGui.QAction('Delete', self)
        menu.addAction(delete)
        menu.popup(QtGui.QCursor.pos())
        delete.triggered.connect(self.delete_item)

    def delete_item(self):
        index = self.selectedIndexes()[0]
        item = self.parent.model.itemFromIndex(index)
        self.parent.model.removeRow(item.row())
        self.parent.clear_input()