one, two, three = [1,2,3]
print(one)

first, *middle, last = [54,89,74,25,62,58,53,87]

print(middle[0])
print(sum(middle)//len(middle))

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

list3 = zip(list1, list2)
print(list3)

for a,b in list3:
    print(a+b)