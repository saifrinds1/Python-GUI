import sys
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def Up(self, dis):
        print("up {}".format(dis))

    def Down(self, dis):
        print("down {}".format(dis))

    def Right(self, dis):
        print("right {}".format(dis))

    def Left(self, dis):
        print("left {}".format(dis))    

    def init_ui(self):
        self.up = QtWidgets.QPushButton('UP')
        self.up.clicked.connect(self.Up)
        self.down = QtWidgets.QPushButton('DOWN')
        self.down.clicked.connect(self.Down)
        self.right = QtWidgets.QPushButton("RIGHT")
        self.right.clicked.connect(self.Right)
        self.left= QtWidgets.QPushButton('LEFT')
        self.left.clicked.connect(self.Left)

        HBox = QtWidgets.QHBoxLayout()
        HBox.addStretch()
        HBox.addWidget(self.up)
        HBox.addStretch()

        HBox1 = QtWidgets.QHBoxLayout()
        HBox1.addStretch()
        HBox1.addWidget(self.left)
        HBox1.addStretch()
        HBox1.addWidget(self.right)
        HBox1.addStretch()

        HBox2 =QtWidgets.QHBoxLayout()
        HBox2.addStretch()
        HBox2.addWidget(self.down)
        HBox2.addStretch()

        VBox = QtWidgets.QVBoxLayout()
        VBox.addStretch()
        VBox.addLayout(HBox)
        VBox.addStretch()
        VBox.addLayout(HBox1)
        VBox.addStretch()
        VBox.addLayout(HBox2)
        VBox.addStretch()

        self.setLayout(VBox)
        self.show()


MouseControl = QtWidgets.QApplication(sys.argv)
ControlWindow = Window()
sys.exit(MouseControl.exec_())        