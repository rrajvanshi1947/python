# def selectionSort(a):
#     if not a or len(a) == 1:
#         return

#     for i in range(len(a)-1):

#         temp = a[i]
#         k = i
#         for j in range(i+1, len(a)):
#             if a[j] < temp:
#                 temp = a[j]
#                 k = j 
#         a[i], a[k] = a[k], a[i]
#     return

# arr = [2,4,1,3,7]
# selectionSort(arr)
# print(arr)


# def selectionSort(a):
#     if not a or len(a) == 1:
#         return

#     for i in range(len(a)-1):
#         temp = a[i]
#         k = i
#         for j in range(i+1, len(a)):
#             if a[j] < temp:
#                 temp = a[j]
#                 k = j
#         a[i], a[k] = temp, a[i]

def selectionSort(a):
    if not a or len(a) == 1:
        return

    for i in range(len(a)-1):
        temp = a[i]
        k = i
        for j in range(i+1, len(a)):
            if temp > a[j]:
                temp = a[j] 
                k = j
        
        a[i], a[k] = temp, a[i]

arr = [2,3,1,4,3,7]
selectionSort(arr)
print(arr)
















