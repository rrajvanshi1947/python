def longestCommon(a, b):
    m = len(a)
    n = len(b)
    if m == 0 or n == 0:
        return 0

    arr2d = [[0]*(n+1)]*(m+1)

    for i in range(m):
        for j in range(n):
            if a[i] == b[j]:
                arr2d[i+1][j+1] = arr2d[i][j] + 1
            else:
                arr2d[i+1][j+1] = max(arr2d[i+1][j+1])
