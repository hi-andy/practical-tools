import os
import re
import urllib.request

import bs4
import requests


def get_urls(in_url):
    response = requests.get(in_url)
    soup = bs4.BeautifulSoup(response.text, "html5lib")
    return [img.attrs.get('src') for img in soup.select('div.browse-listing img')]


def save_img(img_url, file_path='book/img'):
    # 获取图片原始文件名
    file_name = re.search('.*/(.*\.(png)|(jpg)|(gif))$', img_url)
    # 处理路径分割符
    file_path = re.sub('/|\\\\', os.sep, file_path)

    if str(file_name) != 'None':
        save_file_name = file_path + '/' + file_name.group(1)
        try:
            if not os.path.exists(file_path):
                os.makedirs(file_path)
            # 下载图片，并保存到文件夹中
            urllib.request.urlretrieve(img_url, save_file_name)
        except IOError as e:
            print('文件操作失败', e)
        except Exception as e:
            print('错误 ：', e)


main_url = 'https://findicons.com/pack/2787/beautiful_flat_icons'

urls = get_urls(main_url)

for url in urls:
    save_img(url)
