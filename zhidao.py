import requests
import bs4
import time

domain = 'http://zhidao.agutong.com'


def get_urls():
    urls = []
    title = []
    for num in range(1, 35):
        url = 'http://zhidao.agutong.com/entries?page=' + str(num)
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text, "html5lib")
        for a in soup.select('div.terms a[href^=/entries/]'):
            urls.append(a.attrs.get('href'))

        for tag in soup.select('div.name-tag'):
            title.append(tag.string)

        time.sleep(3)

    return urls, title


results = get_urls()

links = results[0]
titles = results[1]
for key, value in enumerate(links):
    with open('目录.html', 'a') as f:
        f.write('<a href="{}">{}</a><br/>'.format(domain + value, titles[key]))
