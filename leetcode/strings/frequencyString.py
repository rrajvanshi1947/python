def f( s):
        if not s:
            return 0
        
        dic = {}
        order = 200
        for char in s:
            if ord(char) < order:
                order = ord(char)
                dic = {char: 1}
            elif ord(char) == order:
                dic[char] += 1
                
        return list(dic.values())[0]
    
def numSmallerByFrequency(queries, words):
    if not queries or not words:
        return []
    
    arr = [0]*len(queries)
    for i in range(len(queries)):
        value = f(queries[i])
        for j in range(len(words)):
            if value < f(words[j]):
                arr[i] += 1
                
    return arr

a = ['ccbd', 'aaaaaaa']
b = ["zaaaz", 'a', 'aaaa', 'bdcc', 'ddddddd']
print(numSmallerByFrequency(a, b))