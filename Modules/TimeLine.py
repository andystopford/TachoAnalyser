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
        self.box_list = []
        self.flag_list = []
        self.draw_ticks()
        self.draw_key()

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

    def draw_key(self):
        xform = QtGui.QTransform()
        col = QtGui.QColor()

        drive_box = QtGui.QGraphicsRectItem(590, 90, 50, 20)
        col.setRgb(255, 150, 150)
        drive_box.setBrush(col)
        self.addItem(drive_box)
        drive_box_label = QtGui.QGraphicsTextItem("Driving")
        self.addItem(drive_box_label)
        drive_box_label.setTransform(xform.translate(590, 87))

        break_box = QtGui.QGraphicsRectItem(690, 90, 50, 20)
        col.setRgb(150, 255, 150)
        break_box.setBrush(col)
        self.addItem(break_box)
        break_box_label = QtGui.QGraphicsTextItem("Break")
        self.addItem(break_box_label)
        break_box_label.setTransform(xform.translate(105, 0))

        work_box = QtGui.QGraphicsRectItem(790, 90, 50, 20)
        col.setRgb(255, 213, 140)
        work_box.setBrush(col)
        self.addItem(work_box)
        work_box_label = QtGui.QGraphicsTextItem("Working")
        self.addItem(work_box_label)
        work_box_label.setTransform(xform.translate(93, 0))

    def add_activities(self, activity_list):
        col = QtGui.QColor()
        for item in activity_list:
            if item.mode == "Driving":
                col.setRgb(255, 150, 150)  # Pink
            if item.mode == "Break":
                col.setRgb(109, 255, 174)  # Pale green
            if item.mode == "Working":
                col.setRgb(255, 205, 117)  # pale orange
            start = item.start
            duration = item.duration
            self.activity_box(start, 20, duration, col)

    def activity_box(self, x, y, w, col):
        box = QtGui.QGraphicsRectItem(x, y, w, 20)
        box.setPen(col)
        box.setBrush(col)
        self.addItem(box)
        box.setZValue(0.5)
        self.box_list.append(box)

    def infr_flag(self, time, rule):
        # To align the flag's pointer correctly, subtract 25 from the desired minute
        xform = QtGui.QTransform()
        if rule == "hgv":
            flag = QtSvg.QGraphicsSvgItem('./icons/drive_infr.svg')
            flag.setTransform(xform.translate((time - 25), -20))
        else:
            flag = QtSvg.QGraphicsSvgItem('./icons/wtd_infr.svg')
            flag.setTransform(xform.translate((time - 25), 45))
        self.addItem(flag)
        self.flag_list.append(flag)

    def clear_timeline(self):
        for box in self.box_list:
            self.removeItem(box)
        for flag in self.flag_list:
            self.removeItem(flag)
        self.flag_list = []
        self.box_list = []