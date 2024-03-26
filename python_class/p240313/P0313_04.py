#
'''
import lotto
#import math -> 사용방법  math.floor() 이름.함수명()
from math import *  #이름 생략가능

from lotto import num_generate
#====같은말 lotto.num_generate(l)

import math as m #모듈명을 줄여서 사용가능.별칭부여
import lotto as lo  
'''
import math
import math as m
print(dir(m))


'''
l=[0]*45


# while True:
#     lotto.screen()
lo.screen(1)
lo.num_generate(1)

#ceil - 올림
print(m.ceil(12.2)) #13
#floor -버림
print(m.floor(12.9))  #12
#round- 반올림
print(round(12.6)) #13
'''