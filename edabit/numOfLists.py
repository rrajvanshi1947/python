def num_of_sublists(lst):
	return sum((1 for item in lst if type(item) == list))

def num_of_sublists(lst):
	return sum(isinstance(i, list) for i in lst)

t1 = time.clock()
num_of_sublists([])
t2 = time.clock()