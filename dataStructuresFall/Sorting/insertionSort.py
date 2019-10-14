# def insertionSort(a):
#     if not a or len(a) == 1:
#         return   

#     for i in range(1, len(a)):
#         val = a[i]
#         j = i-1
#         while j >= 0 and a[j] > val:
#             a[j], a[j+1] = val, a[j]
#             j -= 1
    
#     return a

# arr = [1,1,1,3,-17,2,7,0]
# print(insertionSort(arr))

def insertionSort(a):
    if not a or len(a) == 1:
        return

    for i in range(1, len(a)):
        j = i

        while j > 0 and a[j] < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]
            j -= 1 

def insertionSort(a):
    if not a or len(a) == 1:
        return

    for i in range(1, len(a)):
        
        j = i
        while j >= 1 and a[j] < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]
            j -= 1


arr = [1,1,1,3,-17,2,7,0]
insertionSort(arr)
print(arr)















