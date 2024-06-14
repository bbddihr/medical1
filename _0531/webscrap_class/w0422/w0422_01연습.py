import requests
from bs4 import BeautifulSoup

url = "https://browse.auction.co.kr/list?category=22160000&k=31&p=1"

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}
res=requests.get(url,headers=headers)
res.raise_for_status()
#데이터불러오기
soup=BeautifulSoup(res.text,"lxml")


#파일저장
# with open("yeogi.html","w",encoding="utf8") as f:
#     f.write(soup.prettify())


    
    
#print(soup.prettify())
print(len(soup.find("div",{"id":"section--inner_content_body_container"})))

#aas=divs.find_all("a")
#divs=div.find_all("div")
print(div.text)
#print(soup.title.text)
print("제목 : ",div.find("span",{"class":"text--title"}).text)
print("가격 : ",div.find("strong",{"class":"text__price-seller"}).text)
print("평점 : ",div.find("strong",{"class":"text__price-seller"}).text)
print("후기: ",div.find("li",{"class":"item awards"}).text)
print("a태그: ",div.find("a",{"class":"link--itemcard"}).text)

