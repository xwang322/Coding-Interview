# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        return self.dfs(root, 0)

    def dfs(self, root, tempsum):
        if not root:
            return 0
        tempsum = tempsum*10 + root.val
        if not root.left and not root.right:
            return tempsum
        return self.dfs(root.left, tempsum)+self.dfs(root.right, tempsum)