import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup

#selenium으로 정보 가져오기
browser=webdriver.Chrome()
url="https://jumin.mois.go.kr/ageStatMonth.do"
browser.get(url)
time.sleep(3)
soup=BeautifulSoup(browser.page_source,"lxml")
with open("population.html","w",encoding="utf8") as f:
    
    f.write(soup.prettify()) 
# print("완료")
tb=soup.find("table",{"id":"contextTable"})
tbody=tb.find("tbody")
# print(trs)
trs=tbody.find_all("tr")
print(trs[1])
tds=trs[1].find_all("td")
seoul=tds[2].text
# print("서울특별시 인구수:  ",tds[2].text)
print("서울특별시 인구수:  ",seoul.text)
print("tds개수: ",len(tds))
tds=trs[4].find_all("td")
incheon=tds[2].text
# print("인천광역시 인구수:  ",tds[4].text)
print("인천광역시 인구수:  ",incheon.text)
tds=trs[9].find_all("td")
kyunggi=tds[2].text
print("경기도 인구수:  ",kyunggi.text)

int(seoul.replace(",",""))+int(incheon.replace(",","")+int(kyunggi.replace(",","")))