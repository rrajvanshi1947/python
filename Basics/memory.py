import memory_profiler as mem_profile
import time

print('Memory (Before): ' + str(mem_profile.memory_usage()) + 'MB' )
t1 = time.clock()

arr = []
for _ in range(100000):
    arr.append(_)

print(arr[0])

print('Memory (After): ' + str(mem_profile.memory_usage()) + 'MB' )
print(time.clock())
arr = arr[:-50000]
print('Memory (After): ' + str(mem_profile.memory_usage()) + 'MB' )
t1 = time.clock()
print((t2-t1)*1000, 'ms')