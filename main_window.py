import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from Template1 import Ui_Form
from Dialog import Ui_Dialog

if __name__ == '__main__':
    '''程序一'''
    app = QApplication(sys.argv)  # 创建应用程序

    mainwindow = QWidget()  # 创建主窗口
    mainwindow.setGeometry(100, 100, 100, 200)  #平移位置的(x,y,w,h)，(x,y)为角点,(w,h)为offset
    ui = Ui_Form()  # 实例化窗口对象
    ui.setupUi(mainwindow)  # 向主窗口添加控件
    mainwindow.show()  # 显示窗口

    sys.exit(app.exec_())  # 程序执行循环


    '''程序二'''
    # app = QApplication(sys.argv)  # 创建应用程序
    # mainwindow = QWidget()  # 创建主窗口
    # mainwindow.setGeometry(100, 100, 100, 200)  # 平移位置的(x,y,w,h)，(x,y)为角点,(w,h)为offset
    # ui = Ui_Dialog()  # 实例化窗口对象
    #
    # ui.setupUi(mainwindow)  # 向主窗口添加控件
    #
    # mainwindow.show()  # 显示窗口
    # sys.exit(app.exec_())  # 程序执行循环

