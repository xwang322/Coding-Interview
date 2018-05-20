'''
BST给定lower bound和upper bound，找到BST里面在这个范围内的所有的node val
'''
import bisect
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def findRangeBST(root, lowerlimit, upperlimit):
    if not root:
        return []
    inorder = []
    stack = []
    while root or stack:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            inorder.append(root.val)
            root = root.right
    index1 = bisect.bisect_left(inorder, lowerlimit)
    index2 = bisect.bisect_right(inorder, upperlimit)
    return inorder[index1 : index2]

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
node7.right = node8
answer = findRangeBST(node6, 3, 8)
print answer
