def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    
    temp = n
    dic = {}
    
    while temp != 1 and temp not in dic:
        dic[temp] = 1
        a = temp
        arr =[]
        while a:
            arr.append(a%10)
            a = a//10
            
        temp = 0
        for el in arr:
            temp += el**2
                
        
    if temp == 1:
        return True
    else:
        return False
# # print(isHappy(20))
dic = {1: 1}
dic['b'] = 2
print(dic)