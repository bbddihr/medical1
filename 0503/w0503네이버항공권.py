# [ 3. 네이버 항공권 ]
# - 웹스크래핑을 통해
# - 6/26 ~ 6/27
# - 항공사 출발시간 도착시간 소요시간 금액을
# - db에 저장하시오.
# - db에서
# - 항공사별 그룹핑해서 출력하시오.
# - 시간 검색기능을 구현하시오.
# ( 출발하려는 시간을 입력하세요. >> )
# - 시간을 입력하면 입력된 시간 이후로 검색
# - 없으면 검색한 데이터가 없다고 나옴.
# * flight 테이블
# fno - 숫자타입(4) 시퀀스
# airline - 문자타입(100)
# departure_time - 날짜타입
# arrival_time - 날짜타입
# flight_time - 문자타입(20)
# price - 숫자타입(10)

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
url="https://flight.naver.com/"

browser=webdriver.Chrome()
browser.maximize_window()
browser.get(url)
time.sleep(2)

elem=browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div/div[2]/div[2]/button[1]')
elem.click()
time.sleep(1)

elem=browser.find_elements(By.XPATH,'//b[text()="25"]')
elem[1].click()
time.sleep(1)

time.sleep(1)
elem=browser.find_elements(By.XPATH,'//b[text()="26"]')
elem[1].click()
time.sleep(1)

elem=browser.find_elements(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div/div[2]/button/span')
elem.click()
time.sleep(100)

soup = BeautifulSoup(browser.page_source,"lxml")

flights=soup.find("div",{"class":"domestic_Flight__sK0eA"})
name=soup.find("b",{"class":"airline_name__Tm2wJ"})

print(len(flights))