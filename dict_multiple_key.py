names = [{'fname': 'Roopam', 'lname': 'Raghuvanshi'},
 {'fname': 'Supreeti', 'lname': 'Chohan'}, 
 {'fname': 'Roopam', 'lname': 'Rajvanshi'}]

for name in sorted(names, key = lambda item: item['fname']):
    print name
