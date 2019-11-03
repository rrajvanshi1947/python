class Node():
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self, rootValue):
        self.root = Node(rootValue)

def isSymmetric(root):
        if not root:
            return True
        
        arr1 = arr2 = []
        def inorder(node):
            if node:
                inorder(node.left)
                arr1.append(node.val)
                inorder(node.right)
                
        inorder(root.left)
        print('1', arr1)
        
        # arr2 = []
        print(arr2)
        def postorder(node):
            if node:
                postorder(node.right)
                arr2.append(node.val)
                # print(arr2)
                postorder(node.left)
                
        postorder(root.right)
        print('2', arr2)

        if arr1 == arr2:
            print('here')
            return True
        return False

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(2)
tree.root.left.right = Node(3)
tree.root.right.right = Node(3)
# tree.root.right.right = Node(3)
# tree.root.right.left = Node(6)
# tree.root.right.right = Node(7)

print(isSymmetric(tree.root))

a = b = []
a.append(1)
print(b, a)
print('a'*3)