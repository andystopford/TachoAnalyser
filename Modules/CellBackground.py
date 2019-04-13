from PyQt4 import QtCore, QtGui


class CellBackground(QtGui.QStyledItemDelegate):
    def __init__(self, parent, row, col):
        super(CellBackground, self).__init__(parent)
        self.parent = parent
        self.row = row
        self.col = col

    def paint(self, painter, option, index):
        super(CellBackground, self).paint(painter, option, index)
        horiz_header = self.parent.yearView.horizontalHeader()
        cell_x = horiz_header.sectionSize(0)
        vert_header = self.parent.yearView.verticalHeader()
        cell_y = vert_header.sectionSize(0)
        wtd_colour = QtGui.QColor(255, 0, 255)
        hgv_colour = QtGui.QColor(255, 0, 0)

        size = QtCore.QSize()
        size.setHeight(cell_y)
        size.setWidth(cell_x)
        rect = QtCore.QRect(QtCore.QPoint(option.rect.x(), option.rect.y()
                                          + cell_y), size)

        if index.row() == self.row and index.column() == self.col:
            wtd_triangle = QtGui.QPolygon(3)
            wtd_triangle.setPoint(0, QtCore.QPoint(option.rect.x()+cell_x,
                                                   option.rect.y()))  # top right
            wtd_triangle.setPoint(1, QtCore.QPoint(option.rect.x(),
                                                   option.rect.y()))
            wtd_triangle.setPoint(2, QtCore.QPoint(option.rect.x(),
                                                   option.rect.y()+cell_y))  # bottom left

            hgv_triangle = QtGui.QPolygon(3)
            hgv_triangle.setPoint(0, QtCore.QPoint(option.rect.x() + cell_x,
                                                   option.rect.y()))
            hgv_triangle.setPoint(1, QtCore.QPoint(option.rect.x() + cell_x,
                                                   option.rect.y() + cell_y))
            hgv_triangle.setPoint(2, QtCore.QPoint(option.rect.x(),
                                                   option.rect.y() + cell_y))

            painter.save()
            painter.setRenderHint(painter.Antialiasing)
            painter.setBrush(QtGui.QBrush(QtGui.QColor(wtd_colour)))
            painter.setPen(QtGui.QPen(QtGui.QColor(wtd_colour)))
            painter.drawPolygon(wtd_triangle)
            painter.setBrush(QtGui.QBrush(QtGui.QColor(hgv_colour)))
            painter.drawPolygon(hgv_triangle)
            painter.setPen(QtGui.QPen(QtGui.QColor('black')))
            painter.drawText(QtCore.QPoint(option.rect.x() + (cell_x/4),
                                           option.rect.y() + (cell_y * 0.7)), "OK")
            painter.restore()

