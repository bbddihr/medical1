import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup

#selenium으로 정보 가져오기
browser=webdriver.Chrome()
browser.get("https://comic.naver.com/bestChallenge")
time.sleep(3)
soup=BeautifulSoup(browser.page_source,"lxml")
with open("webtoons2.html","w",encoding="utf8") as f:
    f.write(soup.prettify()) 
print("완료")




# url="https://comic.naver.com/bestChallenge"
# headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}

# res=requests.get(url, headers=headers)
# res.raise_for_status()

# soup=BeautifulSoup(res.text,"lxml")

# print(soup.prettify())

# with open("webtoon.html","w",encoding="utf8") as f:
#     f.write(soup.prettify())
    
# print("완료") 

# browser=webdriver.Chrome()
# browser.get("https://www.naver.com/")

# time.sleep(10)
# elem = browser.find_element("MyView-module__link_login___HpHMW")
# elem
# elem.click()
 