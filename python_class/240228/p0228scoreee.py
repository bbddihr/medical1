score = [[80,90,85], [70,80,90],[84,92,80],[72,81,76]]
name = ['홍길동','유관순','이순신','김구']
total = []

for i in range(len(score)):
    
    for j in range(len(score[i])):
        print(score[i][j])
print()

for i in range(len(score)):
    s=0
    for j in range(len(score[i])):
        s=s+score[i][j] 
    print(s)
    total.append(s)
print(total)

for i in range(4):
    if total[i]


