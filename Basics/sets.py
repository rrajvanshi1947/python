firstSet = {'Lily', 'Rose', 'Eucalyptus', 'Jasmine', 'Rosemarry'}

print(firstSet)

if 'Sunflower' in firstSet:
    print('Sunflower\'s already there')
else:
    firstSet.add('Sunflower')
    print(firstSet)