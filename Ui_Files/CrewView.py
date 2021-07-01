import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow
from PyQt5.uic import loadUi
from MovieItem import MovieItem
from BookTicket import BookTicket
import CrewBooking
from db import *
from MessageBox import MessageBox

class CrewView(QMainWindow):
    def __init__(self, widget = None):
        self.widget = widget
        super(CrewView, self).__init__()
        loadUi("crew_view.ui", self)

        if self.widget != None:
            self.widget.setFixedHeight(749)
            self.widget.setFixedWidth(847)
        else:
            self.widget = QtWidgets.QStackedWidget()
            
        self.bookTicket.clicked.connect(self.__bookTicket)
        self.movieButton_2.clicked.connect(self.__checkBookings)
        self.next.clicked.connect(self.__next)
        self.back.clicked.connect(self.__back)
        self.logoutButton.clicked.connect(self.logOut)
        
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
            self.widgs[x] = MovieItem(show)
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
    
    def __bookTicket(self):
        self.a = BookTicket()
        self.a.show()
    
    def __checkBookings(self):
        self.b = CrewBooking.CrewBooking(self.widget)
        self.widget.addWidget(self.b)
        self.widget.removeWidget(self)
    
    def logOut(self):
        self.widget.setFixedHeight(604)
        self.widget.setFixedWidth(804)
        for i in range(self.widget.count()):
            self.widget.removeWidget(self.widget.widget(1))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    booking = CrewView()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(booking)
    widget.setFixedHeight(749)
    widget.setFixedWidth(847)
    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")