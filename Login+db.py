import sqlite3
import re
import hashlib
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPalette, QColor, QPixmap, QFont


class MainApp(QMainWindow):
    db = "data.db"

    def __init__(self, parent=None, *args):
        super(MainApp, self).__init__(parent=parent)

        self.setFixedSize(640, 480)
        self.setWindowTitle("Login")
        self.setWindowIcon(QIcon("login.png"))

        # paleta = QPalette()
        # paleta.setColor(QPalette.Background, QColor(10, 133, 80))
        # self.setPalette(paleta)

        self.UI()

    def UI(self):
        paleta2 = QPalette()
        paleta2.setColor(QPalette.Window, QColor(73, 19, 131))

        self.frameTitulo = QFrame()
        self.frameTitulo.setFrameStyle(QFrame.NoFrame)
        self.frameTitulo.setFixedHeight(30)
        self.frameTitulo.setAutoFillBackground(True)
        self.frameTitulo.setPalette(paleta2)

        # Label Icono
        labelIcono = QLabel(self)
        labelIcono.setFixedWidth(120)
        labelIcono.setFixedHeight(120)
        labelIcono.setPixmap(QPixmap("login.png").scaled(100, 100, Qt.KeepAspectRatio,
                                                         Qt.SmoothTransformation))
        labelIcono.move(270, 70)

        self.labelmail = QLabel(self)
        self.labelmail.setGeometry(int(640 / 2 - 70), 5, 200, 40)
        self.labelmail.setText('LOGIN')
        self.labelmail.setFont(QFont('Arial', 40))
        self.labelmail.setStyleSheet("font-weight: bold")
        self.labelmail.setFixedWidth(200)
        self.labelmail.setFixedHeight(100)

        self.central_widget = QWidget()
        self.setCentralWidget(self.centralWidget())

        # Email
        self.email = QLineEdit(self)
        self.email.setPlaceholderText("Email")
        self.email.setClearButtonEnabled(True)
        self.email.setGeometry(int(600 / 2 - 60), 190, 160, 30)

        # Password
        self.password = QLineEdit(self)
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setClearButtonEnabled(True)
        self.password.setGeometry(int(600 / 2 - 60), 230, 160, 30)

        # Botton
        self.login = QPushButton('Register', self)
        self.login.setGeometry(int(650 / 2 - 55), 280, 100, 30)
        self.login.clicked.connect(self.sing_in)
        self.email.returnPressed.connect(self.sing_in)
        self.password.returnPressed.connect(self.sing_in)

    def MBoxi(self):
        mensajei = QMessageBox.information(self, 'Register Correct', 'Registered User')

    def MBoxw(self):
        mensajei = QMessageBox.critical(self, 'Register Incorrect', 'Email or Password Invalid')

    def db_connection(self, query, parameters=()):
        if self.sing_in:
            with sqlite3.connect(self.db) as conn:
                cursor = conn.cursor()
                result = cursor.execute(query, parameters)
                conn.commit()
                return result

    def sing_in(self):
        email = self.email.text()
        passwordi = self.password.text()
        if email != '' and re.match('[^@]+@[^@]+\.[^@]+', email) and passwordi != '':
            encry = hashlib.sha256(passwordi.encode('utf-8')).hexdigest()
            query = '''INSERT INTO Users (Email, Password) VALUES (?, ?)'''
            parameters = (email, encry)
            self.db_connection(query, parameters)
            self.email.clear()
            self.password.clear()
            self.MBoxi()

        else:
            self.MBoxw()



if __name__ == '__main__':
    app = QApplication([])
    window = MainApp()
    window.show()
    app.exec_()
