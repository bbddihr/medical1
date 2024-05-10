import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/main/ranking/popularDay.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}

res=requests.get(url,headers=headers)
res.raise_for_status()

# print(res.text)
soup= BeautifulSoup(res.text,"lxml")
# with open("test.html","w",encoding="utf8") as f:
#     f.write(soup.prettify())
    
    
print(soup.title.text) #soup 태그사용해서 text 글자를 출력 
print(soup.a)          #soup 태그사용
print(soup.div)        
print(soup.a.attrs)     #soup a태그의 속성값 출력
print(soup.a["href"])   #soup   a태그의 속성값 출력

# print(soup.find("div",attrs={"id":"footer"}))
