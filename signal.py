from PyQt5 import QtCore
from PyQt5.QtCore import QObject


class Signal(QObject):
    pyqtSignal = QtCore.pyqtSignal(object)

    def create(self,data):
        self.pyqtSignal.emit(data)

    def connect(self,function):
        self.pyqtSignal.connect(function)