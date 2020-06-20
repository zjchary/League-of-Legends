
# 垂直，水平布局

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QHBoxLayout, QVBoxLayout


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.Init_UI()

    def Init_UI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('学点编程吧')

        bt1 = QPushButton('剪刀', self)
        # bt1.move(50, 250)

        bt2 = QPushButton('石头', self)
        # bt2.move(150, 250)

        bt3 = QPushButton('布', self)
        # bt3.move(250, 250)

        hbox = QHBoxLayout()  # 创建一个水平框布局
        hbox.addStretch(1)  # 添加一个拉伸因子，为1等分
        hbox.addWidget(bt1)  # 下面是三个按钮
        hbox.addStretch(1)
        hbox.addWidget(bt2)
        hbox.addStretch(1)
        hbox.addWidget(bt3)

        vbox = QVBoxLayout()  # 水平布局放置在垂直布局中。
        vbox.addStretch(1)
        vbox.addLayout(hbox)  # 垂直框中的拉伸因子将按钮的水平框推到窗口的底部。

        self.setLayout(vbox)  # 设置窗口主要布局

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exit(app.exec_())
