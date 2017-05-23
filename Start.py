#!/usr/bin/python3.4
import sys

from PyQt4 import QtGui, Qt

from TachoAnalyser import MainWindow

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())