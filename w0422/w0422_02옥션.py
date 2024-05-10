import requests
from bs4 import BeautifulSoup

url="https://browse.auction.co.kr/list?category=22160000"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}
res=requests.get(url,headers=headers)
res.raise_for_status()
#데이터불러오기


soup=BeautifulSoup(res.text,"lxml")
#파일저장
with open("auction.html","w",encoding="utf8") as f:
     f.write(soup.prettify())

#print(soup.prettify())


print("-"*40)
print(len(soup.find("div",{"id":"section--inner_content_body_container"})))
print("-"*40)
section=soup.find("div",{"id":"section--inner_content_body_container"})
divs=section.find_all("div",{"class":"section--module_wrap"})
#복수개 찾기 find_all
itemcards=section.find_all("div",{"class":"section--itemcard_info"})

for i,itemcard in enumerate(itemcards[0:10]):
    print("[",i+1,"번째]")
    print("제목 : ",itemcards[2].find("span",{"class":"text--title"}).text)
    # print("개수 : ",len(itemcards))  #100개
    price=int((itemcard.find("strong",{"class":"text__price-seller"}).text).replace(",",""))
    print("금액 : ",'{0:,}'.format(price))  #완료
    if itemcard.find("ul",{"class":"list--score"}).text=="":
        print("후기평점: 없음")
    else:
        list_score= itemcard.find("ul",{"class":"list--score"})
        # print("정수형 변경전 구매건수: ",list_score.find("span",{"class":"text--buycnt"}).text[4:])
        # print("후기평점: ",list_score.find("span",{"class":"for-a11y"}).text[5:-1])
        
        # 후기평점 4.9이상 출력
        if list_score.find("span",{"class":"for-a11y"}).text[5:-1] != "":
            for_a11y=float(list_score.find("span",{"class":"for-a11y"}).text[5:-1])
            if for_a11y >4.5:
                print("후기 평점: ",for_a11y)
            else:
                print("후기 평점: 미달")
        else:
            print("후기평점: 없음")
                
        #구매건수비교
        buycnt=int(list_score.find("span",{"class":"text--buycnt"}).text[3:])
        if buycnt >2:
            print("구매건수: ",buycnt)
        else:
            print("구매건수: 구매건수가 적어 생략")    
            
        print("-"*40)
    



#replace 함수   ,를 제거, int 타입 변경, '{0:}'.format(num)
        # try:
        #     #구매 3
        #     review=float(list_score.find("span",{"class":"for-a11y"}).text[4:8])
        #     buycnt=int(list_score.find("span",{"class":"text--buycnt"}).text[3:])
        #     if buycnt >2:
        #         print("구매건수: ",buycnt)
        #     else:
        #         print("구매건수: 구매건수가 적어 생략")
           
                
        # except:
        #     print("예외처리가 되었습니다.")