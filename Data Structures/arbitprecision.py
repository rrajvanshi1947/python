# A = [9,9,9,9,9,9,9]

# # for i in reversed(range(0, 10)):
# #     print(i)

# # def func(a):
# #     a[len(a)-1] = 0
# #     if a[len(a)-2] == 9:
# #         func(a[:len(a)-1])
# #     a[len(a)-2] += 1
# #     return a

# # def func(a):
# #     if 0 <= a[len(a)-2] < 9:
# #         a[len(a)-1] = 0
# #         a[len(a)-2] += 1
# #         return a
# #     a = func(a[:len(a)-1])
# #     a.append(0)
# #     return a

# # def increment(a):
# #     flag = False
# #     for el in a:
# #         if el == 9:
# #             flag = True
# #         else:
# #             flag = False
# #             break
# #     if flag == True:
# #         new_a = [1]
# #         for i in range(len(a)):
# #             new_a.append(0)
# #         return new_a

# #     if 0 <= a[len(a)-1] < 9:
# #         a[len(a)-1] += 1
# #         return a
# #     else:
# #         a = func(a)
# #         return a

# #his way
# def increment(a):
#     A[-1] += 1
#     for i in reversed(range(1,len(a))):
#         if A[i] != 10:
#             return A
#         A[i] = 0
#         A[i-1] += 1
#     if A[0] == 10:
#         A[0] = 1
#         A.append(0)
#         return A
#     return A



    
    

# print(increment(A))

def arbitPrecision(arr):
    string = ''
    for value in arr:
        string += str(value)
    number = int(string) + 1 
    returnedArr = []
    strArray = str(number)
    for i in range(len(strArray)):
        returnedArr += int(strArray[i])
    return returnedArr
print(arbitPrecision([1,2,2]))