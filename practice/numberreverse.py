number = input('Enter the number.\n')

# numStr = list(str(number))
# numStr.reverse()

# for i in range(len(numStr)):
#     print(numStr[i], end = "")

# print('\n')

number = str(number)
newnumber = ''

for i in range(len(number) -1, -1, -1):
    newnumber += number[i]

print(newnumber)

