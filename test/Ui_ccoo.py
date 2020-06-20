
# 垂直0---99

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLCDNumber, QDial, QApplication, QSlider


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        lcd = QLCDNumber(self)  # 接受信号
        # dial = QDial(self) # 发送信号
        dial = QSlider(self)  # 发送信号

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('学点编程吧')

        lcd.setGeometry(100, 50, 150, 60)
        dial.setGeometry(120, 120, 100, 100)

        dial.valueChanged.connect(lcd.display)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
