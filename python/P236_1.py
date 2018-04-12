# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        pathP = self.dfs(root, p)
        pathQ = self.dfs(root, q)
        lenP = len(pathP)
        lenQ = len(pathQ)
        answer = None
        for i in range(min(lenP, lenQ)):
            if pathP[i] == pathQ[i]:
                answer = pathP[i]
        return answer
        
        
        
    def dfs(self, root, p):
        stack = []
        visit = None
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                peek = stack[-1]
                if peek.right and visit != peek.right:
                    root = peek.right
                else:
                    if peek == p:
                        return stack
                    visit = stack.pop()
                    root = None
        return stack