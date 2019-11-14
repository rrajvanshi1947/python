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

arr = [[0]*6 for i in range(6)]
for i in range(6):
    arr[i][i] = 1
print(arr)


        # if s =="":
        #     return s
        # length=''
        # s1=s[::-1]
 
        # for c,i in enumerate(s):
        #     for m,j in enumerate(s1):
        #         if i == j:
        #             temp=s[c:len(s)-m]
        #             if temp == temp[::-1]:
        #                 length = max(length, temp, key = len)
        #                 break
        
        # return length
                    
