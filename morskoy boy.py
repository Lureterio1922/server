from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
import settings
from shop import Ship, VERTICAL, HORIZONTAL


class Pole(QWidget):
    def paintEvent(self, event):
        painter = QPainter(self)
        x=10
        y=10

        font=painter.font()
        font.setPixelSize(13)
        painter.setFont(font)

        for i in range(settings.w+1):
            painter.drawLine(x, 10, x, settings.h*settings.size+10)
            x+=settings.size
        for i in range(settings.h+1):
            painter.drawLine(10, y, settings.w*settings.size+10, y)
            y+=settings.size
        s=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
        x=settings.size/2+5
        for symbol in s:
            painter.drawText(x,10,symbol)
            x+=settings.size
        d=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T']
        y=settings.size/2+12
        for symbol in d:
            painter.drawText(0,y,symbol)
            y+=settings.size

if __name__ == "__main__":
    app = QApplication([])

    window = QMainWindow()
    window.resize(1000, 1000)

    pole = Pole()
    pole.setFixedSize(settings.w*settings.size+11, settings.h*settings.size+11)
    pole.move(settings.a, settings.b)
    window.layout().addWidget(pole)

    pole2 = Pole()
    pole2.setFixedSize(settings.w*settings.size+11, settings.h*settings.size+11)
    pole2.move(settings.a+settings.w*settings.size+4*settings.size, settings.b)
    window.layout().addWidget(pole2)

    for i in range(settings.ship_1):
        ship= Ship(1,VERTICAL)
        ship.move(settings.x1,settings.y1)
        settings.x1+=settings.size+10
        window.layout().addWidget(ship)

    for i in range(settings.ship_2):
        ship = Ship(2, VERTICAL)
        ship.move(settings.x1, settings.y2)
        settings.x1 += settings.size + 50
        window.layout().addWidget(ship)

    for i in range(settings.ship_3):
        ship = Ship(3, VERTICAL)
        ship.move(settings.x1, settings.y3)
        settings.x1 += settings.size + 70
        window.layout().addWidget(ship)

    for i in range(settings.ship_4):
        ship = Ship(4, VERTICAL)
        ship.move(settings.x1, settings.y4)
        settings.x1 += settings.size + 10
        window.layout().addWidget(ship)



    window.show()
    app.exec()