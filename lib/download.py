import requests
from PyQt5.QtCore import QThread, pyqtSignal, QMutex
from model.file import *

qm = QMutex()


class downloadThread(QThread):
    success = pyqtSignal(int)
    error = pyqtSignal(int)
    wait = pyqtSignal(int)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.video_url = None
        self.video_collection = None
        self.video_type = None
        self.video_user = None
        self.title = None
        self.id = None

        self.headers ={
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
        }

    def set_data(self, data):
        self.id = data['id']
        self.title = self.replace(data['title'])
        self.video_url = data['video_url']
        self.video_user = data['video_user']
        self.video_type = data['video_type']
        self.video_collection = data['video_collection']

        # 特殊字符处理

    @staticmethod
    def replace(title):
        title = title.replace('\\', '')
        title = title.replace('/', '')
        title = title.replace(':', '')
        title = title.replace('*', '')
        title = title.replace('?', '')
        title = title.replace('"', '')
        title = title.replace('<', '')
        title = title.replace('>', '')
        title = title.replace('|', '')
        title = title.replace('\n', '')
        return title

    def run(self):
        # 线程锁
        qm.lock()
        self.wait.emit(self.id)
        # 检查保存文件夹是否存在
        create_file()
        # 获取保存路径
        path = get_path()
        if self.video_type == '主页':
            title = f'【{self.id + 1}】 {self.title}'
            path = f'{path}/{self.video_type}/{self.video_user}'
            # 判断文件夹是否存在
            if not os.path.exists(path):
                os.makedirs(path)
        if self.video_type == '喜欢':
            title = f'【{self.id + 1}】 {self.title}'
            path = f'{path}/{self.video_type}/{self.video_user}'
            # 判断文件夹是否存在
            if not os.path.exists(path):
                os.makedirs(path)
        if self.video_type == '合集':
            title = f'【第{self.id + 1}集】 {self.title}'
            path = f'{path}/{self.video_type}/{self.video_user}/{self.video_collection}'
            # 判断文件夹是否存在
            if not os.path.exists(path):
                os.makedirs(path)

        # 下载视频
        try:
            response = requests.get(self.video_url, headers=self.headers)
            with open(f'{path}/{title}.mp4', 'wb') as f:
                f.write(response.content)
            self.success.emit(self.id)
        except Exception as e:
            self.error.emit(self.id)
            log(e)
        # 线程解锁
        qm.unlock()







