from PyQt4 import QtGui, QtCore, Qt

import sys, os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'Modules'))
from TableView import*
from YearView import*

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self). __init__()
        # Specify the central widget for QMainWindow (not needed for QWidget ui)
        self.centralWidget = QtGui.QWidget()
        self.setCentralWidget(self.centralWidget)
        self.buttonSave = QtGui.QPushButton("Save")
        self.buttonBack = QtGui.QPushButton("<<")
        self.buttonForward = QtGui.QPushButton(">>")
        self.selectDriver = QtGui.QComboBox()
        self.label = QtGui.QLabel()
        self.label.setText("Year")
        self.yearView = YearView(self)      # Temp
        self.textInput = QtGui.QTextEdit()
        self.buttonClear = QtGui.QPushButton("Clear")
        self.buttonCalc = QtGui.QPushButton("Calculate")
        self.commentsBox = QtGui.QTextEdit()
        self.dayView = QtGui.QTableWidget()
        self.buttonAdd = QtGui.QPushButton("Add")
        self.workGraph = QtGui.QGraphicsView()

        # the basic layout:
        box = QtGui.QGridLayout()
        # Top button bar
        top_button_widget = QtGui.QWidget()
        top_button_layout = QtGui.QHBoxLayout()
        top_button_widget.setLayout(top_button_layout)
        top_button_layout.addWidget(self.buttonSave)
        top_button_layout.addWidget(self.buttonBack)
        top_button_layout.addWidget(self.label)
        top_button_layout.addWidget(self.buttonForward)
        top_button_layout.addWidget(self.selectDriver)
        self.label.setAlignment(Qt.Qt.AlignCenter)
        # Calendar secn
        top_box = QtGui.QWidget()
        top_box_layout = QtGui.QVBoxLayout()
        top_box.setLayout(top_box_layout)
        top_box_layout.addWidget(top_button_widget)
        top_box_layout.addWidget(self.yearView)
        # Calc buttons
        calc_box = QtGui.QWidget()
        calc_box_layout = QtGui.QHBoxLayout()
        calc_box.setLayout(calc_box_layout)
        calc_box_layout.addWidget(self.buttonClear)
        calc_box_layout.addWidget(self.buttonCalc)
        # Left mid top
        textInput_box = QtGui.QWidget()
        textInput_layout = QtGui.QVBoxLayout()
        textInput_box.setLayout(textInput_layout)
        textInput_layout.addWidget(self.textInput)
        # Left mid box
        left_mid_box = QtGui.QWidget()
        left_mid_layout = QtGui.QVBoxLayout()
        left_mid_box.setLayout(left_mid_layout)
        left_mid_layout.addWidget(textInput_box)
        left_mid_layout.addWidget(calc_box)
        # Right mid bottom
        add_box = QtGui.QWidget()
        add_layout = QtGui.QVBoxLayout()
        add_box.setLayout(add_layout)
        add_layout.addWidget(self.commentsBox)
        add_layout.addWidget(self.buttonAdd)
        # Right mid top
        dayView_box = QtGui.QWidget()
        textInput_layout = QtGui.QVBoxLayout()
        dayView_box.setLayout(textInput_layout)
        textInput_layout.addWidget(self.dayView)
        # Right mid
        splitter_R_mid = QtGui.QSplitter(Qt.Qt.Vertical)
        splitter_R_mid.addWidget(dayView_box)
        splitter_R_mid.addWidget(add_box)
        # Middle
        splitter_central = QtGui.QSplitter(Qt.Qt.Horizontal)
        splitter_central.addWidget(left_mid_box)
        splitter_central.addWidget(splitter_R_mid)
        # Top and middle
        splitter_top = QtGui.QSplitter(Qt.Qt.Vertical)
        splitter_top.addWidget(top_box)
        splitter_top.addWidget(splitter_central)
        # Bottom
        splitter_bottom = QtGui.QSplitter(Qt.Qt.Vertical)
        splitter_bottom.addWidget(splitter_top)
        splitter_bottom.addWidget(self.workGraph)
        box.addWidget(splitter_bottom)
        self.centralWidget.setLayout(box)
        QtGui.QApplication.setStyle(Qt.QStyleFactory.create('cleanlooks'))
        self.resize(1341, 718)




if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())