# def bubbleSort(a):
#     if not a or len(a) == 1:
#         return a

#     for i in range(len(a)):
#         for j in range(len(a)-1-i):
#             if a[j] > a[j+1]:
#                 a[j], a[j+1] = a[j+1], a[j]
#     return a

# arr = [2,4,1,3,7]
# print(bubbleSort(arr))

# def bubbleSort(a):
#     if not a or len(a) == 1:
#         return

#     for j in range(len(a)):
#         for i in range(len(a)-j-1):
#             if a[i] > a[i+1]:
#                 a[i], a[i+1] = a[i+1], a[i]

def bubbleSort(a):
    if not a or len(a) == 1:
        return

    for j in range(len(a)):
        for i in range(len(a)-1-j):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]


arr = [2,4,1,3,7,3,2]
bubbleSort(arr)
print(arr)

















