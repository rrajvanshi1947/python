def even_odd_transform(lst, n):
	for value in lst:
		if value%2 == 0:
			value -= 2*n
			continue
		value += 2*n
	return lst

print(even_odd_transform([1,4,3,6,7], 2))