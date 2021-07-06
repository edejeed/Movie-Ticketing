import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow
from PyQt5.uic import loadUi
from db import *
from AddMovie import AddMovie
import BookingList
import CrewList
import Genre
import CinemaList
import AdminList
import movie
from MessageBox import MessageBox

class MovieList(QMainWindow):
    def __init__(self, widget = None):
        super(MovieList, self).__init__()
        loadUi("../Ui_Files/movie_list.ui", self)

        self.widget = widget
        if self.widget != None:
            self.widget.setFixedWidth(810)
            self.widget.setFixedHeight(635)

        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableWidget.doubleClicked.connect(self.openInfo)

        self.showButton.clicked.connect(self.__showClicked)
        self.ticketsButton.clicked.connect(self.__ticketsClicked)
        self.cinemaButton.clicked.connect(self.__cinemaClicked)
        self.genreButton.clicked.connect(self.__genreClicked)
        self.crewButton.clicked.connect(self.__crewClicked)
        self.adminButton.clicked.connect(self.__adminClicked)
        self.logoutButton.clicked.connect(self.logOut)

        self.addMovie.clicked.connect(self.__addClicked)

        self.id = []
        self.loadMovieList()
    
    def __addClicked(self):
        self.a = AddMovie(self)
        self.a.show()

    def loadMovieList(self):
        res = GetMovieList()
        self.id = []
        self.tableWidget.setRowCount(len(res))

        for movie in enumerate(res):
            self.id.append(movie[1][0])
            self.tableWidget.setItem(movie[0], 0, QtWidgets.QTableWidgetItem(str(movie[1][1])))
            self.tableWidget.setItem(movie[0], 1, QtWidgets.QTableWidgetItem(str(movie[1][2])))

    def openInfo(self):
        id = self.id[self.tableWidget.currentRow()]
        self.a = AddMovie(self, "e", id)
        self.a.show()

    def __showClicked(self):
        self.a = movie.MovieScreen(self.widget)
        self.widget.addWidget(self.a)
        self.widget.removeWidget(self)

    def __ticketsClicked(self):
        self.a = BookingList.BookingList(self.widget)
        self.widget.addWidget(self.a)
        self.widget.removeWidget(self)

    def __cinemaClicked(self):
        self.a = CinemaList.CinemaList(self.widget)
        self.widget.addWidget(self.a)
        self.widget.removeWidget(self)
    
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

    def logOut(self):
        self.widget.setFixedHeight(604)
        self.widget.setFixedWidth(804)
        for i in range(self.widget.count()):
            self.widget.removeWidget(self.widget.widget(1))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    genre = MovieList()
    genre.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")