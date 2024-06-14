import oracledb

# conn=oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
# cursor=conn.cursor() 

# sql ="create table mem(id varchar2(30) primary key,pw varchar2(30), name varchar(30),mdate date)"

# cursor.close()
# conn.close()

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

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36","Accep-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}


for i in range(5):
    url = "https://www.yeogi.com/domestic-accommodations?searchType=KEYWORD&keyword=%ED%98%B8%ED%85%94&checkIn=2024-06-05&checkOut=2024-06-06&personal=2&freeForm=true"

    browser = webdriver.Chrome()
    # browser.maximize_window()
    browser.get(url)
    
    time.sleep(2)
    soup = BeautifulSoup(browser.page_source,"lxml")

    with open("ygi.html","w",encoding="utf8") as f:
        f.write(soup.prettify())
        


    # hotels=soup.find("div",{"class":"css-1qumol3"})
    hotels=soup.find_all("a",{"class":"gc-thumbnail-type-seller-card css-wels0m"})
    print(len(hotels))
    # print(len(hotels))
    # img = soup.find("img",{"class":"thumbnail-image desktop:hover:bg-backgroundOverlayDarkInactive"})
    # print("제목:  ",soup.find("h3",{"class":"gc-thumbnail-type-seller-card-title css-1asqkxl"}).text)
    # print("별점:  ",soup.find("span",{"class":"css-9ml4lz"}).text)
    # print("가격:  ",soup.find("span",{"class":"css-5r5920"}).text)
    # print(soup.title.get_text())
    title=hotels[0].find("h3",{"class":"gc-thumbnail-type-seller-card-title css-1asqkxl"})
    print(title)






