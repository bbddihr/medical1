import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup

url="https://comic.naver.com/bestChallenge"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}

res=requests.get(url, headers=headers)
res.raise_for_status()

soup=BeautifulSoup(res.text,"lxml")

# print(soup.prettify())

# with open("webtoon.html","w",encoding="utf8") as f:
#     f.write(soup.prettify())
    
# print("완료") 

divs=(soup.find("div",{"class":"Aside__aside_wrap--iF5ju"}))
# wraps=divs.find_all("ul",{"class":"component_wrap"})
# wraps=divs.find_all("ul",{"class":"AsideList__content_list--FXDvm AsideList__challenge--HeKuU"})
print(divs)
uls=soup.find("ul",{"class":"AsideList__content_list--FXDvm AsideList__challenge--HeKuU"})
# print(uls)
# print("순위:  ",soup.find("strong",{"class":"AsideList__ranking--sNPZy"}).text)
# print("제목:  ",soup.find("span",{"class":"ContentTitle__title--e3qXt"}).text)
# print("ul: ",soup.find("ul",{"class":"AsideList__content_list--FXDvm AsideList__challenge--HeKuU"}))








# browser=webdriver.Chrome()
# browser.get("https://www.naver.com/")

# time.sleep(10)
# elem = browser.find_element("MyView-module__link_login___HpHMW")
# elem
# elem.click()
 