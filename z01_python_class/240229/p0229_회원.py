member = []
count=0
# 이름을 입력받아서 [1.홍길동] [2.유관순] [3.이순신]
while True:
    print('1.입력')
    print('2.전체출력')
    print('3.검색출력')
    print('4.검색삭제')
    print('5.수정')
    print('0.종료')
    ch = int(input('원하는 번호를 선택하세요>'))
    print('-'*25)
    if ch == 1 :
        print('입력')
        name=input('이름을 입력해주세요>')
        count +=1
        m = [count, name]
        member.append(m)
    elif ch == 2:
        print('출력')
        print('번호\t이름')
        for i in range(len(member)):
            print('{}\t{}'.format(member[i][0],member[i][1]))
        #print(member)
        #번호 이름
        # 1 홍길동
        # 2 유관순 
    elif ch == 3:
        searName=input('검색할 학생 이름>>') 
        print('번호\t이름') 
        for i, m in enumerate(member):
            if searName in m:
                print('{}\t{}'.format(member[i][0],member[i][1]))
                
    elif ch == 4:
        delname=input('삭제하고싶은 학생의 이름 입력하세요>>')
    
        for i, m in enumerate(member):
            if delname in m:
                del(member[i]) 
                print('{}님이 삭제되었습니다'.format(delname))
    
    elif ch == 5:
        print('수정입니다')
        reName=input('수정하고 싶은 학생의 이름을 입력해주세요>')
        for i, m in enumerate(member):
            if reName in m:
                print(reName, '님을 선택하셨습니다.')
                ch_num=input('수정하고 싶은 항목을 선택해 주세요(1.번호수정, 2. 이름수정)')
                if ch_num == '1':
                    print(reName,'님의 번호 수정을 선택하셨습니다.')
                    print(reName,'님의 번호는',member[i][0],'입니다')
                    #수정하는 코드 입력을 받아서 수정하기 
                    stu_num = input('새로운 번호를 입력해주세요>')
                    stu_num = int(stu_num)
                    member[i][0] =stu_num
                elif ch_num == '2':
                    print(reName,'님의 번호 수정을 선택하셨습니다.')
                    print(reName,'님의 번호는',member[i][1],'입니다')
                    stu_name = input('변경할 이름을 입력해주세요>')
                    member[i][1]=stu_name
                else:
                    print('잘못입력하셨습니다')
                    break
                
    elif ch == 0:
        print('종료')
        break
    else:
        print('다시입력')


