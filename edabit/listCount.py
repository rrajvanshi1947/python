# import mem_profile
import random
import time



# def return_unique(lst):
#   return [i for i in lst if lst.count(i)==1]

a = []
for i in range(1000):
    a.append(1)
a += [2,3]




  #Preffered Solution
# from collections import OrderedDict
def  return_unique(lst):
    d= dict()
    for a in lst:
        if a not in d:
            d[a]=1
        else:
            d[a]+=1
    return [i for i,v in d.items() if v==1]

t1 = time.clock()
print(return_unique(a))
t2 = time.clock()
print(t2-t1)

