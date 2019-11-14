def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    arr = [None]*(len(nums1)+len(nums2))
    i = j = k = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            arr[k] = nums1[i]
            i += 1
        else:
            arr[k] = nums2[j]
            j += 1
        k += 1
        
    while i < len(nums1):
        arr[k] = nums1[i]
        i += 1
        k += 1
    while j < len(nums2):
        arr[k] = nums2[j]
        j += 1
        k += 1
    
    # print(arr)
    if len(arr)%2:
        return arr[len(arr)//2]
    else:
        return (arr[len(arr)//2]+arr[len(arr)//2-1])/2

a, b = [1,2], [4,6]
print(findMedianSortedArrays(a,b))

z = ['a', 'b', '.', 'c']
print(''.join(z).replace('.',''))

a = {(i,1) for i in range(5)}
print(a)