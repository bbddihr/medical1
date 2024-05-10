#기본구문-복사해서쓰기________________________________________________________________________
#res= requests.get("http://www.google.com")
import requests   #웹정보,소스 가져오는 라이브러리
#url="http://www.google.com"
url="http://www.melon.com"
res=requests.get("http://www.melon.com")
res.raise_for_status()   #에러코드 발생시 프로그램을 종료 200 ---->
#_________________________________________________________________________

print(res.status_code)  #응답코드 값 200,404, 406...

if res.status_code ==requests.codes.OK:  #응답코드:200과 같다.
    print("정상적인 페이지 호출")
else:
    print("접근할 수 없음 [에러코드: ]",res.status_code,"]")
    