from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow,QWidget,QLabel,QMessageBox
from PyQt6.QtGui import QPixmap
from customViews import Clickablelabel,Clickablewidget
import sys
from app import Ui_MainWindow as appwindow
from user import User
from usermanager import UserManager
import subprocess
 
 
class Ui_MainWindow(QMainWindow):
    

    def login(self,user):
        python_file = 'app.py'
         
        try:
           subprocess.run(['python', python_file, user], check=True)
        except subprocess.CalledProcessError as e:
           print(f"Error running {python_file}: {e}")
           
              


    def get_signups(self):
        first_name =self.firstname.text()
        last_name=self.lastname.text()
        email=self.signemail.text()
        password=self.signpassword.text()
        password_repeat=self.signpasswordrepeat.text()

        if first_name=="" or last_name=="" or email =="" or password=="" or password_repeat=="":
             
         self.show_errmessage("Can't process one or more empty fields")
        
        
        else: 
         if self.usermanager.user_exists(email):
            self.show_errmessage("User already exists")

         else:
              if password.strip()==password_repeat.strip():
                 
                 user =User(first_name, last_name,email,password)
                 self.usermanager.add_user(user)
              else:
                 self.show_errmessage("Passwords don't match")

            
                     

    def show_errmessage(self,msg):
            popup = QMessageBox()
            
            popup.setStyleSheet("background-color:#f6fafd; color:#174FC9; font-weight:bold;")
            popup.setWindowTitle("Error")
            popup.setText(msg)
         
            popup.setIcon(QMessageBox.Icon.Information)

            
            popup.exec()



    def get_logins(self):
        password=self.loginpassword.text()
        email=self.loginemail.text()


        if self.usermanager.user_exists(email):
         user=self.usermanager.get_user_by_email(email)
         if user.get_password().strip() == password.strip():
                    print("login succes")
                    print(user.firstname+": "+ user.last_name)
                    self.login(user.email)
                
         else:
                    self.show_errmessage("Incorrect password")


        else:
             self.show_errmessage("Account does not exists create an account if you dont have any yet")
             
         
 



    def __init__(self):
        super().__init__()
        self.usermanager=UserManager()
        self.MainWindow=QWidget()
        self.MainWindow.resize(783, 553)
        self.MainWindow.setStyleSheet("background-image:url(./images/bg.png.png)")
        self.centralwidget = QWidget(parent=self.MainWindow)
         
        self.widget_3 = QtWidgets.QWidget(parent=self.centralwidget)
        self.setCentralWidget(self.MainWindow)
        self.widget_3.setGeometry(QtCore.QRect(30, 30, 721, 451))
        self.widget_3.setStyleSheet("background:none;\n"
"background-color:rgb(246, 250, 253);\n"
"border-radius:25px;\n"
"border-style:none;")
        self.widget_3.setObjectName("widget_3")
        self.label_2 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_2.setGeometry(QtCore.QRect(120, 120, 91, 61))
        self.label_2.setStyleSheet("background:none;\n"
"font: 18pt \"Mongolian Baiti\";\n"
"color:rgb(58, 58, 58);\n"
"font-weight:bold;")
        self.label_2.setObjectName("label_2")
        self.widget_4 = QtWidgets.QWidget(parent=self.widget_3)
        self.widget_4.setGeometry(QtCore.QRect(60, 190, 191, 31))
        self.widget_4.setStyleSheet("background:none;\n"
"background-color:#9BBAFF;\n"
"border-style:none;\n"
"border-radius:15px;\n"
"")
        self.widget_4.setObjectName("widget_4")
        self.loginemail = QtWidgets.QLineEdit(parent=self.widget_4)
        self.loginemail.setGeometry(QtCore.QRect(20, 0, 141, 31))
        self.loginemail.setStyleSheet("color:#ffffff;")
        self.loginemail.setClearButtonEnabled(True)
        self.loginemail.setObjectName("loginemail")
        self.widget_5 = QtWidgets.QWidget(parent=self.widget_3)
        self.widget_5.setGeometry(QtCore.QRect(60, 230, 191, 31))
        self.widget_5.setStyleSheet("background:none;\n"
"background-color:#9BBAFF;\n"
"border-style:none;\n"
"border-radius:15px;\n"
"")   
        self.widget_5.setObjectName("widget_5")
        self.loginpassword = QtWidgets.QLineEdit(parent=self.widget_5)
        self.loginpassword.setGeometry(QtCore.QRect(20, 0, 141, 31))
        self.loginpassword.setStyleSheet("color:#ffffff;")
        self.loginpassword.setClearButtonEnabled(True)
        self.loginpassword.setObjectName("loginpassword")
        self.widget_6 = QtWidgets.QWidget(parent=self.widget_3)
        self.widget_6.setGeometry(QtCore.QRect(450, 140, 191, 31))
        self.widget_6.setStyleSheet("background:none;\n"
"background-color:#9BBAFF;\n"
"border-style:none;\n"
"border-radius:15px;\n"
"")
        self.widget_6.setObjectName("widget_6")
        self.firstname = QtWidgets.QLineEdit(parent=self.widget_6)
        self.firstname.setGeometry(QtCore.QRect(20, 0, 141, 31))
        self.firstname.setStyleSheet("color:#ffffff;")
        self.firstname.setClearButtonEnabled(True)
        self.firstname.setObjectName("firstname")
        self.widget_7 = QtWidgets.QWidget(parent=self.widget_3)
        self.widget_7.setGeometry(QtCore.QRect(450, 190, 191, 31))
        self.widget_7.setStyleSheet("background:none;\n"
"background-color:#9BBAFF;\n"
"border-style:none;\n"
"border-radius:15px;\n"
"")
        self.widget_7.setObjectName("widget_7")
        self.lastname = QtWidgets.QLineEdit(parent=self.widget_7)
        self.lastname.setGeometry(QtCore.QRect(20, 0, 141, 31))
        self.lastname.setStyleSheet("color:#ffffff;")
        self.lastname.setClearButtonEnabled(True)
        self.lastname.setObjectName("lastname")
        self.widget_8 = QtWidgets.QWidget(parent=self.widget_3)
        self.widget_8.setGeometry(QtCore.QRect(450, 240, 191, 31))
        self.widget_8.setStyleSheet("background:none;\n"
"background-color:#9BBAFF;\n"
"border-style:none;\n"
"border-radius:15px;\n"
"")
        self.widget_8.setObjectName("widget_8")
        self.signpassword = QtWidgets.QLineEdit(parent=self.widget_8)
        self.signpassword.setGeometry(QtCore.QRect(20, 0, 141, 31))
        self.signpassword.setStyleSheet("color:#ffffff;")
        self.signpassword.setClearButtonEnabled(True)
        self.signpassword.setObjectName("signpassword")
        self.widget_9 = QtWidgets.QWidget(parent=self.widget_3)
        self.widget_9.setGeometry(QtCore.QRect(450, 290, 191, 31))
        self.widget_9.setStyleSheet("background:none;\n"
"background-color:#9BBAFF;\n"
"border-style:none;\n"
"border-radius:15px;\n"
"")
        self.widget_9.setObjectName("widget_9")
        self.signpasswordrepeat = QtWidgets.QLineEdit(parent=self.widget_9)
        self.signpasswordrepeat.setGeometry(QtCore.QRect(20, 0, 141, 31))
        self.signpasswordrepeat.setStyleSheet("color:#ffffff;")
        self.signpasswordrepeat.setClearButtonEnabled(True)
        self.signpasswordrepeat.setObjectName("signpasswordrepeat")
        self.widget_10 = QtWidgets.QWidget(parent=self.widget_3)
        self.widget_10.setGeometry(QtCore.QRect(450, 340, 191, 31))
        self.widget_10.setStyleSheet("background:none;\n"
"background-color:#9BBAFF;\n"
"border-style:none;\n"
"border-radius:15px;\n"
"")
        self.widget_10.setObjectName("widget_10")
        self.signemail = QtWidgets.QLineEdit(parent=self.widget_10)
        self.signemail.setGeometry(QtCore.QRect(20, 0, 141, 31))
        self.signemail.setStyleSheet("color:#ffffff;")
        self.signemail.setClearButtonEnabled(True)
        self.signemail.setObjectName("signemail")
        self.label_3 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_3.setGeometry(QtCore.QRect(450, 70, 211, 61))
        self.label_3.setStyleSheet("background:none;\n"
"font: 18pt \"Mongolian Baiti\";\n"
"color:rgb(58, 58, 58);\n"
"font-weight:bold;")
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(parent=self.widget_3)
        
        self.label.setGeometry(QtCore.QRect(320, 10, 81, 71))
        self.label.setStyleSheet("background:none;\n"
"")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./images/logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.loginbtn = QtWidgets.QWidget(parent=self.widget_3)
        
        self.loginbtn.setGeometry(QtCore.QRect(90, 290, 131, 31))
        self.loginbtn.setStyleSheet("background:none;\n"
" \n"
"border-style:none;\n"
"border-radius:15px;\n"
"background-color:rgb(72, 72, 72);\n"
"")
        self.loginbtn.setObjectName("loginbtn")
        #self.label_4 = QLabel(self.loginbtn)
        self.label_4=Clickablelabel(self.loginbtn)
        self.label_4.setGeometry(QtCore.QRect(40, 0, 51, 31))
        self.label_4.setStyleSheet("background:none;\n"
" \n"
"border-style:none;\n"
"border-radius:25px;\n"
"color:#ffffff;\n"
"font-weight:bold;")
        self.label_4.setObjectName("label_4")
        self.signupbtn = QtWidgets.QLabel(self.widget_3)
        self.signupbtn.setGeometry(QtCore.QRect(480, 390, 131, 31))
        self.signupbtn.setStyleSheet("background:none;\n"
" \n"
"border-style:none;\n"
"border-radius:15px;\n"
"background-color:rgb(72, 72, 72);\n"
"")
        self.label_4.clicked.connect(self.get_logins)

        self.signupbtn.setObjectName("signupbtn")
        self.label_5 = Clickablelabel(parent=self.signupbtn)
        self.label_5.setGeometry(QtCore.QRect(40, 0, 51, 31))
        self.label_5.setStyleSheet("background:none;\n"
" \n"
"border-style:none;\n"
"border-radius:25px;\n"
"color:#ffffff;\n"
"font-weight:bold;")
        self.label_5.setObjectName("label_5")
        self.label_5.clicked.connect(self.get_signups)

          
 
        _translate = QtCore.QCoreApplication.translate
       
        self.label_2.setText(_translate("MainWindow", "Login "))
     
        self.loginemail.setPlaceholderText(_translate("MainWindow", "Email..."))
        self.loginemail.text
        self.loginpassword.setPlaceholderText(_translate("MainWindow", "Password..."))
     
        self.firstname.setPlaceholderText(_translate("MainWindow", "First name..."))
       
        self.lastname.setPlaceholderText(_translate("MainWindow", "Last nmae..."))
      
        self.signpassword.setPlaceholderText(_translate("MainWindow", "Password..."))
   
        self.signpasswordrepeat.setPlaceholderText(_translate("MainWindow", "Password - repeat..."))
    
        self.signemail.setPlaceholderText(_translate("MainWindow", "Email..."))
        self.label_3.setText(_translate("MainWindow", "Create an account"))
        self.label_4.setText(_translate(" ", "Sign in"))
        self.label_5.setText(_translate(" ", "Sign up"))



if __name__=="__main__":
        app = QApplication(sys.argv)
        # Create the app window and display products
        qw=QMainWindow()
        print ("ramsmsmsms")

        window = Ui_MainWindow()
        window.setFixedHeight(600)
        window.setFixedWidth(850)
        window.show()
        currentwindow=window
        sys.exit(app.exec())
