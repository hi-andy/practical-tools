import os
import re
from urllib.request import unquote

import bs4
import requests


class MP3(object):

    def __init__(self):
        self.domain = 'http://www.ysts8.com'
        self.main_url = 'http://www.ysts8.com/Yshtml/Ys4049.html'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36"
        }

    def get_url(self, in_url):
        response = requests.get(in_url, headers=self.headers)
        soup = bs4.BeautifulSoup(response.text, "html5lib")
        urls = [a.attrs.get('href') for a in soup.select('ul a[href^=/play_4049]')]
        # 选集
        selected = []
        for url in urls:
            number = re.match('.*_([0-9]{3,4})\.html', url)
            if str(number) != 'None':
                if int(number.group(1)) < 901:
                    continue
                selected.append(url)
                break

        return selected

    # http://180h.ysts8.com:8000/官场商战/官途/官途955.mp3
    def get_file_url(self, in_url):
        in_url = self.domain + in_url
        response = requests.get(in_url, headers=self.headers)
        soup = bs4.BeautifulSoup(response.text, "html5lib")
        url = re.search('url=(.*)&amp;?jiidx', str(soup.select('iframe')))
        if str(url) != 'None':
            url = unquote(url.group(1), encoding='gbk')
        return url

    def save_file(self, url, file_path='mp3'):
        file_url = 'http://180h.ysts8.com:8000/' + url
        file_name = re.search('.*/(.*\.mp3$)', url)
        if str(file_name) != 'None':
            save_file_name = re.sub('/|\\\\', os.sep, file_path) + '/' + file_name.group(1)
            try:
                if not os.path.exists(file_path):
                    os.makedirs(file_path)

                r = requests.get(file_url)
                with open(save_file_name, "wb") as code:
                    code.write(r.content)

            except IOError as e:
                print('文件操作失败', e)
            except Exception as e:
                print('错误 ：', e)


mp3 = MP3()
page_urls = mp3.get_url(mp3.main_url)
for link in page_urls:
    mp3_url = mp3.get_file_url(link)
    mp3.save_file(mp3_url)

# for index in range(1004, 1015):
# file = 'http://180h.ysts8.com:8000/官场商战/官途/官途%d.mp3' % index
# mp3.save_file(file)
