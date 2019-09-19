import math

#Nice try bro!
# def intToBin(number):
#     if type(number) == float or number <= 0:
#         return 'Error'
    
#     tempNumber = number
#     binaryNumber = ''
#     firstPower = math.floor(math.log2(tempNumber))
#     print(firstPower)
#     firstPowerString = str(math.floor(math.log2(tempNumber)))
#     while tempNumber > 0:
#         x = math.floor(math.log2(tempNumber))
#         binaryNumber += str(x)
#         tempNumber = tempNumber%2**x
    
#     print(binaryNumber)
#     arr = ['0']*(firstPower+1)    #int(binaryNumber[0])
#     print(arr)
#     for char in binaryNumber[len(firstPowerString) - 1:]:
#         arr[int(char)] = '1'

#     string = ''.join(arr)
#     return string[::-1]

def intToBin(number):
    if type(number) is not int or number < 0:
        return 'Error'

    binary = ''
    temp = number
    while temp > 0:
        binary += str(temp%2)
        temp = temp//2
    return binary[::-1]



print(intToBin(9991651.1*10))
print(''.join(reversed('asfs')))