# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # dfs
    def minDepth(self, root):
        return self.height(root)

    def height(self, root):
        if not root:
            return 0
        if root.left and not root.right:
            return self.height(root.left)+1
        if root.right and not root.left:
            return self.height(root.right)+1
        else:
            return min(self.height(root.left), self.height(root.right)) + 1