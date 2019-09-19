def sumLists(*args):
    print(sum(args, []))

a = [1,2,3,4,2,1]
b = [2,3]
c = [3,4]

sumLists(a,b,c)

print(sum(a[:2]))

print(round(51.2, 2))

def accumulate(lst):
    # return [ sum(lst[:lst.index(x)+1]) for x in lst ]
    return [ sum(lst[:i+1]) for i in range(len(lst)) ]

print(accumulate(a))

def findRepeat(lst):
    return [ lst[i] for i in range(len(lst)) if lst[i] in lst[i+1:] ]

print(findRepeat(a))