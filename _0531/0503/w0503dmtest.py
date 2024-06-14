
#역대관객순
#이미지,제목,누적관객수,날짜
#이미지 저장까지
#2023,2022,2021,2020

#콘솔창에 출력하고,db에 저장하시오.
#daum_movie 테이블
# dno시퀀스
#title 문자타입(100)
#img 문자타입(100)
#audience누적관객수 숫자타입(10)
#ddate 날짜타입
import oracledb
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor()

sql ="create table daum_movie(dno number(4) primary key,title varchar2(100) not null, img varchar2(100), audience number(10), ddate date)"
cursor.execute(sql)

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36","Accep-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
browser=webdriver.Chrome()

url="https://search.daum.net/search?w=tot&q=2020%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
browser.get(url)

soup=BeautifulSoup(browser.page_source,"lxml")

# with open("daum_movie.html","w",encoding="utf-8") as f:
#     f.write(soup.prettify())
for i in range(4):
    url=f"https://search.daum.net/search?w=tot&q=202'{i}'%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
    browser = webdriver.Chrome()
    # browser.maximize_window()
    browser.get(url)
    movies=soup.find_all("div",{"class":"c-item-content"})
    print(len(movies))                        
    print("-"*30)
    for idx, movie in enumerate(movies):    
        c=movie.find("span",{"class":"badge-basic"})
        print('순위 :',c.text)
        print("-"*30)
        # img=soup.find()
        try:
            img = movie.find("img")["src"]
            print("이미지링크 : ",img)
        except:
            img = ""
            print(f"이미지링크 : {img}")
        print("-"*30)
        title=movie.find("strong",{"class":"tit-g clamp-g"})
        print('제목 :',title.text)
        print("-"*30)
        audience=movie.find("p",{"class":"conts-desc clamp-g"})
        audience=int(audience.text[4:-3].replace(",",""))
        print('관객수: ',audience)
        print("-"*30)
        ddate=movie.find("span",{"class":"conts-subdesc clamp-g"})
        print('개봉일: ',ddate.text)
        print("-"*30)
        
cursor.close()
conn.close()
