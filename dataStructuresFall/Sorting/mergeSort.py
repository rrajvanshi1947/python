# def mergeSort(a):

#     if len(a) > 1:
#         left = a[:len(a)//2]
#         right = a[len(a)//2:]

#         mergeSort(left)
#         mergeSort(right)

#         i = j = k = 0
#         while i < len(left) and j < len(right):
#             if left[i] <= right[j]:
#                 a[k] = left[i]
#                 i += 1
#             else:
#                 a[k] = right[j]
#                 j += 1
#             k += 1
        
#         while i < len(left):
#             a[k] = left[i]
#             i += 1
#             k += 1
#         while j < len(right):
#             a[k] = right[j]
#             j += 1
#             k += 1



# arr = [2,1,4,3,556, 3, 12,4521,0]
# mergeSort(arr)
# print(arr)

# def mergeSort(a):
#     if len(a) > 1:
#         left = a[:len(a)//2]
#         right = a[len(a)//2:]

#         mergeSort(left)
#         mergeSort(right)

#         i = j = k = 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 a[k] = left[i]
#                 i += 1
#             else:
#                 a[k] = right[j]
#                 j += 1
#             k +=1

#         while i < len(left):
#             a[k] = left[i]
#             i += 1
#             k += 1
#         while j < len(right):
#             a[k] = right[j]
#             j += 1
#             k += 1

def mergeSort(a):
    if len(a) <= 1:
        return 

    left = a[:len(a)//2]
    right = a[len(a)//2:]
    mergeSort(left)
    mergeSort(right)

    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        a[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        a[k] = right[j]
        j += 1
        k += 1

    # return a

arr = [2,1,4,3,556, 3, 12,4521,0]
mergeSort(arr)
print(arr)














