#split() #문자열 분리** 많이 씀

hobby = "게임,골프,독서"

print(hobby.split())  #['게임,골프,독서'] 리스트타입으로 분리 
print(hobby.split(','))  #['게임', '골프', '독서'] 리스트타입으로 분리 

h_data="2023-10-23,1,강원도 강릉시,강릉동인병원,383,21,033)651-6167,강릉대로419번길 42,종합"
print(h_data.split(","))
h_list = h_data.split(",")
print("병상수: ", h_list[4])

#split함수의 쓰임:
#csv파일 ->리스트파일로 만들어서 
#데이터분석에서 많이 쓰임

a_data="2023-10-23/1/강원도 강릉시/강릉동인병원/383/21/033)651-6167/강릉대로419번길 42/종합"
a_list = a_data.split("/")
print("병상수: ",a_list[4])

ss="%"
print(ss.join('파이썬'))  #파%이%썬

s_date="2023/03/08"
s_date_list=s_date.split("/")  #['2023', '03', '08']
print(s_date_list)
#리스트로 분리해서 출력하시오. 
s_time = "2023:03:08:16:48:00"
s_time_list=s_time.split(":")   #['2023', '03', '08', '16', '48', '00']
print(s_time_list)

today = "2024/03/08"
#10년 후의 날짜를 출력하시오. 2034/03/08 
t_list=today.split("/")
t_list[0] =int(t_list[0])+10
# today2="{}/{}/{}".format(t_list[0],t_list[1],t_list[2])
today2="{}/{}/{}".format(*t_list)
print(today2)


