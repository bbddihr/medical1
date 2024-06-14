import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup

#selenium으로 정보 가져오기
browser=webdriver.Chrome()
browser.get("https://comic.naver.com/bestChallenge")
#페이지로딩시간을 최대한 보장
time.sleep(3)
soup=BeautifulSoup(browser.page_source,"lxml")
# with open("webtoons2.html","w",encoding="utf8") as f:
#     f.write(soup.prettify()) 
# print("완료")
list_ul=soup.find("ul",{"class":"AsideList__content_list--FXDvm AsideList__challenge--HeKuU"})
print(list_ul)

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}

def main():
    lis=list_ul.find_all("li")
    print(len(lis))
    print("갯수: ",len(li))
    item_boxs=soup.find_all('div','component_wrap')[3]
    items=item_boxs.find_all('li','AsideList__item--i30ly')
    for item in items:
        title=item.find('span','ContentTitle__title--e3qXt').text
        img_url=item.find('img')['src']
        print("순위:  ",item.find("strong",{"class":"AsideList__ranking--sNPZy"}).text)
        print("제목:  ",item.find("span",{"class":"text"}).text)
        print("작가:  ",item.find("a",{"class":"ContentAuthor__author--CTAAP"}).text)
        print("이미지링크: ",img_poster)
        # img_poster=li.find("img",{"class":"Poster__image--d9XTI"})['src'])
        #이미지파일 저장방법
        img_poster = requests.get(img_url)
        #with open()
        
        
    



# print("순위:  ",lis[0].find("strong",{"class":"AsideList__ranking--sNPZy"}).text)
# print("제목:  ",lis[0].find("span",{"class":"text"}).text)
# print("작가:  ",lis[0].find("a",{"class":"ContentAuthor__author--CTAAP"}).text)
# print("이미지링크:  ",lis[0].find("img",{"class":"Poster__image--d9XTI"})['src'])
# print("갯수: ",len(lis))

# for li in lis:
#     print("순위:  ",li.find("strong",{"class":"AsideList__ranking--sNPZy"}).text)
#     print("제목:  ",li.find("span",{"class":"text"}).text)
#     print("작가:  ",li.find("a",{"class":"ContentAuthor__author--CTAAP"}).text)









# divs=(soup.find("div",{"class":"Aside__aside_wrap--iF5ju"}))
# wraps=divs.find_all("div",{"class":"component_wrap"})
# print(wraps)



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
 