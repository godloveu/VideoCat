# VideoCat（视频猫）

## 简介

VideoCat是一款基于Python使用Pyqt5开发的视频爬虫工具，目前仅支持抖音（后续等成熟后再陆续添加其他平台）

由于Python3.10是不支持Windows10以下的系统，所以我们的软件无法在Windows10以下的系统运行。

## 功能

目前支持的功能：爬取抖音 主页、喜欢、合集

## 软件展示

![](https://dav.uoll.cn/d/%E9%98%BF%E9%87%8C%E4%BA%91/Blog/%E8%BD%AF%E4%BB%B6%E6%94%B6%E8%97%8F/Windows/%E5%9B%BE%E7%89%87/81Q6%5DKDDCIYG6PV5LKQX5K7.png?sign=RLqG62rSpIcHd_BxcEh2jGCtMmX8q8OoRH5X74cAOds=:0)

![](?sign=33dLcXl0QpvCJc-NjjeQcuB2Ohb949FuwJUQgJrf_l8=:0)

## 教程

### 获取链接

#### 1.获取主页和喜欢链接

(电脑用户可以直接使用网页版用户主页上方的链接)

![](?sign=8gVkR4Mcdgw-wDQGUITnBDCrnnlF-CL_2uwzSXWgdKU=:0)

#### 2.获取合集链接

（只能通过手机获取）

![](?sign=Z6gOPc0Nf6Q9O096q7AVNqLgQBa3sD6MiC0DiJv1Ejo=:0)



### 获取数据

#### 1.获取主页和喜欢数据

主页和喜欢数据获取的链接都是用户主页的，软件不对链接进行正则处理所以粘贴时不要带有链接以外的内容。

点击获取数据后会弹出浏览器进行滑块验证，验证完毕后不要自己手动去关闭浏览器软件会自行关闭（自行关闭会导致数据获取失败）

浏览器自动关闭后等待几秒钟数据才会开始获取。

#### 2.获取合集数据

合集链接只能通过手机软件内获取，软件不对链接进行正则处理所以粘贴时不要带有链接以外的内容。

点击后不需要进行滑块验证直接等待数据获取完毕即可



### 视频下载

不管是单个下载还是全部下载都请先等待数据全部获取完毕否则出现任何问题不予处理。
如果下载闪退的请使用管理员身份运行软件



## 软件下载

点此下载: [VideoCat](https://dav.uoll.cn/d/%E9%98%BF%E9%87%8C%E4%BA%91/Blog/%E8%BD%AF%E4%BB%B6%E6%94%B6%E8%97%8F/Windows/%E7%A8%8B%E5%BA%8F/VideoCat%20install.exe?sign=el8ZZ8CZhxgBXdTDBQIOTLkTBfUNGis2mrgIsD52pAc=:0)

## 更新说明

#### 2023-01-10 15:43

修复所有功能恢复数据获取

优化下载速度去除进度条，解决部分卡死闪退问题

限制每次数据最多获取一万条（避免数据过多软件卡死）
