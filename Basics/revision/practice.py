import memory_profiler as mem_profile
import time

print('Memory (Before): ' + str(mem_profile.memory_usage()) + 'MB')
print(time.clock())

arr = []
for _ in range(100000):
    arr.append(_)

print(arr[0])

print('Memory (After): ' + str(mem_profile.memory_usage()) + 'MB')
print(time.clock())
arr = arr[:-50000]
print('Memory (After): ' + str(mem_profile.memory_usage()) + 'MB')
print(time.clock())

# print(r"C:\\\"raj\\no\"entry")

# a = [1,2]    
# b = [1,2]
# print(a==b)
# print(a is b)
# print(id(a))
# print(id(b))

# print('a is {} and b is {}'.format(a, b))

for i in range(1, 11):
    if i%2 == 0:
        print(i-1, end= ' ')
    else:
        print(i+1, end= ' ')