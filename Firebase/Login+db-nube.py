import sqlite3
import re
import hashlib
import pyrebase
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainApp(QMainWindow):
    db = "data.db"

    def __init__(self, parent=None, *args):
        super(MainApp, self).__init__(parent=parent)

        self.setFixedSize(640, 480)
        self.setWindowTitle("APP")

        self.config = {
            "apiKey": "AIzaSyByk3pQ8hnicP5giFYHvhSbfvge20EmX2s",
            "authDomain": "login-30737.firebaseapp.com",
            "databaseURL": "https://databaseName.firebaseio.com",
            "storageBucket": "login-30737.appspot.com"
        }

        self.firebase = pyrebase.initialize_app(self.config)
        self.auth = self.firebase.auth()


        self.labelmail = QLabel(self)
        self.labelmail.setGeometry(int(640 / 2 - 90), 190, 200, 20)
        self.labelpass = QLabel(self)
        self.labelpass.setGeometry(int(640 / 2 - 60), 180, 100, 30)

        self.central_widget = QWidget()
        self.setCentralWidget(self.centralWidget())

        # Email
        self.email = QLineEdit(self)
        self.email.setPlaceholderText("Email")
        self.email.setClearButtonEnabled(True)
        self.email.setGeometry(int(640 / 2 - 60), 50, 100, 30)

        # Password
        self.password = QLineEdit(self)
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setClearButtonEnabled(True)
        self.password.setGeometry(int(640 / 2 - 60), 100, 100, 30)
        # Botton
        self.login = QPushButton('Login', self)
        self.login.setGeometry(int(640 / 2 - 60), 150, 100, 30)
        self.login.clicked.connect(self.sing_in)
        self.email.returnPressed.connect(self.sing_in)
        self.password.returnPressed.connect(self.sing_in)

    def sing_in(self):
        email = self.email.text()
        passwordi = self.password.text()
        if email != '' and re.match('[^@]+@[^@]+\.[^@]+', email) and passwordi != '':
            self.labelmail.setText('Email Valid')
            encry = hashlib.sha256(passwordi.encode('utf-8')).hexdigest()
            user = self.auth.create_user_with_email_and_password(email, encry)
            print(user)
            self.email.clear()
            self.password.clear()
            self.labelmail.setText('Register Okay')
            self.labelmail.setStyleSheet('background:green; color:black')
        else:
            self.labelmail.setText('Email not valid or Password invalid')
            self.labelmail.setStyleSheet('background: red; color:black')

            return False
        return True


if __name__ == '__main__':
    app = QApplication([])
    window = MainApp()
    window.show()
    app.exec_()
