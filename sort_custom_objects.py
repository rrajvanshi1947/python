from operator import attrgetter

class User:
    def __init__(self, x, y):
        self.name = x
        self.userID = y

    def __repr__(self):
        return self.name +':'+ str(self.userID)

users = [User('Roopam', 1),
        User('Shubham', 2),
        User('Anshul', 3),
        User('Supreeti', 4),
        ]

for user in sorted(users, key = attrgetter('name')):
    print user

for user in sorted(users, key = attrgetter('userID')):
    print user