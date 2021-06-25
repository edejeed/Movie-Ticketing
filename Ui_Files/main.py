import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow
from PyQt5.uic import loadUi
import sqlite3


class WelcomeScreen(QMainWindow):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("choose-role.ui", self)
        self.admin.clicked.connect(self.gotoadmin)
        self.crew.clicked.connect(self.gotocrew)

    @staticmethod
    def gotoadmin():
        admin = AdminScreen()
        widget.addWidget(admin)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    @staticmethod
    def gotocrew():
        crew = CrewScreen()
        widget.addWidget(crew)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class CrewScreen(QMainWindow):
    def __init__(self):
        super(CrewScreen, self).__init__()
        loadUi("crew_main.ui", self)
        self.crewlog.clicked.connect(self.login)
        self.crewsign.clicked.connect(self.signup)

    @staticmethod
    def login():
        login = CrewLogin()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    @staticmethod
    def signup():
        signup = CrewSignup()
        widget.addWidget(signup)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class CrewLogin(QMainWindow):
    def __init__(self):
        super(CrewLogin, self).__init__()
        loadUi("crew_login.ui", self)
        self.crew_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.enter.clicked.connect(self.loginfunction)

    def loginfunction(self):
        user = self.crew_user.text()
        password = self.crew_pass.text()

        try:
            if len(user) == 0 or len(password) == 0:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Please Input Informations!")
                x = msg.exec_()
            else:
                conn = sqlite3.connect("crew_data.db")
                cur = conn.cursor()
                cur.execute("SELECT * FROM crew_data WHERE username=?", (user,))
                rows = cur.fetchall()
                for row in rows:
                    if user == row[0] and password == row[1]:
                        moviescreen = MovieScreen()
                        widget.addWidget(moviescreen)
                        widget.setCurrentIndex(widget.currentIndex() + 1)
                    else:
                        msg = QMessageBox()
                        msg.setWindowTitle("Error")
                        msg.setText("The password you’ve entered is incorrect!")
                        x = msg.exec_()
        except:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("The username you entered isn’t connected to an account!")
            x = msg.exec_()


class CrewSignup(QMainWindow):
    def __init__(self):
        super(CrewSignup, self).__init__()
        loadUi("crew_signup.ui", self)
        self.crew_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.crew_pass1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.enter.clicked.connect(self.signupfunction)

    def signupfunction(self):
        user = self.crew_user.text()
        password = self.crew_pass.text()
        confirmpassword = self.crew_pass1.text()

        if len(user) == 0 or len(password) == 0 or len(confirmpassword) == 0:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Please Input Informations!")
            x = msg.exec_()

        elif password != confirmpassword:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Passwords do not match!")
            x = msg.exec_()

        else:
            conn = sqlite3.connect("crew_data.db")
            cur = conn.cursor()

            user_info = [user, password]
            cur.execute('INSERT INTO crew_data (username, password) VALUES (?,?)', user_info)

            conn.commit()
            conn.close()

            msg = QMessageBox()
            msg.setWindowTitle("Success")
            msg.setText("Account Created!")
            x = msg.exec_()

            moviescreen = MovieScreen()
            widget.addWidget(moviescreen)
            widget.setCurrentIndex(widget.currentIndex() + 1)


class AdminScreen(QMainWindow):
    def __init__(self):
        super(AdminScreen, self).__init__()
        loadUi("admin_main.ui", self)
        self.adminlog.clicked.connect(self.login)
        self.adminsign.clicked.connect(self.signup)

    @staticmethod
    def login():
        login = AdminLogin()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    @staticmethod
    def signup():
        signup = AdminSignup()
        widget.addWidget(signup)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class AdminLogin(QMainWindow):
    def __init__(self):
        super(AdminLogin, self).__init__()
        loadUi("admin_login.ui", self)
        self.admin_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.enter.clicked.connect(self.loginfunction)

    def loginfunction(self):
        user = self.admin_user.text()
        password = self.admin_pass.text()

        try:
            if len(user) == 0 or len(password) == 0:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Please Input Informations!")
                x = msg.exec_()
            else:
                conn = sqlite3.connect("admin_data.db")
                cur = conn.cursor()
                cur.execute("SELECT * FROM admin_data WHERE username=?", (user,))
                rows = cur.fetchall()
                for row in rows:
                    if user == row[0] and password == row[1]:
                        moviescreen = MovieScreen()
                        widget.addWidget(moviescreen)
                        widget.setCurrentIndex(widget.currentIndex() + 1)
                    else:
                        msg = QMessageBox()
                        msg.setWindowTitle("Error")
                        msg.setText("The password you’ve entered is incorrect!")
                        x = msg.exec_()
        except:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("The username you entered isn’t connected to an account!")
            x = msg.exec_()


class AdminSignup(QMainWindow):
    def __init__(self):
        super(AdminSignup, self).__init__()
        loadUi("admin_signup.ui", self)
        self.admin_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.admin_pass1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.enter.clicked.connect(self.signupfunction)

    def signupfunction(self):
        user = self.admin_user.text()
        password = self.admin_pass.text()
        confirmpassword = self.admin_pass1.text()

        if len(user) == 0 or len(password) == 0 or len(confirmpassword) == 0:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Please Input Informations!")
            x = msg.exec_()

        elif password != confirmpassword:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Passwords do not match!")
            x = msg.exec_()

        else:
            conn = sqlite3.connect("admin_data.db")
            cur = conn.cursor()

            user_info = [user, password]
            cur.execute('INSERT INTO admin_data (username, password) VALUES (?,?)', user_info)

            conn.commit()
            conn.close()

            msg = QMessageBox()
            msg.setWindowTitle("Success")
            msg.setText("Account Created!")
            x = msg.exec_()

            moviescreen = MovieScreen()
            widget.addWidget(moviescreen)
            widget.setCurrentIndex(widget.currentIndex() + 1)


class MovieScreen(QMainWindow):
    def __init__(self):
        super(MovieScreen, self).__init__()
        loadUi("movies.ui", self)


# main
app = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(600)
widget.setFixedWidth(800)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
