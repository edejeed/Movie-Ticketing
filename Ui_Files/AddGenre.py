import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow
from PyQt5.uic import loadUi
from db import *
from MessageBox import MessageBox

class BookTicket(QMainWindow):
    def __init__(self):
        super(BookTicket, self).__init__()
        loadUi("add_genre.ui", self)
        self.addGenreButton.clicked.connect(self.__addGenreClicked)

    def __addGenreClicked(self):
        if self.genreName.text() != "":
            AddGenre(self.genreName.text())
            MessageBox.showInformationMessage("Genre added.", "Success")
        else:
            MessageBox.showErrorMessage("Please accomplish all fields.", "Error")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    booking = BookTicket()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(booking)
    widget.setFixedHeight(276)
    widget.setFixedWidth(261)
    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")