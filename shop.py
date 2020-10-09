from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget, QLabel

import settings

HORIZONTAL=0
VERTICAL=1

class Ship(QLabel):
    number_of_palubs = None
    orientation = None

    def __init__(self,number_of_palubs,orientation):
        QWidget.__init__(self)
        self.number_of_palubs = number_of_palubs
        self.orientation = orientation
        if orientation == HORIZONTAL:
            self.setFixedSize(number_of_palubs*settings.size + 1,settings.size+1)

        if orientation == VERTICAL:
            self.setFixedSize(settings.size+1,number_of_palubs*settings.size+1)


    def mousePressEvent(self,event):
        self.start_x = event.x()
        self.start_y = event.y()
        print(f"PRESS{event.x()} {event.y()}")

    def mouseMoveEvent(self,event):
        x=self.x()+event.x()-self.start_x
        y=self.y()+event.y()-self.start_y
        self.move(x,y)
        print((f"MOVE{event.x()} {event.y()}"))

    def mouseDoubleClickEvent(self,event):
        if self.orientation==HORIZONTAL:
            self.orientation=VERTICAL
            self.setFixedSize(settings.size+1,self.number_of_palubs*settings.size+1)
        else:
            self.orientation=HORIZONTAL
            self.setFixedSize(self.number_of_palubs * settings.size + 1,settings.size + 1)






    def paintEvent(self,event):
        QWidget.paintEvent(self, event)
        painter=QPainter(self)

        x=0
        y=0

        if self.orientation== HORIZONTAL:
            for i in range(self.number_of_palubs):
                painter.drawRect(x,y,settings.size,settings.size)
                x+=settings.size
        if self.orientation == VERTICAL:
            for i in range(self.number_of_palubs):
                painter.drawRect(x,y,settings.size,settings.size)
                y+=settings.size


