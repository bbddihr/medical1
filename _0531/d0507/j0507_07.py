import pandas as pd
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
import pyautogui

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36","Accep-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
browser = webdriver.Chrome()
browser.maximize_window()

for year in range(2019,2024):
    
url = f"https://search.daum.net/search?w=tot&q={year}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
browser.get(url)
time.sleep(2)
soup = BeautifulSoup(browser.page_source,"lxml")
items=soup.find("ul",{"class":"c-list-basic ty_flow35"})
movie_list=items.find_all("li")
#list 타입 저장
list1 = []
list1.append(10)
list1.append(20)
list1.append(30)
list1.append(40)
# m_dict['viewer']
# 평점 가져오기
elem = browser.find_element(By.XPATH,'//strong[@class="tit-g clamp-g"]')
time.sleep(1)
elem.click()
time.sleep(1)


d_rating = soup.find("span",{"class":"gem-star-point"})
rating = d_rating.find("span",{"class":"ico-pmp"}).nextSibling.strip()
print("제목 : ",rating)
# 데이터 저장
year_list.append(year)
title_list.append(title)
viewer_list.append(viewer)
rating_list.append(rating)
browser.back()
'''
movies=items.find_all("li")
for movie in movies:

    title=movie.find("strong",{"class":"tit-g clamp-g"})
    count=movie.find("p",{"class":"conts-desc clamp-g"})
    count=movie.find("p",{"class":"ico-pmp"}).nextSigling.strip()
    star=movie.find("span",{"class":"gem-star-point"})
    print("제목 :",title.text)
    print("_"*30)
    print("누적관객: ",count.text)
    print("_"*30)
    
    print("별점: ",star.text)
    print("_"*30)
      
#dict 타입 저장
m_dict = {}
'''
