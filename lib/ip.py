import requests
from model.file import *


def get_ip():
    # 打开ip池文件
    url = 'https://tools.uoll.cn/ip.txt'
    # 读取ip池文件
    try:
        ip_pool = requests.get(url).text
        # 将ip池文件转换为列表
        ip = ip_pool.split('\n')
        return ip
    except Exception as e:
        log(e)
