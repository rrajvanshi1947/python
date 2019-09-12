def rmel(nums, val):
    for i in range(len(nums)):
        if nums[i] == val:
            nums = nums[:len(nums):i]
            while nums[i] == val:
                nums = nums[:len(nums):i]

a = [1,2,3,4,5,6,7,8,9,9,5,3,2]
rmel(a, 5)
print(a)