fruits = ['딸기','사과','자몽','포도','수박','자몽']
#만약에 자몽을 삭제
#리스트명.remove('요소명')
print(fruits)
# fruits.remove('자몽')
# print(fruits)
#del(리스트명[번호])
del(fruits[5])
print(fruits)

for index, elem in enumerate(fruits):
    print('{}는 {}번째에 있습니다.'.format(elem,index))

'''
##### enumerate 함수
# index를 넣고 싶을때 사용   # index:0부터 시작
for i , name in enumerate(names):
    print('{}.{}'.format(i,name))
    
#start를 넣으면 시작인덱스를 지정할수 있다    
for i , name in enumerate(names, start=1):  ## index:1부터 시작
    print('{}.{}'.format(i,name))
    
names=['홍길동','유관순','이순신','강감찬','김구']
#         0       1        2        3       4
for i , name in enumerate(names):
    print('{}는 {}번째에 있습니다'.format(name,i))
    '''
    
