def accumulating_list(lst):
	return [sum(lst[:i+1]) for i in range(len(lst) - 1)]

a = [1,1,1,1,1]
print(a[:3])
for num in a:
    print(a[:a.index(num)])


print(accumulating_list([1,2,1,1]))