def longest(a):
    if not a:
        return 0
    elif len(a) == 1:
        return 1

    longestArr = [1]*len(a)

    for i in range(1, len(a)):
        for j in range(0, i):
            if a[j] <= a[i]:
                longestArr[i] = max(longestArr[i], longestArr[j]+1)
                
    return max(longestArr)



a = [10,22,9,33,21,22,23,24,50,60]
print(longest(a))
