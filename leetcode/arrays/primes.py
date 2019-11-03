import math 

def checkPrime(n):
    if n <= 1:
        return False

    arr = [0]*2 + [1 for i in range(2, int(n**0.5) + 1)]
    for i in range(len(arr)):
        if arr[i]:
            if n//i == n/i:
                return False
            for j in range(2*i, len(arr), i):
                arr[j] = 0

    return True

print(checkPrime(213))


print(int(math.log10(10)))