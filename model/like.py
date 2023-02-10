from PyQt5.QtCore import QThread, pyqtSignal
import requests
from lib.ip import get_ip
from lib.cookie import get_cookie
from model import file


class lickThread(QThread):
    success = pyqtSignal(str, str)
    error = pyqtSignal(str)
    complete = pyqtSignal(str)
    info = pyqtSignal(str, str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url = None
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'}
        self.username = None
        self.user_id = None
        self.cursor = 0

    def set_data(self, url):
        self.url = url

    def run(self):
        try:
            # 链接重定向
            self.url = requests.get(self.url, headers=self.header).url
            # 获取用户id
            self.user_id = self.url.split('user/')[1].split('?')[0]
        except Exception as e:
            self.error.emit('链接错误')
            file.log(e)
            return

        # 获取cookie
        self.header['Cookie'] = get_cookie(self.url)
        if self.header['Cookie'] is None:
            self.error.emit('验证失败')
            return
        # 获取代理ip
        ip = get_ip()
        # ip数量
        ip_count = len(ip)
        # ip索引
        ip_index = 0

        error = 0
        cursor = 0

        while True:
            # 代理服务器
            proxies = {
                "HTTP": 'HTTP://' + ip[ip_index],
                "HTTPS": 'HTTPS://' + ip[ip_index]
            }

            api = f'https://www.iesdouyin.com/web/api/v2/aweme/like/?reflow_source=reflow_page&sec_uid={self.user_id}&count=21&max_cursor={self.cursor}'
            try:
                resp = requests.get(api, headers=self.header, proxies=proxies).json()
                error = 0
            except Exception as e:
                if error == 20:
                    self.error.emit('获取失败')
                    file.log(e)
                    return
                ip_index += 1
                error += 1
                if ip_index == ip_count - 1:
                    ip_index = 0
                continue

            try:
                aweme_list = resp['aweme_list']
            except KeyError:
                continue
            for aweme in aweme_list:
                if cursor == 10000:
                    self.complete.emit('最多获取10000条数据')
                    return
                try:
                    video_url = aweme['video']['download_addr']['url_list'][0]
                except KeyError as e:
                    file.log(e)
                    continue
                title = aweme['desc']
                video_url = aweme['video']['play_addr']['url_list'][0]
                if self.username is None:
                    self.username = aweme['author']['nickname']
                    self.info.emit(self.username, '')
                self.success.emit(title, video_url)
                cursor += 1
            # 判断是否还有下一页
            if resp['has_more']:
                self.cursor = resp['max_cursor']
                ip_index += 1
                if ip_index == ip_count - 1:
                    ip_index = 0
            else:
                self.complete.emit('数据获取完成')
                break
