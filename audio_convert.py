#!/usr/bin/env python3
import os
import re
import subprocess


# 音频格式批量转换
# '-v', 'quiet', 安静模式，不输出日志
# "-ab", "64k", 指定码率
# "-ar", "44100", 指定采样率
def audio_convert(in_dir, out_dir='../mp3/', format='.mp3'):
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    files = os.listdir(in_dir)
    for file in files:
        match = re.match(r'.*(\d{2,}).*', file)
        if str(match) != 'None':
            newName = match.group(1).rjust(4, '0') + '.' + file[-2:] + format

            source_file = in_dir + file
            out_file = os.path.join(out_dir, newName)
            subprocess.call(['/usr/local/bin/ffmpeg', '-v', 'quiet', '-i', source_file, "-qscale:a", "9", out_file, '-y'])
            break


# 文件目录
file_in = '/Users/andy/Downloads/guan2/'
file_out = '/Users/andy/Downloads/newGuan/'

audio_convert(file_in, file_out)
