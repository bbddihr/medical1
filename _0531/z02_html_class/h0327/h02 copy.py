##파일을 읽어와서 출력하시오.
#파일열기
#상대경로:medical1 폴더안
with open("c:/workspace/medical1/h0327/aaa/member1.csv","r",encoding="utf-8") as f:
    while True:
        txt=f.readline()
        if txt=="": break
        mem=txt.split(",")
        print(mem[0],mem[1]) 
    



