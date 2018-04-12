# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    ''' DFS method
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None
        pathP = self.dfs(root, p)
        pathQ = self.dfs(root, q)
        answer = None
        for i in range(min(len(pathP), len(pathQ))):
            if pathP[i] == pathQ[i]:
                answer = pathP[i]
        return answer
        
    def dfs(self, root, node):
        if not root:
            return path
        stack = []
        visit = None
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                peek = stack[-1]
                if peek.right and visit != peek.right:
                    root = peek.right
                else:
                    if peek == node:
                        return stack
                    visit = stack.pop()
                    root = None
        return stack
        '''
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None
        dictionary = {root: None}
        stack = [root]
        while p not in dictionary or q not in dictionary:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
                dictionary[node.left] = node
            if node.right:
                stack.append(node.right)
                dictionary[node.right] = node
        temp = set()
        while p:
            temp.add(p)
            p = dictionary[p]
        while q not in temp:
            q = dictionary[q]
        return q
        