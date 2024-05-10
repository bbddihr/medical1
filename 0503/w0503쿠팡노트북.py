# [ 2. 쿠팡 - 노트북   ]
# 검색 - 노트북으로 해서
# 총 1,2,3페이지 까지 검색해서
# 콘솔에 출력하고, db에 저장하시오.
# - coupang 테이블
# cno 시퀀스
# title 문자타입(100)
# img 문자타입(100)
# price 숫자타입(10)
# grade 숫자타입(10)
# eval_num 숫자타입(10)
# 제목, 이미지, 금액, 평점, 평가수


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

conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor()

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36","Accep-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
browser = webdriver.Chrome()
browser.maximize_window()
url="https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=9&backgroundColor="
browser.get(url)
time.sleep(2)

soup = BeautifulSoup(browser.page_source,"lxml")

products = soup.find_all("li",{"class":"search-product"})
# print("전체 개수 : ",len(products))
# print("-"*30)

for product in products:
    
    title = product.find("div",{"class":"name"})
    print("제목: ",title.text.strip()) 
    print("-"*30)
    img = product.find("img")["src"]
    print("이미지링크 : ",img)
    print("-"*30)
    price = product.find("strong",{"class":"price-value"})
    print("금액 :  ",price.text.replace(",","").strip()) 
    print("-"*30)
    try:
        grade=product.find("em",{"class":"rating"})
        grade=grade.text
        print("평점: ",grade)
    except:
        grade=""
        print(f'{grade}')
    print("-"*30)
    try:
        eval_num=product.find("span",{"class":"rating-total-count"})
        eval_num=eval_num.text
        print("평가수:  ",eval_num.text[1:-1]) 
    except:
        eval_num=""
        print(f'{eval_num}')

    print("-"*30)
