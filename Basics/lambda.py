power = lambda x: print(x**2)

power(25)

fullName = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()

print(fullName(' kobe', 'BRYAN'))

a= 'asc'

if a.startswith('a'):
    print('yay!')

# return [movie[0] for movie in movies if movie[1] < 2000 ]
# return [title for (title, year) in movies if year < 2000]