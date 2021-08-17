import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QStackedWidget
#from PyQt5.QtGui import QIcon
from PyQt5 import *
from PyQt5.uic import loadUi
from PyQt5.uic.properties import QtWidgets

class MainWindow(QMainWindow):
    def init (self):
        super (MainWindow,self).__init__()
        loadUi("Main.ui",self)

class Station_1(QMainWindow):
    def __init__(self):
        super(Station_1,self).__init__()
        loadUi("Station_1.ui",self)

# main
app = QApplication(sys.argv)
widget=QStackedWidget() 
mainWindow=MainWindow()
Station1=Station_1()
widget.addWidget(mainWindow)
widget.addWidget(Station1) 
widget.setFixedHeight(595)
widget.setFixedWidth(1350)
widget.addWidget(mainWindow)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")
    

