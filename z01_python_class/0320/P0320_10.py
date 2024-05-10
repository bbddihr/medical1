print(range(10))
a=range(10)
print(a)

print(list(range(10)))
print([i for i in range(10)])


a_dic = {"a":"홍길동","b":"이순신","c":"유관순"}
for key in a_dic:
    print(a_dic[key])
for key in a_dic.keys():
    print(key)
for val in a_dic.values():
    print(val)
for k,v in a_dic.items():
    print(k,v)
    