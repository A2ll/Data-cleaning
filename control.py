from untitled import Ui_Form
import time
from 表格数据分析_单线程 import WorkThread1
from 表格数据提取_单线程 import WorkThread2
from 上传数据库_单线程 import WorkThread3
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5 import QtWidgets
import sys
from module import DocPro
import os


class MainForm(Ui_Form, QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.t1 = WorkThread1()
        self.t2 = WorkThread2()
        self.t3 = WorkThread3()
        self.t1.trigger.connect(self.print_return)
        self.t1.trigger1.connect(self.progress_bar)
        self.t2.trigger.connect(self.print_return)
        self.t2.trigger1.connect(self.progress_bar)
        self.t3.trigger.connect(self.print_return)
        self.t3.trigger1.connect(self.progress_bar)
        self.files_list = []
        self.dir_path = ''
        self.target_dir = ''

    def setupUi(self, Main_Form):
        super().setupUi(Main_Form)
        self.pushButton.clicked.connect(self.main)

    def main(self):
        if self.radioButton1.isChecked():
            self.dir_path = QFileDialog.getExistingDirectory(self, "选取文件夹", "./")
            if self.dir_path != '':
                self.files_list = DocPro().dir_ergodic(self.dir_path)
                self.target_dir = os.path.dirname(self.dir_path) + '/拆分文件/'
                t1_flag = self.checkBox_2.isChecked()
                self.t1.set(self.dir_path, self.files_list, self.target_dir, t1_flag)
                time.sleep(1)
                self.t1.start()
        elif self.radioButton.isChecked():
            if self.lineEdit.text() != '':
                self.dir_path = QFileDialog.getExistingDirectory(self, "选取文件夹", "./")
                if self.dir_path != '':
                    self.files_list = DocPro().dir_ergodic(self.dir_path)
                    self.target_dir = os.path.dirname(self.dir_path) + '/符合的数据/'
                    self.t2.set(self.dir_path, self.files_list, self.target_dir)
                    self.t2.set_key(self.lineEdit.text())
                    time.sleep(1)
                    self.t2.start()
            else:
                self.textBrowser.append('输入需要提取的关键字,支持正则表达式。例如：.*姓名;.*手机')
        elif self.radioButton_2.isChecked():
            if self.lineEdit_2.text() != '' and self.lineEdit_3.text() != '' and self.lineEdit_4.text() != '' and \
                    self.lineEdit_5.text() != '':
                self.dir_path = QFileDialog.getExistingDirectory(self, "选取文件夹", "./")
                if self.dir_path != '':
                    self.files_list = DocPro().dir_ergodic(self.dir_path)
                    if self.checkBox.isChecked() and self.lineEdit_6.text() == []:
                        self.textBrowser.append('输入文件名所插入的列（从0开始数）')
                    else:
                        self.t3.set(self.files_list, self.lineEdit_6.text(), self.checkBox.isChecked())
                        self.t3.set_sql(self.lineEdit_3.text(), self.lineEdit_4.text(), self.lineEdit_2.text(),
                                        self.lineEdit_7.text(), self.lineEdit_5.text())
                        time.sleep(1)
                        self.t3.start()
            else:
                self.textBrowser.append('输入服务器相关配置')
        else:
            self.textBrowser.append('选择需要的功能')

    def print_return(self, pr):
        self.textBrowser.append(pr)

    def progress_bar(self, i):
        self.progressBar.setValue(i)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = QMainWindow()
    ui = MainForm()  # 中间控制端
    ui.setupUi(mainWin)
    mainWin.show()
    sys.exit(app.exec_())
