def solution(arr):
    if not arr:
        return None

    x = 1 - arr[0]
    sum = 1
    for i in range(1, len(arr)):
        if sum + arr[i] < 1:
            x += 1 - sum - arr[i]
            sum = 1
        else:
            sum += arr[i]
    return x

print(solution([3,2]))

a = [0,1]


for i in range(5,8):
    print('here')