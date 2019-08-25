prices = {
    'milk': 45,
    'dal': 180,
    'petrol': 75,
    'flour': 220
}

print(min(zip(prices.values(), prices.keys())))
print(max(zip(prices.keys(), prices.values())))
print(sorted(zip(prices.keys(), prices.values())))