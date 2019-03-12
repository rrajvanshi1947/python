def sleepin(weekday, vacation):
    if not weekday  or vacation:
        print(True)
    else:
        print(False)
sleepin(True, False)
sleepin(False, False)
sleepin(True, True)

def string(word, num):
    print(word*num)

string('Hi', 3)

def doubleString(word):
    newword = ''
    for i in word:
        newword += 2*i
    print(newword)

doubleString('asa')