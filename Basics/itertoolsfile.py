import itertools

data = 'abbcddaaafffccg'

# keys = groups = lengths = []
sorte = sorted(data)
print(sorte)
keys = [(k, len(list(g))) for k, g in itertools.groupby(data)]
print(keys)
groups = [list(g) for k, g in itertools.groupby(data)]
print(groups)

# print(keys, '\n')
# print(groups, '\n')
# print(lengths, '\n')
a = [('a', 1), ('b', 2)]
print(a[0][1])
b = 'adf'
c = 'a'
# print(b[0].ASCIIcode())
print(ord('A'), ord('z'))
if c <= 'z':
    print('here')
d = 'a'

if 1 != 1 and 2 != 2:
    print('1')
elif 3 == 3:
    print('2')
elif 4 == 4:
    print('3')

s = z = 0
s += 5 if 1==1 else  -7
print(s, z)

a = [2,2,3]
a = [1]+ a
print(a)

f = float('-inf')
print(f)

if f == '-inf':
    print('jas')

a = [1,2,4]
b = [1,0,0,1,0]
# for el in a:
# b.remove(0)
# b = b - [1]
b.extend([3]*2)
print(b)
print(-0)

print('!'.isalnum())