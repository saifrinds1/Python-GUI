import sys
from PyQt5 import QtWidgets


class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def btn_click(self):
        print("I am Clicked")
        self.l.setText("Button is clicked")

    def init_ui(self):
        self.b = QtWidgets.QPushButton('Push Me')
        self.l = QtWidgets.QLabel('I have not been clicked yet')

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.l)
        h_box.addStretch()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.b)
        v_box.addLayout(h_box)

        self.setLayout(v_box)
        self.setWindowTitle("Practice3SignalSlot")

        self.b.clicked.connect(self.btn_click)

        self.show()

app = QtWidgets.QApplication(sys.argv)        
a_window = Window()
sys.exit(app.exec_())
