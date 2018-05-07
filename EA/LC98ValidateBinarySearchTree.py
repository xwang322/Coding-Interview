# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        return self.dfs(root, -float('inf'), float('inf'))

    def dfs(self, root, minval, maxval):
        if not root:
            return True
        if minval < root.val < maxval:
            return self.dfs(root.left, minval, root.val) and self.dfs(root.right, root.val, maxval)
        else:
            return False
