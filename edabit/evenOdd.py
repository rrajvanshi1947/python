def even_odd_transform(lst, n):
	# for value in lst:
	# 	if value%2 == 0:
	# 		value -= 2*n
	# 		continue
	# 	value += 2*n
	# return lst

	lst = [ value + 2*n if value%2 == 1 else value - 2*n for value in lst ]
	return lst

print(even_odd_transform([1,4,3,6,7], 2))

arr = [1,4,3,6,7]