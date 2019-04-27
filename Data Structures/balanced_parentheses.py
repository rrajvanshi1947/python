from stack2 import Stack

def isMatch(first, Second):
    if first is '{' and Second is '}':
        return True
    elif first is '[' and Second is ']':
        return True
    elif first is '(' and Second is ')':
        return True    
    else:
        return False

def parenCheck(characters):
    s = Stack()
    balanced = True
    index = 0 

    while index < len(characters) and balanced:
        if characters in '{[()}]':
            if characters[index] in '{[(':
                s.push(characters[index])
            else:
                if s.isEmpty():
                    balanced = False
                else:
                    top = s.pop()
                    if not isMatch(top, characters[index]):
                        balanced = False 
        index += 1

    if s.isEmpty() and balanced:
        return True
    else:
        return False

#Just to check for '{[()]}' 
# def parenCheck(input):
#     flist = []
#     for char in input:
#         if char in '{[()]}':
#             flist.append(char)
#     if len(flist)%2 != 0:
#         print('Unbalanced')
#         return
#     j = len(flist) - 1
#     for i in range(len(flist)//2):
#         if flist[i] is '{' and flist[j] is '}' or flist[i] is '[' and flist[j] is ']' or flist[i] is '(' and flist[j] is ')':
#             j -= 1
#             continue
#         else:
#             print('Unbalanced parentheses')
#             return
#     print('Balanced')
#     return



parenCheck('({[})')