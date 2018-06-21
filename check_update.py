#!/usr/bin/env python3
import json
import os
import re

import requests


# 可将脚本放入环境变量，故在执行脚本外层目录存放数据
data_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '/data/'
data_file = data_dir + 'data.json'
data = {}

if os.path.isfile(data_file):
    with open(data_file, 'r') as f:
        data = json.load(f)
else:
    if not os.path.exists(data_dir):
        os.mkdir(data_dir)
    data['kindle_version'] = '0'

# 检查 Kindle 软件更新 URL
url = 'https://www.amazon.cn/gp/help/customer/display.html?nodeId=201756220'

r = requests.get(url)
m = re.search('[\u4e00-\u9fa5]+([\d\.\d\.?]{3,11})', r.text)

if str(m) != 'None':
    new_ver = m.group(1)
    if new_ver != data['kindle_version']:
        updated = input('There is a new version: ' + data['kindle_version'] + ' => ' + new_ver + ' \nNeed to mark updated. please input "Y" :')
        if updated == 'Y':
            data['kindle_version'] = new_ver
            with open(data_file, 'w') as outfile:
                json.dump(data, outfile, ensure_ascii=False)
                outfile.write('\n')
                print('Mark updated.')
    else:
        print('No new version.')
else:
    print('Error: No data detected!')
