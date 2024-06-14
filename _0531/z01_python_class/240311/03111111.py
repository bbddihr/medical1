import operator

fruits = [
    "apple","banana","kiwi","pear","peach",
    "apple","apple","kiwi","kiwi","peach", "peach",   
    "apple","pear","apple","apple","pear","pear","pear",      
     "peach", "banana","banana" ]

counter = {}


for f in fruits:
    if f not in counter:
        counter[f] = 0
    counter[f] += 1
    
print(counter)
