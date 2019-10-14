def minimumTotal(triangle):
    """
    :type triangle: List[List[int]]
    :rtype: int
    """
    if not triangle:
        return None
    
    sum = 0
    for lis in triangle:
        if lis:
            sum += min(lis)
        
    return sum

a = [[-1],[2,3],[1,-1,-3]]
print(minimumTotal(a))