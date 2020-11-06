import socket
from concurrent.futures.thread import ThreadPoolExecutor

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QTextEdit

from signal import Signal


def infinite_server():
    while True:
        connection, address = sock.accept()

        data = connection.recv(1024).decode("utf-8")

        signal.create(data)
        #text1=lineEdit.text()
        #lineEdit.setText(data + "\n" + text1)
        # data.split()
        # c = data.split(',')
        # x = c[0]
        # y = c[1]
        # button = QPushButton()
        # button.setFixedSize(100, 100)
        # button.move(int(x), int(y))
        # window.layout().addWidget(button)
        print(f"Message'{data}' received from address :{address}" )
        # connection.sendall(b"Hello,Makhrov")
        connection.close()


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("192.168.0.115",2525))
sock.listen()
print("CheNit1")














def signal_function(data):
    data.split()
    c = data.split(',')
    x = c[0]
    y = c[1]
    button = QPushButton()
    button.setFixedSize(100, 100)
    button.move(int(x), int(y))
    window.layout().addWidget(button)

    # button = QPushButton()
    # button.move(0, 0)
    # button.resize(100, 100)
    # window.layout().addWidget(button)


app = QApplication([])

window = QMainWindow()
window.resize(1000, 1000)

button=QPushButton()
button.move(100,0)
button.resize(100,100)
window.layout().addWidget(button)

signal = Signal()
signal.connect(lambda data: signal_function(data))


window.show()

executor = ThreadPoolExecutor(2)
executor.submit(lambda:infinite_server())

app.exec()





