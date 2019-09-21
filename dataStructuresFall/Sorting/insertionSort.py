def insertionSort(a):
    if not a or len(a) == 1:
        return   

    for i in range(1, len(a)):
        val = a[i]
        j = i-1
        while j >= 0 and a[j] > val:
            a[j], a[j+1] = val, a[j]
            j -= 1
    
    return a

arr = [2,4,1,3,7,2,7,0]
print(insertionSort(arr))