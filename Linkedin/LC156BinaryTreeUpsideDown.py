# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        if not root:
            return None
        return self.helper(root)

    def helper(self, node):
        if not node.left:
            return node
        root = self.helper(node.left)
        node.left.left = node.right
        node.left.right = node
        node.left = None
        node.right = None
        return root
            
