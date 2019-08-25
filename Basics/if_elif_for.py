name = "Roopam"

if name is "Roopam":
    print("Hey Roopam! How's the Python learning coming along?")
    print("What are your plans for tomorrow?")
elif name is "Shubham":
    print("What's up Shubham?")
else:
    print("Wrong guy")
    print(len(name))

names = ('Roopam', 'Anshul', 'Kunwar', 'Suri', 'Ravi')  #This is a tuple. A list can also be used here and we'll get the same result.
for n in names[:4]:
    print(n)
    print(len(n))
    
