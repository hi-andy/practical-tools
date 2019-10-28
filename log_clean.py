#!/usr/local/bin/python3
import os
import time

logDirs = [
    '/Users/hua/Sites/youbank/application/log',
    '/Users/hua/Sites/youbank/runtime/log'
]
interval = 7 * 24 * 3600  # 间隔时间


# 遍历文件夹
def get_files(file_dir):
    all_files = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            file_name = os.path.join(root, file)
            all_files.append(file_name)

    return all_files


for log_dir in logDirs:
    files = get_files(log_dir)
    for file in files:
        print(file)
        create_time = os.path.getctime(file)
        if create_time < int(time.time()) - interval:
            os.remove(file)
