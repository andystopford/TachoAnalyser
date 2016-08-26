#!/usr/bin/python
# -*- coding: utf-8 -*-
######################################################################

#Copyright (C)2015 Andy Stopford                                
#
#This is free software: you can redistribute it and/or modify 
#under the terms of the GNU General Public License
#as published by the Free Software Foundation; version 2.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, see <http://www.gnu.org/licenses/>.

#######################################################################

from PyQt4.QtCore import *
from PyQt4.QtGui import *


class DateItem(QTableWidgetItem):
    """
    Instantiated for each day of the year 
    stores events for that day
    """
    def __init__(self):
        QTableWidgetItem.__init__(self)
        self.event_list = []

    def add_event(self, event):
        self.event_list.append(event)


class DateEvent():
    """
    Spans selected number of days and stores data 
    for those days
    """
    def __init__(self, dates):
        self.event_dates = dates

    def tag(self, tag):
        self.event_tag = tag

    def content(self, text):
        self.event_content = text

    def get_tag(self):
        return self.event_tag

    def get_content(self):
        return self.event_content

    def get_dates(self):
        return self.event_dates