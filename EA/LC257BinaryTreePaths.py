# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        if not root:
            return []
        answer = []
        self.dfs(root, answer, '')
        return answer

    def dfs(self, root, answer, path):
        path += str(root.val)
        if not root.left and not root.right:
            answer.append(path)
        if root.left:
            self.dfs(root.left, answer, path + '->')
        if root.right:
            self.dfs(root.right, answer, path + '->')
        
