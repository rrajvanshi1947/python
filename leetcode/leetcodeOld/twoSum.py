# Two numbers add to a specific target

# def targetSum(list, target):
#     reqList = []
#     for i in range(0, len(list)):
#         for j in range(i+1, len(list)):
#             if list[i]+list[j] == target:
#                 reqList = [list[i], list[j]]
#                 return reqList 
#     return 'No solution'

# print(targetSum([1,2,3,4,5,6,7,8,9], 12 ))


def twoSum(nums, target):
    ourdict = {}
    for i in range(0, len(nums)):
        if target - nums[i] not in ourdict:
            ourdict[nums[i]] = i
        else:
            return [ourdict[target - nums[i]], i]

print(twoSum([1,2,3,4,5,6,7,8,9], 12 ))


#Function to find duplicates. Dictionary provide an efficient way for lookups saving time.
# def findDuplicate(givenList):
#     ourDict = {}
#     List = []
#     for item in givenList:
#         if item not in ourDict:
#             ourDict[item] = 1
#         else:
#             List.append(item)
#     return List
