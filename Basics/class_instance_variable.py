class Plane:
    type = 'Air borne'

    def __init__(self, model):
        self.model = model

    def printModelType(self):
        print(self.model)
        print(self.type)

f = Plane('F-16')
f.printModelType()
m = Plane('MIG-21')
m.printModelType()