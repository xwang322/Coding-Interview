# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        return self.DFS(root)[1]
    
    def DFS(self, root):
        if not root:
            return (0, 0)
        l = self.DFS(root.left)
        r = self.DFS(root.right)
        return (l[1]+r[1], max(l[1]+r[1], l[0]+r[0]+root.val))
        
        