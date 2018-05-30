# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        if not root:
            return []
        answer = []
        queue = [root]
        while queue:
            length = len(queue)
            temp = float('-inf')
            for i in range(length):
                node = queue.pop(0)
                if node.val > temp:
                    temp = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            answer.append(temp)
        return answer
