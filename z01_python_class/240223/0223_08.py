#점수를 입력받아서
#1. 90점이상이면 A 80점이상이면 B
#70점 이상이면 C 나머지는 F를 출력해보세요 (elif)

#2. 98점 이상 A+ 90-93사이는 A-
# B+, B-, C+, C-


a=int(input('점수를 입력하세요'))
#90점이상애들
if a>=90:
    if a>=98:
        print('A+')
    elif 93>a:
        print('A')
    else:
        print('A-')
        
    
    


    
    