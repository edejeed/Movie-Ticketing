import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow
from PyQt5.uic import loadUi
from db import *
from MessageBox import MessageBox

class BookTicket(QMainWindow):
    def __init__(self):
        super(BookTicket, self).__init__()
        loadUi("../Ui_Files/book-a-ticket.ui", self)

        self.movieTitle.currentIndexChanged.connect(self.__cbChanged)
        self.cinemaName.currentIndexChanged.connect(self.__cbChanged)
        self.bookTicketButton.clicked.connect(self.__bookTicketClicked)

        self.movieID = []
        self.cinemaID = []

        self.__loadMovieList()
        self.__loadCinemaList()
        
    def __bookTicketClicked(self):
        if self.movieTitle.currentIndex() > 0 and self.cinemaName.currentIndex() > 0 and self.noOfTickets.value() > 0 and self.schedule.currentIndex() > 0:
            AddNewBooking(self.movieID[self.movieTitle.currentIndex()-1], self.cinemaID[self.cinemaName.currentIndex()-1], self.noOfTickets.value())
            MessageBox.showInformationMessage("Booking successful.", "Success")
            self.movieTitle.setCurrentIndex(0)
            self.cinemaName.setCurrentIndex(0)
            self.noOfTickets.setValue(0)
            self.schedule.setCurrentIndex(0)
        else:
            MessageBox.showErrorMessage("Please accomplish every field.", "Error")

    def __cbChanged(self):
        if self.movieTitle.currentIndex() > 0 and self.cinemaName.currentIndex() > 0:
            self.schedule.clear()
            self.__loadSchedule()

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
        
    def __loadSchedule(self):
        schedList = getScheduleList(self.movieID[self.movieTitle.currentIndex()-1], self.cinemaID[self.cinemaName.currentIndex()-1])
        self.schedule.addItem("")
        for sched in schedList:
            self.schedule.addItem(f"Day: {sched[0]} Time: {sched[1]}")
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    booking = BookTicket()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(booking)
    widget.setFixedHeight(400)
    widget.setFixedWidth(274)
    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")