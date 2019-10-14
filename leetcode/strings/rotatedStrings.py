# def rotatedDigits(N):
    
#     dic1 = {0, 1, 8}
#     dic2 = {2,5,6,9}
#     count = 0
    
#     for num in range(1, N+1):
#         temp = num
#         flag = 0
#         print(temp)
#         while temp:
#             digit = temp%10
#             print(digit)
#             if digit in dic1:
#                 print('dic1')
#                 flag += 1
#             elif digit in (3,4,7):
#                 print('here')
#                 flag = len(str(num))
#                 break
                
#             temp = temp//10
        
#         if flag == len(str(num)):
#             continue
#         else:
#             count += 1
    
#     return count

# print(rotatedDigits(10))        
    
# for char in range('a', 'z'):
    # print(char)

a = ['hello', 'sedf']
for i in range(len(a)):
    a[i] = a[i].replace('e', 'a')
print(a)
a = {1,2,3}
print(str(a))
b = 'aaaavvveeevfbff'