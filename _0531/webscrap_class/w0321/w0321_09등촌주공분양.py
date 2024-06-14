import requests
from bs4 import BeautifulSoup

url="https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&q=%EB%93%B1%EC%B4%8C%EC%A3%BC%EA%B3%B5+%EB%B6%84%EC%96%91"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"}
res=requests.get(url,headers=headers)
res.raise_for_status()

soup=BeautifulSoup(res.text,"lxml")

# with open("real.html","w",encoding="utf8") as f:
    # f.write(soup.prettify())
    
    
#등촌주공3단지 매매시세,전세시세 출력하시오



real=soup.find("ol",{"class":"list_place"})
li_list=real.find_all("li")


for i in range(len(li_list)):
    # print(len(li_list) 
    title=li_list[i].find("div",{"class":"wrap_tit"}).a.text.strip()
    dd_list=li_list[i].find_all("dd",{"class":"f_red"})
    print("제목: ",title)
    print(len(dd_list))
    print()
    print("매매시세: ",dd_list[0].text)
    print("전세시세: ",dd_list[1].text)
    


# r_list=real.find_all("")

# print([0].text)








'''
url ="https://finance.naver.com/sise/lastsearch2.naver"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup=BeautifulSoup(res.text,"lxml")
# print(soup)
s_all = soup.find("div",{"class":"box_type_l"})
tr_list =s_all.find_all("tr")
samsung=tr_list[2]
td_list=samsung.find_all("td")
print("순위 : ",td_list[0].text)
print("종목명 : ",td_list[1].find("a").text)
print("검색비율 : ",td_list[2].text)
print("현재가 : ",td_list[3].text)
print(len(tr_list))
'''