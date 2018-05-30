# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        return self.helper(root, 0)

    def helper(self, root, height):
        if not root:
            return height
        return max(self.helper(root.left, height+1), self.helper(root.right, height+1))
