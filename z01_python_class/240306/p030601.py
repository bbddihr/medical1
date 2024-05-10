fruit = { 'peach':'복숭아','orange':'오렌지','apple':'사과',
         'pear':'배','grapes':'포도','mango':'망고','kiwi':'키위'}

answer=0
wrong=0

for f in fruit:
    eng_in=input("{}를 영어로 입력하세요".format(fruit[f]))
    print("입력한 단어:{}".format(eng_in))
    if eng_in == f:
        print("정답입니다.")
        answer+=1
    else:
        print("오답입니다. 정답:{}".format(f))
        wrong += 1
        
