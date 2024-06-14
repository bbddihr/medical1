import pandas as pd
df=pd.read_excel('score.xlsx',index_col='지원번호')
df

df.describe()  #컬럼별 대략적인 정보, 최소값,최대값,평균 등 확인 
df.head()  #상단 5개 출력
df.tail()   #하단 5개 출력
df.values    #컬럼별 타입,크기 정보
df.index      #rows데이터 배열로 출력
df.info()      #index 정보
df.columns      #컬럼정보
df.shape         #데이터 크기 정보

df['키'].min()
