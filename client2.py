
import socket
from random import randint

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

#sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock.connect(("192.168.0.115", 2525))

#sock.sendall("Prosto kak bolt polojit".encode('utf-8'))


#sock.close()



def buttonClickedConnect():
    x=randint(0,800)
    y=randint(0,800)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("192.168.0.115", 2525))
    x1=str(x)
    y1=str(y)
    c=x1+','+y1
    sock.sendall(c.encode('utf-8'))

    sock.close()



app= QApplication([])

window = QMainWindow()
window.resize(1000, 1000)


button = QPushButton()
button.setFixedSize(100,100)
button.move(100,100)
window.layout().addWidget(button)
button.clicked.connect(lambda: buttonClickedConnect())
#
window.show()
#
#
#
#
#
app.exec()