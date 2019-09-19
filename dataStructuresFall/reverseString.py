def reverse(string):
    reversedString = ''
    stack = []
    for char in string:
        stack.append(char)
    for _ in range(len(stack)):
        reversedString += stack.pop()
    return reversedString

print(reverse('Roopam Rajvanshi'.split()))