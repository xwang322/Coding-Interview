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
        if not node.left and not node.right:
            if node.val == target:
                path += [node.val]
                answer.append(path)
                return
        self.dfs(answer, node.left, target-node.val, path+[node.val])
        self.dfs(answer, node.right, target-node.val, path+[node.val])
