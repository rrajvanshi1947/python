def partition(a, low, high):
    index = low
    for i in range(low, high):
        if a[i] <= a[high]:
            a[i], a[index] = a[index], a[i]
            index += 1
    
    a[index], a[high] = a[high], a[index]
    return index


def quickSort(a, low, high):
    if low < high:
        index = partition(a, low, high)
        quickSort(a, low, index-1)
        quickSort(a, index+1, high)

arr = [170, 45, 75, 90, 802, 24, 2, 66] 
quickSort(arr, 0, len(arr)-1)
print(arr)
