#프로그램 구현중에 잘못된 코드 : 구문 오류
print("[리스트 출력 프로그램]")
#예외처리를 하면 오류가 나더라도 
#프로그램이 종료되지않음 
#런타임 오류 : 프로그램 실행 중에 발생하는 오류
# while True:
try: #오류가 발생될것같은 지점
    num = int(input("숫자를 입력하세요."))
    a_list=[1,2,3,4,5]
    for i in range(int(num)):
        print(a_list[i])
except:
    print("구문에 오류가 났습니다.")

