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

print(parenCheck('(((ksdfk)sd;fjaf))afl;jsaf21123@$%{()kashdkahfka[][][]}'))
