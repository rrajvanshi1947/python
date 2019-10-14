class Node():
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self, rootValue):
        self.root = Node(rootValue)

    def preorder(self, node):
        if node:
            print(node.data, end="-")
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end="-")
            self.inorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end="-")

    def levelOrderTraversal(self):
        queue = []
        queue.append(self.root)
        while len(queue) > 0:
            print(queue[0].data, end= ' ')
            dequeuedNode = queue.pop(0)
            if dequeuedNode.left:
                queue.append(dequeuedNode.left)
            if dequeuedNode.right:
                queue.append(dequeuedNode.right)

    def reverseLevelOrder(self, node):
        if not node:
            return
        queue = []
        stack = []
        queue.append(node)
        while len(queue) > 0:
            tempNode = queue.pop(0)
            stack.append(tempNode)
            if tempNode.right:
                queue.append(tempNode.right)
            if tempNode.left:
                queue.append(tempNode.left)

        while len(stack) > 0:
            print(stack.pop().data, end = ' ') 

    def height(self, node):
        if not node:
            return -1
        leftHeight = self.height(node.left)
        rightHeight = self.height(node.right)
        
        return 1 + max(leftHeight, rightHeight)

    def size(self, node):
        if not node:
            return 0
        size = 0
        queue = []
        queue.append(node)
        while len(queue) > 0:
            tempNode = queue.pop(0)
            size += 1
            if tempNode.left:
                queue.append(tempNode.left)
            if tempNode.right:
                queue.append(tempNode.right)
            
        return size


        #     1
        #    / \
        #   2   3
        #  / \ / \
        #  4  56  7
        #   /
        #  8

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.left.left = Node(8)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
# tree.preorder(tree.root)
# tree.inorder(tree.root)
# tree.postorder(tree.root)
# print(tree)
# tree.levelOrderTraversal()
# tree.reverseLevelOrder(tree.root.left)
# print(tree.height(tree.root))
print(tree.size(tree.root.left))



   