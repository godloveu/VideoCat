from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from model.file import *


def get_cookie(url):
    try:
        mobile_emulation = {"deviceName": "iPhone 6/7/8"}
        options = Options()
        options.add_experimental_option("mobileEmulation", mobile_emulation)
        s = Service(executable_path='Chrome/chromedriver.exe')
        # 创建浏览器对象
        browser = webdriver.Chrome(options=options, service=s)

        # 访问网页
        browser.get(url)
        # 获取https://www.douyin.com/的cookie
        while True:
            title = browser.title
            if '抖音' in title:
                break
        cookie = browser.get_cookies()
        # 关闭浏览器
        browser.quit()
        # 将cookie拼接成字符串
        cookie_str = ''
        for i in cookie:
            cookie_str += i['name'] + '=' + i['value'] + ';'
        return cookie_str
    except Exception as e:
        log(e)
        return None
