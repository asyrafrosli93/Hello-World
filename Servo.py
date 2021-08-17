import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()

    btn1 = QPushButton("A")
    btn2 = QPushButton("B")
    btn3 = QPushButton("C")

    hbox = QHBoxLayout(w)

    hbox.addWidget(btn1)
    hbox.addWidget(btn2)
    hbox.addWidget(btn3)

    w.resize(500,500)
    w.setWindowTitle("ASYRAF")
    w.show()
    sys.exit(app.exec_())

