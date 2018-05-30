# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        if not root:
            return -1
        first = root.val
        second = float('inf')
        queue = [root]
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.pop(0)
                if first < node.val < second:
                    second = node.val
                if node.left and node.right:
                    queue.append(node.left)
                    queue.append(node.right)
        return -1 if second == float('inf') else second
