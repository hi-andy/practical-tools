import os
import re
import urllib.request

import bs4
import requests

headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36"
        }

def get_url(in_url):
    response = requests.get(in_url)
    soup = bs4.BeautifulSoup(response.text, "html5lib")
    return [img.attrs.get('src') for img in soup.select('div.browse-listing img')]


def get_url2(in_url):
    try:
        response = requests.get(in_url, headers=headers)
        print(response.text)
        soup = bs4.BeautifulSoup(response.text, "html5lib")
        urls = [img for img in soup.select('div._wy _2j _wz img')]
        return urls
    except requests.exceptions.ConnectionError:
        requests.status_code = "Connection refused"


def save_img(img_url, file_path='images/'):
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


main_url = 'https://www.pinterest.com/pin/511088257683635896/'

urls = get_url2(main_url)

print(urls)
# for url in urls:
#     save_img(url)
