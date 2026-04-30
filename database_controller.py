import sys
from PyQt6 import QtWidgets, uic

class MainController(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("DataBase_Main.ui", self)

        self.btn_Insert.clicked.connect(self.add_user)

    def add_user(self):
        name = self.txt_Name.text()
        last_name = self.txt_Last_Name.text()
        email = self.txt_Email.text()
        password = self.txt_Password.text()
        confirm_password = self.txt_Confirm_Password.text()

        if name.strip() == "" or last_name.strip() == "" or email.strip() == "" or password.strip() == "" or confirm_password.strip() == "":
            QtWidgets.QMessageBox.warning(self, "Fill out the blanks, would ya?")
        elif password.strip() != confirm_password.strip():
            QtWidgets.QMessageBox.warning(self, "Hey, the passwords are not the same my dude")
        else:
            #Blah Blah Blah