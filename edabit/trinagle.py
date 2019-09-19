# def thirdEdge(side1, side2):
#     return side1 + side2 - 1

# print(thirdEdge(3,4))

print(round(44, 4))

string = 'skldnflf'
print(string.rindex('f', 4, 8)) #The last index is not included. One less than it is considered.

dic = {'cost': 123, 'sell': 124, 'units': 5}

def profit(dictionary):
    return (dictionary['sell'] - dictionary['cost'])*dictionary['units']

print(profit(dic))