A = [1,2,1,1,2,0,1,1,0]

def reach(a):
    if not a:
        print('Input an array')
    else:
        maxReach = 0
        for i in range(len(a)):
            if i > maxReach:
                return False
            if maxReach >= len(a) - 1:
                return True
            maxReach = max(maxReach, a[i]+i)

print(reach(A))