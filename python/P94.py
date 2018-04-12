# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    '''
    def inorderTraversal(self, root):
        answer = []
        self.helper(root, answer)
        return answer
    
    def helper(self, node, answer):
        if node:
            self.helper(node.left, answer)
            answer.append(node.val)
            self.helper(node.right, answer)
    '''
    def inorderTraversal(self, root):
        answer = []
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                answer.append(node.val)
                root = node.right
        return answer