
    
def num_input(my_lotto):
    print("[나의 로또번호입력]")
    for i in range(6):
        my_num=int(input(f"{i+1}번째 로또번호를 입력하세요.>>"))
        my_lotto[i]=my_num
    print("내가 입력한 번호 : ",my_lotto)

def num_check(lotto,lucky_lotto,my_lotto,win_num,win_amount):
    #win_num=[]  (초기화 여기서 하면 안됨. 주소값을 다시만듦)
     for i in range(6):
         lucky_lotto[i] = lotto[i]
     print("[ 번호 확인]")
     print("로또번호: ", lucky_lotto)            
     print("내가 입력한 번호: ",my_lotto)
#몇개 맟췃는지 확인소스
     for i in my_lotto:
         if i in lucky_lotto:
             win_num.append(i)
     print("당첨된 번호는",win_num)
#당첨금액 출력 
     print("당첨금액 : {:,d} 원".format(win_amount[len(win_num)]))