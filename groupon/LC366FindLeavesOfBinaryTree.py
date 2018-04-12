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
        answer = []
        dictionary = collections.defaultdict(list)
        self.level(root, dictionary)
        for i in range(len(dictionary)):
            answer.append(dictionary[i+1])
        return answer

    def level(self, root, dictionary):
        if not root:
            return 0
        left = self.level(root.left, dictionary)
        right = self.level(root.right, dictionary)
        height = max(left, right)+1
        dictionary[height] += [root.val]
        return height
