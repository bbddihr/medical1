import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 파일에서 가져오기
with open("flight.html","r",encoding='utf8') as f:
    soup = BeautifulSoup(f, 'lxml')
# 287개 항공권 조회
# print("-"*40)
# for문 287개 출력


flights = soup.find_all("div",{"class":"domestic_Flight__sK0eA"})
print("항공권 개수 : ",len(flights))
# print(flights[0])

# items=item_boxs.find_all('li','AsideList__item--i30ly')
#     for item in items:
#         title=item.find('span','ContentTitle__title--e3qXt').text
#         img_url=item.find('img')['src']
#         print("순위:  ",item.find("strong",{"class":"AsideList__ranking--sNPZy"}).text)
#         print("제목:  ",item.find("span",{"class":"text"}).text)
#         print("작가:  ",item.find("a",{"class":"ContentAuthor__author--CTAAP"}).text)
#         print("이미지링크: ",img_poster)
#         # img_poster=li.find("img",{"class":"Poster__image--d9XTI"})['src'])
#         #이미지파일 저장방법
#         img_poster = requests.get(img_url)
#         #with open()
        
flights = soup.find_all("div",{"class":"domestic_Flight__sK0eA"})
for i, flight in enumerate(flights):
    # 100,000원 이하만 출력될수 있도록 하시오.
    price=int((flight.find("i",{"class":"domestic_num__2roTW"}).text).replace(",",""))
    if price>100000:
        print("--- 10만원 이상인 항공권입니다.---")
        continue
    print('_'*40)
    print("[",(i+1),"번째]")
    airline_name = flight.find("b",{"class":"airline_name__Tm2wJ"})
    print("항공사 : ",airline_name.text.strip())
    route_times = flight.find_all("b",{"class":"route_time__-2Z1T"})
    print("출발시간 : ",route_times[0].text.strip())
    print("도착시간 : ",route_times[1].text.strip())
    air_price = flight.find("i",{"class":"domestic_num__2roTW"})
    price=int((flight.find("i",{"class":"domestic_num__2roTW"}).text).replace(",",""))
    price=int((flight.find("i",{"class":"domestic_num__2roTW"}).text).replace(",",""))
    #price=int(air_price.replace(",",""))
    print("가격 : ",price)
