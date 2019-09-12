#Reverse an integer

# def reverseNumber(x):
    # a = 0
    # if x >= 0:
    #     a = int(str(x)[::-1])
    # else:
    #     a = -1*int(str(x)[1:][::-1])

    # if a > 2**31 - 1 or a < -2**31:
    #     return 0
    # return a

# print(reverseNumber(459649461319843136484616418461698468497941651489798646198749165189778))
    

def reverseNumber(x):
    rev = 0
    if x == 0:
        return 0
    elif x > 0:
        while x > 0:
            rev *= 10
            rev += x%10
            x //= 10
        return rev
    else:
        x = -x
        while x > 0:
            rev *= 10
            rev += x%10
            x //= 10
        return -rev

print(reverseNumber(51560))