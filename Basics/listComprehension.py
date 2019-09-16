a = [value**2%5 for value in range(1, 10)]

print(a)

b = [2,3,4]
c = [5,6,7]
e = [8,9,10]
d = [(a,b,f) for a in b for b in c for f in e]
print(d)