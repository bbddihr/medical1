#입력 : 이름, 아이디, 비밀번호 ( input)
# 5명을 입력받아서 member 리스트를 만드세요

member = []  #[[홍길동, ,aaa,111],[유관순, bbb, 111]]
'''
member 리스트를
이름 아이디 비밀번호
홍길동 aaaa 11111
이순신 bbbb 22222

형식으로 출력해보세요
'''
name=[]
for i in range(5):
    name=input("이름을 입력하세요>>")
    uid=input("아이디를 입력하세요>>")
    upw=input("비밀번호를 입력하세요>>")
    m = [name, uid, upw]
    member.append(m) 
    print(member)  
    
for i in member:
    print('이름\t아이디\t비밀번호')
    print('{}\t{}\t{}\t'. format(member[0][0], member[0][1], member[0][2]))
    print('{}\t{}\t{}\t'. format(member[1][0], member[1][1], member[1][2]))
    print('{}\t{}\t{}\t'. format(member[2][0], member[2][1], member[2][2]))

a=len(member) #5
for i in range(len(member)):   # i   0 1 2 3 4 숫자대신에 i  
    print('{}\t{}\t{}\t'. format(member[i][0], member[i][1], member[i][2]))
    
        
# for i in member:
#     print('이름\t아이디\t비밀번호')
#     print('{}\t{}\t{}\t'. format(member[0][0], member[0][1], member[0][2]))
#     print('{}\t{}\t{}\t'. format(member[1][0], member[1][1], member[1][2]))
#     print('{}\t{}\t{}\t'. format(member[2][0], member[2][1], member[2][2]))
   