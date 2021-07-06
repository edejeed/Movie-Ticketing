import sys
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow
from PyQt5.uic import loadUi
from db import *
from MessageBox import MessageBox

class AddShow(QMainWindow):
    def __init__(self, parent=None, mode = "a", id=None, p=None):
        super(AddShow, self).__init__()
        loadUi("../Ui_Files/add_showing.ui", self)

        self.p = p
        self.parent = parent
        self.mode = mode
        self.id = id

        self.enter.clicked.connect(self.__enterClicked)

        self.movieID = []
        self.cinemaID = []

        self.__loadMovieList()
        self.__loadCinemaList()

        self.delB.clicked.connect(self.__delBClicked)
        self.delB.setVisible(False)

        if self.mode == "e":
            self.__loadInfo()
            self.delB.setVisible(True)
    
    def __delBClicked(self):
        r = MessageBox.showConfirmationMessage("Stop showing this movie?", "Confirmation")
        if r == QtWidgets.QMessageBox.Yes:
            UpdateShowing(self.id)
        if self.p != None:
            self.p.loadShows()

    def __loadInfo(self):
        res = GetShowInfo(self.id)
        
        self.movieTitle.setCurrentIndex(self.movieID.index(res[0][1])+1)
        self.cinemaName.setCurrentIndex(self.cinemaID.index(res[0][2])+1)
        self.dateEdit.setDate(QtCore.QDate.fromString(res[0][3], 'yyyy-MM-dd'))
        self.timeEdit.setTime(QtCore.QTime.fromString(res[0][4], 'hh:mm:ss'))
        
    def __enterClicked(self):
        if self.movieTitle.currentIndex() > 0 and self.cinemaName.currentIndex() > 0 :

            if self.mode == "a":
                AddNewShow(self.movieID[self.movieTitle.currentIndex()-1], self.cinemaID[self.cinemaName.currentIndex()-1], self.dateEdit.date().toString("yyyy-MM-dd"),self.timeEdit.time().toString("hh:mm:ss"), 1)
                MessageBox.showInformationMessage("Add new show successful.", "Success")
                self.movieTitle.setCurrentIndex(0)
                self.cinemaName.setCurrentIndex(0)
                if self.parent != None:
                    self.parent.loadShows()
            else:
                UpdateShow(self.id,self.movieID[self.movieTitle.currentIndex()-1], self.cinemaID[self.cinemaName.currentIndex()-1], self.dateEdit.date().toString("yyyy-MM-dd"),self.timeEdit.time().toString("hh:mm:ss"), 1)
            
                if self.p != None:
                    self.p.loadShows()
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