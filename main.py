# from PyQt5.QtCore import QTimer
# from random import randint
#
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
# # global timer
# global button
# # def timer_tick(button):
# #
# #     x=button.x()
# #     y=button.y()
# #     button.move(x+5,y+5)
# class ArtemiyLuchshiy(QMainWindow):
#     def keyPressEvent(self, event):
#         global button
#         if event.key() == Qt.Key_Space:
#             button = QPushButton()
#             button.setFixedSize(100,100)
#             window.layout().addWidget(button)
#             button.move(randint(0,1000),randint(0,1000))
#             # self.close()



# def clicked(button):
#     global timer
#     timer=QTimer()
#     timer.setInterval(10)
#     timer.timeout.connect(lambda:timer_tick(button))
#     timer.start()
def fibbonachi(a):
    if a in(1,2):
        return 1
    return(fibbonachi(a-1)+fibbonachi(a-2))

def factorial(a):
    if a==0:
        return 1
    return factorial(a-1) * a


    m,n=input().split()
    m=int(m)
    n=int(n)
    list= input().split()
    sumt=0
    curr=1
    sumt1=0
    for next in list:
        next = int(next)
        if next>curr:
            res=next-curr
            sumt+=res
        elif next ==curr:
            res=0
            sumt+=res
        else:
            res=m-(curr-next)
            sumt += res
        curr=next
    print(sumt)
    # app=QApplication([])
    #
    # window=ArtemiyLuchshiy()
    # window.show()
    # window.setFixedSize(1000,1000)


    # button.setText('Нажми меня')
    # button.clicked.connect(lambda:(button))
    print(fibbonachi(35))
    print(factorial(35))