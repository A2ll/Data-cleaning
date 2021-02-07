import pandas as pd
import xlrd
import os
import sys
import re
from PyQt5.QtCore import pyqtSignal, QThread
from module import DocPro
from PyQt5.QtWidgets import QApplication


class WorkThread2(QThread):
    trigger = pyqtSignal(str)
    trigger1 = pyqtSignal(float)

    def __init__(self):
        super(WorkThread2, self).__init__()
        self.re_list = []
        self.list_1 = []
        self.num = 0
        self.keys = ['.*姓名', '.*手机']
        self.files_list = []
        self.dir_path = ''
        self.target_dir = ''

    def set(self, dir_path, files_list, target_dir):
        self.dir_path = dir_path
        self.files_list = files_list
        self.target_dir = target_dir

    def set_key(self, keys):
        self.keys = keys.split(';')

    def func_4(self):
        self.dir_path = DocPro().folder_access()
        self.files_list = DocPro().dir_ergodic(self.dir_path)
        self.target_dir = os.path.dirname(self.dir_path) + '/符合的数据/'

    def run(self):
        self.func_3(self.target_dir)
        self.trigger.emit('使用的关键字为：%s' % self.keys)
        num_all = len(self.files_list)
        for file_path in self.files_list:
            self.num += 1
            try:
                excel = pd.ExcelFile(file_path)
                for sheet_name in excel.sheet_names:  # 获取excel文件内表名
                    df = pd.read_excel(file_path, sheet_name=sheet_name)
                    self.list_1 = []
                    tolist = df.columns.tolist()
                    if not tolist:
                        pass
                    else:
                        try:
                            self.list_1 = self.func_2(df)
                            data = pd.read_excel(file_path, sheet_name=sheet_name, usecols=self.list_1)
                            data.to_excel(self.target_dir + os.path.basename(file_path) + '_' + sheet_name + '.xlsx',
                                          index=False)
                            self.trigger.emit('发现文件：' + os.path.basename(file_path) + '_' + sheet_name)
                        except ValueError:
                            print(os.path.basename(file_path) + '_' + sheet_name)
                            pass
            except xlrd.biffh.XLRDError:
                if 'xls' in str(file_path):
                    pass
                else:
                    try:
                        df = pd.read_csv(file_path)
                        self.list_1 = []
                        self.list_1 = self.func_2(df)
                        data = pd.read_csv(file_path, usecols=self.list_1)
                        data.to_excel(self.target_dir + os.path.basename(file_path) + '.xlsx', index=False)
                        self.trigger.emit('发现文件：' + os.path.basename(file_path))
                    except ValueError:
                        print(os.path.basename(file_path))
                        pass
            self.trigger1.emit(self.num / num_all * 100)
        print('已运行完成')
        self.trigger.emit('已运行完成')
        self.trigger.emit("##" * 20)
        self.num = 0
        self.trigger1.emit(0)

    @staticmethod
    def func_3(target_dir):
        try:
            os.mkdir(target_dir)
        except:
            pass

    def func_2(self, df):
        list_2 = []
        for key in self.keys:
            list_2.append(self.func_1(df, key))
        return list_2

    @staticmethod
    def func_1(df, str2):  # 模糊查询某一个关键词在表中行列 适用于CSV和EXCEL
        flag = True
        tolist = df.columns.tolist()
        j = 0
        for str1 in tolist:
            if re.match(str2, str(str1)):
                flag = False
                break
            else:
                j += 1
        i = 0
        while i < 10 and flag:
            j = 0
            try:
                data = df.loc[i].values
                for str1 in data:
                    try:
                        if re.match(str2, str(str1)):
                            flag = False
                            break
                    except TypeError:
                        pass
                    j += 1
                i += 1
            except KeyError:
                i += 1
        if flag:
            return '-10086'
        else:
            return j


if __name__ == '__main__':
    app = QApplication(sys.argv)
    t = WorkThread2()
    t.func_4()
    t.run()
