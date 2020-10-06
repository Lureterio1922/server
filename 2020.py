from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class ClickableLabel(QPushButton):
    start_x=None
    start_y=None

    def mousePressEvent(self,event):
        self.start_x = event.x()
        self.start_y = event.y()
        print(f"PRESS{event.x()} {event.y()}")

    def mouseMoveEvent(self,event):
        x=self.x()+event.x()-self.start_x
        y=self.y()+event.y()-self.start_y
        self.move(x,y)
        print((f"MOVE{event.x()} {event.y()}"))




if __name__ == "__main__":
    app = QApplication([])

    window = QMainWindow()
    window.resize(1000, 1000)

    button=ClickableLabel()
    button.resize(50,50)
    button.move(150,150)
    window.layout().addWidget(button)

    window.show()
    app.exec_()