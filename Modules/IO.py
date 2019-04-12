import sys
import xml.etree.ElementTree as ET
sys.path.append("./Modules")
from PyQt4 import QtCore, QtGui
from Year import *

class DataIO:
    def __init__(self, parent):
        self.parent = parent

    def open(self, path):
        """Opens the selected driver's year file"""
        with open(path, "r") as fo:
            tree = ET.ElementTree(file=path)
            root = tree.getroot()
            for date in root:
                comms = date[0]
                acts = date[1]
                infrs = date[2]
                self.add_day(date.text, comms.text, acts.text, infrs.text)

    def add_day(self, date, comments, activities, infringements):
        """For each recorded day in the selected driver's year file, populates
        the appropriate model"""
        if date is not None:
            date = QtCore.QDate.fromString(date)
            day = date.day()
            month = date.month()
            year = date.year()
            year_instance = Year(self, year)
            col = year_instance.get_column(month, day)
            row = month - 1
            current_model = self.parent.model_dict[year]
            item = current_model.item(row, col)
            comment = QtGui.QStandardItem()
            activity = QtGui.QStandardItem()
            infringed = QtGui.QStandardItem()
            item.setChild(0, 2, comment)
            item.setChild(0, 3, activity)
            item.setChild(0, 4, infringed)
            comment.setData(comments)
            activity.setData(activities)
            infringed.setData(infringements)
            if infringed.data() is None:
                item.setBackground(QtGui.QColor(109, 255, 174))
            if infringed.data() == "hgv":
                item.setBackground(QtGui.QColor(255, 150, 150))
            if infringed.data() == "wtd":
                item.setBackground(QtGui.QColor(255, 205, 117))
            if infringed.data() == "both":
                pixmap = QtGui.QPixmap('./icons/dual_infr.svg')
                brush = QtGui.QBrush(pixmap)
                item.setBackground(brush)
            self.parent.infringements = ""

    def save(self, model_dict):
        for key in model_dict:
            root = ET.Element('Root')
            tree = ET.ElementTree(root)
            path = './Data/' + self.parent.driver + str(key) + '.xml'
            model = model_dict[key]
            data = []
            for row in range(model.rowCount()):
                data.append([])
                for column in range(model.columnCount()):
                    item = model.item(row, column)
                    if item.child(0, 3) is not None:
                        date = item.child(0, 1)  # Qdate
                        comments = item.child(0, 2)  # Comments
                        activities = item.child(0, 3)  # Activities
                        infringements = item.child(0, 4)   # Infringements
                        if date:
                            date = date.data()
                            date = date.toString()
                            print(date)
                            comments = comments.data()
                            activities = activities.data()
                            infringements = infringements.data()
                            # Set ET sub-elements
                            dte = ET.SubElement(root, "Date")
                            comms = ET.SubElement(dte, 'Comments')
                            acts = ET.SubElement(dte, 'Activities')
                            infrs = ET.SubElement(dte, 'Infringements')
                            dte.text = date
                            comms.text = comments
                            acts.text = activities
                            infrs.text = infringements
                            with open(path, "wb") as fo:
                                tree.write(fo)




