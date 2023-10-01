from PyQt6.QtWidgets import QLabel, QWidget,QDialog,QPushButton,QVBoxLayout
from PyQt6 import QtCore, QtGui, QtWidgets



class Clickablewidget(QWidget):
    clicked = QtCore.pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()
    def enterEvent(self, event):
        # This will be triggered when the mouse enters the widget's area
        print("Mouse entered")
        self.setStyleSheet("background:none;\n"
                                          "background-color:#9BBAFF;\n"
                                          "border-style:none;\n"
                                          "border-radius: 50px;")

    def leaveEvent(self, event):
        # This will be triggered when the mouse leaves the widget's area
        print("Mouse left")
        self.setStyleSheet("background:none;\n"
                                          "background-color:#f6fafd;\n"
                                          "border-style:none;\n"
                                          "border-radius: 50px;")


class Clickablelabel(QLabel):
    def __init__(self,parent):
        self.parent=parent
        super().__init__(parent=self.parent)
        
       

        
    clicked = QtCore.pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()

 

  