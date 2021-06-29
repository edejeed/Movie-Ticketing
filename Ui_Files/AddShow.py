import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow
from PyQt5.uic import loadUi
from db import *
from MessageBox import MessageBox

class AddShow(QMainWindow):
    def __init__(self, parent=None):
        super(AddShow, self).__init__()
        loadUi("add_showing.ui", self)

        self.parent = parent

        self.enter.clicked.connect(self.__enterClicked)

        self.movieID = []
        self.cinemaID = []

        self.__loadMovieList()
        self.__loadCinemaList()
        
    def __enterClicked(self):
        if self.movieTitle.currentIndex() > 0 and self.cinemaName.currentIndex() > 0 :

            AddNewShow(self.movieID[self.movieTitle.currentIndex()-1], self.cinemaID[self.cinemaName.currentIndex()-1], self.dateEdit.date().toString("yyyy-MM-dd"),self.timeEdit.time().toString("hh:mm:ss"), 1)
            MessageBox.showInformationMessage("Add new show successful.", "Success")
            if self.parent != None:
                self.parent.loadShows()
            self.movieTitle.setCurrentIndex(0)
            self.cinemaName.setCurrentIndex(0)
        else:
            MessageBox.showErrorMessage("Please accomplish every field.", "Error")

    def __loadMovieList(self):
        movieList = GetMovieList()
        self.movieTitle.addItem("Select Movie")

        for movie in movieList:
            self.movieID.append(movie[0])
            self.movieTitle.addItem(movie[1])
    
    def __loadCinemaList(self):
        cinemaList = GetCinemaList()
        self.cinemaName.addItem("Select Cinema")

        for cinema in cinemaList:
            self.cinemaID.append(cinema[0])
            self.cinemaName.addItem(cinema[1])
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    booking = AddShow()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(booking)
    widget.setFixedHeight(400)
    widget.setFixedWidth(274)
    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")