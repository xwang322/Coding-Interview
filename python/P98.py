# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        return self.dfs(root, float('-inf'), float('inf'))
    
    def dfs(self, root, minnum, maxnum):
        if not root:
            return True
        if root.val >= maxnum or root.val <= minnum:
            return False
        return self.dfs(root.left, minnum, root.val) and self.dfs(root.right, root.val, maxnum)