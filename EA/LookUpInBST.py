'''
问了BST lookup (int val)的实现
'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def lookUpinBST(root, target):
    if not root:
        return False
    if root.val == target:
        return True
    elif root.val > target:
        return lookUpinBST(root.left, target)
    else:
        return lookUpinBST(root.right, target)

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)
node9 = TreeNode(9)
node10 = TreeNode(10)
node6.left = node3
node6.right = node9
node3.left = node2
node3.right = node5
node2.left = node1
node5.left = node4
node9.left = node7
node9.right = node10
answer = lookUpinBST(node6, 8)
print answer
