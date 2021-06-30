import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
import MovieList
import movie
import Genre
import CrewList
import AdminList
from db import *


class BookingList(QMainWindow):
    def __init__(self, widget = None):
        super(BookingList, self).__init__()
        loadUi("tickets.ui", self)

        self.widget = widget
        if self.widget != None:
            self.widget.setFixedHeight(600)
            self.widget.setFixedWidth(800)

        self.bookingList.setColumnCount(3)
        self.bookingList.setHorizontalHeaderLabels(["Movie","Cinema", "Number of Tickets"])
        self.bookingList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.bookingList.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        self.movieButton.clicked.connect(self.__movieButtonClicked)
        self.showButton.clicked.connect(self.__showClicked)
        self.cinemaButton.clicked.connect(self.__cinemaClicked)
        self.genreButton.clicked.connect(self.__genreClicked)
        self.crewButton.clicked.connect(self.__crewClicked)
        self.adminButton.clicked.connect(self.__adminClicked)

        self.__loadBookings()
    
    def __loadBookings(self):
        res = GetMovieCinemaOfBooking()
        
        self.bookingList.setRowCount(len(res))
        for booking in enumerate(res):
            self.bookingList.setItem(booking[0], 0, QtWidgets.QTableWidgetItem(str(booking[1][0])))
            self.bookingList.setItem(booking[0], 1, QtWidgets.QTableWidgetItem(str(booking[1][1])))
            self.bookingList.setItem(booking[0], 2, QtWidgets.QTableWidgetItem(str(booking[1][2])))

    def __showClicked(self):
        self.a = movie.MovieScreen(self.widget)
        self.widget.addWidget(self.a)
        self.widget.removeWidget(self)
    
    def __movieButtonClicked(self):
        self.a = MovieList.MovieList(self.widget)
        self.widget.addWidget(self.a)
        self.widget.removeWidget(self)

    def __cinemaClicked(self):
        pass
    
    def __genreClicked(self):
        self.a = Genre.Genre(self.widget)
        self.widget.addWidget(self.a)
        self.widget.removeWidget(self)

    def __crewClicked(self):
        self.a = CrewList.CrewList(self.widget)
        self.widget.addWidget(self.a)
        self.widget.removeWidget(self)
    
    def __adminClicked(self):
        self.a = AdminList.AdminList(self.widget)
        self.widget.addWidget(self.a)
        self.widget.removeWidget(self)

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