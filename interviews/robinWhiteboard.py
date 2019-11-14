import math
def maxRepeat(nums):        # This is to find number which exists more than 50% of times
    num, count = nums[0], 1
    for i in range(1, len(nums)):
        if count == 0:
            num = nums[i]
            count = 1
        elif nums[i] == num:
            count += 1
        else:
            count -= 1
    print(count, num)
    return num
    
# print(maxRepeat([1,2,1,2,3,1,4,3,5,1]))

# Print all elements occuring more than n/3 times
def maxi(nums):
    num1 = num2 = None
    count1 = count2 = 0
    for i in range(len(nums)):
        if num1 is None and nums[i] != num2:
            print('here1', nums[i])
            num1 = nums[i]
            count1 = 1
        elif num2 is None and nums[i] != num1:
            print('here2', nums[i])
            num2 = nums[i]
            count2 = 1
        elif nums[i] not in (num1, num2):
            print('here3', nums[i])
            count1 -= 1
            if not count1:
                num1 = None
            count2 -= 1
            if not count2:
                num2 = None
        elif nums[i] in (num1, num2):
            print('here4', nums[i])
            if nums[i] == num1:
                count1 += 1
            else:
                count2 += 1
    
    count1 = count2 = 0
    for num in nums:
        if num == num1:
            count1 += 1
        elif num == num2:
            count2 += 1

    arr = []
    if count1 > len(nums)/3:
        arr.append(num1)
    if count2 > len(nums)/3:
        arr.append(num2)
    return arr


# print(maxi([2,2,1,3,3,1,3,1,1,1,2,2,2,2,2,2,1,1]))

# Function returns all combinations of 3 characters, permutations not needed.
def combinations(s, n):
    arr = []
    for i in range(len(s)-n+1):
        string = s[i:i+n-1]
        for j in range(i+n-1, len(s)):
            arr.append(string+s[j])
    return arr

print(combinations('abcde', 4))        