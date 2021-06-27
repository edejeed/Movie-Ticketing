import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow
from PyQt5.uic import loadUi
from MovieItem import MovieItem
from item import Ui_Form
import sqlite3

class MovieScreen(QMainWindow):
    def __init__(self):
        super(MovieScreen, self).__init__()
        loadUi("movies.ui", self)
        self.addTicket.clicked.connect(self.__addMovie)
        self.gridLayout.setSpacing(0)
        self.__gridX = 0
        self.__gridY = 0

    def __addMovie(self):
        self.gridLayout.addWidget(MovieItem("1", "poggers","what  what what"), self.__gridY, self.__gridX)
        
        if self.__gridX == 2:
            self.__gridX = 0
            self.__gridY += 1
        else:
            self.__gridX += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    movies = MovieScreen()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(movies)
    widget.setFixedHeight(600)
    widget.setFixedWidth(800)
    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")