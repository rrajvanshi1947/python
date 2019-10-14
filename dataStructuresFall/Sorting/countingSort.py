#This won't work for negative numbers

# def countingSort(a):
#     if not a or len(a) == 0:
#         return a

#     count = [0]*(max(a)+1)
#     for i in range(len(a)):
#         count[a[i]] += 1

#     # sort = []
#     for i in range(len(count)):
#         if count[i] != 0:
#             temp = count[i]
#             while temp != 0:
#                 print(i, end= ' ')
#                 temp -= 1

def countingSort(a):
    if not a or len(a) == 1:
        return a

    count = [0]*(max(a)+1000)
    for i in range(len(a)):
        count[a[i]] += 1

    for i in range(1, len(count)):
        count[i] += count[i-1]


    sorte = [0]*len(a)
    for i in range(len(a)):
        sorte[count[a[i]]-1] = a[i]
        count[a[i]] -= 1

    return sorte


arr = [1,4,1,2,100,5,2]
print(countingSort(arr))