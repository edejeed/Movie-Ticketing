import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from db import *


class BookingList(QMainWindow):
    def __init__(self, widget = None):
        super(BookingList, self).__init__()
        loadUi("tickets.ui", self)

        self.bookingList.setColumnCount(3)
        self.bookingList.setHorizontalHeaderLabels(["Movie","Cinema", "Number of Tickets"])
        self.bookingList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.bookingList.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        self.__loadBookings()
    
    def __loadBookings(self):
        res = GetMovieCinemaOfBooking()
        print(res)
        self.bookingList.setRowCount(len(res))
        for booking in enumerate(res):
            self.bookingList.setItem(booking[0], 0, QtWidgets.QTableWidgetItem(str(booking[1][0])))
            self.bookingList.setItem(booking[0], 1, QtWidgets.QTableWidgetItem(str(booking[1][1])))
            self.bookingList.setItem(booking[0], 2, QtWidgets.QTableWidgetItem(str(booking[1][2])))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    movies = BookingList()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(movies)
    widget.setFixedHeight(600)
    widget.setFixedWidth(800)
    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")