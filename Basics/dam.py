# def h(pos, heights):
#     if not pos or not heights:
#         return 0

#     arr = []
#     for i in range(1, len(pos)-1):
#         if pos[i] == pos[i+1] - 1:
#             continue
        
#         if heights[i] == heights[i+1]:
#             arr.append(heights[i] + math.ceil(abs(pos[i] - pos[i+1])/2))
#         else:
#             # if pos[i+1] - pos[i] < abs(heights[i] - heights[i+1]):
#             #     arr.append(max(heights[i], heights[i+1]) - 1)
#             if pos[i+1] - pos[i] == abs(heights[i] - heights[i+1]):
#                 arr.append(max(heights[i], heights[i+1])-1)
#             else:
#                 arr.append(max(heights[i] - heights[i+1]) + math.ceil(abs(heights[i] - heights[i+1])/4))

#     return max(arr)

a = 1
b = int(a)
print(b)
        