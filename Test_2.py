import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5 import uic

#load both ui file
uifile_1 = 'Main.ui'
form_1, base_1 = uic.loadUiType(uifile_1)

uifile_2 = 'Station_1.ui'
form_2, base_2 = uic.loadUiType(uifile_2)

class Example(base_2, form_2):
    def __init__(self):
        super(base_2,self).__init__()
        self.setupUi(self)
        #self.pushButton14.clicked.connect(self.change)

    def change(self):
        self.main = MainPage()
        self.main.show()
        self.close()

class MainPage(base_1, form_1):
    def __init__(self):
        super(base_1, self).__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())