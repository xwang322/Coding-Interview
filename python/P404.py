# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0
        answer = []
        self.dfs(root, answer)
        return sum(answer)
    
    def dfs(self, root,answer):
        if root.left and not root.left.left and not root.left.right:
            answer.append(root.left.val)
        if not root.left and not root.right:
            return
        if root.left:
            self.dfs(root.left, answer)
        if root.right:
            self.dfs(root.right, answer)