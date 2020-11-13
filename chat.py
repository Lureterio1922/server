from concurrent.futures.thread import ThreadPoolExecutor
import socket

from PyQt5.QtWidgets import QPushButton, QApplication, QMainWindow, QTextEdit

from signal import Signal

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("192.168.0.115", 6666))
server_socket.listen()


def signal_function(textField,data):
    tExt = textField.toPlainText()
    textField.setText(tExt + '\n' +data)

from concurrent.futures.thread import ThreadPoolExecutor
import socket

from PyQt5.QtWidgets import QPushButton, QApplication, QMainWindow, QTextEdit

from signal import Signal

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("192.168.0.115", 6666))
server_socket.listen()


def signal_function(textField,data):
    tExt = textField.toPlainText()
    textField.setText(tExt + '\n' +data)



def infinite_server():
    while True:
        connection, address = server_socket.accept()
        data = connection.recv(1024).decode("utf-8")
        if address[0] == '192.168.0.153':
            data='Artemy - '+data
        if address[0] == '192.168.0.109':
            data='Vadim - ' +data
        if address[0] == '192.168.0.144':
            data='Hacker - '+data

        signal.create(data)
        connection.close()







def send_to_Artemy(textField2):
    text = textField2.toPlainText()
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(("192.168.0.153", 6666))

        sock.sendall(text.encode("utf-8"))
        sock.close()
    except Exception as e:
        print("Artemy is not available")


def send_to_Artem(textField2):
    text = textField2.toPlainText()
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(("192.168.0.144", 7777))

        sock.sendall(text.encode("utf-8"))
        sock.close()
    except Exception as e:
        print("Artem is not available")


app = QApplication([])

window = QMainWindow()
window.resize(1000, 1000)

textField = QTextEdit()
textField.resize(400,800)
textField.move(0,0)
window.layout().addWidget(textField)


button=QPushButton()
button.move(350,810)
button.resize(100,100)
button.setText("Artemy")
window.layout().addWidget(button)
button.clicked.connect(lambda:send_to_Artemy(textField2))

button=QPushButton()
button.move(250,810)
button.resize(100,100)
button.setText("Artem")
window.layout().addWidget(button)
button.clicked.connect(lambda:send_to_Artem(textField2))

textField2 = QTextEdit()
textField2.resize(250,100)
textField2.move(0,810)
window.layout().addWidget(textField2)

signal = Signal()
signal.connect(lambda data: signal_function(textField,data))


window.show()

executor = ThreadPoolExecutor(2)
executor.submit(lambda:infinite_server())

app.exec()

def infinite_server():
    while True:
        connection, address = server_socket.accept()
        data = connection.recv(1024).decode("utf-8")
        if address[0] == '192.168.0.153':
            data='Artemy - '+data
        if address[0] == '192.168.0.109':
            data='Vadim - ' +data
        if address[0] == '192.168.0.144':
            data='Hacker - '+data

        signal.create(data)
        connection.close()







def send_to_Artemy(textField2):
    text = textField2.toPlainText()
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(("192.168.0.153", 6666))

        sock.sendall(text.encode("utf-8"))
        sock.close()
    except Exception as e:
        print("Artemy is not available")


def send_to_Artem(textField2):
    text = textField2.toPlainText()
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(("192.168.0.144", 7777))

        sock.sendall(text.encode("utf-8"))
        sock.close()
    except Exception as e:
        print("Artem is not available")


app = QApplication([])

window = QMainWindow()
window.resize(1000, 1000)

textField = QTextEdit()
textField.resize(400,800)
textField.move(0,0)
window.layout().addWidget(textField)


button=QPushButton()
button.move(350,810)
button.resize(100,100)
button.setText("Artemy")
window.layout().addWidget(button)
button.clicked.connect(lambda:send_to_Artemy(textField2))

button=QPushButton()
button.move(250,810)
button.resize(100,100)
button.setText("Artem")
window.layout().addWidget(button)
button.clicked.connect(lambda:send_to_Artem(textField2))

textField2 = QTextEdit()
textField2.resize(250,100)
textField2.move(0,810)
window.layout().addWidget(textField2)

signal = Signal()
signal.connect(lambda data: signal_function(textField,data))


window.show()

executor = ThreadPoolExecutor(2)
executor.submit(lambda:infinite_server())

app.exec()