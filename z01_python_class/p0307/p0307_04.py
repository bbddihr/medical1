stuInfo = {"stuNo": 1,"id":"aaa", 
           "pass":"1111","name":"홍길동",
           "nicName":"길동스"}

#print(stuInfo["tel"]) 없는 키값 입력하면 에러 
print(stuInfo.get("tel")) #None 으로 출력

