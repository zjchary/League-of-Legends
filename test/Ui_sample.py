
# 猜数字

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit
from PyQt5.QtGui import QIcon
from random import randint


class Example(QWidget):

    def __init__(self):

        super().__init__()
        self.initUI()
        self.num = randint(1, 100)  # 随机生成数字

    def initUI(self):

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('学点编程吧--猜数字')
        self.setWindowIcon(QIcon('favicon.ico'))

        self.bt1 = QPushButton('我猜', self)
        self.bt1.setGeometry(115, 150, 70, 30)
        self.bt1.setToolTip('<b>点击这里猜数字</b>')
        self.bt1.clicked.connect(self.showMessage)  # 点击连接函数

        self.text = QLineEdit('在这里输入数字', self)  # 添加凹陷文本
        self.text.selectAll()  # 默认全选文本
        self.text.setFocus()  # 聚焦
        self.text.setGeometry(80, 50, 150, 30)

        self.show()

    def showMessage(self):

        guessnumber = int(self.text.text())
        print(self.num)

        if guessnumber > self.num:
            # QMessageBox.about--->>>弹出对话框
            QMessageBox.about(self, '看结果', '猜大了!')
            self.text.setFocus()
        elif guessnumber < self.num:
            QMessageBox.about(self, '看结果', '猜小了!')
            self.text.setFocus()
        else:
            QMessageBox.about(self, '看结果', '答对了!进入下一轮!')
            self.num = randint(1, 100)
            self.text.clear()
            self.text.setFocus()

    def closeEvent(self, event):
        # 关闭窗口触发

        reply = QMessageBox.question(
            self, '确认', '确认退出吗', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        # 第一个为标题，
        # 第二个为对话框文本。
        # 第三个参数指定出现在对话框中的按钮的组合。
        # 最后一个参数是默认按钮。 它是初始键盘焦点的按钮。 返回值存储在答复变量中。
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
