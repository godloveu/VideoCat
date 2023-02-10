import os
import json
import time


# 获取存储路径
def get_path():
    # 读取confing.json
    with open('config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)
    return config['save_path']


# 创建文件
def create_file():
    path = get_path()
    # 判断主页文件夹是否存在
    if not os.path.exists(f'{path}/主页'):
        os.mkdir(f'{path}/主页')
    # 判断喜欢文件夹是否存在
    if not os.path.exists(f'{path}/喜欢'):
        os.mkdir(f'{path}/喜欢')
    # 判断合集文件夹是否存在
    if not os.path.exists(f'{path}/合集'):
        os.mkdir(f'{path}/合集')


# 创建日志
def log(e):
    # 读取confing.json
    with open('config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)
    # 判断日志写入是否开启
    if not config['log_switch']:
        return
    # 判断文件夹是否存在
    if not os.path.exists(f'Log'):
        os.mkdir(f'Log')

    # 获取当前时间精确到日
    file_name = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    log_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    # 日志格式
    log_format = f'===================={log_time}====================\n' \
                 f'{e}\n'

    # 写入日志
    with open(f'Log/{file_name}.log', 'a', encoding='utf-8') as f:
        f.write(log_format)

