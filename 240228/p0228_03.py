member = []

#입력: 이름, 점수 (input) ['홍길동' , 90]
#총 3명의 정보를 member 리스트에 넣으세요

#print(member) #[['홍길동',90],['유관순',91],['이순신', 95]]


for i in range(3):
    name=input('이름을 입력하세요>>')
    score=int(input('점수를 입력하세요>>'))
    m= [name,score]
    member.append(m)
    print(member)

for i in range(3): 
    name = member[i][0]
    score = member[i][1]
    if score >= 60:
        print('{}님 합격 입니다'.format(name))
    else:
        print('{}님 불합격 입니다'.format(name))
        
    
 
    
#60점 이상이면 홍길동님 불합격입니다. 유관순님 합격입니다
# #member 변수 사용, for, if    
