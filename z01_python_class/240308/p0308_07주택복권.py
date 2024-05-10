import random
#주택복권
#2조 711
#1조 740
#조:1-9까지
#조뒤에-#0-999999
first_num=random.randint(1,9)
last_num = random.randint(0,999999)

lotto=str(first_num)+"조"+"{:6d}".format(last_num)
print(lotto)
#lotto = "1조740042"
#lotto = str(f_num)+"조"+"000001"

#1조10


#lotto = "1조740042"
# #예 :    2조711 -> 1개번호가 맞았습니다.
l_input =input("복권번호를 입력하세요(예:1조111111)>")

#비교하는 프로그램을 구현하시오.
#자리수를 활용하세요.

cnt=0
for i in range(len(lotto)):
    if lotto[i] == l_input[i]:
        cnt += 1
print('맞는개수:',cnt-1)


'''
fruit={'peach':'복숭아','orange':'오렌지','apple':'사과','pear':'배',
       'grapes':'포도','mango':'망고','kiwi':'키위'}
answer=0
wrong=0
# 복숭아 영어로 입력하시오.
# for f in fruit:
#     print("키: ",f, "value: ",fruit[f]) #######

for f in fruit:
    eng_in = input("{}를 영어로 입력하세요.".format(fruit[f]))
    #eng_in = input("{}를 한글로 입력하세요.format(f)
    #프로그램 하시오.
    print("입력한 단어:{}".format(eng_in))
    if eng_in==f:
        print("정답입니다")
        answer+=1
    else:
        print("오답입니다.정답은:{}".format(f))
        wrong+=1
   
print("[문제 체크]")
print("총문제:", len(fruit))
print("정답: answer") 
'''
