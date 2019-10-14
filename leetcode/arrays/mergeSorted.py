def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    
    # for i in range(m+n):
    i = k = 0
    while i < m+n and k < n:
        if not nums2:
            return
        
        if not nums1[i]:
            break
        
        if nums1[i] > nums2[k]:
            temp = nums1[i]
            nums1[i] = nums2[k]
            k += 1
            print(i+1,m+i-1)
            if i+1 == m+i-1:
                nums1[i+1], temp =  temp, nums1[i+1]

            for z in range(i+1,m+i-1):
                print('here')
                nums1[z], temp =  temp, nums1[z]
                
        i += 1
        
    while k < n:
        nums1[i] = nums2[k]
        k += 1
        i += 1

a = [2,0]

b = [1]

merge(a, 2, b, 1)
print(a)
