#***count/find***/rfind/index/rindex/starswith/endwith



ss="파이썬 공부는 즐겁습니다.공부가 모두 재미있지는 않습니다"
#존재하는 문자가 몇번 나왔는지 확인 
print(ss.count("공부"))
print(ss.count("자바"))  #없을때는 0출력

print(ss.find("공부"))    #존재하는 문자열의 위치값이 출력
print(ss.find("자바"))    #없을때 -1출력
print(ss.find("공부",7))  #문자열 7번째자리 이후 부터 검색시작해 위치값 출력
print(ss.rfind("공부"))    #rfind ->오른쪽에서부터 찾으려면
print("-"*20)
print(ss.index("공부"))
#print(ss.index("자바"))   #없는단어는 에러
print(ss.rindex("공부"))   
print(ss.startswith("않습니다")) #시작하는 문자열 #맞으면 true
print(ss.endswith("않습니다"))  #끝나는 문자열

