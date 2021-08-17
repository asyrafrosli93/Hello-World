import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi('Main.ui',self)
        self.pushButton_14.clicked.connect(self.Station_1)
        self.pushButton_12.clicked.connect(self.Station_2)
        #self.btnRegisterPage.clicked.connect(self.executeRegisterPage)

    def Station_1(self):
        loadUi('Station_1.ui',self)
        self.pushButton_16.clicked.connect(self.MainPage)
        #self.pushButton_14.clicked.connect(self.executeLoginPage)
        #self.btnRegisterPage.clicked.connect(self.executeRegisterPage)

    def Station_2(self):
        loadUi('Station_2.ui',self)
        #self.pushButton_16.clicked.connect(self.MainPage)

     
def main():
   app = QApplication(sys.argv)
   ex = MainWindow()
   sys.exit(app.exec_())


""""
class LoginPage(QDialog):
    def executeLoginPage(self): 
        login_page = LoginPage()
        login_page.exec_()
        loadUi('Station_1.ui', self)
"""

if __name__=="__main__":    
    app = QApplication(sys.argv)
    home = MainWindow()
    #Station1 = MainWindow.Station_1()
    #Station2 = MainWindow.Station_2()
    MainPage = MainWindow.MainPage()
    widget = QStackedWidget()
    widget.addWidget(home)
    #widget.addWidget(Station1)
    #widget.addWidget(Station2)
    widget.show()
    sys.exit(app.exec_())


