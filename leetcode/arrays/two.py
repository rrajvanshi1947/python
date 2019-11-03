import random

def f():
    for i in range(10):
        a = random.randrange(1, 11)
        b = 10 - a
        print(a,'+',b,'=')

# f()

obj = {
     'name': 'Peter',
     'age': 56,
     'kids': [
         {
             'name': 'Jill',
             'age': 23,
             'kids': [{
                 'name': 'Jeter',
                 'age': 1
             }, {
                 'name': 'Bill',
                 'age': 2
             }]
         }
     ]
 } 

def f(ob):
    if not ob:
        return 0

    # total =

    def helper(ob):
        return ob['age'] + helper(ob.kids) 
