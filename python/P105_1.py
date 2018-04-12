# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        length = len(preorder)
        if length == 0:
            return None
        if length == 1:
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:index+1], inorder[0:index])
        root.right = self.buildTree(preorder[index+1:length], inorder[index+1:length])
        return root
        