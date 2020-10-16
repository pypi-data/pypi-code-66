import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QWidget


class UsernameWindow(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self)
        self.setWindowTitle("Client Window")
        self.resize(350, 100)

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Enter your name:')
        self.line = QLineEdit(self)

        self.line.move(130, 20)
        self.line.resize(200, 32)
        self.nameLabel.move(20, 20)

        self.submit_btn = QPushButton('OK', self)
        self.submit_btn.move(20, 60)
        self.submit_btn.resize(310, 32)
        self.submit_btn.clicked.connect(self.passUsername)

    def passUsername(self):

        subprocess.Popen(
            f'python client_main.py -name {self.line.text()}',
            creationflags=subprocess.CREATE_NEW_CONSOLE)

        self.close()


app = QApplication(sys.argv)
window = UsernameWindow()
window.show()
app.exec_()
