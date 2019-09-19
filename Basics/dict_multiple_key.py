names = [{'fname': 'Roopam', 'lname': 'Rajvanshi'},
{'fname': 'Roopam', 'lname': 'Raghuvanshi'},
 {'fname': 'Supreeti', 'lname': 'Chohan'}]

for name in sorted(names, key = lambda item: item['fname']+item['lname']):
    print(name)
