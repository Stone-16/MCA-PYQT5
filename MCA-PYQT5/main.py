import sys

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout

from ui.mainwindow import Ui_MainWindow

from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
import matplotlib.pyplot as plt


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 初始化放大区
        self.detailLayout = QVBoxLayout(self.detailFrame)
        self.detailPlot = PlotCanvas(self.centralwidget)
        self.detailLayout.addWidget(self.detailPlot)

        # 绑定绘图按钮事件
        self.paintButton.clicked.connect(self.paint_button_clicked)
        self.clearButton.clicked.connect(self.detailPlot.clear)

        # 定义一个定时器
        self.timer = QTimer()
        # 触发事件
        self.timer.timeout.connect(self.addHihgt)

        # 绑定是否定时刷新
        self.timerButton.toggled.connect(self.dynamic_plot)

    def paint_button_clicked(self):
        # 获取用户的输入
        self.detailPlot.period = float(self.periodEdit.text())
        self.detailPlot.hight = float(self.hightEdit.text())
        # 重新绘图
        self.detailPlot.plot()

    def dynamic_plot(self):
        # 通过是否选中定时刷新按钮来决定启动或者停止定时器
        if self.timerButton.isChecked():
            # 触发间隔为500ms
            self.timer.start(500)
        else:
            self.timer.stop()

    def addHihgt(self):
        self.detailPlot.hight += 1
        # 设置显示的幅度
        self.hightEdit.setText(str(self.detailPlot.hight))
        self.detailPlot.plot()


# 在Matplotlib的基础上定义一个绘图类
class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=4, height=4):
        # 正常显示中文
        plt.rcParams['font.family'] = ['SimHei']
        # 正常显示负号
        plt.rcParams['axes.unicode_minus'] = False
        # 设置背景色并初始化
        self.fig = plt.figure(facecolor='#ffffff')
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        self.period = 0.1
        self.hight = 10.0
        self.x = np.arange(512)
        self.y = self.hight * (1 + np.sin(self.x * self.period))

        # 鼠标经过时的响应
        self.fig.canvas.mpl_connect('motion_notify_event', self.motion)
        self.cursor_x = 0

    def plot(self):
        self.clear()
        # 绘图
        self.y = self.hight * (1 + np.sin(self.x * self.period))
        plt.plot(self.x, self.y, 'r')
        # 光标
        self.cursor = plt.axvline(color='skyblue')
        # 鼠标位置显示的文字
        self.text = plt.text(0, 0, '0', fontsize=10)
        self.plot_cursor()
        self.draw()

    def motion(self, event):
        if not event.inaxes:
            return

        x = int(np.round(event.xdata))
        self.cursor_x = x
        self.plot_cursor()
        self.draw()

    def plot_cursor(self):
        self.cursor.set_xdata(self.cursor_x)
        self.text.set_position((self.cursor_x, self.y[self.cursor_x]))
        self.text.set_text('{:.2f}'.format(self.y[self.cursor_x]))

    def clear(self):
        # 清空画布
        plt.clf()
        self.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    styleFile = "./style.qss"
    f = open(styleFile, 'r')
    qssStyle = f.read()
    f.close()
    window.setStyleSheet(qssStyle)
    window.show()
    sys.exit(app.exec_())
