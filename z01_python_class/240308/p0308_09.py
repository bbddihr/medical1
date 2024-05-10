import random

random_num = str(random.randint(10000,99999)) #random_num은 숫자이므로 str() 씌워줌
print("[랜덤숫자 맞추기]")                     #문자열로 바꿔야 
print("랜덤숫자 : ",random_num)
a_input = input("숫자 5자리를 입력하세요")

#숫자자리로 확인해서 맞춘개수를 출력하시오.

cnt=0
for i in range(len(str(random_num))):
    if random_num[i]==a_input[i]:
        cnt += 1
print('맞는개수:', cnt )






        


