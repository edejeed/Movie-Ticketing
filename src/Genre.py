import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow
from PyQt5.uic import loadUi
from db import *
from AddGenre import AddGenre
import BookingList
import CinemaList
import MovieList
import CrewList
import AdminList
import movie
from MessageBox import MessageBox

class Genre(QMainWindow):
    def __init__(self, widget = None):
        super(Genre, self).__init__()
        loadUi("../Ui_Files/genre-list.ui", self)

        self.widget = widget
        if self.widget != None:
            self.widget.setFixedWidth(621)
            self.widget.setFixedHeight(550)

        #Table
        self.genreList.setColumnCount(2)
        self.genreList.setHorizontalHeaderLabels(["id","Genre"])
        self.genreList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.genreList.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.genreList.doubleClicked.connect(self.openInfo)

        self.delGenre.clicked.connect(self.__deleteClicked)
        self.searchButton.clicked.connect(self.__searchClicked)
        self.addGenre.clicked.connect(self.__addGenreClicked)

        self.showButton.clicked.connect(self.__showClicked)
        self.ticketsButton.clicked.connect(self.__ticketsClicked)
        self.cinemaButton.clicked.connect(self.__cinemaClicked)
        self.movieButton.clicked.connect(self.__movieButtonClicked)
        self.crewButton.clicked.connect(self.__crewClicked)
        self.adminButton.clicked.connect(self.__adminClicked)
        self.logoutButton.clicked.connect(self.logOut)
        
        self.showGenreList()

    def __addGenreClicked(self):
        self.b = AddGenre(self)
        self.b.show()

    def __searchClicked(self):
        l = GetGenreList(f"WHERE genre LIKE '%{self.lineEdit.text()}%'")
        self.showGenreList(l)

    def __deleteClicked(self):
        if self.genreList.selectedItems() == []:
            return

        id = self.genreList.item(self.genreList.currentRow(), 0).text()

        m = MessageBox.showConfirmationMessage("Delete Genre?", "Confirmation")
        
        if(m == QtWidgets.QMessageBox.Yes):
            try:
                DeleteGenre(id)
                MessageBox.showInformationMessage("Genre Deleted.", "Success")
                self.showGenreList()
            except Exception as e:
                MessageBox.showInformationMessage("Unable to delete genre.", "Error")
        

    def showGenreList(self, data = []):
        if data != []:
            genreList = data
        else:
            genreList = GetGenreList()
        # print(genreList)
        self.genreList.setRowCount(len(genreList))

        for genre in enumerate(genreList):
            self.genreList.setItem(genre[0], 0, QtWidgets.QTableWidgetItem(str(genre[1][0])))
            self.genreList.setItem(genre[0], 1, QtWidgets.QTableWidgetItem(str(genre[1][1])))

    def openInfo(self):
        id = self.genreList.item(self.genreList.currentRow(), 0).text()
        self.b = AddGenre(self, "e", id)
        self.b.show()
    
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
    
    def __ticketsClicked(self):
        self.a = BookingList.BookingList(self.widget)
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
    genre = Genre()
    genre.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")