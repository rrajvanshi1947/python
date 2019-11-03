def lengthOfLongestSubstring(self, s: str) -> int:
    if not s:
         return 0
        
    dic, arr = collections.defaultdict(int), []
    
    i = 0
    while i < len(s):
        for j in range(i, len(s)):
            if not dic[s[j]]:
                dic[s[j]] += 1
                if j == len(s)-1:
                    arr.append(len(dic.keys()))
                    return max(arr)

            else:
                arr.append(len(dic.keys()))
                dic.clear()
                if s[i] == s[j]:
                    break
                else:
                    for k in range(i+1, j):
                        if s[k] == s[j]:
                            i = k 
                            break
                    break
            
        i += 1
        
    # if dic:
    #     arr.append(len(dic.keys()))
        
    return max(arr)