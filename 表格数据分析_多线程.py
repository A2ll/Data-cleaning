import pandas as pd
import xlrd
import time
from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5.QtWidgets import QApplication, QMainWindow
from module import DocPro
import sys


class WorkThread(QThread):
    trigger = pyqtSignal(list)  #需要注明返回数据类型

    def __init__(self):
        super(WorkThread, self).__init__()

    def set(self, file_path):  #传入参数
        self.file_path = file_path

    def run(self):
        try:
            excel = pd.ExcelFile(self.file_path)
            for sheet_name in excel.sheet_names:  # 获取excel文件内表名
                df = pd.read_excel(self.file_path, sheet_name=sheet_name, header=0)
                tolist = df.columns.tolist()
                if not tolist:
                    pass
                elif not tolist and sheet_name == 'sheet1':
                    print(self.file_path)
                else:
                    # self.trigger.emit([str(self.file_path) + '_' + sheet_name, tolist])
                    print([str(self.file_path) + '_' + sheet_name, tolist])
                    pass
        except xlrd.biffh.XLRDError:
            if 'xls' in str(self.file_path):
                print(self.file_path)
                pass
            else:
                df = pd.read_csv(self.file_path, header=0)
                tolist = df.columns.tolist()
                # self.trigger.emit([str(self.file_path), tolist])
                print([str(self.file_path), tolist])


class MainForm():
    trigger = pyqtSignal(list)

    def __init__(self):
        super().__init__()
        self.t = WorkThread()
        self.re_list = []

    # def setupUi(self, Main_Form):
    #     super().setupUi(Main_Form)
    #     self.pushButton.clicked.connect(self.func_1)

    def func_1(self):
        dir_path = DocPro().folder_access()  # 获取选择文件夹绝对路径
        files_list = DocPro().dir_ergodic(dir_path)  # 获取所选文件夹中所有文件的绝对路径
        for file_path in files_list:  # files_list[0]文件夹内所有文件的据对路径
            time.sleep(0.5)
            self.t.set(file_path)
            self.t.trigger.connect(self.func_2)
            self.t.start()
        # self.func_3()
        # print(self.re_list)

    def func_2(self, return_list):
        self.re_list.append(return_list)

    def func_3(self):
        df = pd.DataFrame(self.re_list, columns=['文件路径', '标题内容'])
        df.to_excel("./" + str(time.process_time()) + "表头分析结果.xlsx", index=False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    n = MainForm()
    n.func_1()
