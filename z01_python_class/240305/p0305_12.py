import operator 
#클래스 정렬

#딕셔너리 정렬
t_dic = {}
t_list = []
t_dic={'peach':'복숭아','orange':'오렌지','apple':'사과','pear':'배',
       'grapes':'포도','mango':'망고','kiwi':'키위'}

# print(sorted(t_dic.items(),key=operator.itemgetter(1)))
#(peach,복숭아),(orange,오렌지) ...

## 1일때 
## 중요 외우기 [('mango', '망고'), ('pear', '배'), ('peach', '복숭아'), ('apple', '사과'), ('orange', '오렌지'), ('kiwi', '키위'), ('grapes', '포도')]

## 0일때 [('apple', '사과'), ('grapes', '포도'), ('kiwi', '키위'), ('mango', '망고'), ('orange', '오렌지'), ('peach', '복숭아'), ('pear', '배')]

# print(sorted(t_dic.items(),key=operator.itemgetter(0),reverse=True))
t_list=(sorted(t_dic.items(),key=operator.itemgetter(1)))
print(t_list)

# print(t_dic.keys()) key값
# print(t_dic.values()) value값
# print(t_dic.items())  튜플




# a=[5,7,4,8,1,9,3,2]
# a.sort()  #순차정렬
# print(a)
# print("-"*50)
# b=[5,7,4,8,1,9,3,2]
# b.sort(reverse=True) #역순정렬
# print(b)

#3개의 숫자를 입력받아 순서대로 출력하시오.
#17,50,12
#12,17,50

# num =[0,0,0]
# for i in range(3):
#     print(i)
#     num[i] = input(f"{i+1}번째 숫자를 입력하세요.")
# print("최대값 : ",max(*num))  #################3 
# print("최소값 : ",max(num[0],num[1],num[2]))
# num.sort()   
# print(num)
    
    ##num[i] = input(f"{i+1}번째 숫자를 입력하세요.") ;f포멧
    #input("{}번째 숫자를 입력하세요.".format(i+1))   ;f포멧
    

