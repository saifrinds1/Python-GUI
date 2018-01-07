import sys
from PyQt5 import QtWidgets


def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    b = QtWidgets.QPushButton("Push Me")
    l = QtWidgets.QLabel("Look at me")
    w.setWindowTitle("Practice2 of BoxLayout")
    h_box = QtWidgets.QHBoxLayout()
    h_box.addStretch()
    h_box.addWidget(l)
    h_box.addStretch()
    v_box = QtWidgets.QVBoxLayout()
    v_box.addWidget(b)
    v_box.addLayout(h_box)
    w.setLayout(v_box)
    w.setGeometry(100, 100, 300, 300)
    w.show()
    sys.exit(app.exec_())

window()    