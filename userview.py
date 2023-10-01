import sys
import json
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QScrollArea, QMessageBox
from customViews import Clickablewidget,Clickablelabel 
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from product import Products
from functools import partial
from usermanager import UserManager
from PyQt6 import QtCore, QtGui, QtWidgets
import subprocess
import argparse
from welcome import Ui_MainWindow as loginpage
from user import User


class Ui_MainWindow(QMainWindow):
    

    def showscreen(self,app,user):
        
        # Create the app window and display products
        qw=QMainWindow()
        window = Ui_MainWindow(user)
        window.setFixedHeight(600)
        window.setFixedWidth(850)
        window.show()
         
        self.currentwindow=window
        # self.currentwindow.hide()
        
        sys.exit(app.exec())

 
    
    
    def logout(self):
       
       self.currentwindow.hide()
       self.login()
      
         
    def login(self):
        python_file = 'welcome.py'
         
        try:
           subprocess.run(['python', python_file], check=True)
        except subprocess.CalledProcessError as e:
           print(f"Error running {python_file}: {e}")
           

    def __init__(self, user):
        super().__init__()
        self.currentwindow=self.window()
        self.MainWindow=QWidget()
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(783, 553)
        self.MainWindow.setStyleSheet("background-image:url(./images/bg.png.png)")
        self.centralwidget = QWidget(parent=self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
      
        self.widget_3 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(30, 30, 721, 451))
        self.widget_3.setStyleSheet("background:none;\n"
"background-color:rgb(246, 250, 253);\n"
"border-radius:25px;\n"
"border-style:none;")
        self.widget_3.setObjectName("widget_3")
        self.label = QtWidgets.QLabel(parent=self.widget_3)
        self.label.setGeometry(QtCore.QRect(330, 10, 61, 61))
        self.label.setStyleSheet("background:none;\n"
"")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./images/user_icon.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_2.setGeometry(QtCore.QRect(70, 160, 91, 31))
        self.label_2.setStyleSheet("font: 700 12pt \"Times New Roman\";")
        self.label_2.setObjectName("label_2")
        self.firstname = QtWidgets.QLabel(parent=self.widget_3)
        self.firstname.setGeometry(QtCore.QRect(150, 160, 291, 31))
        self.firstname.setStyleSheet("font: 700 9pt \"Times New Roman\";")
        self.firstname.setObjectName("firstname")
        self.label_4 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_4.setGeometry(QtCore.QRect(70, 210, 91, 31))
        self.label_4.setStyleSheet("font: 700 12pt \"Times New Roman\";")
        self.label_4.setObjectName("label_4")
        self.lastname = QtWidgets.QLabel(parent=self.widget_3)
        self.lastname.setGeometry(QtCore.QRect(150, 210, 291, 31))
        self.lastname.setStyleSheet("font: 700 9pt \"Times New Roman\";")
        self.lastname.setObjectName("lastname")
        self.loginbtn = QtWidgets.QWidget(parent=self.widget_3)
        self.loginbtn.setGeometry(QtCore.QRect(290, 300, 131, 31))
        self.loginbtn.setStyleSheet("background:none;\n"
" \n"
"border-style:none;\n"
"border-radius:15px;\n"
"background-color:rgb(72, 72, 72);\n"
"")
        self.loginbtn.setObjectName("loginbtn")
        self.label_6 = Clickablelabel(parent=self.loginbtn)
        self.label_6.clicked.connect(self.logout)
        self.label_6.setGeometry(QtCore.QRect(40, 0, 51, 31))
        self.label_6.setStyleSheet("background:none;\n"
" \n"
"border-style:none;\n"
"border-radius:25px;\n"
"color:#ffffff;\n"
"font-weight:bold;")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_7.setGeometry(QtCore.QRect(450, 160, 91, 31))
        self.label_7.setStyleSheet("font: 700 12pt \"Times New Roman\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_8.setGeometry(QtCore.QRect(500, 160, 201, 31))
        self.label_8.setStyleSheet("font: 700 9pt \"Times New Roman\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_9.setGeometry(QtCore.QRect(450, 210, 91, 31))
        self.label_9.setStyleSheet("font: 700 12pt \"Times New Roman\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_10.setGeometry(QtCore.QRect(520, 210, 181, 31))
        self.label_10.setStyleSheet("font: 700 9pt \"Times New Roman\";")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_11.setGeometry(QtCore.QRect(240, 80, 241, 31))
        self.label_11.setStyleSheet("font: 700 18pt \"Times New Roman\";\n"
"color:rgb(102, 102, 102);")
        self.label_11.setObjectName("label_11")
        self.setCentralWidget(self.centralwidget)

    


        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>First name:</p></body></html>"))
        self.firstname.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">" + str(user.firstname)+" </span></p></body></html>"))
        self.label_4.setText(_translate(" ", "<html><head/><body><p>Last name:</p></body></html>"))
        self.lastname.setText(_translate("MainWindow", "<html><head/><body><p>"+ str(user.last_name)+" </p></body></html>"))
        self.label_6.setText(_translate(" ", "Log out"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p>Email:</p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p>"+ str(user.email)+"</p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p>Password:</p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p>"+ str(user.password)+"</p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">USer Details</p></body></html>"))


if __name__ == "__main__":

 parser = argparse.ArgumentParser()
 parser.add_argument("argument", type=str, help="An argument to pass to the script.")
 args = parser.parse_args()

 print(args.argument)
 appp = QApplication(sys.argv)
 email=str(args.argument)
 UserMgr=UserManager()
 user= UserMgr.get_user_by_email(email)



 print(user.firstname)
 print(user.last_name)


 app=Ui_MainWindow(user)

 app.showscreen(appp,user)

