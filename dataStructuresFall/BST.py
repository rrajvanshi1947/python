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

    def maximum(self):
        temp = self.root
        while temp.right:
            temp = temp.right

        print(temp.data)

    def minimum(self):
        temp = self.root
        while temp.left:
            temp = temp.left

        print(temp.data)

    def BSTutil(self, node, mini, maxi):
        if not node:
            return True
        
        if node.data < mini or node.data > maxi:
            return False

        return self.BSTutil(node.left, mini, node.data-1) and self.BSTutil(node.right, mini, node.data+1)

    def BSTCheck(self, node):
        return self.BSTutil(node, -1000000000, 100000000)

tree = BST(4)
tree.root.left = Node(2)
tree.root.right = Node(5)
tree.root.left.left = Node(1)
tree.root.left.right = Node(3)


# tree = BST(10)
# tree.root.left = Node(2)
# tree.root.right = Node(12)
# tree.root.left.left = Node(0)
# tree.root.left.left.left = Node(-1)
# tree.root.left.right = Node(4)
# tree.root.right.left = Node(11)
# tree.root.right.right = Node(14)

# tree.insert(14)
# print(tree.root.right.left.right.data)
tree.find(2)
tree.maximum()
tree.minimum()
print(tree.BSTCheck(tree.root))


# def test(value):
#     # string = ''
#     return testProperty(value)

# def testProperty(value):
#     return value**0

# print(test(0))

        
        