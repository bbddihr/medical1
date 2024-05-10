import operator 


numbers = [1,2,4,6,4,3,6,7,1,3,4,3,4,7,7,7,7,1,1,1,7]
counter={}
# counter["1"]=2
# counter["2"]=1
# print(counter)
for number in numbers:
    if number not in counter:  #counter 딕셔너리에 키값이 없으면
        counter[number] = 0   #딕셔너리에 추가
    
    counter[number] +=1        #딕셔너리 1을 증가
        

print(sorted(counter.items(),key=operator.itemgetter(0),reverse=True))
print(counter)
       

 
 
  
#     print(i)
#     num[i] = input(f"{i+1}번째 숫자를 입력하세요.")
# print("최대값 : ",max(*num))  #################3 
# print("최소값 : ",max(num[0],num[1],num[2]))
# num.sort()   
# print(num)   