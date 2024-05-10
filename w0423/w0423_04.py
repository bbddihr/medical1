import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

browser=webdriver.Chrome()
url = "http://finance.naver.com"
browser.get(url)
time.sleep(3)
# elem=browser.find_element(By.XPATH,'//*[@id="shortcutArea"]/ul/li[6]/a')
# elem.click()
# time.sleep(3)
elem=browser.find_element(By.CLASS_NAME,'btn_more4')
elem.click()
time.sleep(3)
soup=BeautifulSoup(browser.page_source,"lxml")
print(soup.prettify())
with open('stock.html','w',encoding='utf-8') as f:
    f.write(soup.prettify())
time.sleep(100)