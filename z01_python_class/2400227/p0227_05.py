'''
# 0 - 20 사이의 5의 배수로 이루어진 리스트를 만들어보세요
# 출력: [0,5,10,15,20]
# a=[]
# a.append(1)
# a.append(2) 
# print(a)
num = []
# for, append
for i in range(0,21,5):
    print(i)
    
# for i in range(21):
    #if i %5 == 0 :
    #    print(i)
'''   
num = [] 
for i in range(21):
    if i %5 == 0 :   # 만약 5의 배수가 
        num.append(i)  # i =0 일때 [0]
                       # i = 1    [0,1]
        print(num)   # i의 값이 0,5,10,15,20 ...

lan= ['c', 'python', 'java', 'jquery', 'css']

#1. 하나하나 출력해보기 -for 사용
#   1) in 리스트 사용
for f in lan:
    print(f)
    
#   2) in range() 사용
for f in range(len(lan)): 
    # for i in range(5)  i=0,1,2,3,4...
    print(lan[f])

#2. 카운터변수 i 사용해서 :
#   1. c
#   2. python
#   3. java
#   4. jquery
#   5. css

for f in range(5):    
    print(f)
    print(lan[f])
    print('{}. {}'.format(f+1, lan[f]))
    
for f in range(1,6,1):
    #print(f)
    #print(lan[i])
    print('{}.{}'.format(f,lan[f-1]))   

num = [1,-1,2,3,-4,5,6,-8,9,-10]
#양수면 양수 음수면 음수 출력 for 사용
for i in num:
    print(i, end=':')   #### 
    if i>0:
        print('양수')
    else:
        print('음수')

print('{}:양수'.format(i))
print('{}:양수'.format(i))   
    
for i in range(len(num)): # i : 0,1,2,3 ..
    if num[i] >= 0 : 
        print('{} : 양수'.format(num[i]))
    else:
        print('{}: 음수'.format(num[i]))
        
       
    
   
          
