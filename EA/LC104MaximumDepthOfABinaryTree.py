# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        answer = self.dfs(root, 0)
        return answer

    def dfs(self, root, answer):
        if not root:
            return answer
        answer += 1
        return max(self.dfs(root.left, answer), self.dfs(root.right, answer))
