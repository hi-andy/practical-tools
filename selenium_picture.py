from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = 'https://www.cng.com/'
url = 'https://www.pinterest.com/pin/511088257683635896'
# url = 'http://www.cnscg.com/'

browser = webdriver.Chrome()
browser.get(url)

elem = browser.find_element_by_name('wd')
elem.send_keys("东湖渔庄")
elem.send_keys(Keys.RETURN)

print(browser.page_source)