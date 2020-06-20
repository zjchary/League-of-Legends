
# 界面设置，0--99

import sys
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtWidgets import QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication, QPushButton
from PyQt5.QtGui import QIcon


class SigSlot(QWidget):
    # QWidget小部件是PyQt5中所有用户界面对象的基类
    def __init__(self, parent=None):
        QWidget.__init__(self)
        self.setWindowTitle('XXOO_HH')  # 设置标题
        lcd = QLCDNumber(self)
        slider = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()  # 水平
        vbox.addWidget(lcd)
        vbox.addWidget(slider)

        self.setLayout(vbox)

        slider.valueChanged.connect(lcd.display)
        self.resize(350, 250)  # 设置宽、高
        self.move(300, 300)  # 左上角点移动到(x,y)
        # == self.setGeometry(300, 300, 350, 250)
        self.setWindowIcon(QIcon('favicon.ico'))  # 创建图标

        qbtn = QPushButton('退出', self)  # 0-标签, 1-父窗口小部件
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        # PyQt5中的事件处理系统采用信号和槽机制构建。
        # 如果我们点击按钮，点击的信号被发出。
        # 槽可以是Qt槽函数或任何Python可调用的函数。
        # QCoreApplication包含主事件循环; 它处理和调度所有事件。 instance（）方法给我们当前的实例。
        # 点击的信号连接到终止应用程序的quit（）方法。
        qbtn.resize(70, 30)
        qbtn.move(50, 50)


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建一个app
    qb = SigSlot()
    qb.show()
    # show()方法在屏幕上显示窗口小部件。 一个小部件首先在内存中创建，然后在屏幕上显示。
    sys.exit(app.exec_())  # 关闭app
