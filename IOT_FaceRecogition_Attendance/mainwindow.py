# Author BIGBOSS
# April 2022
# IOT人脸识别签到系统
# WX：BIGBOSSyifi
# Mail：bigbossyifi@gmail.com
# *-

import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
import resource_rc      #加载资源文件
# from model import Model
from out_window import Ui_OutputDialog


class Ui_Dialog(QDialog):
    def __init__(self):
        super(Ui_Dialog, self).__init__()
        loadUi("mainwindow.ui", self)       #加载QTUI文件

        self.runButton.clicked.connect(self.runSlot)

        self._new_window = None
        self.Videocapture_ = None

    def refreshAll(self):
        print("当前调用人俩检测摄像头编号（0为笔记本内置摄像头，1为USB外置摄像头）：")
        self.Videocapture_ = "0"

    @pyqtSlot()
    def runSlot(self):
        print("IOT人脸识别签到系统运行中...")
        self.refreshAll()
        print(self.Videocapture_)
        ui.hide()  # UI隐藏
        self.outputWindow_()  # 创建新的窗体

    def outputWindow_(self):
        """
        在GUI中创建人脸识别区域的窗体
        """
        self._new_window = Ui_OutputDialog()
        self._new_window.show()
        self._new_window.startVideo(self.Videocapture_)
        print("人脸识别功能初始化中....")
        print("人脸识别功能初始化完成！")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())
