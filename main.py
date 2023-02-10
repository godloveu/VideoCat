import sys

from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMainWindow
from PyQt5.QtWidgets import QFileDialog
from head import *
from update import *
from model.like import *
from model.home import *
from model.collection import *
from lib.download import *
from lib.updates import *
import json


class MainWindow(QWidget, HeadWindow):

    def __init__(self):
        super().__init__()
        '''主页'''
        # 按钮点击事件
        self.ui.pushButton_8.clicked.connect(self.getClick)  # 获取数据
        self.ui.pushButton_9.clicked.connect(self.download_all)  # 全部下载

        '''设置页面'''
        self.log_switch()
        self.save_path()

    # getData
    def getClick(self):
        # 初始化数据
        self.initData()
        # 获取选择框选中的数据
        getSelect = self.ui.comboBox.currentText()
        # 获取输入框的数据
        getEdit = self.ui.lineEdit.text()

        # 判断输入框是否为空
        if getEdit == '':
            QMessageBox.information(self, '提示', '分享链接不能为空')
            return
        # 设置类型
        self.ui.label_17.setText(getSelect)
        # 判断类型
        if getSelect == '主页':
            self.getHome(getEdit)
        elif getSelect == '喜欢':
            self.getLike(getEdit)
        elif getSelect == '合集':
            self.getCollection(getEdit)

    # 获取主页数据
    def getHome(self, url):
        threads = homeThread(self)
        threads.set_data(url)
        threads.info.connect(self.add_info)
        threads.success.connect(self.table_add_success)
        threads.error.connect(self.table_add_fail)
        threads.complete.connect(self.table_add_complete)
        threads.start()

    # 获取喜欢数据
    def getLike(self, url):
        # 开启线程
        threads = lickThread(self)
        threads.set_data(url)
        threads.info.connect(self.add_info)
        threads.success.connect(self.table_add_success)
        threads.error.connect(self.table_add_fail)
        threads.complete.connect(self.table_add_complete)
        threads.start()

    # 获取合集数据
    def getCollection(self, url):
        self.ui.label_24.show()
        self.ui.label_25.show()
        # 开启线程
        threads = collectionThread(self)
        threads.set_data(url)
        threads.info.connect(self.add_info)
        threads.success.connect(self.table_add_success)
        threads.error.connect(self.table_add_fail)
        threads.complete.connect(self.table_add_complete)
        threads.start()

    # 用户信息
    def add_info(self, name, collection):
        self.ui.label_7.setText(name)
        self.ui.label_25.setText(collection)

    # 添加数据
    def table_add_success(self, title, url):
        # 获取行数
        table_count = self.ui.tableWidget.rowCount()
        # 添加行
        self.ui.tableWidget.insertRow(table_count)
        # 创建下载按钮
        button = QtWidgets.QPushButton()
        button.setText("下载")
        button.setFixedSize(50, 20)
        # 设置左边外边距
        button.setStyleSheet(
            'QPushButton{background-color:rgb(85, 85, 255);color:rgb(255, 255, 255);border-radius:5px;}'
            'QPushButton:pressed{padding-left:2.5px;padding-top:2.5px;}')
        # 按钮点击事件
        # 输出当前行数
        button.clicked.connect(lambda: self.download(table_count))

        # 添加数据
        self.ui.tableWidget.setItem(table_count, 0, QTableWidgetItem(str(table_count + 1)))  # 序号
        self.ui.tableWidget.item(table_count, 0).setTextAlignment(Qt.AlignCenter)
        self.ui.tableWidget.setItem(table_count, 1, QTableWidgetItem(title))  # 标题
        self.ui.tableWidget.item(table_count, 1).setTextAlignment(Qt.AlignCenter)
        self.ui.tableWidget.setItem(table_count, 2, QTableWidgetItem(url))  # 链接
        self.ui.tableWidget.item(table_count, 2).setTextAlignment(Qt.AlignCenter)
        self.ui.tableWidget.setItem(table_count, 3, QTableWidgetItem('等待下载'))  # 链接
        self.ui.tableWidget.item(table_count, 3).setTextAlignment(Qt.AlignCenter)

        # 居中放置 按钮
        self.ui.tableWidget.setCellWidget(table_count, 4, QtWidgets.QWidget())  # 创建一个空的widget
        self.ui.tableWidget.cellWidget(table_count, 4).setLayout(QtWidgets.QHBoxLayout())  # 设置空的widget的布局为水平布局
        self.ui.tableWidget.cellWidget(table_count, 4).layout().addWidget(button)  # 将按钮放入水平布局中
        self.ui.tableWidget.cellWidget(table_count, 4).layout().setAlignment(QtCore.Qt.AlignCenter)  # 设置按钮居中

        # 更新视频数量
        self.ui.label_19.setText(str(table_count + 1))

    # 数据获取失败
    def table_add_fail(self, txt):
        QMessageBox.information(self, '提示', txt)

    # 数据获取完成
    def table_add_complete(self, txt):
        QMessageBox.information(self, '提示', txt)

    # 初始化数据
    def initData(self):
        self.ui.label_7.setText('未获取')
        self.ui.label_17.setText('未获取')
        self.ui.label_25.setText('未获取')
        self.ui.label_19.setText('0')
        self.ui.label_21.setText('0')
        self.ui.label_23.setText('0')
        self.success = 0
        self.fail = 0
        # 请空表格
        self.ui.tableWidget.setRowCount(0)
        self.collection = None

        self.ui.label_24.hide()
        self.ui.label_25.hide()

    # 下载视频
    def download(self, table_count):
        id = table_count  # 数据行数
        title = self.ui.tableWidget.item(id, 1).text()  # 视频标题
        url = self.ui.tableWidget.item(id, 2).text()  # 视频链接

        video_user = self.ui.label_7.text()  # 用户名
        video_type = self.ui.label_17.text()  # 视频类型
        video_collection = self.ui.label_25.text()  # 合集名称

        data = {
            'id': id,
            'title': title,
            'video_url': url,
            'video_user': video_user,
            'video_type': video_type,
            'video_collection': video_collection
        }

        # 更新状态
        self.ui.tableWidget.setItem(id, 3, QTableWidgetItem('排队下载'))
        self.ui.tableWidget.item(id, 3).setTextAlignment(Qt.AlignCenter)
        # 开启线程
        threads = downloadThread(self)
        threads.set_data(data)
        threads.wait.connect(self.download_wait)
        threads.success.connect(self.download_success)
        threads.error.connect(self.download_error)
        threads.start()

    # 全部下载
    def download_all(self):
        # 获取行数
        table_count = self.ui.tableWidget.rowCount()
        if table_count == 0:
            QMessageBox.information(self, '提示', '请先获取数据')
            return
        else:
            for i in range(table_count):
                self.download(i)

    # 等待下载
    def download_wait(self, id):
        # 更新状态
        self.ui.tableWidget.setItem(id, 3, QTableWidgetItem('正在下载'))
        # 设置样式
        self.ui.tableWidget.item(id, 3).setTextAlignment(Qt.AlignCenter)
        self.ui.tableWidget.item(id, 3).setForeground(QBrush(QColor(85, 85, 255)))

    # 下载成功
    def download_success(self, id):
        # 更新状态
        self.ui.tableWidget.setItem(id, 3, QTableWidgetItem('下载成功'))
        # 设置样式
        self.ui.tableWidget.item(id, 3).setTextAlignment(Qt.AlignCenter)
        self.ui.tableWidget.item(id, 3).setForeground(QBrush(QColor(0, 255, 0)))
        self.success += 1
        self.ui.label_21.setText(str(self.success))

    # 下载失败
    def download_error(self, id):
        self.ui.tableWidget.setItem(id, 3, QTableWidgetItem('下载失败'))
        # 设置样式
        self.ui.tableWidget.item(id, 3).setTextAlignment(Qt.AlignCenter)
        self.ui.tableWidget.item(id, 3).setForeground(QBrush(QColor(255, 0, 0)))
        self.fail += 1
        self.ui.label_23.setText(str(self.fail))

    '''以下为设置页面配置'''

    # 日志开关
    def log_switch(self):
        self.log_switch_show()

    # 日志开关显示
    def log_switch_show(self):
        # 读取config.json
        with open('config.json', 'r', encoding='utf-8') as f:
            config = json.load(f)
        if config['log_switch']:
            self.ui.pushButton_19.show()
            self.ui.pushButton_20.hide()
        else:
            self.ui.pushButton_19.hide()
            self.ui.pushButton_20.show()

        # 按钮点击事件
        self.ui.pushButton_19.clicked.connect(lambda: self.log_close(config))
        self.ui.pushButton_20.clicked.connect(lambda: self.log_open(config))

    # 开启日志
    def log_open(self, config):
        config['log_switch'] = True
        with open('config.json', 'w', encoding='utf-8') as f:
            json.dump(config, f)
        self.log_switch_show()

    # 关闭日志
    def log_close(self, config):
        config['log_switch'] = False
        with open('config.json', 'w', encoding='utf-8') as f:
            json.dump(config, f)
        self.log_switch_show()

    def save_path(self):
        # 读取config.json
        with open('config.json', 'r', encoding='utf-8') as f:
            config = json.load(f)
        # 文本框显示
        if config['save_path'] == 'Download':
            # 设置内容为空
            self.ui.lineEdit_6.setText('')
        else:
            self.ui.lineEdit_6.setText(config['save_path'])

        # 按钮点击事件
        self.ui.pushButton_21.clicked.connect(lambda: self.save_path_set(config))

    # 保存路径设置
    def save_path_set(self, config):
        # 选择目录
        path = QFileDialog.getExistingDirectory(self, '选择保存路径', './')
        if path:
            config['save_path'] = path
            with open('config.json', 'w', encoding='utf-8') as f:
                json.dump(config, f)
            self.save_path()


class UpdateWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.m_Position = None
        self.m_flag = None
        self.ui = Ui_updete()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明

        # 检查配置
        url = 'https://tools.uoll.cn/data.json'
        data = requests.get(url).json()
        # 更新按钮
        self.ui.pushButton_2.clicked.connect(lambda: os.system('start ' + data['url']))
        # 更新内容
        self.ui.label_3.setText(data['content'])

    # 拖动
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))

    def mouseMoveEvent(self, QMouseEvent):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    if updates():
        window = UpdateWindow()
    else:
        window = MainWindow()
    window.show()
    app.exec()
