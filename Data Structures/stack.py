class Stack:
    def __init__(self):
        self.itemlist = []

    def push(self, value):
        self.itemlist.append(value)

    def pop(self):
        return self.itemlist.pop()

    def isEmpty(self):
        return self.itemlist == []

    def peek(self):
        if not self.isEmpty():
            return self.itemlist[-1]    

    def getStack(self):
        return self.itemlist

new = Stack()
new.push(3)
new.push(4)
new.push(5)
print(new.getStack())
print(new.peek())
print(new.pop())
print(new.getStack())
print(new.pop())
print(new.pop())
print(new.isEmpty())    
