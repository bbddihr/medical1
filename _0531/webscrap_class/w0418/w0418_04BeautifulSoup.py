import requests
from bs4 import BeautifulSoup

url="https://finance.naver.com/sise/lastsearch2.naver"
headers={"User-Agent":"https://www.whatismybrowser.com/detect/what-is-my-user-agent/"}
res=requests.get(url,headers=headers)
res.raise_for_status()

print(type(res.text))

# with open("stock.html","w",encoding="utf8") as f:
#     f.write(res.text)

soup=BeautifulSoup(res.text,"lxml")   #text를 html파싱  
#()있으면 함수. 없으면 변수. 첫글자대문자(BeautifulSoup).>>> 이거는클라스
print(res.text)   
print(soup.prettify())
# with open("stock2.html","w",encoding="utf-8") as f:
#     f.write(soup.prettify())

print("<title>:  ",soup.title)     # soup.태그를 입력
print("<title> text: ",soup.title.get_text())  #태그의 글자를 가져옴. JS에서는 val()
print("<title> text: ",soup.title.text)  #태그의 글자를 가져옴.괄호없음.
print("<a> 태그:  ", soup.a)  #메인메뉴로 바로가기
print("<a> 태그글자: ", soup.a.text)
print("<a> 속성전체: ", soup.a.attrs) # 태그의 속성값 가져옴
print("<a>[1개의 속성]: ", soup.a["href"]) #태그의 1개 속성 가져옴.
 
