from PyQt5 import QtWidgets, QtCore
from PyQt5.uic import loadUi

class MovieItem(QtWidgets.QWidget):
    def __init__(self, show = ["","","","","",""]): 
        super(MovieItem,self).__init__()
        loadUi("item.ui", self)

        self.id = show[5]
        self.title.setText(show[0])
        self.cinema.setText(show[4])
        self.date.setText(QtCore.QDate.fromString(show[2], 'yyyy-MM-dd').toString('MMMM d, yyyy'))
        self.time.setText(QtCore.QTime.fromString(show[3], 'hh:mm:ss').toString('h:mm AP'))
        


        

        