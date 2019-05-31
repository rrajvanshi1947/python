class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, start):
        if value < start.data:
            if not start.left:
                start.left = Node(value)
            else:
                self._insert(value, start.left)
        elif value > start.data:
            if not start.right:
                start.right = Node(value)
            else:
                self._insert(value, start.right)
        else:
            print('No duplicates allowed')

    def find(self, value):
        if not self.root:
            return
        else:
            return self._find(value, self.root)

    def _find(self, value, start):
        if value == start.data:
            return True 
        elif value < start.data and start.left:
            return self._find(value, start.left)
        elif value > start.data and start.right:
            return self._find(value, start.right)
        else:
            return False

# '''                1
#                   / \
#                 -2   4    4251637         4526731
#                 / \ / \
#               -5   03  7        '''

fTree = BST()
fTree.insert(1)
fTree.insert(-2)
fTree.insert(4)
fTree.insert(-5)
fTree.insert(0)
fTree.insert(3)
fTree.insert(7)
print(fTree.find(4))