"""使用QT获取文件夹或文件路径的操作类
dir_path = DocPro().folder_access()  # 获取选择文件夹绝对路径
files_list = DocPro().dir_ergodic(dir_path)  # 获取所选文件夹中所有文件的绝对路径
"""
import pathlib
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
import os


class DocPro(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

    def folder_access(self):
        dir_path = QFileDialog.getExistingDirectory(self, "选取文件夹", "./")  # 选择文件夹
        return dir_path

    def dir_ergodic(self, dir_path):  # 文件夹遍历，并输出文件夹内文件list
        dir_names = []
        for f_path, dirs, fs in os.walk(dir_path):
            for f in fs:
                path_r = pathlib.Path(os.path.join(f_path, f))  # 获取每个文件的绝对路径
                dir_names.append(path_r)
        if len(dir_names) == 0:  # 用来辨别是文件夹还是单个文件
            path_r = pathlib.Path(dir_path)  # 获取每个文件的绝对路径
            dir_names.append(path_r)
            return dir_names  # 文件夹内所有文件的绝对路径，所选文件的绝对路径
        else:
            return dir_names


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ui = DocPro()  # 中间控制端
#     ui.dir_ergodic(ui.folder_access())

