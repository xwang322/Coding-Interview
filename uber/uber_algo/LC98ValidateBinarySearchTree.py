# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        return self.isValidBSTrange(root, -float('inf'), float('inf'))

    def isValidBSTrange(self, node, low, high):
        if not node:
            return True
        if not low < node.val < high:
            return False
        else:
            flag1 = True
            flag2 = True
            if node.left:
                flag1 = self.isValidBSTrange(node.left, low, node.val)
            if node.right:
                flag2 = self.isValidBSTrange(node.right, node.val, high)
            return flag1 and flag2
