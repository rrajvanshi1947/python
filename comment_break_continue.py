''' This is an example
of multi line comment
print('Hello')
'''

#This is an example of single line comment

print 'My value is ', 9

names = ['Roopam', 'Raj', 'Shubham', 'Anshul']
for n in names[0:4]:
    if n is 'Shubham':
        print('You found Shubham')
        break
    else:
        print(n)

for n in names:
    if n is 'Roopam':
        continue
    print(n)

for n in range(21):
    if n%4 is 0:
        print(n)