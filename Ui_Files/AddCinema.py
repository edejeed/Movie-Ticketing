import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from db import *
from MessageBox import MessageBox

class AddCinema(QMainWindow):
    def __init__(self, parent = None, mode = "a", id = None):
        super(AddCinema, self).__init__()
        loadUi("add_cinema.ui", self)
        self.addCinemaButton.clicked.connect(self.__addCinemaClicked)

        self.parent = parent
        self.mode = mode
        self.id = id

        if mode == "e":
            self.__loadInfo()
    
    def __loadInfo(self):
        info = GetCinemaList(f"WHERE id = {self.id}")
        self.cinemaName.setText(str(info[0][1]))
        self.capacity.setValue(info[0][2])

    def __addCinemaClicked(self):
        if self.cinemaName.text() != "" and self.capacity.value() != 0:
            if self.mode == "a":
                AddNewCinema(self.cinemaName.text(), self.capacity.value())
                MessageBox.showInformationMessage("Cinema added.", "Success")
                self.cinemaName.setText("")
                self.capacity.setValue(0)
            else:
                UpdateCinema(self.id, self.cinemaName.text(), self.capacity.value())
                MessageBox.showInformationMessage("Cinema updated.", "Success")
                self.parent.showCinemaList()
            
            if self.parent != None:
                self.parent.showCinemaList()
        else:
            MessageBox.showErrorMessage("Please accomplish all fields.", "Error")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    booking = AddCinema()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(booking)
    widget.setFixedHeight(276)
    widget.setFixedWidth(261)
    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")