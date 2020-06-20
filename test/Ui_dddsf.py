
# 响应鼠标

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QMessageBox)
from PyQt5.QtCore import (pyqtSignal, QObject)


class Signal(QObject):
    showmouse = pyqtSignal()
    # 我们创建一个名为showmouse的新信号。
    # 该信号在鼠标按压事件期间发出。 该信号连接到QMainWindow的about（）的槽。


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle('学点编程吧')

        self.s = Signal()  # 创建信号
        self.s.showmouse.connect(self.about)  # 连接信号

        self.show()

    def about(self):
        QMessageBox.about(self, '鼠标', '你点鼠标了吧！')

    def mousePressEvent(self, e):
        # 自定义showmouse信号连接到QMainWindow的about（）的槽
        self.s.showmouse.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
