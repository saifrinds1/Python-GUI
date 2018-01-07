import sys

from PyQt5 import QtWidgets, QtGui

def window ():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    l1 = QtWidgets.QLabel(w)
    l1.setText("Hello World")
    l1.move(130,50)
    l2 = QtWidgets.QLabel(w)
    l2.setPixmap(QtGui.QPixmap("pngPicture.png"))
    l2.move(120,90)
    w.setWindowTitle("MyFirstApplication")
    w.setGeometry(100, 100, 500, 600)
    w.show()
    sys.exit(app.exec_())

window()    

