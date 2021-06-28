import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow
from PyQt5.uic import loadUi
from db import *
from MessageBox import MessageBox

class BookTicket(QMainWindow):
    def __init__(self):
        super(BookTicket, self).__init__()
        loadUi("add_cinema.ui", self)
        self.addCinemaButton.clicked.connect(self.__addCinemaClicked)

    def __addCinemaClicked(self):
        if self.cinemaName.text() != "" and self.capacity.value() != 0:
            AddCinema(self.cinemaName.text(), self.capacity.value())
            MessageBox.showInformationMessage("Cinema added.", "Success")
            self.cinemaName.setText("")
            self.capacity.setValue(0)
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