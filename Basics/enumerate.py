arr = ['su', 'bm', 'me', 'ta', 'gm', 'vw', 'fe', 'ch']

# for item in enumerate(arr):
#     print(item)

# for item in enumerate(arr, 4):
#     print(item)

for index, item in enumerate(arr):
    print("Index: {}, Item: {}".format(index, item))

dic = dict(enumerate(arr))
print(dic)

a = [(i, j) for i, j in enumerate(dic)]
print(a)

dic2 = {'a':1, 'b':2, 'c':3}
print(sorted(dic2.keys()))
b = [(i,j) for i,j in enumerate(dic2)]
print(b)

# dic1 = dict(arr)
# print(dic1)

a = [1,2]
z = [3,4]
print(sum((a,z),[]))
print(a.pop(-1))

c = ['a', 'b']
d = ['e', 'f']
print([i for i in zip(c,d)])
k, l = zip(*zip(c, d))
print(k, l)

print('G'.join(c).join(d).join(['h', 'i']))
print(int('1000',2))