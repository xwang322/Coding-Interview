# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object): 
    # how to construct a tree structure from dict
    """
    def isBalanced(self, root):
        if not root:
            return True
        if abs(self.height(root.left)-self.height(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        return False
    
    def height(self, root):
        if not root:
            return 0
        return max(self.height(root.left), self.height(root.right))+1
    """
    def isBalanced(self, root):
        return self.height(root) != -1
          
    def height(self, node):
        if not node:
            return 0
        left_height = self.height(node.left)
        if left_height == -1:
            return -1
        right_height = self.height(node.right)
        if right_height == -1:
            return -1
        if abs(left_height-right_height) > 1:
            return -1
        return max(left_height, right_height) +1