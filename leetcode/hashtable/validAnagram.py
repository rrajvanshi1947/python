def isAnagram(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    dic = {}
    for char in s:
        if char not in dic:
            dic[char] = 1
        else:
            dic[char] += 1
            
    for char in t:
        if char not in dic:
            return False
        else:
            dic[char] -= 1
            
    for k,v in dic.items():
        if v != 0:
            return False
    
    return True