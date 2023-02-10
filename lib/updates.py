import requests


def updates():
    Vesrion = '1.0.2'  # 当前版本
    url = 'https://tools.uoll.cn/data.json'
    response = requests.get(url).json()
    new_version = response['Version']
    if new_version > Vesrion:
        return True
    else:
        return False
