import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By #요소선택
from selenium.webdriver.common.by import Keys  #키워드입력

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}
url="https://www.naver.com/"

browser=webdriver.Chrome()
browser.get(url)
elem = browser.find_element(By.XPATH,'//*[@id="shortcutArea"]/ul/li[6]/a')
elem.click()


#새창으로 페이지이동 
browser.switch_to.window(browser.window_handles[1])

#새창 요소 선택
elem=browser.find_element(By.XPATH,'//*[@id="container"]/div[2]/div/div[3]/a/em')

import time
import random
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
url="https://www.daum.net/"
browser=webdriver.Chrome()

browser.get(url)
time.sleep(random.randint(2,5))
elem=browser.find_element(By.CLASS_NAME,'btn_login')
time.sleep(random.randint(2,5))
elem.click()

input_js='document.getElementById("loginId--1").value="{id}";\
            document.getElementById("password--2").value="{pw}";\
                '.format(id="2ya2ya--@daum.net",pw="yojo2bbo5")

time.sleep(random.randint(2,5))
browser.execute_script(input_js)

#자바스크립트 명령어실행


#로그인버튼 클릭
# # 아이디 입력창 선택
# elem = browser.find_element(By.ID,'id')
# # 글자 입력
# elem.send_keys("aaa")
# time.sleep(random.randint(2,5))
# elem = browser.find_element(By.ID,'pw')
# elem.send_keys("1111")
time.sleep(random.randint(2,5))
# elem=browser.find_element(By.CLASS_NAME,'btn_g highlight submit')
elem=browser.find_element(By.XPATH,'//*[@id="mainContent"]/div/div[1]/form/div[5]/button[1]')
time.sleep(random.randint(2,5))
#로그인 버튼 클릭
elem.click()
# time.sleep(100) 
time.sleep(random.randint(2,5))

#이메일
elem=browser.find_element(By.NAME,'loginId')
elem.send_keys('aaa@daum.net')
time.sleep(2)
