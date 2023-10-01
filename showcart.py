import sys
import json
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QScrollArea, QMessageBox
from customViews import Clickablewidget,Clickablelabel 
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from usermanager import UserManager
from cartitem import cartitem
from functools import partial
from PyQt6 import QtCore, QtGui, QtWidgets


All_products=[]

cart_items=[]


 
class cartpage(QMainWindow):

    
    
         

    def __init__(self, cartitems):
        super().__init__()
        self.products=cartitems
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)
        scroll_area = QScrollArea()

        # Create the content for the scroll area
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)

        for prod in cartitems:
            item_widget = QWidget()
            item_layout = QHBoxLayout(item_widget)
            item_widget.setGeometry(0, 0, 641, 201)
            textswidget=QWidget()
            text_stack=QVBoxLayout(textswidget)

            row_widget=QWidget()
            row_layout=QHBoxLayout(row_widget)
            
            background_widget=Clickablewidget()
            background_layout=QVBoxLayout(background_widget)
            background_widget.setStyleSheet("background:none;\n"
                                          "background-color:#f6fafd;\n"
                                          "border-style:none;\n"
                                          "border-top-right-radius: 50px;\n"
                                          "border-bottom-right-radius: 50px;")
            background_widget.clicked.connect(partial(self.label_clicked, prod[0]))

            self.widget = QtWidgets.QWidget()
            self.widget.setGeometry(0, 0, 641, 201)
             
            self.widget.setObjectName("widget")
            self.label = QLabel()
            self.label.setGeometry(20, 20, 181, 161)
            self.label.setText("")
            image_size = int(self.width() * 0.3)
            self.label.setFixedWidth(image_size)
            self.label.setFixedHeight(image_size)
 
            self.label.setPixmap(QtGui.QPixmap("./images/carticon.png"))
            self.label.setScaledContents(True)
            self.label.setObjectName("label")
            self.label_2 = QtWidgets.QLabel(parent=self.widget)
            self.label_2.setGeometry(220, 30, 391, 41)
            self.label_2.setStyleSheet("background:none;\n"
                                           "font:  11pt \"Lucida Fax\";\n"
                                           "color:rgba(0, 0, 0,.6)")
            self.label_2.setObjectName("label_2")

            self.label_3 = QtWidgets.QLabel(parent=self.widget)
            self.label_3.setGeometry(220, 80, 401, 51)
            self.label_3.setStyleSheet("background:none;\n"
                                           "font:  11pt \"Lucida Fax\";\n"
                                           "color:rgba(0, 0, 0,.6)")
            self.label_3.setObjectName("label_3")

            self.label_4 = QtWidgets.QLabel(parent=self.widget)
            self.label_4.setGeometry(490, 150, 81, 31)
            

            self.label_4.setStyleSheet("background:none;\n"
                                           "font:  15pt \"Lucida Fax\";\n"
                                           "color:rgb(255, 85, 0)")
            self.label_4.setObjectName("label_4")
            _translate = QtCore.QCoreApplication.translate
            self.label_2.setText(_translate("widget", "<h2><p>"+prod[1]+"</p></h2>"))
            self.label_3.setText(_translate("widget", ""))
            self.label_4.setText(_translate("widget", "<p><span style=\" font-weight:700;\">"+prod[2]+"</span></p>"))
           
            item_layout.addWidget(self.label)
            text_stack.addWidget(self.label_2)
            text_stack.addWidget(self.label_3)
            text_stack.addWidget(self.label_4)

            
            row_layout.addWidget(item_widget)
            row_layout.addWidget(textswidget)
            background_layout.addWidget(row_widget)
            
            scroll_layout.addWidget(background_widget)
            


        scroll_area.setWidget(scroll_content)
        layout.addWidget(scroll_area)

    def label_clicked(self, id):
         print (len(self.products))
     
         for pdt in self.products:
          if pdt[0]==id:
           
            popup = QMessageBox()
            
            popup.setStyleSheet("background-color:#f6fafd; color:#174FC9; font-weight:bold;")
            popup.setWindowTitle("Remove from cart")
            popup.setText("Do you want to remove this from your cart?")
            icon= QPixmap("./images/carticon.png")
         
            popup.setIconPixmap(icon.scaled(50, 50, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio))

            popup.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
            popup.accepted.connect(partial(self.removefromcart, pdt[0]))
            popup.exec()
            
            
            
    def showscreen(self,app,cartitems):
        
        # Create the app window and display products
        qw=QMainWindow()
        window = cartpage(cartitems)
        window.setFixedHeight(600)
        window.setFixedWidth(850)
        window.show()
        currentwindow=window
        
        sys.exit(app.exec())
        return currentwindow


    def removefromcart(self,id):
     print(id)
     

     usmg=UserManager()
     usmg.deletecartitem(id)


    # new_cart_=cartitem(product.title,product.price)
    # usmg=UserManager()
    # usmg.add_tocart(new_cart_)
    # usmg.getcartitems()
          

if __name__ == "__main__":
 app = QApplication(sys.argv)
 UserMgr=UserManager()
 usercartdata= UserMgr.getcartitems()
 window = cartpage(usercartdata)
 window.setFixedHeight(600)
 window.setFixedWidth(850)
 window.show()
 currentwindow=window
 sys.exit(app.exec())
