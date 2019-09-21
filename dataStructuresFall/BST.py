class Node():
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class BST():
    def __init__(self, value):
        self.root = Node(value)
        
    def insert(self, value):
        tempNode = self.root
        while tempNode:
            if value < tempNode.data:
                if not tempNode.left:
                    tempNode.left = Node(value)
                    return
                else:
                    tempNode = tempNode.left
            elif value > tempNode.data:
                if not tempNode.right:
                    tempNode.right = Node(value)
                    return
                else:
                    tempNode = tempNode.right
            else:
                print('Value already present!')
                return

    def find(self, value):
        tempNode = self.root
        while tempNode:
            if value == tempNode.data:
                print('Found')
                return
            elif value < tempNode.data:
                if tempNode.left:
                    tempNode = tempNode.left
                else:
                    print('Not Found')
                    return
            else:
                if tempNode.right:
                    tempNode = tempNode.right
                else:
                    print('Not Found')
                    return

    def test(self, node):
        string = ''
        self.testProperty(node, string)

    def testProperty(self, node):





tree = BST(10)
tree.root.left = Node(2)
tree.root.right = Node(12)
tree.root.left.left = Node(0)
tree.root.left.left.left = Node(-1)
tree.root.left.right = Node(4)
tree.root.right.left = Node(6)
tree.root.right.right = Node(14)

# tree.insert(14)
# print(tree.root.right.left.right.data)
tree.find(2)

        