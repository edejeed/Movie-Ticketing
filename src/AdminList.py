import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow
from PyQt5.uic import loadUi
from db import *
from AddGenre import AddGenre
import BookingList
import MovieList
import CinemaList
import Genre
import movie
import CrewList
from MessageBox import MessageBox

class AdminList(QMainWindow):
    def __init__(self, widget = None):
        super(AdminList, self).__init__()
        loadUi("../Ui_Files/admin.ui", self)

        self.widget = widget
        if self.widget != None:
            self.widget.setFixedWidth(804)
            self.widget.setFixedHeight(604)

        #Table
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["id","username"])
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        self.showButton.clicked.connect(self.__showClicked)
        self.ticketsButton.clicked.connect(self.__ticketsClicked)
        self.cinemaButton.clicked.connect(self.__cinemaClicked)
        self.genreButton.clicked.connect(self.__genreClicked)
        self.movieButton.clicked.connect(self.__movieButtonClicked)
        self.crewButton.clicked.connect(self.__crewClicked)
        self.logoutButton.clicked.connect(self.logOut)

        self.loadCrew()
    
    def loadCrew(self):
        res = GetUserList(1)
        self.tableWidget.setRowCount(len(res))

        for crew in enumerate(res):
            self.tableWidget.setItem(crew[0], 0, QtWidgets.QTableWidgetItem(str(crew[1][0])))
            self.tableWidget.setItem(crew[0], 1, QtWidgets.QTableWidgetItem(str(crew[1][1])))
    
    def __showClicked(self):
        self.a = movie.MovieScreen(self.widget)
        self.widget.addWidget(self.a)
        self.widget.removeWidget(self)
    
    def __movieButtonClicked(self):
        self.a = MovieList.MovieList(self.widget)
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

    def __ticketsClicked(self):
        self.a = BookingList.BookingList(self.widget)
        self.widget.addWidget(self.a)
        self.widget.removeWidget(self)
    
    def __crewClicked(self):
        self.a = CrewList.CrewList(self.widget)
        self.widget.addWidget(self.a)
        self.widget.removeWidget(self)

    def logOut(self):
        self.widget.setFixedHeight(604)
        self.widget.setFixedWidth(804)
        for i in range(self.widget.count()):
            self.widget.removeWidget(self.widget.widget(1))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    genre = AdminList()
    genre.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")