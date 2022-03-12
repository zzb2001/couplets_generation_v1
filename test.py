# import sys
# from PyQt5 import QtWidgets
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import QDialog, QHBoxLayout, QLabel
#
#
# class MyWindow(QDialog):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("MainWindow")
#         self.setWindowFlags(Qt.WindowCloseButtonHint)
#         layout = QHBoxLayout()
#         self.btn = QtWidgets.QPushButton(self)
#         self.btn.setText("Jump")
#         self.btn.clicked.connect(self.jump)
#         _1 = QLabel(self)
#         _1.setText(" " * 5)
#         _2 = QLabel(self)
#         _2.setText(" " * 5)
#         layout.addWidget(_1)
#         layout.addWidget(self.btn)
#         layout.addWidget(_2)
#         self.setLayout(layout)
#
#     def jump(self):
#         child = DialogOfYouNeed()
#         child.exec_()
#
#
# class ChildDialogUi(QDialog):
#     def __init__(self):
#         super().__init__()
#
#         layout = QHBoxLayout()
#         self.label = QLabel(self)
#         self.label.setText("This is child dialog.")
#         layout.addWidget(self.label)
#         self.setLayout(layout)
#
#
# class DialogOfYouNeed(ChildDialogUi):
#     def __init__(self):
#         super().__init__()
#
#         # write down you logic code here
#
#
# if __name__=='__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     main = MyWindow()
#     main.show()
#     sys.exit(app.exec_())



# from PyQt5 import QtWidgets
# import sys
#
# app = QtWidgets.QApplication(sys.argv)
# w = QtWidgets.QWidget()
#
# grab_btn = QtWidgets.QPushButton('Grab Screen')
#
# def click_handler():
#     screen = QtWidgets.QApplication.primaryScreen()
#     screenshot = screen.grabWindow(w.winId(),x=0, y=0, width=10, height=5)
#     screenshot.save('shot.jpg', 'jpg')
#     w.close()
#
# grab_btn.clicked.connect(click_handler)
#
# layout = QtWidgets.QVBoxLayout()
# layout.addWidget(grab_btn)
# w.setLayout(layout)
# w.show()
#
# sys.exit(app.exec_())

'''动态添加'''
# from PyQt5.QtCore import *
# from PyQt5.QtWidgets import *
# import sys
#
# class Worker(QThread):
#     sinOut = pyqtSignal(str) # 自定义信号，执行run()函数时，从相关线程发射此信号
#
#     def __init__(self, parent=None):
#         super(Worker, self).__init__(parent)
#         self.working = True
#         self.num = 0
#
#     def __del__(self):
#         self.working = False
#         self.wait()
#
#     def run(self):
#         while self.working == True:
#             file_str = 'File index {0}'.format(self.num) # str.format()
#             self.num += 1
#
#             # 发出信号
#             self.sinOut.emit(file_str)
#
#             # 线程休眠2秒
#             self.sleep(2)
#
#
# class MainWidget(QWidget):
#     def __init__(self, parent=None):
#         super(MainWidget, self).__init__(parent)
#
#         self.setWindowTitle("QThread 例子")
#
#         # 布局管理
#         self.listFile = QListWidget()
#         self.btnStart = QPushButton('开始')
#         layout = QGridLayout(self)
#         layout.addWidget(self.listFile, 0, 0, 1, 2)
#         layout.addWidget(self.btnStart, 1, 1)
#
#         # 连接开始按钮和槽函数
#         self.btnStart.clicked.connect(self.slotStart)
#
#         # 创建新线程，将自定义信号sinOut连接到slotAdd()槽函数
#         self.thread = Worker()
#         self.thread.sinOut.connect(self.slotAdd)
#
#     # 开始按钮按下后使其不可用，启动线程
#     def slotStart(self):
#         self.btnStart.setEnabled(False)
#         self.thread.start()
#
#     # 在列表控件中动态添加字符串条目
#     def slotAdd(self, file_inf):
#         self.listFile.addItem(file_inf)
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     demo = MainWidget()
#     demo.show()
#     sys.exit(app.exec_())



'''多线程发射信号简单例子'''
# from Dialog import Ui_Dialog
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import QThread, pyqtSignal
# import sys
# import time
#
# class MyWin(QWidget,Ui_Dialog):
#     """docstring for Mywine"""
#     def __init__(self):
#         super(MyWin, self).__init__()
#         self.setupUi(self)
#         self.mythread = MyThread() # 实例化自己建立的任务线程类
#         self.mythread.signal.connect(self.callback) #设置任务线程发射信号触发的函数
#
#     def test(self): # 这里test就是槽函数, 当点击按钮时执行 test 函数中的内容, 注意有一个参数为 self
#         self.mythread.start() # 启动任务线程
#
#     def callback(self,i): # 这里的 i 就是任务线程传回的数据
#         self.pushButton.setText(i)
#
# class MyThread(QThread): # 建立一个任务线程类
#     signal = pyqtSignal(str) #设置触发信号传递的参数数据类型,这里是字符串
#     def __init__(self):
#         super(MyThread, self).__init__()
#
#     def run(self): # 在启动线程后任务从这个函数里面开始执行
#         for i in range(10):
#             self.signal.emit(str(i)) #任务线程发射信号用于与图形化界面进行交互
#             time.sleep(1)
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     mywin = MyWin() # 实例化一个窗口小部件
#     mywin.setWindowTitle('Hello world!') # 设置窗口标题
#     mywin.show() #显示窗口
#     sys.exit(app.exec())

from PyQt5 import QtWidgets, QtCore
import sys
from PyQt5.QtCore import *
import time


# 继承QThread
class Runthread(QtCore.QThread):
    #  通过类成员对象定义信号对象
    _signal = pyqtSignal(str)

    def __init__(self):
        super(Runthread, self).__init__()

    def __del__(self):
        self.wait()

    def run(self):
        for i in range(100):
            time.sleep(0.05)
            self._signal.emit(str(i))  # 注意这里与_signal = pyqtSignal(str)中的类型相同
        self._signal.emit(str(100))


class Example(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        # 按钮初始化
        self.button = QtWidgets.QPushButton('开始', self)
        self.button.setToolTip('这是一个 <b>QPushButton</b> widget')
        self.button.resize(self.button.sizeHint())
        self.button.move(120, 80)
        self.button.clicked.connect(self.start_login)  # 绑定多线程触发事件

        # 进度条设置
        self.pbar = QtWidgets.QProgressBar(self)
        self.pbar.setGeometry(50, 50, 210, 25)
        self.pbar.setValue(0)

        # 窗口初始化
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('OmegaXYZ.com')
        self.show()

        self.thread = None  # 初始化线程

    def start_login(self):
        # 创建线程
        self.button.setEnabled(False)
        self.thread = Runthread()
        # 连接信号
        self.thread._signal.connect(self.call_backlog)  # 进程连接回传到GUI的事件
        # 开始线程
        self.thread.start()

    def call_backlog(self, msg):
        self.pbar.setValue(int(msg))  # 将线程的参数传入进度条
        if msg == '100':
            # self.thread.terminate()
            del self.thread
            self.button.setEnabled(True)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = Example()
    myshow.show()
    sys.exit(app.exec_())


