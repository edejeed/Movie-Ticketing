import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow
from PyQt5.uic import loadUi
from db import *
from AddMovie import AddMovie
from MessageBox import MessageBox

class MovieList(QMainWindow):
    def __init__(self, widget = None):
        super(MovieList, self).__init__()
        loadUi("movie_list.ui", self)

        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableWidget.doubleClicked.connect(self.openInfo)

        self.id = []
        self.loadMovieList()
    
    def loadMovieList(self):
        res = GetMovieList()

        self.tableWidget.setRowCount(len(res))

        for movie in enumerate(res):
            self.id.append(movie[1][0])
            self.tableWidget.setItem(movie[0], 0, QtWidgets.QTableWidgetItem(str(movie[1][1])))
            self.tableWidget.setItem(movie[0], 1, QtWidgets.QTableWidgetItem(str(movie[1][2])))

    def openInfo(self):
        id = self.id[self.tableWidget.currentRow()]
        self.a = AddMovie(self, "e", id)
        self.a.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    genre = MovieList()
    genre.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")