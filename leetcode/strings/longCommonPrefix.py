# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         if len(strs) == 0:
#             return '' 
#         res = ''
#         strs = sorted(strs)
#         for i in strs[0]:
#             if strs[-1].startswith(res+i):
#                 res += i
#             else:
#                 break
#         return res

# example = Solution()
# arr = ['msdf', 'dfms', 'df']
# print(example.longestCommonPrefix('MCMXCIV'))


#         prefixList = []
#         for i in range(len(strs[0])):
#             if strs[0][i] in strs[1]:
#                 prefixList += strs[0][i]
#                 secondIndex = strs[1].index(strs[0][i])
#                 for j in range(i+1, max(len(strs[1]), len(strs[0]))):
#                     if strs[0][j] == strs[1][secondIndex+1]:
#                         prefixList += strs[0][j]
#                         secondIndex += 1
#                         continue
#                     break
#         if not prefixList:
#             return ''
        
#         prefix = ''
#         for char in prefixList:
#             string += char
#         for string in strs:
#             if prefix in string:
#                 continue
#             return ''
#         return prefix


