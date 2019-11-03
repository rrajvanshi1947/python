def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """

    # nums = 1
    # print(nums[len(nums)-k:] + nums[:len(nums)-k])
    # a = nums[len(nums)-k:] + nums[:len(nums)-k]
    # print(a)
    nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k]
    # print(nums)

a = [_ for _ in range(1,11)]
rotate(a, 3)
print(a)

a = 'abc'
b = list(a)
print(b)