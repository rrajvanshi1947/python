def maxSum(a):
    arr = [[0]*(i+1) for i in range(len(a))]
    arr[0] = [a[0]]
    for i in range(1,len(a)):
        for j in range(len(a[:i])+1):
            if j == i:
                arr[i][j] = a[i]
                continue
            arr[i][j] = arr[i-1][j]+a[i] 
    maxArr = []
    for item in arr:
        maxArr.append(max(item))
    val = max(maxArr)
    index = maxArr.index(val)
    return (a[arr[index].index(val):index+1], val)

a = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSum(a))