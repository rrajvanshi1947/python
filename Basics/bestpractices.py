#Python best practices
'''
1 enumerate
2 zip function
3 Tuple unpacking
4 Dictionaries value found or not
5 Python for else only used with break statement
6 with open('text.txt') as fo: 
7 try, except, else, finally
FInally is executed even if an exception occurs and there in no except: parameter given before crashing.
8 Use izip so that zip doesn't create additional resource. This way you're just iterating over the list.
'''
universities = ['SJSU', 'UCLA', 'MIT', 'NYU', 'Penn', 'Stanford']

first, *rest, last = universities
print(rest)

for i, university in enumerate(universities):
    print(i, university)

print(universities.index('MIT'))

x= 1
y=2
x,y = y,x
print(x,y)

dic = {'R': 28, 'D': 28}
age = dic.get('D', 'unknown')
print(age)

students = {'Roopam': 'Employed', 'Ravi': 'Employed', 'Divya': 'Employed', 'Anshul': 'Employed', 'X': 'Unemployed', 'Y': 'Unemployed'}

for k in students:              #for loop for keys in dic is not in sequential order
    if students[k] == 'Unemployed':
        print(k, 'is unemployed.')
        break           #You've to use break
else:
    print('All are employed! :)')

    #Looping through a list in a reversed way

colors = ['blue', 'violet', 'magenta', 'red', 'yellow']

# for color in reversed(colors):
#         print(color)

for color in sorted(colors, reverse = True):
        print(color)