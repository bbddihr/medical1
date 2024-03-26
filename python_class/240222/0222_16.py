import datetime # 날짜 관련 기능을 가져옴 
now = datetime.datetime.now() #오늘 날짜 시분초 가져옴

print(now) 

print(now.year) 
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

#시간을 사용해서
#지금이 오전이면 오전입니다. 오후면 오후입니다 출력

#[현재는 17시로 오후입니다.}

now=datetime.datetime.now()
print(now)
print(now.hour)
if now.hour >12:
    print("지금은 오후입니다")
else:
    print("지금은 오전입니다")
    
h=now.hour
m=now.month
if now.hour >12:
    print("현재는 {}시로 오후입니다".format(now.hour))
    
h=now. hour #시간
#오전
if h<12 :
    print('현재는 {}시로 오전입니다.'.format(h))

#1. 짝수달입니다. 홀수달입니다.
m=now.month
if m % 2 ==0:
    print("짝수달입니다.")

# 월 겨울 3-11월이면 겨울이 아닙니다. 그 외의 경우에는 겨울입니다.
m=now.month
if 3<=m<=11:
    print('겨울이 아닙니다')
else:
    print('겨울입니다')
    
