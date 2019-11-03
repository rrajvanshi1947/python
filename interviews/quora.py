def solution(arr, k, s):
    if not arr:
        return 0
    
    summ = [sum(arr[:i]) for i in range(k, 0, -1)]
    count = summ.count(s)
    print(summ)

    for i in range(1, len(arr)-k+1):
        for j in range(len(summ)):
            summ[j] = summ[j] - arr[i-1] + arr[i+k-j-1]
            if summ[j] == s:
                count += 1
        print(summ)

    summ2 = sum(arr[len(arr)-k+1:])
    if summ2 == s:
        count += 1

    i = len(arr)-1
    while i != len(arr)-k+1:
        if summ2 - arr[i] == s:
            count += 1
            
        summ2 -= arr[i]
        i -= 1

    return count

print(solution([1,2,4,-1,6,1,2,10, 11,23,0,1023], 3, 6))
print(sum([1]))