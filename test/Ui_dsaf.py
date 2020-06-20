
# 表单布局

import sys
from PyQt5.QtWidgets import (
    QWidget, QPushButton, QApplication, QFormLayout, QLabel, QLineEdit, QTextEdit)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.Init_UI()

    def Init_UI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('学点编程吧')

        formlayout = QFormLayout()  # 创建一个表单 管理输入型控件和关联的标签组成的那些Form表单
        nameLabel = QLabel("姓名")
        nameLineEdit = QLineEdit("")
        introductionLabel = QLabel("简介")
        introductionLineEdit = QTextEdit("")

        # 向表单中增加一行，内容是我们定义的小部件。
        formlayout.addRow(nameLabel, nameLineEdit)
        formlayout.addRow(introductionLabel, introductionLineEdit)
        self.setLayout(formlayout)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exit(app.exec_())
