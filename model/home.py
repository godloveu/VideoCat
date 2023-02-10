from PyQt5.QtCore import QThread, pyqtSignal
import requests
from lib.ip import get_ip
from lib.cookie import get_cookie
from model import file


class homeThread(QThread):
    success = pyqtSignal(str, str)
    error = pyqtSignal(str)
    complete = pyqtSignal(str)
    info = pyqtSignal(str, str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url = None
        self.header = {
            'Cookie': 'FOLLOW_LIVE_POINT_INFO="MS4wLjABAAAAT5wOVe79tIx40ldo2PaHqqH-66yxuWqNiGsMSz5mgkQ/1673107200000/0/0/1673060426718"; FOLLOW_NUMBER_YELLOW_POINT_INFO="MS4wLjABAAAAT5wOVe79tIx40ldo2PaHqqH-66yxuWqNiGsMSz5mgkQ/1673107200000/0/0/1673061026719"; sso_uid_tt=b1b11786c0f5c5ee8d8d3a16692d6ea5; sso_uid_tt_ss=b1b11786c0f5c5ee8d8d3a16692d6ea5; sid_ucp_sso_v1=1.0.0-KGIwYjljZGVmZDAxZjFiY2ZkMmEwNDQyZDFkYTg3NmE3MzU4ODUxOTYKCRDKveOdBhjvMRoCbHEiIDcxOTgzMDM0OTcyNjhiNjlmYjFjOTZiZWI2ZjZjZGE0; ssid_ucp_sso_v1=1.0.0-KGIwYjljZGVmZDAxZjFiY2ZkMmEwNDQyZDFkYTg3NmE3MzU4ODUxOTYKCRDKveOdBhjvMRoCbHEiIDcxOTgzMDM0OTcyNjhiNjlmYjFjOTZiZWI2ZjZjZGE0; odin_tt=8f784d4fb1e8f8cd3b58ff5bcc412994507f9ce4e9d10f0383151ef34e6e73b2; sid_guard=ec3bfe308abd488f3e27cdb91b079e44|1673060042|21600|Sat,+07-Jan-2023+08:54:02+GMT; uid_tt=c476006fd7594a41cf595513929c8c82; uid_tt_ss=c476006fd7594a41cf595513929c8c82; sid_tt=ec3bfe308abd488f3e27cdb91b079e44; sessionid=ec3bfe308abd488f3e27cdb91b079e44; sessionid_ss=ec3bfe308abd488f3e27cdb91b079e44; sid_ucp_v1=1.0.0-KDFiMGY3MDI5MmI5MTQ0ZTk1ZGJkMWY3OWFjZmYxNjg4MTAzYmI4OTEKCBDKveOdBhgNGgJobCIgZWMzYmZlMzA4YWJkNDg4ZjNlMjdjZGI5MWIwNzllNDQ; ssid_ucp_v1=1.0.0-KDFiMGY3MDI5MmI5MTQ0ZTk1ZGJkMWY3OWFjZmYxNjg4MTAzYmI4OTEKCBDKveOdBhgNGgJobCIgZWMzYmZlMzA4YWJkNDg4ZjNlMjdjZGI5MWIwNzllNDQ; tt_scid=dd7v.G5LEvkaIHO8lq90tkTyoGqRh27pf5bOgVkIi5CP4N9gFycZW42gfSUSPdIfb7cb; ttwid=1|bFFMAP1RIMkgAvj58GNyOaAPM3xnddwkom-MWNwwC2k|1673062118|0fd4ec1f30e55739d975b2c5013a1025276788fa591a61ad74829a1e410a8259; home_can_add_dy_2_desktop="0"; passport_csrf_token=2593a6fba303ad735bef3f962244560e; passport_csrf_token_default=2593a6fba303ad735bef3f962244560e; __ac_nonce=063b8e6ed00e207eeb9b0; __ac_signature=_02B4Z6wo00f01mvOFVAAAIDBPkyez.Ku-hZr.hHAAPlatfvLEzr2AXhN1RUYVY6LiDi.l6zoo-OoO3n8mLI2iDg-gBvKY5LOf4hMPi0oAanHNNR0lu.0Ii5l7wUr7Y7QG5Oe3b-XoUUtcOKH10; s_v_web_id=verify_lcldzqr2_ZDYT72jz_rV73_4ZdH_BjPU_CUlkg59oZeV3; _tea_utm_cache_2018=undefined; msToken=EfgMKq-QLdIb53MLVti14xiNvhYTGG0ZnqnKc6ouGdmdSP8CvLVxrFuFjXfqiyx46Sjm16VrccN21lyVSXw7bO83Hj-OnRTYNM8yLe0V_p-4v726qaCYOLA=; msToken=paPLb-LnWiNmmf6xzknLaMidXSOMH0-k668zrBx9VVrn9niC5VtxTxWTkxyQUlQ8eUpYfduIUDOhTfaYFzHEDRy0u3MY_6IwRRI8RNabRcwgpg1_ExhYVsdm-5ZwNbzl',
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

            api = f'https://www.iesdouyin.com/web/api/v2/aweme/post/?reflow_source=reflow_page&sec_uid={self.user_id}&count=21&max_cursor={self.cursor}'
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
