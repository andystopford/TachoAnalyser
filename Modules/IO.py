import sys
import xml.etree.ElementTree as ET
sys.path.append("./Modules")

class DataIO:
    def __init__(self, parent, path):
        self.path = path
        self.parent = parent    # i.e. Ui_MainWindow

    def open(self):
        with open(self.path, "r") as fo:
            tree = ET.ElementTree(file=self.path)
            root = tree.getroot()
            for date in root:
                activities = date[0]
                comments = date[1]
                self.parent.add_day(date.text, comments.text, activities.text)

    def add_day(self):
        activities = self.parent.ui.textInput.toPlainText()
        comments = self.parent.ui.commentsBox.toPlainText()
        model = self.parent.model
        model.add_date(self.parent.date, activities, comments)

    def save(self):
        model = self.parent.model
        root = ET.Element('Root')
        tree = ET.ElementTree(root)
        mod_root = model.invisibleRootItem()
        for i in range(0, mod_root.rowCount()):
            date = ET.SubElement(root, "Date")
            activities = ET.SubElement(date, 'Activities')
            comments = ET.SubElement(date, 'Comments')
            day = mod_root.child(i)
            date.text = day.text()  # The xml text
            comm = model.item(day.row(), 1)
            comments.text = comm.text()
            acts = model.item(day.row(), 2)
            activities.text = acts.text()

        with open(self.path, "wb") as fo:   # Must be 'wb', not 'w' in Python 3
            tree.write(fo)

        # TODO append to existing file, error message if no driver selected


