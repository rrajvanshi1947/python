# def wordBreak(s, wordDict): 
#     def f(wordDict, arr):
#         for word in arr:
#                 a = len(arr)
#                 if word:
#                     for i in range(len(wordDict)):
#                         if wordDict[i] in word:
#                             arr += word.split(wordDict[i])
#                             print(arr)
#                             print(len(arr))
#                             arr = [i for i in arr if i]
#                             print(arr)
#                             print(len(arr))
#                             break
#                         if i == len(wordDict)-1:
#                             print(len(arr))
#                             print(word)
#                             return False
                        
#                 # if a == len(arr):
#                 #     return False
                
#                 # arr = [i for i in arr if i]


#         return True
                
#     arr = []
#     for word in wordDict:
#         if word in s:
#             arr = s.split(word)
#             arr = [i for i in arr if i]
#             break
#     print(arr)
#     if not arr:
#         return False 
    
#     return f(wordDict, arr)

s = 'leetcode'
q = [s]
print(q)
# dic = ['leet', 'code']
# print(wordBreak(s, dic))