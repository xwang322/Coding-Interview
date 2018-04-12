# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        if not root:
            return
        right = root.right
        if root.left:
            self.flatten(root.left)
            tail = root.left
            while tail.right:
                tail = tail.right
            root.left, root.right, tail.right = None, root.left, right
        self.flatten(root.right)
        