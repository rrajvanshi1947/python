import math
def findPairs(nums, k):
    if not nums or k < 0:
            return 0
        
        # if k == 0:
        #     return len(nums)
        
        # nums = list(set(nums))
    dic = {}
    count = 0
    for i in range(len(nums)):
        for j in  range(i+1, len(nums)):
            if nums[i] - nums[j] in (k, -k):
                if (nums[i], nums[j]) in dic or (nums[j], nums[i]) in dic:
                    pass
                else:
                    count += 1
                    dic[(nums[i], nums[j])] = dic[(nums[j], nums[i])] = 1
                
    return count

a = [3,1,4,1,5]
print(findPairs(a, 2))

n = 1
def f(n):
    return False if n else True
print(f(n))

print(int(math.log10(10)))
a = 'abc'
print(a.split())
print(ord('A'), ord('a'))