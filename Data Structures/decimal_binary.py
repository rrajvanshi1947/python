from stack2 import Stack

print(int('100', 2))

def conversion(num):
    if num == 0:
        return 0
    elif num < 0:
        print('Enter a positive number')  
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


num = input('Enter the number\n')
num = int(num)
print(conversion(num))



