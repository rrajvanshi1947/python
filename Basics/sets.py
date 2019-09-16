firstSet = {'Lily', 'Rose', 'Eucalyptus', 'Jasmine', 'Rosemarry'}

print(firstSet)

if 'Sunflower' in firstSet:
    print('Sunflower\'s already there')
else:
    firstSet.add('Sunflower')
    print(firstSet)

newSet = set([1,2,3,4,5])
print(type(newSet))
print(newSet)
newSet.add(6)
print(newSet)
newSet2 = {8,9}
newSet.update([7,8], newSet2)
print(newSet)
newSet.remove(8)    #Remove will throw error in case the value is not in set but discard won't
newSet.discard(7)
print(newSet)

s1 = {1,2,3}
s2 = {2,3,4}
s3 = {3,4,5}
s4 = s1.intersection(s2)
print(s4)
s5 = s1.intersection(s2, s3)
print(s5)
print(s1.difference(s2))
print(s2.difference(s1, s3))
print(s1.symmetric_difference(s2))

#Sets have O(1) complexity for some reason. Maybe they represent dictionaries