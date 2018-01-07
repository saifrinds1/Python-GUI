import sys
from PyQt5 import QtWidgets


def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    b = QtWidgets.QPushButton(w)
    l = QtWidgets.QLabel(w)
    b.setText("Push Me")
    l.setText('Look at Me')
    w.setWindowTitle("Practice1 of Push Buttons")
    b.move(100, 50)
    l.move(210,100)
    w.setGeometry(100, 100, 300, 300)
    w.show()
    sys.exit(app.exec_())

window()    