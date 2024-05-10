from datetime import datetime

from pytz import timezone

# print(datetime.now(timezone('Asia/Seoul')))
now=datetime.now()
print("시간을 포멧에 맞춰 출력하기")
# Y년을 의미, m:월  d:일 H:시 M:분 S:초
# 일자시간의 포멧을 설정하는 함수

output_a = now.strftime("%Y년%m월 %d일 %H시 %M분 %S초")
output_b = now.strftime("%Y-%M-%d %H:%M:%S")
output_c = now.strftime("%Y-%M-%d %H:%M:%S")
output_d = now.strftime("%Y-%M-%d")
print(output_a)
print(output_b)
print(output_c)
print(output_d)


# import datetime
# from datetime import datetime

# print("현재시간 출력")
# now = datetime.now()

print(now.year+1,"년")
print(now.month+6,"월")
print(now.day,"일")
print(now.hour,"시")
print(now.minute,"분")
print(now.second,"초")
print()
