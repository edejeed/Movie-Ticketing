import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow
from PyQt5.uic import loadUi
from db import *
from MessageBox import MessageBox

class AddMovie(QMainWindow):
    def __init__(self):
        super(AddMovie, self).__init__()
        loadUi("add_movies.ui", self)

        self.genreList = []
        self.__loadGenre()

        self.save.clicked.connect(self.__addMovie)

    def __loadGenre(self):
        res = GetGenreList()
        x = 0
        y = 0

        for genre in res:
            cb = QtWidgets.QCheckBox()
            cb.setText(genre[1])
            self.genreList.append(cb)
            self.gridLayout.addWidget(cb, x,y)
            if y == 2:
                y = 0
                x+=1
            else:
                y+=1

    def __addMovie(self):
        movieGenre = []
        for genre in enumerate(self.genreList):
            if genre[1].isChecked():
                movieGenre.append(genre[0] + 1)
    
        if self.title.text() != "" and self.synopsis.toPlainText() != "":
            AddNewMovie(self.title.text(), self.synopsis.toPlainText())
            res = GetMovieList(f"WHERE title=\'{self.title.text()}\' AND synopsis=\'{self.synopsis.toPlainText()}\'")
            for mg in movieGenre:
                AddMovieGenre(res[0][0], mg)
            MessageBox.showInformationMessage("Movie added successfully.", "Success")
        else:
            MessageBox.showErrorMessage("Please accomplish all fields and make sure to add a genre.", "Error") 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    booking = AddMovie()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(booking)
    widget.setFixedHeight(679)
    widget.setFixedWidth(804)
    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")