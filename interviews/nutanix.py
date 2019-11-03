def solution(A, B, m, x, y):
    if not A:
        return 0
    
    count = 1
    wt = 0
    
    if len(A) <= x:
        wt = sum(A)
    else:
        wt = sum(A[:x])
    takenCont = min(x, len(A))
    if wt > y:
        i = x-1
        while wt > y:
            wt -= A[i]
            takenCont = i
            i -= 1
    
    count +=  min(len(B[:takenCont]), len(set(B[:takenCont])))
    if takenCont < len(A):
        A, B = A[takenCont:], B[takenCont:]
        return count + solution(A, B, m, x, y)
    else:
        return count
    

print(solution([100, 30, 50], [2,1,3], 5, 2, 150))