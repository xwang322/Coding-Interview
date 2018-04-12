# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        if not root:
            return []
        answer = []
        self.dfs(answer, root, sum, [])
        return answer

    def dfs(self, answer, node, target, path):
        if not node:
            return
        if node and not node.left and not node.right:
            path.append(node.val)
            if sum(path) == target:
                answer.append(path)
            return
        self.dfs(answer, node.left, target, path+[node.val])
        self.dfs(answer, node.right, target, path+[node.val])
