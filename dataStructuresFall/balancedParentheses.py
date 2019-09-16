import memory_profiler as mem_profile
import time

def checkBalance(string):
    arr = []
    for char in string:
        if char in ['{', '[', '(']:
            arr.append(char)
        elif char is '}':
            if arr[-1] == '{':
                arr.pop()
                continue
            else:
                return 'Unbalanced'
        elif char is ')':
            if arr[-1] == '(':
                arr.pop()
                continue
            else:
                return 'Unbalanced'
        elif char is ']':
            if arr[-1] == '[':
                arr.pop()
                continue
            else:
                return 'Unbalanced'
    return 'Balanced' if not arr else 'Unbalanced'

print('Memory (Before): ' + str(mem_profile.memory_usage()) + 'MB' )
t1 = time.clock()

f = open('x.txt', 'r')
fr = f.read()
f.close()
print(checkBalance(fr))

print('Memory (After): ' + str(mem_profile.memory_usage()) + 'MB' )
t2 = time.clock()
print((t2-t1)*1000, 'ms')