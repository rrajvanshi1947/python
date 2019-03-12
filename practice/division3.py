print('Enter the two numbers seperated by space.')
x, y = map(int, input().split())

def avFunction(a, b):
    numList = []
    if b-a == 1 & a%3 == 1:
        print('There is no number in the range which is divisble by 3.')
    elif a%3 == 0:
        for x in range(a,b,3):
            numList.append(x)
        if b%3 == 0:
            numList.append(b)
        av = sum(numList)/len(numList)
        print(av)

    elif a%3 == 1:
        for x in range(a+2,b,3):
            numList.append(x)
        if b%3 == 0:
            numList.append(b)
        av = sum(numList)/len(numList)
        print(av)

    else:
        for x in range(a+1,b,3):
            numList.append(x)
        if b%3 == 0:
            numList.append(b)
        av = sum(numList)/len(numList)
        print(av)

avFunction(x, y)