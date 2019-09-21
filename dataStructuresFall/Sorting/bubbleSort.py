def bubbleSort(a):
    if not a or len(a) == 1:
        return a

    for i in range(len(a)):
        for j in range(len(a)-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

arr = [2,4,1,3,7]
print(bubbleSort(arr))