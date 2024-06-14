import requests
from bs4 import BeautifulSoup
url="https://finance.naver.com/sise/lastsearch2.naver"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res=requests.get(url,headers)
res.raise_for_status()

soup=BeautifulSoup(res.text,"lxml")

#print(soup)

#태그로 찾는방법 title, get_text(), text, a.attrs, a["href"]
#class로 찾는 방법
#print(soup.find("tbody"))
#find:태그정보 찾기 함수, class로 찾는 방법
#print(soup.find(attrs={"class":"box_type_l"}))
print(soup.find("tr",attrs={"class":"type1"}))  #find, find_all, class
#print(soup.find("tr",{"class":"type1"})) #attrs 생략가능
type_tr = soup.find("tr",{"class":"type1"})
#print("th : ",type_ths.th)  #1번째 만나는 th태그만-1개만 찾아줌.
#print(type_ths.find_all("th"))  #모든것- 모든 th태그
ths=type_tr.find_all  #*******변수선언 가능
for th in ths:
    print("제목: ",th.text)
    