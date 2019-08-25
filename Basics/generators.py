#Square numbers in a list

# def square(nums):
#     for i in nums:
#         yield i*i

# result = list(square([1,2,3,4,5]))
# print(result)

result = (x**2 for x in [1,2,3,4,5])        #Also gives a generator
print(result)



import mem_profile
import random
import time

print('Memory (Before): {}Mb'.format(mem_profile.memory_usage_psutil()))
t1 = time.clock()