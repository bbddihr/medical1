import oracledb
import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0"}
browser=webdriver.Chrome()
browser.maximize_window()
time.sleep(3)
url='https://namu.wiki/RecentChanges'
browser.get(url)
res=requests.get(url,headers=headers)
res.raise_for_status()
time.sleep(2)
soup=BeautifulSoup(browser.page_source,"lxml")

print("-"*40)
# with open("namu.html","w",encoding="utf-8") as f:
#     f.write(soup.prettify())

divs=soup.find("div",{"class":"b5G6-Ki+"})
div01=divs.find("div")
# for div in divs[0:4]:
    
#     search=soup.find("div",{"class":"tMX2P1XP"})
#     print("검색제목: ",search)
#     category=soup.find("li",{"class":"_5YOCljOj"})
#     print("분류: ",category)
#     content=soup.find("span",{"id":"개요"})
#     print("개요:  ",content)
#     print("-"*40)
# time.sleep(50)
