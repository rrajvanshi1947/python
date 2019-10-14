def myPow(x, n):
    # value = 1
    # if n > 0:
    #     while n > 0:
    #         value *= x
    #         n -= 1
    # else:
    #     while n < 0:
    #         value *= 1/x
    #         n += 1
        
    # return value

    # if n == 0:
    #     return 1
    # if n > 0:
    #     return x*myPow(x, n-1)
    # elif n < 0:
    #     return 1/(x*myPow(x, n-1))

    if n == 0:
        return 1

    if n < 0:
        return 1/myPow(x, -n)

    temp = myPow(x, n//2)
    if n%2 == 0:
        return temp*temp
    else:
        return x*temp*temp

print(myPow(2.00,-40))
print(2**-40)