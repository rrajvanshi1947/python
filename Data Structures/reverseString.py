def reverseString():
    string = input('Enter the string\n')
    # reversedString = ''
    # for i in range(len(string) - 1, -1, -1):
    #     reversedString += string[i]
    # print(reversedString)
    print(list((reversed(string))))


while True:
    reverseString()

# a = 'Roopam'
# print(a[::-1])

# from stack2 import Stack

# def reverseString():
#     value = input('Enter the string\n')
#     reversedStringStack = Stack()
#     for char in value:
#         reversedStringStack.push(char)
#     reversedString = ''
#     while not reversedStringStack.isEmpty():
#         reversedString += reversedStringStack.pop()
#     print(reversedString)

# while True:
#     reverseString()

