## 1. 야놀자 홈페이지 이동
## 2. 검색창에 호텔 입력
## 3. 날짜선택
# 4. ,6월 5일,6일 클릭
# 5. 확인버튼클릭
# 6. 검색창 클릭>enter 키 입력 
# 7. 검색진행
# 8. 스크롤 이동 반복
# 9. 정보창이 띄워지면 이미지,제목,평점, 평가수, 숙박비용 저장.
#10. yanolja 테이블
# yno,img, title, grade,grade_num,price 

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
url="https://www.yanolja.com/?utm_source=google_sa&utm_medium=cpc&utm_campaign=20738115572&utm_content=160897187931&utm_term=kwd-327025203539&gad_source=1&gclid=CjwKCAjw88yxBhBWEiwA7cm6pRmAji_Yz97xSRqI2zZht7VQGeFxBVGJoh6G-arrJnWmw4N3TjGmaxoCF-oQAvD_BwE"

browser=webdriver.Chrome()
browser.maximize_window()
browser.get(url)
time.sleep(2)

elem=browser.find_element(By.XPATH,'//*[@id="__next"]/section/header/section/a[2]/div/div/span[2]')
time.sleep(1)
elem.click()

time.sleep(1)
# elem = browser.find_element(By.CLASS_NAME,'link_name')
elem=browser.find_element(By.CLASS_NAME,'SearchInput_input__342U2')
time.sleep(5)
elem.click()
time.sleep(5)
elem.send_keys('호텔')
#elem.send_keys(Keys.ENTER)
# time.sleep(3)
# elem=browser.find_element(By.XPATH,'//*[@id="__next"]/div[1]/main/div/div[1]/form/div/div[2]/div[1]/button')
# elem.click()
time.sleep(1)
elem=browser.find_element(By.XPATH,'//*[@id="__next"]/div[1]/main/div/div[1]/form/div/div[2]/div[1]/button')
elem.click()
time.sleep(2)
elem=browser.find_elements(By.XPATH,'//td[text()="5"]')
elem[1].click()
time.sleep(1)
time.sleep(1)
elem=browser.find_elements(By.XPATH,'//td[text()="6"]')
elem[1].click()
time.sleep(1)
elem=browser.find_element(By.XPATH,'/html/body/div[4]/div/div/section/section[4]/button')
elem.click()
time.sleep(2)
elem=browser.find_element(By.XPATH,'//*[@id="__next"]/div[1]/main/div/div[1]/form/div/div[2]/div[2]/button')
elem.click()
time.sleep(2)
elem=browser.find_element(By.XPATH,'/html/body/div[5]/div/div/section/div/div[2]/div/button')
elem.click()
time.sleep(1)
elem=browser.find_element(By.XPATH,'//button[@class="SearchInput_input__342U2"]')
time.sleep(1)
elem.click()
#엔터키쳐서보내기
elem=browser.find_element(By.XPATH,'//*[@id="__next"]/div[1]/main/div/div[1]/form/div/div[1]/div/input')
elem.send_keys('호텔')
elem.send_keys(Keys.ENTER)
elem.click()
elem.click()
time.sleep(10)

elem=WebDriverWait(browser,30).until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="__next"]/div[1]')))

print(elem)
print(elem[0].text)
#화면 스크롤 내리기 
prev_height=browser.execute_script("return document.body.scrollHieght")
print("최초 높이: ",prev_height)

while True:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height==curr_height:
        break   #같으면 중단
    prev_height = curr_height
    print("현재 높이: ",curr_height)
    
    
    
    
    
    
    
time.sleep(100)
