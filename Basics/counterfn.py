from collections import Counter, defaultdict

a = [1,2,3,4,5,6,7,7,1,2,45,1,3,42, 6]

count = Counter(a)
print(count)
print(count[7])
print(count[55])
count[1] = 5
print(count)
print(a)
print(list(count.elements()))   # Ordered list

print(count.most_common(2))

b = [1,2,4,5,6,3,46,236,7]
count2 = Counter(b)
print(count+count2)
print(count-count2)

a = {'a': 3, 'b': 2}
print(list(a.items()))

a = defaultdict(bytes)
print(a[1])