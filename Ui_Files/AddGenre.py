import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow
from PyQt5.uic import loadUi
from db import *
from MessageBox import MessageBox

class AddGenre(QMainWindow):
    def __init__(self, parent = None, mode="a", id=None):
        super(AddGenre, self).__init__(parent)
        loadUi("add_genre.ui", self)

        self.p = parent
        self.mode = mode
        self.id = id
        self.addGenreButton.clicked.connect(self.__addGenreClicked)

        if mode == "e":
            self.addGenreButton.setText("Confirm Edit")
            self.systemLabel.setText("Edit")
            self.__showEditInfo(id)

    def __showEditInfo(self, id):
        info = GetGenreList(f"WHERE genreID = {id}")
        self.genreName.setText(info[0][1])

    def __addGenreClicked(self):
        if self.genreName.text() != "":
            if self.mode != "e":
                AddNewGenre(self.genreName.text())
                MessageBox.showInformationMessage("Genre added.", "Success")
                self.genreName.setText("")
            else:
                UpdateGenre(self.id, self.genreName.text())
                MessageBox.showInformationMessage("Genre edited.", "Success")
            
            if self.p != None:
                self.p.showGenreList()
            
        else:
            MessageBox.showErrorMessage("Please accomplish all fields.", "Error")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    booking = AddGenre()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(booking)
    widget.setFixedHeight(276)
    widget.setFixedWidth(261)
    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")