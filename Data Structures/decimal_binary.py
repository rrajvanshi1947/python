# from stack2 import Stack

print(int('100', 16))

def conversion(num):
    if num == 0:
        return 0
    elif num < 0:
        print('Number entered has to be positive! You should know this by now. :P')  
    s= Stack()
    modulus = 0
    while num > 0:
        modulus = num%2
        s.push(modulus)
        num //= 2
    
    string = ''
    while not s.isEmpty():
        string += str(s.pop())
    return string

#Doing it without the stack DS
# def conversion(value):
#     conv_value = []
#     while value > 0:
#         conv_value.append(str(value%2))
#         value = value//2
#     print(list(reversed(conv_value)))


num = input('Enter the number\n')
num = int(num)
conversion(num)



