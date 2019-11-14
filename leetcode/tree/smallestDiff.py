class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def minDiffInBST(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    def diff(node, smallest, largest):
        if not node:
            return float('inf')
        print(node.val, smallest, largest)
        diff_left = diff(node.left, smallest, node.val)
        diff_right = diff(node.right, node.val, largest)
        print(smallest -  node.val, largest - node.val)
        diff_mins = min(abs(smallest -  node.val), abs(largest - node.val))
        
        return min(diff_left, diff_right, diff_mins)
    
    return diff(root, float('-inf'), float('inf'))

a = TreeNode(4)
a.left = TreeNode(2)
a.right = TreeNode(6)
a.right.left = TreeNode(5)
a.right.right = TreeNode(8)

print(minDiffInBST(a))
