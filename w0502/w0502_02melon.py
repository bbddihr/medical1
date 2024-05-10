import oracledb
import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# 화면이 나타나는 것을 확인
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui


conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor()

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}
browser=webdriver.Chrome()
browser.maximize_window()

url="https://www.melon.com/chart/index.htm"
browser.get(url)
time.sleep(2)

#selenium 
# browser.find_element(By.XPATH,'//span[text()=""]')
# browser.find_elements(By.XPATH,'//button[@class=""]')
# elem.click(),
# elem.send_keys('시가총액')
# elem.send_keys(Keys.ENTER)

soup=BeautifulSoup(browser.page_source,"lxml")
#find, find_all

#파일저장
# with open("melon.html","w",encoding="utf-8") as f:
#     f.write(soup.prettify())
# #파일 불러오기    
# with open("melon.html","r",encoding="utf-8") as f:
#     soup=BeautifulSoup(f,"lxml")
trs=soup.find_all("tr",{"class":"lst50"})
trs1=soup.find_all("tr",{"class":"lst100"})
print(len(trs))
print(len(trs1))

for idx, tr in enumerate(trs):
    print(f"[{idx+1}번째]")
    title=soup.find("h2",{"class":"title"})
    print("1. 제목: ",title)
    rank=trs.find("span",{"class":"rank "}).text.strip()
    print("2. 순위:  ",rank)
    v_rank=
# print("변동순위 :",soup.find("span",{"class":"bullet_icons rank_static"}).text.strip())
       
# print(trs.text.strip())
# print('_'*30)
# print(soup.title.get_text())
# print('_'*30)

# for idx, tr in enumerate(trs):
#     print(f"[{idx+1}번째]")

# print("이미지: ",soup.find("a",{"class":"image_typeAll"}))
# print("타이틀: ",soup.find("div",{"class":"ellipsis rank01"}).span.a.text)
# print("가수: ",soup.find("div",{"class":"ellipsis rank02"}).text)
# print("좋아요수: ",soup.find("span",{"class":"none"}).nextSibling.strip())

'''
# print(.text.strip())
# td[1]=soup.find("span",{"class":"rank"}).text.strip()
# td[2]=soup.find("span",{"class":"none"}).text.strip()
# td[3]=soup.find("a",{"class":"image_typeAll"})
# td[4]=soup.find("div",{"class":"ellipsis rank01"}).span.a.text
# td[7]=soup.find("span",{"class":"cnt"}).text.strip()


melon
순번 시퀀스번호 melon_seq
순위 rank
변동순위 v_rank
이미지 ung
제목 title
가수 singer
좋아요수 likeNum
'''