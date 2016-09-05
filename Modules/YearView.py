from PyQt4 import QtCore, QtGui

class YearView(QtGui.QTableView):
    def __init__(self, parent):
        super(YearView, self).__init__(parent)
        self.parent = parent
        horiz_header = self.horizontalHeader()
        horiz_header.setResizeMode(QtGui.QHeaderView.Stretch)
        vert_header = self.verticalHeader()
        vert_header.setResizeMode(QtGui.QHeaderView.Stretch)
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.connect(self, QtCore.SIGNAL("customContextMenuRequested(QPoint)"), self.right_click)

    def set_selection_model(self, model):
        """
        Set up a QItemSelectionModel - sends the current and previous selection
        - we want the current ([0]) selection
        """
        super(YearView, self).setModel(model)
        self.connect(self.selectionModel(),
                     QtCore.SIGNAL("selectionChanged(QItemSelection, QItemSelection)"),
                     self.get_selection)

    def get_selection(self):
        index = self.selectedIndexes()[0]
        day = self.parent.model.itemFromIndex(index)
        date = day.child(0, 1)
        comm = day.child(0, 2)
        act = day.child(0, 3)
        """
                if comm is not None:
            print(comm.data())
        else:
            print("No comment set")
        if act is not None:
            print(act.data())
        else:
            print("No activities recorded")
            """

        self.parent.clear_input()
        #self.parent.commentsBox.setText(comm.data())
        self.parent.textInput.setText(act.data())
        self.parent.read_input()

    def right_click(self):
        menu = QtGui.QMenu(self)
        delete = QtGui.QAction('Delete', self)
        menu.addAction(delete)
        menu.popup(QtGui.QCursor.pos())
        delete.triggered.connect(self.delete_item)

    def delete_item(self):
        print("Delete")
        index = self.selectedIndexes()[0]
        date = self.parent.model.itemFromIndex(index)
        date.removeRow(0)
        #self.parent.clear_input()
        # TODO clear coloured background - check whole entry is removed
