import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, QSize, QRect
# from test import gui


class PrintWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Messenger'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
        self.messageHistory = []

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.statusBar().showMessage('In progress')

        label1 = QLabel("Chat Window:", self)
        label1.setGeometry(
            QtCore.QRect(
                label1.x(),
                label1.y(),
                label1.width() + 150,
                label1.height()))
        label1.move(50, 20)

        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        # create textbox
        self.textbox = QTextEdit(self)
        self.textbox.move(50, 50)
        self.textbox.resize(540, 300)
        self.textbox.setReadOnly(True)
        # create textbox done

        # create recipient line
        self.recipientLabel = QLabel(self)
        self.recipientLabel.setText('Recipient:')
        self.recipientLine = QLineEdit(self)

        self.recipientLine.move(70, 400)
        self.recipientLine.resize(150, 30)
        self.recipientLabel.move(71, 370)
        # create recipient line done

        # create input line
        self.messageLabel = QLabel(self)
        self.messageLabel.setText('Message:')
        self.messageLine = QLineEdit(self)

        self.messageLine.move(270, 400)
        self.messageLine.resize(250, 30)
        self.messageLabel.move(271, 370)
        # create input line done

        button_search = QPushButton(' >> SEND ', self)
        button_search.clicked.connect(self.SendFunction)
        button_search.resize(60, 40)
        button_search.move(530, 400)

    @pyqtSlot()
    def SendFunction(self):
        self.recipient = self.recipientLine.text()
        self.message = self.messageLine.text()
        print([self.recipient, self.message])
        self.messageLine.setText('')
        self.PrintFunction(f'me to {self.recipient}: {self.message} ')
        gui.sendOut(self.recipient, self.message)

    @pyqtSlot()
    def PrintFunction(self, message):
        self.messageHistory.append(message)
        x = "\n".join(self.messageHistory)
        self.textbox.setText(x)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = PrintWindow()
    window.show()
    sys.exit(app.exec_())
