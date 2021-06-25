from PyQt5 import QtWidgets
from PyQt5.uic import loadUi

class MovieItem(QtWidgets.QWidget):
    def __init__(self, id, title, des): 
        super(MovieItem,self).__init__()
        loadUi("item.ui", self)
        self.id = id
        self.movieDesc.setText(des)

        