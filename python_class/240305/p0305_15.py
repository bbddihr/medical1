import operator 


fruit = ['바나나','바나나',
    '바나나','딸기','배','사과','딸기',
    '딸기','딸기','딸기','사과','딸기',
    '딸기','딸기','딸기','사과','바나나','바나나',
    '바나나','딸기','배','사과','딸기',
    '딸기','딸기','딸기','사과','딸기',
    '딸기','딸기','딸기','사과']
counter={}

for i in fruit:
    if i not in counter:
        counter[i] =0
    counter[i] +=1
    
print(counter)



print(sorted(counter.items(),key=operator.itemgetter(0),reverse=True))
print(counter)    






# for number in numbers:
#     if number not in counter:  #counter 딕셔너리에 키값이 없으면
#         counter[number] = 0   #딕셔너리에 추가
    
#     counter[number] +=1        #딕셔너리 1을 증가
        

# print(sorted(counter.items(),key=operator.itemgetter(0),reverse=True))
# print(counter)
       