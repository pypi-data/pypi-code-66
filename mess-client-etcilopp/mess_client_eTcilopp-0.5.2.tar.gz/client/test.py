import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from form import PrintWindow
import client_c

client = client_c.main()

class MySignals(QObject):
    finished = pyqtSignal(str)

# https://www.learnpyqt.com/courses/concurrent-execution/multithreading-pyqt-applications-qthreadpool/
class SendOut(QRunnable):
    # sendOutSignal = MySignals()
    def __init__(self, recipient, message):
        super(SendOut, self).__init__()
        self.recipient = recipient
        self.message = message

    @pyqtSlot()
    def run(self):
        # client = client_c.main()
        client.message_out(client.s, self.recipient, self.message)
        # while True:
        #     text = input('text?: ')
        #     text += ', бля..'
        #     self.sendOutSignal.finished.emit(text)

class Client(QRunnable):
    messageSignal = MySignals()
    @pyqtSlot()
    def run(self):
        # client = client_c.main()
        while True:
            a = client.message_from_server(client.s)
            self.messageSignal.finished.emit(a)
        # client.run_client()


class Gui(PrintWindow):
    def __init__(self):
        super().__init__()
        self.threadpool = QThreadPool()
        self.show()
        self.run_client()
        # self.sendOut()
       
    def run_client(self):
        client=Client()
        self.threadpool.start(client)
        client.messageSignal.finished.connect(self.print_output)

    def sendOut(self, recipient, message):
        sendOut = SendOut(recipient, message)
        self.threadpool.start(sendOut)
        # sendOut.sendOutSignal.finished.connect(self.get_my_message)

    # def get_my_message(self):
    #     print(self.SendFunction())

    def print_output(self, text):
        self.PrintFunction(text)

app = QApplication(sys.argv)
gui = Gui()
sys.exit(app.exec_())



# class Gui(QRunnable):
#     def __init__(self):
#         self.threadpool = QThreadPool()

#     @pyqtSlot()
#     def run(self):
#         window = PrintWindow()
#         messanger = Message(window)
#         self.threadpool.start(messanger)

#         app = QApplication(sys.argv)
        
#         window.show()
#         sys.exit(app.exec_())

# class Message(QRunnable):
#     def __init__(self, window):
#         self.window = window
#         self.threadpool = QThreadPool()

#     @pyqtSlot()
#     def run(self):
#         while True:
#             message = input('Your message? ')
#             self.window.PrintFunction(message)


#     gui = Gui()
#     gui.run()
#     # self.threadpool.start(gui) 



