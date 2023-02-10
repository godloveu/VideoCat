# 基于main设置无边框拖动
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
# from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAbstractItemView, QFrame, QHeaderView, QMessageBox

from VideoUi import *


class HeadWindow(Ui_VideoCat):
    def __init__(self):
        super().__init__()
        self.m_Position = None
        self.m_flag = None
        self.ui = Ui_VideoCat()
        self.ui.setupUi(self)
        # 主窗口设置
        # 窗口图标
        self.setWindowIcon(QIcon('logo.ico'))
        self.setWindowFlags(Qt.FramelessWindowHint)  # 隐藏边框
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.btn_click()
        self.table_style()
        self.ui.label_24.hide()
        self.ui.label_25.hide()

        # 编辑框禁止输入
        self.ui.lineEdit_6.setReadOnly(True)

    def btn_click(self):
        self.ui.pushButton.clicked.connect(self.page_1)
        self.ui.pushButton_2.clicked.connect(self.page_2)
        self.ui.pushButton_3.clicked.connect(self.page_3)
        self.ui.pushButton_4.clicked.connect(self.page_4)
        self.ui.pushButton_5.clicked.connect(self.page_5)

    def page_1(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.pushButton.setStyleSheet(
            '#pushButton{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}'
            '#pushButton:hover{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}'
            '#pushButton:pressed{padding-left:5px;padding-top:5px;}'
            '#pushButton:focus{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}')
        self.ui.pushButton_2.setStyleSheet(
            '#pushButton_2{border:none;color: rgb(255, 255, 255);font: 18pt "华文行楷";}'
            '#pushButton_2:hover{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}'
            '#pushButton_2:pressed{padding-left:5px;padding-top:5px;}'
            '#pushButton_2:focus{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}')
        self.ui.pushButton_3.setStyleSheet(
            '#pushButton_3{border:none;color: rgb(255, 255, 255);font: 18pt "华文行楷";}'
            '#pushButton_3:hover{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}'
            '#pushButton_3:pressed{padding-left:5px;padding-top:5px;}'
            '#pushButton_3:focus{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}')
        self.ui.pushButton_4.setStyleSheet(
            '#pushButton_4{border:none;color: rgb(255, 255, 255);font: 18pt "华文行楷";}'
            '#pushButton_4:hover{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}'
            '#pushButton_4:pressed{padding-left:5px;padding-top:5px;}'
            '#pushButton_4:focus{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}')
        self.ui.pushButton_5.setStyleSheet(
            '#pushButton_5{border:none;color: rgb(255, 255, 255);font: 18pt "华文行楷";}'
            '#pushButton_5:hover{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}'
            '#pushButton_5:pressed{padding-left:5px;padding-top:5px;}'
            '#pushButton_5:focus{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}')

    def page_2(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.pushButton.setStyleSheet(
            '#pushButton{border:none;color: rgb(255, 255, 255);font: 18pt "华文行楷";}'
            '#pushButton:hover{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}'
            '#pushButton:pressed{padding-left:5px;padding-top:5px;}'
            '#pushButton:focus{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}')
        self.ui.pushButton_2.setStyleSheet(
            '#pushButton_2{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}'
            '#pushButton_2:hover{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}'
            '#pushButton_2:pressed{padding-left:5px;padding-top:5px;}'
            '#pushButton_2:focus{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}')
        self.ui.pushButton_3.setStyleSheet(
            '#pushButton_3{border:none;color: rgb(255, 255, 255);font: 18pt "华文行楷";}'
            '#pushButton_3:hover{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}'
            '#pushButton_3:pressed{padding-left:5px;padding-top:5px;}'
            '#pushButton_3:focus{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}')
        self.ui.pushButton_4.setStyleSheet(
            '#pushButton_4{border:none;color: rgb(255, 255, 255);font: 18pt "华文行楷";}'
            '#pushButton_4:hover{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}'
            '#pushButton_4:pressed{padding-left:5px;padding-top:5px;}'
            '#pushButton_4:focus{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}')
        self.ui.pushButton_5.setStyleSheet(
            '#pushButton_5{border:none;color: rgb(255, 255, 255);font: 18pt "华文行楷";}'
            '#pushButton_5:hover{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}'
            '#pushButton_5:pressed{padding-left:5px;padding-top:5px;}'
            '#pushButton_5:focus{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}')

    def page_3(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.pushButton.setStyleSheet(
            '#pushButton{border:none;color: rgb(255, 255, 255);font: 18pt "华文行楷";}'
            '#pushButton:hover{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}'
            '#pushButton:pressed{padding-left:5px;padding-top:5px;}'
            '#pushButton:focus{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}')
        self.ui.pushButton_2.setStyleSheet(
            '#pushButton_2{border:none;color: rgb(255, 255, 255);font: 18pt "华文行楷";}'
            '#pushButton_2:hover{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}'
            '#pushButton_2:pressed{padding-left:5px;padding-top:5px;}'
            '#pushButton_2:focus{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}')
        self.ui.pushButton_3.setStyleSheet(
            '#pushButton_3{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}'
            '#pushButton_3:hover{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}'
            '#pushButton_3:pressed{padding-left:5px;padding-top:5px;}'
            '#pushButton_3:focus{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}')
        self.ui.pushButton_4.setStyleSheet(
            '#pushButton_4{border:none;color: rgb(255, 255, 255);font: 18pt "华文行楷";}'
            '#pushButton_4:hover{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}'
            '#pushButton_4:pressed{padding-left:5px;padding-top:5px;}'
            '#pushButton_4:focus{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}')
        self.ui.pushButton_5.setStyleSheet(
            '#pushButton_5{border:none;color: rgb(255, 255, 255);font: 18pt "华文行楷";}'
            '#pushButton_5:hover{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}'
            '#pushButton_5:pressed{padding-left:5px;padding-top:5px;}'
            '#pushButton_5:focus{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}')

    def page_4(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        self.ui.pushButton.setStyleSheet(
            '#pushButton{border:none;color: rgb(255, 255, 255);font: 18pt "华文行楷";}'
            '#pushButton:hover{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}'
            '#pushButton:pressed{padding-left:5px;padding-top:5px;}'
            '#pushButton:focus{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}')
        self.ui.pushButton_2.setStyleSheet(
            '#pushButton_2{border:none;color: rgb(255, 255, 255);font: 18pt "华文行楷";}'
            '#pushButton_2:hover{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}'
            '#pushButton_2:pressed{padding-left:5px;padding-top:5px;}'
            '#pushButton_2:focus{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}')
        self.ui.pushButton_3.setStyleSheet(
            '#pushButton_3{border:none;color: rgb(255, 255, 255);font: 18pt "华文行楷";}'
            '#pushButton_3:hover{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}'
            '#pushButton_3:pressed{padding-left:5px;padding-top:5px;}'
            '#pushButton_3:focus{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}')
        self.ui.pushButton_4.setStyleSheet(
            '#pushButton_4{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}'
            '#pushButton_4:hover{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}'
            '#pushButton_4:pressed{padding-left:5px;padding-top:5px;}'
            '#pushButton_4:focus{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}')
        self.ui.pushButton_5.setStyleSheet(
            '#pushButton_5{border:none;color: rgb(255, 255, 255);font: 18pt "华文行楷";}'
            '#pushButton_5:hover{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}'
            '#pushButton_5:pressed{padding-left:5px;padding-top:5px;}'
            '#pushButton_5:focus{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}')

    def page_5(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        self.ui.pushButton.setStyleSheet(
            '#pushButton{border:none;color: rgb(255, 255, 255);font: 18pt "华文行楷";}'
            '#pushButton:hover{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}'
            '#pushButton:pressed{padding-left:5px;padding-top:5px;}'
            '#pushButton:focus{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}')
        self.ui.pushButton_2.setStyleSheet(
            '#pushButton_2{border:none;color: rgb(255, 255, 255);font: 18pt "华文行楷";}'
            '#pushButton_2:hover{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}'
            '#pushButton_2:pressed{padding-left:5px;padding-top:5px;}'
            '#pushButton_2:focus{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}')
        self.ui.pushButton_3.setStyleSheet(
            '#pushButton_3{border:none;color: rgb(255, 255, 255);font: 18pt "华文行楷";}'
            '#pushButton_3:hover{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}'
            '#pushButton_3:pressed{padding-left:5px;padding-top:5px;}'
            '#pushButton_3:focus{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}')
        self.ui.pushButton_4.setStyleSheet(
            '#pushButton_4{border:none;color: rgb(255, 255, 255);font: 18pt "华文行楷";}'
            '#pushButton_4:hover{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}'
            '#pushButton_4:pressed{padding-left:5px;padding-top:5px;}'
            '#pushButton_4:focus{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}')
        self.ui.pushButton_5.setStyleSheet(
            '#pushButton_5{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}'
            '#pushButton_5:hover{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}'
            '#pushButton_5:pressed{padding-left:5px;padding-top:5px;}'
            '#pushButton_5:focus{border:none;color: rgb(85, 85, 255);font: 18pt "华文行楷";background-color: rgb(255, 255, 255);border-radius:20px;}')

    # 无窗口边框拖动
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(Qt.OpenHandCursor)

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(Qt.ArrowCursor)

    # 表格样式
    def table_style(self):
        # 表格设置
        self.ui.tableWidget.setColumnWidth(0, 50)
        self.ui.tableWidget.setColumnWidth(1, 250)
        self.ui.tableWidget.setColumnWidth(2, 250)
        self.ui.tableWidget.setColumnWidth(3, 150)
        self.ui.tableWidget.setColumnWidth(4, 100)
        # 表格头高度
        self.ui.tableWidget.horizontalHeader().setFixedHeight(40)
        # 表格禁止选中
        self.ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 表格禁止编辑
        self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 表格禁止全选
        self.ui.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        # 表格禁止改变行列大小
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        # 关闭选中虚线框
        self.ui.tableWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        # 关闭表头分割线
        self.ui.tableWidget.horizontalHeader().setStyleSheet("QHeaderView::section{border:0px;}")
        # 表头最后一列自动填充
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
        # 表格圆角
        self.ui.tableWidget.setFrameShape(QFrame.NoFrame)
        # 关闭表格左边编号
        self.ui.tableWidget.verticalHeader().setVisible(False)
