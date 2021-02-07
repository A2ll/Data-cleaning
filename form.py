from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from control import MainForm


app = QApplication(sys.argv)
mainWin = QMainWindow()
ui = MainForm() # 中间控制端
ui.setupUi(mainWin)
mainWin.show()
sys.exit(app.exec_())
