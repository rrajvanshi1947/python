class Stack():
    def __init__(self):
        self.array = []         #self.array = [None]*10 to define a size of array

    def push(self, value):
        self.array.append(value)

    def peek(self):
        if self.array:
            return self.array[-1]

    def pop(self):
        if self.array:
            return self.array.pop()

    def isEmpty(self):
        if not self.array:
            return True
        return False

    def printStack(self):
        return self.array

example = Stack()
example.pop()
print(example.peek())
print(example.isEmpty())
example.push(234)
example.push(235)
example.push(236)
example.push(237)
example.push(236)

print(example.printStack())
print(example.pop())
print(example.printStack())
print(example.peek())
print(example.isEmpty())

# a = [1,2,3]
# a[len(a):] = [4]
# print(a)