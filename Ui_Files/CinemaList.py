import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow
from PyQt5.uic import loadUi
from db import *
from AddCinema import AddCinema
import BookingList
import MovieList
import CrewList
import Genre
import AdminList
import movie
from MessageBox import MessageBox

class CinemaList(QMainWindow):
    def __init__(self, widget = None):
        super(CinemaList, self).__init__()
        loadUi("cinema_list.ui", self)

        self.widget = widget
        if self.widget != None:
            self.widget.setFixedWidth(804)
            self.widget.setFixedHeight(604)

        #Table
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["id","Cinema Name", "Capacity"])
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableWidget.doubleClicked.connect(self.openInfo)

        # self.deleteButton.clicked.connect(self.__deleteClicked)
        # self.searchButton.clicked.connect(self.__searchClicked)
        self.addCinema.clicked.connect(self.addCinemaClicked)

        self.showButton.clicked.connect(self.__showClicked)
        self.genreButton.clicked.connect(self.__genreClicked)
        self.ticketsButton.clicked.connect(self.__ticketsClicked)
        self.movieButton.clicked.connect(self.__movieButtonClicked)
        self.crewButton.clicked.connect(self.__crewClicked)
        self.adminButton.clicked.connect(self.__adminClicked)
        
        self.showCinemaList()

    def addCinemaClicked(self):
        self.b = AddCinema(self)
        self.b.show()

    def showCinemaList(self, data = []):
        if data != []:
            cinemaList = data
        else:
            cinemaList = GetCinemaList()
        # print(genreList)
        self.tableWidget.setRowCount(len(cinemaList))

        for cinema in enumerate(cinemaList):
            self.tableWidget.setItem(cinema[0], 0, QtWidgets.QTableWidgetItem(str(cinema[1][0])))
            self.tableWidget.setItem(cinema[0], 1, QtWidgets.QTableWidgetItem(str(cinema[1][1])))
            self.tableWidget.setItem(cinema[0], 2, QtWidgets.QTableWidgetItem(str(cinema[1][2])))

    def openInfo(self):
        id = self.tableWidget.item(self.tableWidget.currentRow(), 0).text()
        self.b = AddCinema(self, "e", id)
        self.b.show()
    
    def __showClicked(self):
        self.a = movie.MovieScreen(self.widget)
        self.widget.addWidget(self.a)
        self.widget.removeWidget(self)
    
    def __movieButtonClicked(self):
        self.a = MovieList.MovieList(self.widget)
        self.widget.addWidget(self.a)
        self.widget.removeWidget(self)
    
    def __ticketsClicked(self):
        self.a = BookingList.BookingList(self.widget)
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    genre = CinemaList()
    genre.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")