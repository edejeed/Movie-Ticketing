import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow
from PyQt5.uic import loadUi
from db import *
from MessageBox import MessageBox

class AddMovie(QMainWindow):
    def __init__(self, parent = None, mode = "a", id = None):
        super(AddMovie, self).__init__(parent)
        loadUi("../Ui_Files/add_movies.ui", self)

        self.parent = parent
        self.mode = mode
        self.id = id

        self.genreList = []
                
        self.gnrID = []
        self.__loadGenre()

        if mode == "e":
            self.__loadEdit()

        self.save.clicked.connect(self.__addMovie)
        self.back.clicked.connect(self.__backButtonClicked)

    def __backButtonClicked(self):
        self.hide()

    def __loadGenre(self):
        res = GetGenreList()
        x = 0
        y = 0

        for genre in res:
            self.gnrID.append(genre[0])
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

        # Checks which checkboxes are selected. Returns ID of selected genres.
        for genre in enumerate(self.genreList):
            if genre[1].isChecked():
                movieGenre.append(self.gnrID[genre[0]])
    
        if self.title.text() != "" and self.synopsis.toPlainText() != "":
            if self.mode == "a":
                AddNewMovie(self.title.text(), self.synopsis.toPlainText())
                res = GetMovieList(f"WHERE title=\'{self.title.text()}\' AND synopsis=\'{self.synopsis.toPlainText()}\'")
                for mg in movieGenre:
                    AddMovieGenre(res[0][0], mg)
                MessageBox.showInformationMessage("Movie added successfully.", "Success")
            else:
                UpdateMovie(self.id, self.title.text(), self.synopsis.toPlainText())
                DeleteMovieGenre(self.id)

                for mg in movieGenre:
                    AddMovieGenre(self.id, mg)

                MessageBox.showInformationMessage("Movie updated.", "Success")
            
            if self.parent != None:
                self.parent.loadMovieList()

        else:
            MessageBox.showErrorMessage("Please accomplish all fields and make sure to add a genre.", "Error") 
            

    def __loadEdit(self):
        mov = GetMovieList(f"WHERE id = {self.id}")
        res = GetMovieGenre(f"WHERE movieID = {self.id}")
        
        # Uses mov instead of res for displaying title and synopsis due to instances where a movie has no genres.
        self.title.setText(mov[0][1])
        self.synopsis.setPlainText(mov[0][2])

        for mgID in res:
            for gID in enumerate(self.gnrID):
                # print(f"{gID[1]} {mgID[4]}")
                if gID[1] == mgID[4]:
                    self.genreList[gID[0]].toggle()

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