# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    '''
    def kthSmallest(self, root, k):
        if not root:
            return None
        if k <= 0:
            return None
        stack = []
        while root:
            stack.append(root)
            root = root.left
        x = 1
        while stack and x <= k:
            node = stack.pop()
            x += 1
            right = node.right
            while right:
                stack.append(right)
                right = right.left
        return node.val
    '''
    def kthSmallest(self, root, k):
        self.count = 0
        self.answer = None
        self.tranverse(root, k)
        return self.answer
    
    def tranverse(self, root, k):
        if not root:
            return
        self.tranverse(root.left, k)
        self.count += 1
        if (self.count == k):
            self.answer = root.val
            return
        self.tranverse(root.right, k)