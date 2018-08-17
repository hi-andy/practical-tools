import os
import re
from urllib.request import unquote

import bs4
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class MP3(object):

    def __init__(self):
        self.domain = 'http://www.ysts8.com'
        self.main_url = 'http://www.ysts8.com/Yshtml/Ys3114.html'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36"
        }

    def get_url(self, in_url):
        response = requests.get(in_url, headers=self.headers)
        soup = bs4.BeautifulSoup(response.text, "html5lib")
        urls = [a.attrs.get('href') for a in soup.select('ul a[href^=/play_]')]
        # 选集
        selected = []
        for url in urls:
            number = re.match('/play_3114_47_1_([\d]{1,3}).html', url)
            if str(number) != 'None':
                if int(number.group(1)) < 208:
                    continue
                selected.append(url)
                # break

        return selected

    def get_file_url(self, in_url):
        in_url = self.domain + in_url

        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get(in_url)
        driver.switch_to.frame('play')

        soup = bs4.BeautifulSoup(driver.page_source, "html5lib")
        url = re.search('src="(.*)"', str(soup.select('audio')))
        if str(url) != 'None':
            url = unquote(url.group(1), encoding='gbk')

        driver.close()
        return url

    def save_file(self, url, file_path='../mp3/'):
        file_name = re.search('.*/([\d]{1,4}).*\.mp3', url)
        if str(file_name) != 'None':
            save_file_name = re.sub('/|\\\\', os.sep, file_path) + file_name.group(1) + '.mp3'
            try:
                if not os.path.exists(file_path):
                    os.makedirs(file_path)

                r = requests.get(url, headers=self.headers)
                with open(save_file_name, "wb") as code:
                    code.write(r.content)

            except IOError as e:
                print('文件操作失败', e)
            except Exception as e:
                print('错误 ：', e)

    def save_file2(self, url, file_name, file_path='../mp3/'):
        save_file_name = re.sub('/|\\\\', os.sep, file_path) + file_name
        try:
            if not os.path.exists(file_path):
                os.makedirs(file_path)

            r = requests.get(url, headers=self.headers)
            with open(save_file_name, "wb") as code:
                code.write(r.content)

        except IOError as e:
            print('文件操作失败', e)
        except Exception as e:
            print('错误 ：', e)


mp3 = MP3()

# 页面搜索链接下载
page_urls = mp3.get_url(mp3.main_url)

for link in page_urls:
    mp3_url = mp3.get_file_url(link)
    mp3.save_file(mp3_url)

# 指定链接下载

# http://pse.ysts8.com:8000/单田芳/单田芳_乱世枭雄485回/001{www.Ysts8.com}.mp3

# for index in range(1, 486):
#     file_name = "%03d" % index
#     save_file_name = "%03d" % index + '.乱世枭雄.mp3'
#     file = 'http://pse.ysts8.com:8000/单田芳/单田芳_乱世枭雄485回/%s{www.Ysts8.com}.mp3' % file_name
#     print(file)
#     mp3.save_file2(file, save_file_name)
#     break
