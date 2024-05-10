import operator

fruits = [
    "apple","banana","kiwi","pear","peach",
    "apple","apple","kiwi","kiwi","peach", "peach",
    "apple","pear","apple","apple","pear","pear","pear",
     "peach", "banana","banana"   ]
#######포멧알아두기
counter={}


for f in fruits:
    if f not in counter:
        counter[f] = 0
    counter[f] += 1
    
print(counter)
#{'apple': 6, 'banana': 3, 'kiwi': 3, 'pear': 5, 'peach': 4}
print("-"*50)
print(counter.items())
dict_items([('apple', 6), ('banana', 3), ('kiwi', 3), ('pear', 5), ('peach', 4)])
# print(sorted(counter.items(),key=operator.itemgetter(0))) #튜플형태 
#print(sorted(counter.items(),key=operator.itemgetter(0),reverse=True)) #튜플형태 

# numbers = [1,2,3,4,5,5,6,7,4,3,2,12,67,8,9]

# counter={}

# for n in numbers:
#     if n not in counter:
#         counter[n] = 0
#     counter[n] += 1
    
# print(counter)