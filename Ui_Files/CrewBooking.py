import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
import CrewView
from db import *


class CrewBooking(QMainWindow):
    def __init__(self, widget = None):
        super(CrewBooking, self).__init__()
        loadUi("crewbooking.ui", self)

        self.widget = widget

        if self.widget != None:
            self.widget.setFixedHeight(600)
            self.widget.setFixedWidth(800)
        else:
            self.widget = QtWidgets.QStackedWidget()

        self.bookingList.setColumnCount(3)
        self.bookingList.setHorizontalHeaderLabels(["Movie","Cinema", "Number of Tickets"])
        self.bookingList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.bookingList.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        self.movieButton.clicked.connect(self.__loadMovies)

        self.__loadBookings()
    
    def __loadBookings(self):
        res = GetMovieCinemaOfBooking()

        self.bookingList.setRowCount(len(res))
        for booking in enumerate(res):
            self.bookingList.setItem(booking[0], 0, QtWidgets.QTableWidgetItem(str(booking[1][0])))
            self.bookingList.setItem(booking[0], 1, QtWidgets.QTableWidgetItem(str(booking[1][1])))
            self.bookingList.setItem(booking[0], 2, QtWidgets.QTableWidgetItem(str(booking[1][2])))

    def __loadMovies(self):
        self.a = CrewView.CrewView(self.widget)
        self.widget.addWidget(self.a)
        self.widget.removeWidget(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    movies = CrewBooking()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(movies)
    widget.setFixedHeight(600)
    widget.setFixedWidth(800)
    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")