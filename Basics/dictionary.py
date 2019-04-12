firstDictionary = {'Audi': 'Q5', "BMW": '328i', 'Mercedes': 'S3', 'Tesla': 'Model X'}

print(firstDictionary)
print(firstDictionary['Mercedes'])

for k, v in firstDictionary.items():
    print(k+'\'s model is', v)
