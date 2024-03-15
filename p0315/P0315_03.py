import P0315_02

member = P0315_02.idpw()
print(member)

# mem.txt 파일에 
#aaa,1111 저장하시오

f=open("mem.txt","w")
f.write("aaa,1111\n")
f.write("bbb,2222\n")
f.write("ccc,3333\n")


f.close()
print("파일이 저장되었습니다.")
