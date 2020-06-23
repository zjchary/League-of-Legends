import sys
import pymysql

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, \
    QDialog, QWidget, QFileDialog, QTreeWidgetItem, QMessageBox
from PyQt5.QtGui import QIcon, QColor, QBrush
from Ui_main import Ui_MainWindow
from Ui_new_project import Ui_Dialog
from Ui_inquire_project import Ui_Form
from Ui_about import Ui_About
from datetime import datetime


class UsingMain(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(UsingMain, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowIcon(QIcon('favicon.ico'))

        self.pushButton_5.clicked.connect(self.Refresh)

        self.actionnew.triggered.connect(self.usingnew)
        self.actionb.triggered.connect(self.usingabout)
        self.pushButton_4.clicked.connect(self.inquire)
        self.treeWidget.itemClicked['QTreeWidgetItem*', 'int'].connect(
            self.function)
        self.pushButton_3.clicked.connect(self.inquired)
        self.pushButton.clicked.connect(self.again)
        self.pushButton_6.clicked.connect(self.download)

        self.change()

    def download(self):
        project = pymysql.connect(
            host='127.0.0.1',
            user='root',
            port=3306,
            password='20000502',
            db='project',
            charset='utf8',
        )
        cur = project.cursor()
        sql = "select sche_annex from schedule where sche_id = {}"\
            .format(self.comboBox_3.currentText())
        if cur.execute(sql):
            res = cur.fetchall()
            text = self.dealDBFileData(res)

            with open(self.comboBox_3.currentText() + type, 'wb') as f:
                f.write(text)
                f.close()
                cur.close()
                project.close()

    def again(self):
        self.inquiredd = UsingInquire(self.comboBox_2.currentText())
        self.inquiredd.show()

    def inquired(self):
        project = pymysql.connect(
            host='127.0.0.1',
            user='root',
            port=3306,
            password='20000502',
            db='project',
            charset='utf8',
        )
        cur = project.cursor()
        cur1 = project.cursor()
        cur2 = project.cursor()
        sql = "select info_name from information;"
        sql1 = "select sche_name, count(*) from schedule group by sche_name having count(*) >= 5;"
        cur.execute(sql)
        cur1.execute(sql1)
        date_info_name = [i[0] for i in cur.fetchall()]
        date_info_max = [i[0] for i in cur1.fetchall()]
        for i in date_info_max:
            if i in date_info_name:
                date_info_name.remove(i)
        self.comboBox_2.clear()
        self.comboBox_2.addItems(date_info_name)
        self.comboBox_2.setCurrentIndex(0)
        sql2 = "select * from information, schedule where info_name = \
            sche_name and info_name in {} ".format(tuple(date_info_name))
        cur2.execute(sql2)
        date_cur2 = cur2.fetchall()
        while self.treeWidget.takeTopLevelItem(0) is not None:
            continue

        for index in range(len(date_cur2)):
            root = QTreeWidgetItem(self.treeWidget)
            root.setText(0, str(date_cur2[index][6]))
            root.setText(1, date_cur2[index][1])
            root.setText(2, date_cur2[index][8])
            root.setText(3, str(date_cur2[index][9]))
            root.setText(4, str(date_cur2[index][10]))
            root.setText(5, str(date_cur2[index][11]))
            if date_cur2[index][11] is not None and date_cur2[index][
                    10] < date_cur2[index][11]:
                for j in range(12):
                    root.setBackground(j, QBrush(QColor("#E10602")))
            root.setText(6, date_cur2[index][12])
            root.setText(7, date_cur2[index][13])
            root.setText(8, date_cur2[index][2])
            root.setText(9, date_cur2[index][3])
            root.setText(10, date_cur2[index][4])
            root.setText(11, date_cur2[index][5])
        cur.close()
        cur1.close()
        cur2.close()
        project.close()

    def function(self, item, column):
        id = item.text(0)
        if item.text(5) == "None":
            project = pymysql.connect(
                host='127.0.0.1',
                user='root',
                port=3306,
                password='20000502',
                db='project',
                charset='utf8',
            )
            cur = project.cursor()
            sql = "update schedule set sche_endtime = '{}' \
                where sche_id = {}; " \
            .format(datetime.now(), id)
            cur.execute(sql)
            project.commit()
            cur.close()
            project.close()
        self.Refresh()

    def change(self):
        pass

    def dealDBFileData(self, data):
        """ 对从数据库fetchall的二进制进行处理 """
        temp = data[0][0].decode('ascii').split('s')
        return bytes([int(ele) for ele in temp])

    def usingnew(self):
        # self.hide()
        self.new = UsingNew()
        self.new.show()

    def usingabout(self):
        self.about = UsingAbout()
        self.about.show()

    def inquire(self):
        curren = int(self.comboBox.currentText()[0])
        line = self.lineEdit.text()
        project = pymysql.connect(
            host='127.0.0.1',
            user='root',
            port=3306,
            password='20000502',
            db='project',
            charset='utf8',
        )
        cur = project.cursor()
        cur1 = project.cursor()
        cur2 = project.cursor()
        info = "select * from information;"
        sche = "select * from schedule;"
        info_sche = "select * from information, schedule \
            where information.info_name = schedule.sche_name"

        if curren == 1:
            sche_1 = "select * from schedule where sche_name like '%{}%';".format(
                line)
            sche = sche_1
        elif curren == 2:
            sche_2 = "select * from schedule where sche_stage like '%{}%';".format(
                line)
            sche = sche_2
        elif curren == 3:
            sche_3 = "select * from schedule where sche_designer like '%{}%';".format(
                line)
            sche = sche_3
        elif curren == 4:
            sche_4 = "select * from schedule where sche_auditor like '%{}%';".format(
                line)
            sche = sche_4
        elif curren == 5:
            sche_5 = "select * from schedule where sche_end < sche_endtime;"
            sche = sche_5
        elif curren == 6:
            info_sche = "select sche_id, info_name, sche_stage, sche_start, sche_end, \
                sche_endtime, sche_designer, sche_auditor, info_unit, \
                info_phone, info_location, info_introduction \
                from information, schedule where info_unit like '%{}%' \
                and information.info_name = schedule.sche_name;".format(line)
        elif curren == 7:
            info_sche = "select sche_id, info_name, sche_stage, sche_start, sche_end, \
                sche_endtime, sche_designer, sche_auditor, info_unit, \
                info_phone, info_location, info_introduction \
                from information, schedule where info_location like '%{}%'\
                and information.info_name = schedule.sche_name;".format(line)

        cur.execute(sche)
        cur1.execute(info)
        cur2.execute(info_sche)
        date_info = cur1.fetchall()
        date_sche = cur.fetchall()
        date_info_sche = cur2.fetchall()

        while self.treeWidget.takeTopLevelItem(0) is not None:
            continue
        if curren in range(1, 6):
            for index in range(len(date_sche)):
                root = QTreeWidgetItem(self.treeWidget)
                root.setText(0, str(date_sche[index][0]))
                root.setText(1, date_sche[index][1])
                root.setText(2, date_sche[index][2])
                root.setText(3, str(date_sche[index][3]))
                root.setText(4, str(date_sche[index][4]))
                root.setText(5, str(date_sche[index][5]))
                if date_sche[index][5] is not None and date_sche[index][
                        4] < date_sche[index][5]:
                    for j in range(12):
                        root.setBackground(j, QBrush(QColor("#E10602")))
                root.setText(6, date_sche[index][6])
                root.setText(7, date_sche[index][7])
                for i in range(len(date_info)):
                    if date_info[i][1] == date_sche[index][1]:
                        root.setText(8, date_info[i][2])
                        root.setText(9, date_info[i][3])
                        root.setText(10, date_info[i][4])
                        root.setText(11, date_info[i][5])
        else:
            for index in range(len(date_info_sche)):
                root = QTreeWidgetItem(self.treeWidget)
                root.setText(0, str(date_info_sche[index][0]))
                root.setText(1, date_info_sche[index][1])
                root.setText(2, date_info_sche[index][2])
                root.setText(3, str(date_info_sche[index][3]))
                root.setText(4, str(date_info_sche[index][4]))
                root.setText(5, str(date_info_sche[index][5]))
                if date_info_sche[index][5] is not None and date_info_sche[
                        index][4] < date_info_sche[index][5]:
                    for j in range(12):
                        root.setBackground(j, QBrush(QColor("#E10602")))
                root.setText(6, date_info_sche[index][6])
                root.setText(7, date_info_sche[index][7])
                root.setText(8, date_info_sche[index][8])
                root.setText(9, date_info_sche[index][9])
                root.setText(10, date_info_sche[index][10])
                root.setText(11, date_info_sche[index][11])

        cur.close()
        project.close()

    def Refresh(self):
        project = pymysql.connect(
            host='127.0.0.1',
            user='root',
            port=3306,
            password='20000502',
            db='project',
            charset='utf8',
        )
        cur = project.cursor()
        cur1 = project.cursor()
        info = "select * from information;"
        sche = "select * from schedule;"
        cur.execute(sche)
        cur1.execute(info)
        date_info = cur1.fetchall()
        date_sche = cur.fetchall()

        while self.treeWidget.takeTopLevelItem(0) is not None:
            continue

        for index in range(len(date_sche)):
            root = QTreeWidgetItem(self.treeWidget)
            root.setText(0, str(date_sche[index][0]))
            root.setText(1, date_sche[index][1])
            root.setText(2, date_sche[index][2])
            root.setText(3, str(date_sche[index][3]))
            root.setText(4, str(date_sche[index][4]))
            root.setText(5, str(date_sche[index][5]))
            if date_sche[index][5] is not None and date_sche[index][
                    4] < date_sche[index][5]:
                for j in range(12):
                    root.setBackground(j, QBrush(QColor("#E10602")))
            root.setText(6, date_sche[index][6])
            root.setText(7, date_sche[index][7])
            if date_sche[index][8] is not None:
                self.comboBox_3.addItem(str(date_sche[index][0]))
            for i in range(len(date_info)):
                if date_info[i][1] == date_sche[index][1]:
                    root.setText(8, date_info[i][2])
                    root.setText(9, date_info[i][3])
                    root.setText(10, date_info[i][4])
                    root.setText(11, date_info[i][5])

        cur.close()
        project.close()


class UsingNew(QDialog, Ui_Dialog):
    def __init__(self, *arges, **kwargs):
        super(UsingNew, self).__init__(*arges, **kwargs)
        self.setupUi(self)
        self.setWindowIcon(QIcon('favicon.ico'))

        self.pushButton.clicked.connect(self.usinginquire)

        self.change()

    def change(self):
        pass

    def usinginquire(self):
        self.name = self.lineEdit_5.text()
        self.info_unit = self.lineEdit.text()
        self.info_phone = self.lineEdit_2.text()
        self.info_location = self.lineEdit_3.text()
        self.info_introduction = self.textEdit.toPlainText()
        if self.name == "" or self.info_unit == "" or \
            self.info_phone == "" or self.info_location == "" or \
                self.info_introduction == "":
            self.messageDialog()
        else:
            self.inquire = UsingInquire(self.name)
            self.inquire.show()

        project = pymysql.connect(
            host='127.0.0.1',
            user='root',
            port=3306,
            password='20000502',
            db='project',
            charset='utf8',
        )
        cur = project.cursor()
        sql1 = "insert into information values(NULL, \
            '{}', '{}', '{}', '{}', '{}')"\
            .format(self.name,
                    self.info_unit,
                    self.info_phone,
                    self.info_location,
                    self.info_introduction)
        cur.execute(sql1)
        cur.close()
        project.close()

    def messageDialog(self):
        msg_box = QMessageBox(QMessageBox.Warning, 'Warning', '必须填满!')
        msg_box.setWindowIcon(QIcon('favicon.ico'))
        msg_box.exec_()


class UsingInquire(QWidget, Ui_Form):
    def __init__(self, name):
        super(UsingInquire, self).__init__()
        self.name = name
        self.setupUi(self)
        self.setWindowIcon(QIcon('favicon.ico'))

        self.pushButton_3.clicked.connect(self.usingnew)
        self.pushButton_4.clicked.connect(self.annex)
        self.pushButton.clicked.connect(self.npnew)

        self.change()

    def npnew(self):
        self.sche_stage = self.comboBox.currentText()
        self.sche_start = self.dateEdit.date().currentDate().toString(
            Qt.ISODate)
        self.sche_end = self.dateEdit_2.date().currentDate().toString(
            Qt.ISODate)
        self.sche_designer = self.lineEdit.text()
        self.sche_auditor = self.lineEdit_2.text()
        self.file = self.openFile(self.lineEdit_3.text())
        if self.sche_stage == "" or self.sche_start == "" or \
            self.sche_end == "" or self.sche_designer == "" or \
                self.sche_auditor == "":
            self.messageDialog()
        else:
            self.messageDialog1()
        project = pymysql.connect(
            host='127.0.0.1',
            user='root',
            port=3306,
            password='20000502',
            db='project',
            charset='utf8',
        )
        cur = project.cursor()
        sql2 = "insert into schedule values(null, \
            '{}', '{}', '{}', '{}', null, '{}', '{}', '{}') "\
            .format(self.name,
                    self.sche_stage,
                    self.sche_start,
                    self.sche_end,
                    self.sche_designer,
                    self.sche_auditor,
                    self.file)
        cur.execute(sql2)
        project.commit()
        cur.close()
        project.close()
        self.close()

    def change(self):
        pass

    def usingnew(self):
        self.close()

    def openFile(self, fileName):
        if fileName == "":
            return ''
        with open(fileName, 'rb') as f:
            type = fileName[-1:-5:-1]
            content = 's'.join([str(ele) for ele in f.read()])
            f.close()
        return content or ''

    def messageDialog1(self):
        msg_box = QMessageBox(QMessageBox.Warning, 'Warning', '写入成功!')
        msg_box.setWindowIcon(QIcon('favicon.ico'))
        msg_box.exec_()

    def messageDialog(self):
        msg_box = QMessageBox(QMessageBox.Warning, 'Warning', '除附件外其他填满!')
        msg_box.setWindowIcon(QIcon('favicon.ico'))
        msg_box.exec_()

    def annex(self):
        fileName1, _ = QFileDialog.getOpenFileName(
            self, "选取文件", "./", "All Files (*);;Text Files (*.txt)")
        self.lineEdit_3.setText(fileName1)


class UsingAbout(QWidget, Ui_About):
    def __init__(self, *arges, **kwargs):
        super(UsingAbout, self).__init__(*arges, **kwargs)
        self.setupUi(self)
        self.setWindowIcon(QIcon('favicon.ico'))

        self.change()

    def change(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = UsingMain()
    win.show()
    sys.exit(app.exec_())
