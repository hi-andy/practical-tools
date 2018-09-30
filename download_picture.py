import os
import random
import re
import time
import urllib.request

import bs4
import requests


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


def get_url3(in_url):
    response = requests.get(in_url)
    print(response.text)
    exit()
    soup = bs4.BeautifulSoup(response.text, "html5lib")
    urls = [img for img in soup.select('div._wy _2j _wz img')]
    return urls


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



# main_url = 'https://www.pinterest.com/resource/NewsHubBadgeResource/get/?source_url=/pin/149533650101648463/&data={"options":{},"context":{}}&_=1530070457495/'
# main_url = 'https://www.google.com/'
# main_url = 'https://www.baidu.com/'


user_agents = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20130406 Firefox/23.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533+(KHTML, like Gecko) Element Browser 5.0',
    'IBM WebExplorer /v0.94',
    'Galaxy/1.0 [en] (Mac OS X 10.5.6; U; en)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14',
    'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko)'
    'Version/6.0 Mobile/10A5355d Safari/8536.25',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko)'
    'Chrome/28.0.1468.0 Safari/537.36',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; TheWorld)']


# main_url = 'https://www.pinterest.com/'
main_url = 'https://www.pinterest.com/pin/511088257683635896'
# main_url = 'https://www.pinterest.com/resource/NewsHubBadgeResource/get/?source_url=%2Fpin%2F149533650101648463%2F&data=%7B%22options%22%3A%7B%7D%2C%22context%22%3A%7B%7D%7D&_=1530070457495'

# for ua in user_agents:
#     print(ua)
#
#
# exit()

head = {
    "Accept": "application/json, text/javascript, */*, q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Cookie": "G_ENABLED_IDPS=google; _b=\"ATXnrb2fnNJNDIJYrcejJ03r6OBrSrRtfPl2BYaeJAaa6eEAzs4Wzg46Iv20mck9Jg8=\"; _auth=1; csrftoken=yAWQ9QVmYn5UIO4mSc0lPr97fP5RAYNy; bei=false; cm_sub=denied; _pinterest_sess=\"TWc9PSYrZTJOb2YycVF1MFJka0RKZTVPR1BkTVJrNHVHSDZFSFplY0tBVlpDVHRGS21oV05BMzYxYXZ2ZlVGaVhzbFcvTlI4UjBDTWpkM3lFeG9RN0xod0ZqTnNmZDhhS29hR3BUYnVzd0JxM2ltdUJ4ZWhUOStDNGZyeGIraWY4V0hsdmE3Mkp6MmtCWVB5ajhEdmVoMi93WXhCRmRzRHdKR0NhaTQ2VGZCUFEwWWllUDg4L1BmSjRtRkRoS1R0bVovQ0hUNFBoQ0ZrQXBKWmRqd3U1QkowempNM1o2a3JZa2lXaDNCNGJ4eVloV1JEWUNlZmpONU1FM0J2VXVqU0NEV0IvSVEwdW10K1FqeE9vTnpOZ1VLM0l4eGI5aFJDMUZQYW00eDRyNS9OSThpUk5heFVnMzgyaFpDS2NDUTFUVS9rWTdkdmlGeFZMQWM5TFRONnRZcTBaQU1qUS9aaDlkZUNZMmIxd2czQktGTTZ1R1ptOWtYb0o5MXdkamdSd0ZDZUo2Z1U3K2c2eXdheTlwODhEZVBVbkFyN1RsMzBlSDF2anJMemZ5ZmpWK2Y4RkgySVFIZWo3dTlWVjZkczZvNkhMNTJYMElpRGVjMGhwbTV0eWxrR3lYWHBXSjRqY3duWTRxSmNFcWJ0NDRiVXhGbksxOVBBei91VlVaWlRzMmpLdkNXMkMrei9FbWsxcmNWQnVKQ2g2QUNBeFhlZnEyR29MQVRZdWhoeXRidVZJak43d0JoVTdKOVJlQWVvUW5YeHUrYnRmU1hlaXUwNGc5OGlkT0JBNkhIcDVGeWZUQS9TUW1xaG1MRjErZTFzRkJOdG9lSERhS0xHaWdYejA0YitZUlBNWEhpTlRjalJ0UXUxc3A0TE4weU04dXpvb05MdGxjeHNoSFU2a0hURkdUOGNzRzRtc0xOclBveHFTWnFSR3g2cGJ0Zk1iZzhuOTFRZnpwcHNJQVBXMERLUUZha0FRMjB4eE9MSzRySjVIM3BhMG4xdmFTa3NCeE92RkdoSFFpZnNGU2svTTN6Z0VSeVNCckxlS0ZzTWFkVEQrU0NDdGlGU0NzSXptZzA4ZStEeEhOenhnc3BETkRGZDI0bW5TJnpxU3d1blhLbk80QllYSWExZnE2M085T1ZKQT0=\"; pnodepath=\"/pin4\"; sessionFunnelEventLogged=1",
    "DNT": "1",
    "Host": "www.pinterest.com",
    "Pragma": "no-cache",
    "Referer": "https://www.pinterest.com/",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "X-APP-VERSION": "f45affb",
    "X-Pinterest-AppState": "background",
    "X-Requested-With": "XMLHttpRequest"
}

payload = {"pin":511088257683635896}

cookies = {
    "G_ENABLED_IDPS":"google",
    "_b":"ATXnrb2fnNJNDIJYrcejJ03r6OBrSrRtfPl2BYaeJAaa6eEAzs4Wzg46Iv20mck9Jg8=",
    "_auth":"1",
    "csrftoken": "yAWQ9QVmYn5UIO4mSc0lPr97fP5RAYNy",
    "bei": "false",
    "cm_sub": "denied",
    "_pinterest_sess": "TWc9PSYrZTJOb2YycVF1MFJka0RKZTVPR1BkTVJrNHVHSDZFSFplY0tBVlpDVHRGS21oV05BMzYxYXZ2ZlVGaVhzbFcvTlI4UjBDTWpkM3lFeG9RN0xod0ZqTnNmZDhhS29hR3BUYnVzd0JxM2ltdUJ4ZWhUOStDNGZyeGIraWY4V0hsdmE3Mkp6MmtCWVB5ajhEdmVoMi93WXhCRmRzRHdKR0NhaTQ2VGZCUFEwWWllUDg4L1BmSjRtRkRoS1R0bVovQ0hUNFBoQ0ZrQXBKWmRqd3U1QkowempNM1o2a3JZa2lXaDNCNGJ4eVloV1JEWUNlZmpONU1FM0J2VXVqU0NEV0IvSVEwdW10K1FqeE9vTnpOZ1VLM0l4eGI5aFJDMUZQYW00eDRyNS9OSThpUk5heFVnMzgyaFpDS2NDUTFUVS9rWTdkdmlGeFZMQWM5TFRONnRZcTBaQU1qUS9aaDlkZUNZMmIxd2czQktGTTZ1R1ptOWtYb0o5MXdkamdSd0ZDZUo2Z1U3K2c2eXdheTlwODhEZVBVbkFyN1RsMzBlSDF2anJMemZ5ZmpWK2Y4RkgySVFIZWo3dTlWVjZkczZvNkhMNTJYMElpRGVjMGhwbTV0eWxrR3lYWHBXSjRqY3duWTRxSmNFcWJ0NDRiVXhGbksxOVBBei91VlVaWlRzMmpLdkNXMkMrei9FbWsxcmNWQnVKQ2g2QUNBeFhlZnEyR29MQVRZdWhoeXRidVZJak43d0JoVTdKOVJlQWVvUW5YeHUrYnRmU1hlaXUwNGc5OGlkT0JBNkhIcDVGeWZUQS9TUW1xaG1MRjErZTFzRkJOdG9lSERhS0xHaWdYejA0YitZUlBNWEhpTlRjalJ0UXUxc3A0TE4weU04dXpvb05MdGxjeHNoSFU2a0hURkdUOGNzRzRtc0xOclBveHFTWnFSR3g2cGJ0Zk1iZzhuOTFRZnpwcHNJQVBXMERLUUZha0FRMjB4eE9MSzRySjVIM3BhMG4xdmFTa3NCeE92RkdoSFFpZnNGU2svTTN6Z0VSeVNCckxlS0ZzTWFkVEQrU0NDdGlGU0NzSXptZzA4ZStEeEhOenhnc3BETkRGZDI0bW5TJnpxU3d1blhLbk80QllYSWExZnE2M085T1ZKQT0=",
    "pnodepath": "/pin4",
    "sessionFunnelEventLogged": "1"
}

index = random.randint(0, 9)
user_agent = user_agents[index]
headers = {'User-agent', user_agent}



page = ''
while page == '':
    try:
        page = requests.get(main_url, headers=head, cookies=cookies, params=payload)
        print(page.status_code)
        break
    except:
        print("Connection refused by the server..")
        print("Let me sleep for 5 seconds")
        print("ZZzzzz...")
        time.sleep(5)
        print("Was a nice sleep, now let me continue...")
        continue

print(page)