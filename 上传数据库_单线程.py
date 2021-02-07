import sys
import os
import xlrd
import pandas as pd
from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5.QtWidgets import QApplication
from sqlalchemy import create_engine
import sqlalchemy
from module import DocPro
import pymysql


class WorkThread3(QThread):
    trigger = pyqtSignal(str)
    trigger1 = pyqtSignal(float)

    def __init__(self):
        super(WorkThread3, self).__init__()
        self.path_list = []
        self.dir_path = ''
        self.file_name_flag = False
        self.column = int
        self.host = ''
        self.db_tables = ''
        self.num = 0
        self.db_name = ''
        self.root = ''
        self.passwd = ''
        self.all_host = ''

    def set(self, path_list, column, file_name_flag):
        self.path_list = path_list
        self.column = column
        self.file_name_flag = file_name_flag

    def set_dir(self):
        self.dir_path = DocPro().folder_access()
        self.path_list = DocPro().dir_ergodic(self.dir_path)

    def set_sql(self, root, passwd, host, db_name, db_tables):
        self.root = root
        self.passwd = passwd
        self.host = host
        self.db_name = db_name
        self.db_tables = db_tables
        self.all_host = 'mysql+pymysql://{}:{}@{}/{}'.format(self.root, self.passwd, self.host, self.db_name)

    def run(self):
        # 连接MySql数据库, //后的参数为: 用户名, 密码, 主机, 数据库名
        engine = create_engine(self.all_host)
        try:
            pd.read_sql("show tables;", con=engine)
            print("connect successfully!")
        except Exception as error:
            print("connect fail! because of :", error)
            # connect to server
            engine = sqlalchemy.create_engine('mysql://{}:{}@{}'.format(self.root, self.passwd, self.host))
            self.trigger.emit('创建数据库{}'.format(self.db_name))
            sql_command = 'CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARSET utf8 COLLATE utf8_general_ci;'.\
                format(self.db_name)
            engine.execute(sql_command)  # create db
            engine = create_engine(self.all_host)
            pd.read_sql("show tables;", con=engine)
            print("connect successfully!")
        num_all = len(self.path_list)
        self.trigger.emit('开始执行数据导入')
        for path in self.path_list:
            self.num += 1
            df = self.func_2(path)
            self.func_1(df, path)
            try:
                df.to_sql(self.db_tables, con=engine, index=False, if_exists="append")
                print("%s insert successfully!" % os.path.basename(path))
            except Exception as error:
                print(os.path.basename(path))
                self.trigger.emit(os.path.basename(path))
                print("insert fail! because of:", error)
                self.trigger.emit("insert fail! because of:", error)
            self.trigger1.emit(self.num / num_all * 100)
        print("##" * 20)
        print("done!")
        self.trigger.emit('数据导入完成')
        self.trigger.emit("##" * 20)
        self.num = 0
        self.trigger1.emit(0)

    def func_1(self, df, path):
        if self.file_name_flag:
            # 注意修改这里插入路径的地方，以免覆盖数据
            df[self.column] = os.path.basename(path)

    def func_2(self, path):
        try:
            df = pd.read_excel(path, header=None)
            return df
        except xlrd.biffh.XLRDError:
            df = pd.read_csv(path)
            return df


if __name__ == '__main__':
    app = QApplication(sys.argv)
    t = WorkThread3()
    # 再表格的第几列插入文件名称
    # t.set([], 8, True)
    t.set_sql('root', '', '127.0.0.1:3306', 'test3', 'my_table')
    t.set_dir()
    t.run()
