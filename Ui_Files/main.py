import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow
from PyQt5.uic import loadUi
from movie import MovieScreen
from MessageBox import MessageBox
from db import *

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
        self.signUpButton.clicked.connect(self.signUpFunction)

    def loginfunction(self):
        user = self.crew_user.text()
        password = self.crew_pass.text()

        msg = QMessageBox()
        msg.setWindowTitle("Error")

        if len(user) == 0 or len(password) == 0:
            msg.setText("Please Input Informations!")
            x = msg.exec_()
        else:
            res = Authenticate(user, password)

            if res:
                moviescreen = MovieScreen()
                widget.addWidget(moviescreen)
                widget.setCurrentIndex(widget.currentIndex() + 1)
            else:
                msg.setText("Incorrect username or password")
                x = msg.exec_()

    @staticmethod
    def signUpFunction():
        CrewScreen().signup()


class CrewSignup(QMainWindow):
    def __init__(self):
        super(CrewSignup, self).__init__()
        loadUi("crew_signup.ui", self)
        self.crew_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.crew_pass1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.enter.clicked.connect(self.signupfunction)
        self.loginButton.clicked.connect(self.loginFunction)

    def signupfunction(self):
        user = self.crew_user.text()
        password = self.crew_pass.text()
        confirmpassword = self.crew_pass1.text()

        if len(user) == 0 or len(password) == 0 or len(confirmpassword) == 0:
            MessageBox.showErrorMessage("Please accomplish all fields.", "Error")

        elif password != confirmpassword:
            MessageBox.showErrorMessage("Passwords do not match!","Error")

        else:
            AddUser(user, password)

            MessageBox.showInformationMessage("Account Created.", "Success")

            widget.removeWidget(self)

    @staticmethod
    def loginFunction(self):
        CrewScreen().login()


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
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.loginButton.clicked.connect(self.loginfunction)
        self.signUpButton.clicked.connect(self.signUpfunction)

    def loginfunction(self):
        user = self.username.text()
        password = self.password.text()

        msg = QMessageBox()
        msg.setWindowTitle("Error")

        
        if len(user) == 0 or len(password) == 0:
            msg.setText("Please Input Information!")
            x = msg.exec_()
        else:
            res = Authenticate(user, password, 1)

            if res:
                moviescreen = MovieScreen(widget)
                widget.addWidget(moviescreen)
                widget.setCurrentIndex(widget.currentIndex() + 1)
            else: 
                msg.setText("Incorrect username or password.")
                x = msg.exec_()

    def signUpfunction(self):
        AdminScreen().signup()


class AdminSignup(QMainWindow):
    def __init__(self):
        super(AdminSignup, self).__init__()
        loadUi("admin_signup.ui", self)
        self.admin_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.admin_pass1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.enter.clicked.connect(self.signupfunction)
        self.signUpButton.clicked.connect(self.loginfunction)

    def signupfunction(self):
        user = self.user.text()
        password = self.admin_pass.text()
        confirmpassword = self.admin_pass1.text()

        if len(user) == 0 or len(password) == 0 or len(confirmpassword) == 0:
            MessageBox.showErrorMessage("Please accomplish all fields.", "Error")

        elif password != confirmpassword:
            MessageBox.showErrorMessage("Passwords do not match!", "Error")

        else:
            AddUser(user, password, 1)

            MessageBox.showInformationMessage("Account Created.", "Success")

            widget.removeWidget(self)

    def loginfunction(self):
        AdminScreen().login()


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
