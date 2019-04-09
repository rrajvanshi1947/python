income = [50,100,150]

def incMoney(value):
    return value*2

new_income = list(map(incMoney, income))
print (new_income)