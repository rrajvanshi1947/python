class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or target < nums[0]:
            return 0
        
        if len(nums) == 1 and target > nums[0]:
            return 1
        elif len(nums) == 1 and target <= nums[0]:
            return 0
        
        position = 0
        
        if target > nums[:len(nums)//2][-1] and target <= nums[len(nums)//2:][0]:
            return len(nums)//2
        # elif target == nums[:len(nums)//2][-1]:
        #     return 
        elif target > nums[:len(nums)//2][-1]:
            position = self.searchInsert(nums[len(nums)//2:], target)
            return len(nums)//2 + position
        elif target < nums[len(nums)//2:][0]:
            position = self.searchInsert(nums[:len(nums)//2], target)
            if position == 0:
                position -= 1
                return (len(nums)//2) + position
            print(position, len(nums))
            return (len(nums)//2) - position

a = Solution()
print(a.searchInsert([1,3], 1))