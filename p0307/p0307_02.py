students = {"stuNo":1, "stuName":"홍길동", "kor":100}
students["eng"]=100  #딕셔너리 추가
students["kor"]=50  #딕셔너리 수정 
del students["stuName"]  #     삭제
print(students) 

# 타입 list, dict, int, float, str
print(students.keys())  #딕셔너리 키값 추출
print(students.values())  #딕셔너리 value값 추출
print(students.items())   #딕셔너리 key, value 토플 형태로 추출
# 토플: 수정, 삭제가 불가능 
print(list(students.keys()))

# list=[1,2,3]
# list.append(4)  #리스트 추가
# print(list)
# del list[0]  #리스트 삭제
# print(list)  
# list[0] = 100  #리스트 수정
# print(list)
# print[3]=1000
# print(list) 