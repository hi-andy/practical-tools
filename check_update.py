#!/usr/bin/env python3
import json
import os
import re
import time

import bs4
import requests


# 显示进度下载
def downloader(url, path):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }

    start = time.time()
    size = 0
    response = requests.get(url, stream=True, headers=headers)
    chunk_size = 1024
    content_size = int(response.headers['content-length'])

    if response.status_code == 200:
        ('文件大小：%0.2f MB' % (content_size / chunk_size / 1024))
        with open(path, 'wb') as file:
            for data in response.iter_content(chunk_size=chunk_size):
                file.write(data)
                size += len(data)

                print(
                    '\r' + '下载进度: %s %.2f%%' % ('#' * int(size * 50 / content_size), float(size / content_size * 100)),
                    end='')

    end = time.time()
    print('\n' + '下载完成！用时%.2f秒' % (end - start))


# json 文件读写
def jsonRW(file_path, in_data):
    if os.path.isfile(file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                for i in in_data:
                    data[i] = in_data[i]

            with open(file_path, 'w') as file:
                json.dump(data, file, ensure_ascii=False)
                file.write('\n')
        except Exception as e:  # 读取异常，重建文件。
            with open(file_path, 'w') as file:
                json.dump(in_data, file, ensure_ascii=False)
                file.write('\n')
    else:
        with open(file_path, 'w') as file:
            json.dump(in_data, file, ensure_ascii=False)
            file.write('\n')


# 可将脚本放入环境变量，故在执行脚本外层目录存放数据
file_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + os.sep
data_file = file_dir + 'data/data.json'
version = {}

if os.path.isfile(data_file):
    with open(data_file, 'r') as f:
        try:
            version = json.load(f)
        except Exception as e:
            version['kindle_version'] = '0'
else:
    if not os.path.exists(file_dir):
        os.mkdir(file_dir)
    version['kindle_version'] = '0'

# 检查 Kindle 软件更新 URL
url = 'https://www.amazon.cn/gp/help/customer/display.html?nodeId=201756220'

response = requests.get(url)
# m = re.search('"(https.*\.bin)".*?下载软件更新([\d\.\d\.?]{3,11})', response.text) # 旧的匹配方式
soup = bs4.BeautifulSoup(response.text, "html5lib")
url = soup.select('a[href^=https://s3.amazonaws.com/firmwaredownloads/]')[0].attrs.get('href')
m = re.search('([\d\.\d\.?]{3,11})(\.bin)', url)

if str(m) != 'None':
    new_ver = m.group(1)
    if new_ver != version['kindle_version']:
        action = input('There is a new version: ' + version[
            'kindle_version'] + ' => ' + new_ver + ' \nNeed to mark updated. please input "M" OR download "Y" :')
        version['kindle_version'] = new_ver
        if action == 'M':
            jsonRW(data_file, version)
            print('Mark updated.')
        elif action == 'Y':
            # 下载更新文件……
            name = re.search('.*/(.*?\.bin)$', url)
            downloader(url, file_dir + str(name.group(1)))
            jsonRW(data_file, version)
            print('File downloaded.')
    else:
        print('No new version.')
else:
    print('Error: No data detected!')
