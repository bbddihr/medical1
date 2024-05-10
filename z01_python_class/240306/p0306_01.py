import operator 

fruit = ['바나나','바나나',
    '바나나','딸기','배','사과','딸기',
    '딸기','딸기','딸기','사과','바나나','바나나',
    '바나나','딸기','배','사과','딸기',
    '딸기','딸기','딸기','사과']

counter ={}  #딕셔너리 생성

#딕셔너리 추가
counter["복숭아"] =5 #딕셔너리 추가 
counter["바나나"]=4  #딕셔너리 추가
counter["바나나"]=1  #딕셔너리 수정

#print(counter["딸기"]) #딕셔너리에 없는 키값을 출력할때 에러
print(counter["바나나"])
if "딸기" not in counter:
    counter["딸기"]=0   #키를 생성 
else:
    print(counter["딸기"])   #키의 value값을 출력
    
for f in fruit:
    counter[f]=0
del counter["복숭아"]   #딕셔너리 삭제
print(counter)
print(type(counter.keys()))     #<class 'dict_keys'> 타입은 class
print(counter.values())
print(counter.items())

a_list = [3,5,7,4,1,2,6]
print(sorted(a_list))
print(a_list.sorted())
