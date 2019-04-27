from queue import Queue
from stack2 import Stack

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)

    def preorderPrint(self, start, traversal):
        # Node>Left>Right
        if start:
            traversal += str(start.data) + '-'
            traversal = self.preorderPrint(start.left, traversal)
            traversal = self.preorderPrint(start.right, traversal)
        return traversal

    def inorderPrint(self, start, traversal):
        # Left>Node>Right
        if start:
            traversal = self.inorderPrint(start.left, traversal)
            traversal += str(start.data) + '-'
            traversal = self.inorderPrint(start.right, traversal)
        return traversal

    def postorderPrint(self, start, traversal):
        # Left>Right>Node
        if start:
            traversal = self.postorderPrint(start.left, traversal)
            traversal = self.postorderPrint(start.right, traversal)
            traversal += str(start.data) + "-"
        return traversal

# '''                1
#                   / \
#                  2   3    4251637         4526731
#                 / \ / \
#                4   56  7        '''

    def levelorderPrint(self, start):
        if not start:
            return
        traversal = str(start.data) + '-'
        q = Queue()
        q.put(start)
        while q.queue:
            a = q.extract()
            if a.left:
                traversal += str(a.left.data) + '-'
                q.put(a.left)
            if a.right:
                traversal += str(a.right.data) + '-'
                q.put(a.right)
        return traversal

    def reverseorderPrint(self, start):
        if not start:
            return
        q = Queue()
        s = Stack()
        q.put(start)
        traversal = ''
        while q.queue:
            a = q.extract()
            s.push(a)
            if a.right:
                q.put(a.right)
            if a.left:
                q.put(a.left) 
        while not s.isEmpty():
            traversal += str(s.peek().data) + '-'
            s.pop()
        return traversal



fTree = BinaryTree(1)
fTree.root.left = Node(2)
fTree.root.right = Node(3)
fTree.root.left.left = Node(4)
fTree.root.left.right = Node(5)
fTree.root.right.left = Node(6)
fTree.root.right.right = Node(7)
print(fTree.preorderPrint(fTree.root, ''))
print(fTree.inorderPrint(fTree.root, ''))
print(fTree.postorderPrint(fTree.root, ''))
print(fTree.levelorderPrint(fTree.root))
print(fTree.reverseorderPrint(fTree.root))
