import requests
from bs4 import BeautifulSoup
url="https://finance.naver.com/sise/lastsearch2.naver"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res=requests.get(url,headers)
res.raise_for_status()

soup=BeautifulSoup(res.text,"lxml")

#네이버 증권 10개까지 출력

t_table=soup.find("table",{"class":"type_5"})
trs=t_table.find_all("tr")

# tds=trs[2].find_all("td")
# for td in tds:
#     print(td.text.strip())
    
# tds=trs[3].find_all("td")
# for td in tds:
#     print(td.text.strip())



for i in range(2,14+1):
    tds=trs[i].find_all("td")
    for td in tds:
        print(td.text.strip())