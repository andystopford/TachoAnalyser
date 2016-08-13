import sys
sys.path.append("./icons")
from PyQt4 import QtGui, QtSvg
import numpy

class TimeLine(QtGui.QGraphicsScene):
    def __init__(self, parent):
        QtGui.QGraphicsScene.__init__(self)
        self.parent = parent
        self.setSceneRect(0, 0, 1440, 50)   # Needs to be multiple of 1440 minutes (1 day)
        col = QtGui.QColor()
        col.setRgb(255, 0, 0)
        #self.activity_box(60, 20, 100, col)
        self.draw_ticks()
        #self.info_flag()
        #self.add_activities()

    def draw_ticks(self):
        # Draw the timeline
        item_list = []
        xform = QtGui.QTransform()
        top_line = QtGui.QGraphicsLineItem(0, 20, 1440, 20)
        bot_line = QtGui.QGraphicsLineItem(0, 40, 1440, 40)
        item_list.append(top_line)
        item_list.append(bot_line)
        ticks = numpy.arange(0, 1490, 60)
        hours = range(0, 25)
        print(ticks)
        for item in ticks:
            tick = QtGui.QGraphicsLineItem(item, 20, item, 40)
            item_list.append(tick)
        hour_x_xform = -19
        hour_y_xform = 37
        for hour in hours:
            hour = str(hour)
            hour = hour.zfill(2)
            hour = hour + ':' + '00'
            hour_label = QtGui.QGraphicsTextItem(hour)
            hour_label.setTransform(xform.translate(hour_x_xform, hour_y_xform))
            item_list.append(hour_label)
            hour_x_xform = 60
            hour_y_xform = 0
        # Group all the components
        group = self.createItemGroup(item_list)
        group.setZValue(1)
        # Draw pale blue background for timeline
        scale = QtGui.QGraphicsRectItem(0, 20, 1440, 20)
        col = QtGui.QColor()
        col.setRgb(160, 195, 255)
        scale.setBrush(col)
        self.addItem(scale)
        scale.setZValue(0)

    def add_activities(self):
        col = QtGui.QColor()
        for item in self.parent.driving_list:
            col.setRgb(255, 150, 150)   # Pink
            start = item.start
            end = item.end
            duration = item.duration
            self.activity_box(start, 20, duration, col)
        for item in self.parent.break_list:
            col.setRgb(150, 255, 150)  # Pale green
            start = item.start
            end = item.end
            duration = item.duration
            self.activity_box(start, 20, duration, col)
        for item in self.parent.work_list:
            col.setRgb(255, 213, 140)   # pale orange
            start = item.start
            end = item.end
            duration = item.duration
            self.activity_box(start, 20, duration, col)


    def activity_box(self, x, y, w, col):
        xform = QtGui.QTransform()
        box = QtGui.QGraphicsRectItem(x, y, w, 20)
        box.setPen(col)
        box.setBrush(col)
        self.addItem(box)
        #box.setTransform(xform.translate(200, 20))
        box.setZValue(0.5)
        #box.setFlag(QtGui.QGraphicsItem.ItemIsMovable)

    def info_flag(self, time):
        # To align the flag's pointer correctly, subtract 25 from the desired minute
        xform = QtGui.QTransform()
        flag = QtSvg.QGraphicsSvgItem('./icons/drive_infr.svg')
        self.addItem(flag)
        flag.setTransform(xform.translate((time - 25), -20))

