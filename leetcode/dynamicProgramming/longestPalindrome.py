def longestPalindrome(s):
    # if not s or len(s) == 1 or len(s) == 2 and s[0] == s[-1]:
    #     return s
    # elif len(s) == 2 and s[0] != s[-1]:
    #     return s[0]
    
    string = s[0]
    arr = [[0]*len(s) for i in range(len(s))]
    for i in range(len(s)):
        arr[i][i] = 1
    i = 0
    while i < len(s)-1:
        if s[i] == s[i+1]:
            arr[i][i+1] = 1
            string = max(string, s[i:i+2], key=len)
        i += 1
    
    k = 2
    while k < len(s):
        i, j = 0, k
        while j < len(s):
            if s[i] == s[j] and arr[i+1][j-1]:
                arr[i][j] = 1
                string = max(string, s[i:j+1], key=len)
            i += 1
            j += 1
        k += 1
    # print(arr)
    return string

# print(longestPalindrome(''))

a = ['c', 'a', 'd']
i = 0
while i < len(a):
    print('asd')
    # a[1:3] = 'b'
    i += 1

print(a)

[[".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".","."],
[".",".",".","R",".",".",".","."],
[".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".","."]]