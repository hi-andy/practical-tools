#!/usr/bin/env python3
# 文件重命名程序

import os
import re

# 存放文件目录
file_dir = '/Users/andy/Downloads/2019/'
# in_dir = input('请输入文件路径:')


files = os.listdir(file_dir)
add_string = ''

count = 0
for file in files:
    # if file == '.DS_Store' : continue
    if file.startswith(".") : continue

    if not os.path.isdir(file):
        # match = re.match(r'(.{2})(\d{3,}).*(\.mp3)$', file)
        match = re.findall(r'\d+', file) # Only number.
        if str(match) != 'None':
            # newName = m.group(2) + '.' + m.group(1) + m.group(3)
            newName = ''.join(match).rjust(4, '0') + '.' + file[-2:] + '.mp3' # 重命名：第01集_官途 => 0001.官途.mp3
            os.rename(file_dir + file, file_dir + newName)
            # print(in_dir + file, out_dir + newName)
            
            count += 1
            # break
    

print('count', count)
