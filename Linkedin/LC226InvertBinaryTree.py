# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        if not root:
            return root
        if root.right and root.left:
            temp1 = root.left
            temp2 = root.right
            root.left = temp2
            root.right = temp1
        elif root.right and not root.left:
            temp1 = root.right
            root.left = temp1
            root.right = None
        elif root.left and not root.right:
            temp1 = root.left
            root.right = temp1
            root.left = None
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root