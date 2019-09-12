# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You may assume no duplicates in the array.

# Example 1:

# Input: [1,3,5,6], 5
# Output: 2
# Example 2:

# Input: [1,3,5,6], 2
# Output: 1
# Example 3:

# Input: [1,3,5,6], 7
# Output: 4
# Example 4:

# Input: [1,3,5,6], 0
# Output: 0

class Solution(object):

    def recursion(self, nums, target):
        if nums[len(nums)//2] > target:
            return searchInsert(nums[:len(nums)//2], target)
        elif nums[len(nums)//2] < target:
            return searchInsert(nums[len(nums)//2:], target)
        else:
            return num[len(nums)//2]


    def searchInsert(self, nums, target):
        num = recursion(nums, target)
        return nums.index
        
        # if len(nums) == 2:
        #     return nums[0]

        
array = [0,1,1,2,2,2,3,4,5]
example = Solution()
print(example.removeDuplicates(array))
print(array)