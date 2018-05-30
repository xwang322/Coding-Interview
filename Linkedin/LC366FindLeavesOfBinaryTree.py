# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        if not root:
            return []
        dictionary = collections.defaultdict(list)
        self.dfs(root, dictionary)
        answer = []
        for i in range(max(dictionary.values())):
            answer.insert(i, [])
        for key in dictionary:
            answer[dictionary[key]-1].append(key.val)
        return answer

    def dfs(self, root, dictionary):
        if not root:
            return 0
        left = self.dfs(root.left, dictionary)
        right = self.dfs(root.right, dictionary)
        height = max(left, right) + 1
        dictionary[root] = height
        return height
