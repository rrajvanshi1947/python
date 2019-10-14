import math
def countPrimes(n):
    if n <= 1:
        return 0
    
    # count = 0
    arr = [2]
    i = 3
    while i < n:
        for j in range(len(arr)):
                if i%arr[j]:
                    continue
                else:
                    i += 2
                    break
                    
                if j == len(arr)-1:
                    arr.append(i)
                    
    return len(arr)

# print(countPrimes(5))

# print(round(math.sqrt(10)))
# print([1,22,3,3].count(0))
a = '         '
print(a.split())
print(bin(int('101',2) - int('10', 2))[2:])