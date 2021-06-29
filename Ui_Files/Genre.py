import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow
from PyQt5.uic import loadUi
from db import *
from AddGenre import AddGenre
from MessageBox import MessageBox

class Genre(QMainWindow):
    def __init__(self):
        super(Genre, self).__init__()
        loadUi("genre-list.ui", self)

        #Table
        self.genreList.setColumnCount(2)
        self.genreList.setHorizontalHeaderLabels(["id","Genre"])
        self.genreList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.genreList.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.genreList.doubleClicked.connect(self.openInfo)

        self.deleteButton.clicked.connect(self.__deleteClicked)
        self.searchButton.clicked.connect(self.__searchClicked)
        
        self.showGenreList()

    def __searchClicked(self):
        l = GetGenreList(f"WHERE genre LIKE '%{self.lineEdit.text()}%'")
        self.showGenreList(l)

    def __deleteClicked(self):
        if self.genreList.selectedItems() == []:
            return

        id = self.genreList.item(self.genreList.currentRow(), 0).text()

        m = MessageBox.showConfirmationMessage("Delete Genre?", "Confirmation")
        
        if(m == QtWidgets.QMessageBox.Yes):
            DeleteGenre(id)
            self.showGenreList()
        
        MessageBox.showInformationMessage("Genre Deleted.", "Success")

    def showGenreList(self, data = []):
        if data != []:
            genreList = data
        else:
            genreList = GetGenreList()
        # print(genreList)
        self.genreList.setRowCount(len(genreList))

        for genre in enumerate(genreList):
            self.genreList.setItem(genre[0], 0, QtWidgets.QTableWidgetItem(str(genre[1][0])))
            self.genreList.setItem(genre[0], 1, QtWidgets.QTableWidgetItem(str(genre[1][1])))

    def openInfo(self):
        id = self.genreList.item(self.genreList.currentRow(), 0).text()
        self.b = AddGenre(self, "e", id)
        self.b.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    genre = Genre()
    genre.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")