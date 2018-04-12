# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        if not root:
            return []
        counts = collections.Counter()
        
        def dfs(node):
            if node:
                counts[node.val] += 1
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        max_value = max(counts.itervalues())
        return [k for k,v in counts.iteritems() if v == max_value]