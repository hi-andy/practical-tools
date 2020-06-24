import os
import re

import bs4
import requests

file = "area.txt"
url = 'https://baike.baidu.com/item/'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}


# 去除类似 [1] 角标
def strip_tag(in_tag):
    #return in_tag.get_text().strip()
    text = re.sub('[\[*?\]]', "/", in_tag.get_text()).strip()
    return re.sub('\/\d+\/', '', text) + "\n"


def get_text(pattern, titles):
    scene = []
    for segment in titles:
        key = re.search(pattern, str(segment))

        if key:
            node = segment.find_next_sibling()
            while True:
                try:
                    # if re.search('<div class="anchor-list ">', str(node)):
                    if re.search('<div class="para-title level-2" label-module="para-title">', str(node)):
                        break

                    scene.append(strip_tag(node))
                    node = node.find_next_sibling()
                except Exception:
                    break

    if ''.join(scene):
        return ''.join(scene).strip() + "\n\n"
    else:
        return pattern + ' >>>>>>>>>>>>>>>>>>>>>>>>> 未找到相关信息' + "\n\n"


with open(file) as f:
    for area in f:
        response = requests.get(url + area, headers=headers)
        soup = bs4.BeautifulSoup(response.text, "html5lib")

        # 概览
        for tag in soup.select('div.lemma-summary'):
            summary = strip_tag(tag)

        # collection = soup.select('div.para-title')
        collection = soup.select('div.level-2')

        pattern1 = '风景名胜|旅游'
        pattern2 = '文化'
        pattern3 = '特产'
        pattern4 = '美食'

        view = get_text(pattern1, collection)
        culture = get_text(pattern2, collection)
        special = get_text(pattern3, collection)
        food = get_text(pattern4, collection)

        path = './area/' + area + '/'
        if not os.path.exists(path):
            os.makedirs(path)

        with open(path + area + '.txt', 'a') as f:
            f.write(
                "##################### 概览 \n\n" + summary +
                "##################### 旅游 \n\n" + view +
                "##################### 文化 \n\n" + culture +
                "##################### 特产 \n\n" + special +
                "##################### 美食 \n\n" + food
            )
        #break
