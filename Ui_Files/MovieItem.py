from PyQt5 import QtWidgets, QtCore
from PyQt5.uic import loadUi
from AddShow import AddShow

class MovieItem(QtWidgets.QWidget):
    sig = QtCore.pyqtSignal(object)

    def __init__(self, show = ["","","","","",""], parent = None): 
        super(MovieItem,self).__init__()
        loadUi("item.ui", self)
        self.parent = parent

        self.id = show[5]
        self.title.setText(show[0])
        self.cinema.setText(show[4])
        self.date.setText(QtCore.QDate.fromString(show[2], 'yyyy-MM-dd').toString('MMMM d, yyyy'))
        self.time.setText(QtCore.QTime.fromString(show[3], 'hh:mm:ss').toString('h:mm AP'))

    def mouseReleaseEvent(self, event):
        self.a = AddShow(self, "e", self.id, self.parent)
        self.a.show()
        super(MovieItem,self).mouseReleaseEvent(event)

