import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
url= "https://watcha.com/browse/webtoon"
#브라우저 열기
browser = webdriver.Chrome()
# browser.maximize_window() # 창 최대화
browser.get(url)
# 페이지로딩 시간대기
# elem = WebDriverWait(browser,30).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="//*[@id="root"]/div[1]/main/div/section[17]/div[2]/ul/li[1]/div"]')))
# print(elem)
# print(elem[0].text)
soup = BeautifulSoup(browser.page_source,"lxml")
toons = soup.find_all("main",{"class":"custom-1br6tpd e1k5czzn0"})
print("웹툰 개수 : ",len(toons))
print(toons[0])
with open("toons.html","w",encoding="utf8") as f:
    f.write(soup.prettify())

prev_height = browser.execute_script("return document.body.scrollHeight")
print("최초 높이 : ",prev_height)
# 스크롤 이동
while True:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    # 재조정된 스크롤 높이
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height:
        break # 같으면 중단하고 빠져나옴.
    prev_height = curr_height
    print("현재 높이 : ",curr_height)






