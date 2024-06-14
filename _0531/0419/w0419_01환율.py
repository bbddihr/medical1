import requests
from bs4 import BeautifulSoup

url="https://www.google.com/search?q=%ED%99%98%EC%9C%A8+1%EB%8B%AC%EB%9F%AC&sca_esv=125395e02bc1fefe&sca_upv=1&ei=0QoiZpWRAuWo2roPxoCQgA8&ved=0ahUKEwjVvbCMz82FAxVllFYBHUYABPAQ4dUDCBA&uact=5&oq=%ED%99%98%EC%9C%A8+1%EB%8B%AC%EB%9F%AC&gs_lp=Egxnd3Mtd2l6LXNlcnAiDu2ZmOycqCAx64us65-sMgoQABiABBhGGIICMgUQABiABDIEEAAYHjIGEAAYHhgPMgYQABgFGB4yBhAAGAgYHjIGEAAYCBgeMgYQABgIGB4yBhAAGAgYHjIGEAAYCBgeMhYQABiABBhGGIICGJcFGIwFGN0E2AEBSP0wUMMEWI4kcAJ4AZABApgBcqABmA-qAQQxOC4zuAEDyAEA-AEBmAIOoAKxCqgCAMICChAAGLADGNYEGEfCAgQQABgDwgILEAAYgAQYsQMYgwHCAggQABiABBixA8ICERAuGIAEGLEDGNEDGIMBGMcBwgILEC4YgAQY0QMYxwHCAg4QLhiABBixAxjRAxjHAcICDhAuGIAEGLEDGIMBGIoFwgIQEAAYgAQYsQMYgwEYRhiCAsICHBAAGIAEGLEDGIMBGEYYggIYlwUYjAUY3QTYAQHCAg4QABiABBixAxiDARiKBcICEBAAGIAEGLEDGEMYgwEYigXCAgoQABiABBhDGIoFwgIVEAAYgAQYsQMYQxiDARiKBRhGGIICwgIhEAAYgAQYsQMYQxiDARiKBRhGGIICGJcFGIwFGN0E2AEBmAMDiAYBkAYKugYGCAEQARgTkgcDNy43oAe7igE&sclient=gws-wiz-serp"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup= BeautifulSoup(res.text,"lxml")

with open('google1.html','w',encoding="utf8") as f:
    f.write(soup.prettify())
    
# title 출력
#print("title: ",soup.title.text)
#해당태그 출력
#print("미국달러: ",soup.find("input",{"class":"lWzCpb ZEB7Fb"}))
#해당태그의 속성값 모두출력
#print("미국달러: ",soup.find("input",{"class":"lWzCpb ZEB7Fb"}).attrs)
#해당태그의 특정속성값 1개 출력
print("미국달러: ",soup.find("input",{"class":"lWzCpb ZEB7Fb"})["value"])
#대한민국 원
print("대한민국 원: ",soup.find("input",{"class":"lWzCpb a61j6"})["value"])

                
