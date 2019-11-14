import math
def climbStairs(n):
        if n>2:
            a1=1
            a2=2
            for i in range(1,n-1):
                ans=a1+a2
                a1=a2
                a2=ans
            return ans
        else:
            return n

print(climbStairs(4))

# a = {'b': 2}
# c = a
# print(a is c)
# d = a.copy()
# print(a is d)
print(math.log2(3.5*10**12))
print([]+[1])