import random
c_number= [0]*13
for i in range(13):
    c_number[i] =i+1
c_number=[1,2,3,4,5,6,7,8,9,10,11,12,13]
#랜덤으로 2개의 숫자를 뽑아서 출력하시오.
#랜덤숫자 : 2->1 번방에 있습니다.
#랜덤숫자 : 9->8 번방에 있습니다.
#큰수 : 9 작은 수 :2
n=random.sample(c_number,2)

for i, j in enumerate(c_number):
    print("랜덤숫자:{}이고 {}번방에 있습니다".format(n[0],c_number[j]))
    print("랜덤숫자:{}이고 {}번방에 있습니다".format(n[1],c_number[j]))
print(n)
if n[0] > n[1]:
    print(f"큰수:{n[0]} 작은수{n[1]}")
else:
    print(f"작은수:{n[0]} 큰수{n[1]}")
for c_num in c_number:
    print(c_num.index(n[0]))