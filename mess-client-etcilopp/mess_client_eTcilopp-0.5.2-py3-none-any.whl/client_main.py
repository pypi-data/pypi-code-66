import sys
from PyQt5.QtCore import *

from PyQt5 import QtCore
from PyQt5.QtWidgets import *

import client_c




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

        self.statusBar().showMessage(f'You are connected as {sys.argv[2]}')

        label1 = QLabel("Chat Window:", self)
        label1.setGeometry(QtCore.QRect(label1.x(), label1.y(), label1.width() + 150, label1.height()))
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
        button_search.resize(60, 30)
        button_search.move(530, 400)

    @pyqtSlot()
    def SendFunction(self):
        self.recipient = self.recipientLine.text()
        self.message = self.messageLine.text()
        # print([self.recipient, self.message])
        self.messageLine.setText('')
        self.PrintFunction(f'me to {self.recipient}: {self.message} ')
        gui.sendOut(self.recipient, self.message)

    @pyqtSlot()
    def PrintFunction(self, message):
        if message:
            self.messageHistory.append(message)
            x = "\n".join(self.messageHistory)
            self.textbox.setText(x)


class MySignals(QObject):
    finished = pyqtSignal(str)


class SendOut(QRunnable):
    # sendOutSignal = MySignals()
    def __init__(self, recipient, message):
        super(SendOut, self).__init__()
        self.recipient = recipient
        self.message = message

    @pyqtSlot()
    def run(self):
        client.message_out(client.s, self.recipient, self.message)


class Client(QRunnable):
    messageSignal = MySignals()

    @pyqtSlot()
    def run(self):
        while True:
            a = client.message_from_server(client.s)
            self.messageSignal.finished.emit(a)


class Gui(PrintWindow):
    def __init__(self):
        super().__init__()
        self.threadpool = QThreadPool()
        self.show()
        self.run_client()
        # self.sendOut()

    def run_client(self):
        client = Client()
        self.threadpool.start(client)
        client.messageSignal.finished.connect(self.print_output)

    def sendOut(self, recipient, message):
        sendOut = SendOut(recipient, message)
        self.threadpool.start(sendOut)

    def print_output(self, text):
        self.PrintFunction(text)


if __name__ == '__main__':
    client = client_c.main(sys.argv[2])
    app = QApplication(sys.argv)
    gui = Gui()
    sys.exit(app.exec_())
