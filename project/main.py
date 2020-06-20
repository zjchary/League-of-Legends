

# 主界面框

import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *


class Main_Project(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle("项目管理系统")
        self.setWindowIcon(QIcon('favicon.ico'))

        menubar = self.menuBar()
        file_1 = menubar.addMenu('新建')
        file_2 = menubar.addMenu('查询')
        filr_3 = menubar.addMenu('修改')

        self.statusBar()
        self.center_show()

    def center_show(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


app = QApplication(sys.argv)
form = Main_Project()
form.show()
sys.exit(app.exec_())
