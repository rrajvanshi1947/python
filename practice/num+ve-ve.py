print('Enter the two numbers seperated by space.')
numList = list(map(int, input().split()))

total = 0
for x in numList:
    if x > 0:
        total += 1

if total == 1:
    print('Yes')
else:
    print('No')