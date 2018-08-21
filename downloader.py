import os
import re
import time

import bs4
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Downloader(object):

    def __init__(self):
        self.domain = 'http://www.woaitingshu.com/'
        self.main_url = 'http://www.woaitingshu.com/mp3/14098.html'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36"
        }

    def get_url(self, in_url):
        response = requests.get(in_url, headers=self.headers)
        soup = bs4.BeautifulSoup(response.text, "html5lib")
        urls = [a.attrs.get('href') for a in soup.select('ul a[href^=/video/14098]')]
        # 选集
        # selected = []
        # for url in urls:
        #     number = re.match('/play_3114_47_1_([\d]{1,3}).html', url)
        #     if str(number) != 'None':
        #         if int(number.group(1)) < 472:
        #             continue
        #         selected.append(url)
        #         # break
        #
        # return selected
        return urls

    def get_file_url(self, in_url):
        in_url = self.domain + in_url
        start = time.time()

        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get(in_url)
        # driver.set_page_load_timeout(30)
        # driver.switch_to.frame('play')
        while True:
            try:
                src = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "audio")))\
                    .get_attribute('src')
            finally:
                if src is None and (start - time.time() > 5):
                    print(start - time.time())
                    driver.refresh()
                else:
                    driver.close()
                    break

        print(src)
        return src

    # 下载文件，指定文件名
    def save_file(self, url, file_name, file_path='../mp3/'):
        full_file_name = re.sub('/|\\\\', os.sep, file_path) + file_name
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        try:
            r = requests.get(url, headers=self.headers)
            with open(full_file_name, "wb") as code:
                code.write(r.content)
        except IOError as e:
            print('文件操作失败', e)
        except Exception as e:
            print('错误 ：', e)

    # 下载文件，从链接查找文件名
    def save_file2(self, url, file_path='../mp3/'):
        file_name = re.search('.*/(.*\.m4a$)', url)
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        if str(file_name) != 'None':
            full_file_name = re.sub('/|\\\\', os.sep, file_path) + file_name.group(1) + '.mp3'
            try:
                r = requests.get(url, headers=self.headers)
                with open(full_file_name, "wb") as code:
                    code.write(r.content)
            except IOError as e:
                print('文件操作失败', e)
            except Exception as e:
                print('错误 ：', e)


downloader = Downloader()

# 页面搜索链接下载
page_urls = downloader.get_url(downloader.main_url)

for index, link in enumerate(page_urls):
    save_file_name = "%03d" % (index + 1) + '.上位.m4a'
    file_url = downloader.get_file_url(link)
    downloader.save_file(file_url, save_file_name)

# 指定链接下载

# http://pse.ysts8.com:8000/单田芳/单田芳_乱世枭雄485回/001{www.Ysts8.com}.mp3

# for index in range(1, 486):
#     file_name = "%03d" % index
#     save_file_name = "%03d" % index + '.乱世枭雄.mp3'
#     file = 'http://pse.ysts8.com:8000/单田芳/单田芳_乱世枭雄485回/%s{www.Ysts8.com}.mp3' % file_name
#     print(file)
#     mp3.save_file(file, save_file_name)
#     break
