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
    




items=soup.find("ul",{"class":"search-product-list"})
n=items.find_all("li")
for i in n[0:10]:
    print("_"*20)
    print("제품명: ",i.find("div",{"class":"name"}).text)
    print("가격: ",i.find("strong",{"class":"price-value"}).text)
    print("별점: ",i.find("em",{"class":"rating"}).text)
    print("_"*20)
        




# item=soup.find('li',{"class":"search-product"})
# print(item.text)

# print("li01순위: ", li01.p.text)
# print("제목 : ", li01.find("a",{"class":"itemname"}).text)
# print("가격 : ", li01.find("div",{"class":"s-price"}).strong.span.text)


#print(soup.find("p",{"class":"no1"}))
# best=soup.find("p",{"class":"no1"})
# print(best.text)

#best_div=soup.find("div",{"class":"best-list"})
#print("div 베스트: ",best_div.text.strip())
#print("li: ",best_div.find("li"))
#li 1개 찾기
#li01=best_div.find("li")
# print("li01순위: ", li01.p.text)
# print("제목 : ", li01.find("a",{"class":"itemname"}).text)
# print("가격 : ", li01.find("div",{"class":"s-price"}).strong.span.text)



#여러개 best 상품 출력
#lis=best_div.find_all("li")
# print("베스트상품갯수: ",len(lis)) 
 
# for li in lis[0:4]:
    
#     # print("베스트상품",li)
#     print("순위: ", li.p.text)
#     print("제목 : ", li.find("a",{"class":"itemname"}).text)
#     print("가격 : ", li.find("div",{"class":"s-price"}).strong.span.text)
#     print("-"*10)
 
 
 
 

 
    
# title 출력
#print("title: ",soup.title.text)
#해당태그 출력
#print("미국달러: ",soup.find("input",{"class":"lWzCpb ZEB7Fb"}))
#해당태그의 속성값 모두출력
#print("미국달러: ",soup.find("input",{"class":"lWzCpb ZEB7Fb"}).attrs)
#해당태그의 특정속성값 1개 출력
#print("미국달러: ",soup.find("input",{"class":"lWzCpb ZEB7Fb"})["value"])
#대한민국 원
#print("대한민국 원: ",soup.find("input",{"class":"lWzCpb a61j6"})["value"])

                
