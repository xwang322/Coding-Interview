# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        answer = 0
        if not root:
            return answer
        else:
            return self.dfs(root.left, root.right, answer+1)
        
        
    def dfs(self, p, q, level):
        if not p and not q:
            return level
        if not p and q:
            return self.dfs(q.left, q.right, level+1)
        if not q and p:
            return self.dfs(p.left, p.right, level+1)
        if p and q:
            return max(self.dfs(p.left, p.right, level+1), self.dfs(q.left, q.right, level+1))