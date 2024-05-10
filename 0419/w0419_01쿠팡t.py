import requests
from bs4 import BeautifulSoup

# url="https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user"
url="https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=recent"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup= BeautifulSoup(res.text,"lxml")

# with open("coupang.html","w",encoding="utf8") as f:
#     f.write(soup.prettify())
    
print(len(soup.find("ul",{"class":"search-product-list"}).find_all("li")))

ul_search=soup.find("ul",{"class":"search-product-list"})
lis=ul_search.find_all("li")
#print("리스트 갯수: ",len(lis))

#print(ul_search.find("li"))


for i,li in enumerate(lis[0:10]):
    #광고상품 제외
    if "search-product__ad-badge" in li['class']:
        continue
    #평점이 5.0이상인것만 출력 -문자와 숫자 비교 에러
    if float(li.find("em",{"class":"rating"}).text) < 5.0:
        continue
    
    #평가 인원수 200명 이상만 출력
    if int(li.find("span",{"class":"rating-total-count"}).text[1:-1]) < 200:
        continue
    
    print("[",i+1,"번째 상품]")
    print("li class: ",li["class"])
    print("제목:  ",li.find("div",{"class":"name"}).text.strip())
    print("가격:  ",li.find("strong",{"class":"price-value"}).text)
    print("별점:  ",li.find("em",{"class":"rating"}).text)
    print("평가인원수:  ",li.find("span",{"class":"rating-total-count"}).text[1:-1])
    print("_"*30)
