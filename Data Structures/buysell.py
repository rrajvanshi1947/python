A = [1234,20000,300000,500000,1230000,123450,12000000000000]

def maxProfit(a):
    minPrice = a[0]
    maxProfit = 0
    for price in a[1:]:
        minPrice = min(minPrice, price)
        compareProfit = price - minPrice
        maxProfit = max(maxProfit, compareProfit)
    return maxProfit

print(maxProfit(A))