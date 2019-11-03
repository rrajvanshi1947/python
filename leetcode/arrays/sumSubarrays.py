import math, heapq
def sol(arr, k):
    if not arr:
        return 0

    a = [0]*(len(arr)-k+1)
    summ = sum(arr[:k])
    a[0] = summ
    for i in range(1,len(arr)-k+1):
        # print(summ, arr[i+k-1], a[i-1])
        a[i] = summ + arr[i+k-1] -arr[i-1]
        # print(a[i])
        summ += arr[i+k-1] - arr[i-1]
    return a

print(sol([1,2,3],2))

def sol2(arr, k):
    if not arr:
        return None

    ans = len(arr)
    total = i = j = 0
    while total <= k and j < len(arr):
        total += arr[i]
        if total == k:
            ans = min(ans, j-i+1)
            total = 0
        j += 1

def brokenCalc(X, Y):
    ans = 0
    while Y > X:
        ans += 1
        if Y%2: Y += 1
        else: Y //= 2
    return ans + X-Y    

print(brokenCalc(13,43))

def s(string):
    lst = list(string)
    lst = list(dict.fromkeys(lst))
    return lst

print(s('hello'))

a = [2,345,12,56,1]
heapq.heapify(a)
while len(a) != 3:
    heapq.heappop(a)
print(a)
print(heapq.heappushpop(a, 2))
print(a)

a= 'rasd'
b = a[::-1]
print(b)