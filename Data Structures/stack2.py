class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)
    
    def pop(self):
        # return self.stack.pop()
        if self.stack:          # If you cannot use the in-built pop() function
            a = self.stack[-1]
            self.stack = self.stack[:len(self.stack) - 1]
            return a

    def peek(self):
        if self.stack:
            return self.stack[-1]
    
    def delete(self):
        self.stack = []

    def getStack(self):
        return self.stack
    
    def isEmpty(self):
        return self.stack == []

# firstPythonStack = Stack()
# print(firstPythonStack.getStack())
# print(firstPythonStack.peek())
# print(firstPythonStack.pop())
# firstPythonStack.push(3)
# firstPythonStack.push(4)
# firstPythonStack.push(5)
# print(firstPythonStack.getStack())
# print(firstPythonStack.peek())
# print(firstPythonStack.pop())
# print(firstPythonStack.getStack())
# firstPythonStack.delete()
# print(firstPythonStack.peek())

