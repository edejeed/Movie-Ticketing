import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from MovieItem import MovieItem
from AddShow import AddShow
import MovieList
import BookingList
import Genre
import CrewList
import AdminList
from db import *


class MovieScreen(QMainWindow):
    def __init__(self, widget = None):
        super(MovieScreen, self).__init__()
        loadUi("movies.ui", self)

        self.widget = widget
        if self.widget != None:
            self.widget.setFixedHeight(750)
            self.widget.setFixedWidth(861)

        self.addTicket.clicked.connect(self.__addMovie)
        self.next.clicked.connect(self.__next)
        self.back.clicked.connect(self.__back)
        self.movieButton.clicked.connect(self.__movieButtonClicked)
        self.ticketsButton.clicked.connect(self.__ticketsClicked)
        self.cinemaButton.clicked.connect(self.__cinemaClicked)
        self.genreButton.clicked.connect(self.__genreClicked)
        self.crewButton.clicked.connect(self.__crewClicked)
        self.adminButton.clicked.connect(self.__adminClicked)
        
        self.pageN = 1
        self.widgs = [MovieItem()]*6
        self.loadShows() 
    
    def __next(self):
        self.pageN +=1

        self.loadShows()

    def __back(self):
        if self.pageN == 1:
            return
        
        self.pageN -=1
        self.loadShows()

    def loadShows(self):
        self.page_4.setText(str(self.pageN))
        res = GetShow(self.pageN)
        self.__gridX = 0
        self.__gridY = 0

        for wid in self.widgs:
            wid.hide()

        x = 0
        for show in res:
            self.widgs[x] = MovieItem(show, self)
            self.gridLayout.addWidget(self.widgs[x], self.__gridY, self.__gridX)
        
            if self.__gridX == 2:
                self.__gridX = 0
                if self.__gridY == 1:
                    pass
                else:
                    self.__gridY += 1
            else:
                self.__gridX += 1

            x+=1

    def __addMovie(self):
        self.a = AddShow(self)
        self.a.show()

    def __movieButtonClicked(self):
        self.a = MovieList.MovieList(self.widget)
        self.widget.addWidget(self.a)
        self.widget.removeWidget(self)
    
    def __ticketsClicked(self):
        self.a = BookingList.BookingList(self.widget)
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
    movies = MovieScreen()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(movies)
    widget.setFixedHeight(750)
    widget.setFixedWidth(861)
    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")