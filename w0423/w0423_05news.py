import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

# browser=webdriver.Chrome()
# url = "https://news.naver.com/main/ranking/popularDay.naver?mid=etc&sid1=111"
# headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}

# soup=BeautifulSoup(browser.page_source,"lxml")
# browser.get(url)
# time.sleep(3)

url = "https://news.naver.com/main/ranking/popularDay.naver?mid=etc&sid1=111"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}
res=requests.get(url,headers=headers)
res.raise_for_status()
soup=BeautifulSoup(res.text,"lxml")


print(soup.prettify())
officeCard=soup.find("div",{"class":"_officeCard _officeCard0"})
ranks=officeCard.find_all("div",{"class":"rankingnews_box"})
print("개수: ",len(ranks)) 




for rank in ranks:
    lis = ranks[0].find_all("li")
    print("lis개수: ",len(lis))
    print("제목: ",lis[0].find("a",{"class":"list_title"}).text)
    


# elem=browser.find_element(By.CLASS_NAME,'btn_more4')
# elem.click()
# time.sleep(3)
# soup=BeautifulSoup(browser.page_source,"lxml")
# print(soup.prettify())
# with open('stock.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify())
# time.sleep(100)