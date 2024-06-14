# students = [[S001, "홍길동", 100,99,87,286,95.33,2],
#             [S002, "유관순", 98,93,87,296,98.67,1],
#             [S003, "이순신", 88,76,30,194,80.33,1],
#             [S004, "김구",100,100,90,300,100.00,1],
#             [S005, "강감찬", 98,85,44,227,75.67,4]]

students=[
{'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33}, 
{'stuNo': 'S002', 'name': '유관순', 'kor': 98, 'eng': 93,'math': 87, 'total': 278, 'avg': 92.67}, 
{'stuNo': 'S003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67}, 
{'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng':100, 'math': 90, 'total': 290, 'avg': 96.67}, 
{'stuNo': 'S005', 'name': '강감찬', 'kor': 98, 'eng': 85,'math': 44, 'total': 227, 'avg': 75.67}]
student={}
cnt=len(students)+1   #학번
while True:
    #전체출력
    count=input('학생전체 출력을 하시겠습니까?(1.확인, 2.취소)')
    if count ==0:
        break
    print('[학생성적출력]')
    print('학번\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
    for s_dic in students:
        for s_key in s_dic:
            print(s_dic[s_key],end="\t")
        print()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
'''     
print('[ 학생성적전체출력 ]')
        print('-'*55)
        
        print('-'*55)
        for stu in students:
            for s in stu:
                print(s, end='\t')
            print()
        kors, engs, maths,totals = 0,0,0,0
        for j, stu in enumerate(students):
            kors+=stu[2]
            engs+= stu[3]
            maths+=stu[4]
            totals+=stu[5]
        avgs = totals/len(students)
        print()
        print('--\t합계\t{}\t{}\t{}\t{}\t{:.2f}'.format(kors,engs,maths,totals,avgs))
        print()    
        '''  