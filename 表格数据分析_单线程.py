import pandas as pd
import xlrd
import os
import time
from PyQt5.QtCore import pyqtSignal, QThread
from module import DocPro
from PyQt5.QtWidgets import QApplication
import sys


class WorkThread1(QThread):
    trigger = pyqtSignal(str)
    trigger1 = pyqtSignal(float)

    def __init__(self):
        super(WorkThread1, self).__init__()
        self.re_list = []
        self.files_list = []
        self.dir_path = ''
        self.target_dir = ''
        self.flag = False
        self.num = 0

    def set(self, dir_path, files_list, target_dir, flag):
        self.dir_path = dir_path
        self.files_list = files_list
        self.target_dir = target_dir
        self.flag = flag

    def set_host(self):
        self.dir_path = DocPro().folder_access()
        self.files_list = DocPro().dir_ergodic(self.dir_path)
        self.target_dir = os.path.dirname(self.dir_path) + '/拆分文件/'
        self.num = 0

    def run(self):
        num_all = len(self.files_list)
        self.trigger.emit('程序已开始运行')
        if self.flag:
            self.func_2(self.target_dir)
            self.trigger.emit('已建立拆分文件夹')
        for file_path in self.files_list:
            self.num += 1
            try:
                excel = pd.ExcelFile(file_path)
                for sheet_name in excel.sheet_names:  # 获取excel文件内表名
                    df = pd.read_excel(file_path, sheet_name=sheet_name)
                    tolist = df.columns.tolist()
                    if not tolist:
                        pass
                    elif not tolist and sheet_name == 'sheet1':
                        print(file_path)
                    else:
                        self.re_list.append([str(file_path) + '_' + sheet_name, tolist])
                        if self.flag:
                            df.to_excel(self.target_dir + os.path.basename(file_path) + '_' + sheet_name +'.xlsx',
                                        index=False)
            except xlrd.biffh.XLRDError:
                if 'xls' in str(file_path):
                    self.trigger.emit('疑似加密文件：%s' % file_path)
                    print('疑似加密文件：%s' % file_path)
                    pass
                else:
                    df = pd.read_csv(file_path)
                    tolist = df.columns.tolist()
                    self.re_list.append([str(file_path), tolist])
                    if self.flag:
                        df.to_excel(self.target_dir + os.path.basename(file_path) + '.xlsx', index=False)
            self.trigger1.emit(self.num / num_all * 100)
        out_path = os.path.dirname(self.dir_path) + "/" + str(time.process_time()) + "表头分析结果.xlsx"
        self.func_3(out_path)
        print('完成')
        self.trigger.emit('已运行完成')
        self.trigger.emit("##" * 20)
        self.num = 0
        self.trigger1.emit(0)

    @staticmethod
    def func_2(target_dir):
        try:
            os.mkdir(target_dir)
        except:
            pass

    def func_3(self, out_path):
        df = pd.DataFrame(self.re_list, columns=['文件路径', '标题内容'])
        df.to_excel(out_path, index=False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    t = WorkThread1()
    t.set_host()
    t.run()

