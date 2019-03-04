class Parent():

    def lastName(self):
        print('Rajvanshi')

class Child():

    def __init__(self):
        self.name = 'Roopam'

class Info(Parent, Child):
    pass

# n = Parent()    
r = Child()
print(r.name)
i = Info()
print(i.name)
print(i.lastName())