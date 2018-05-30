# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not p or not q:
            return None
        dictionary = {}
        queue = []
        queue.append(root)
        dictionary[root] = None
        while p not in dictionary or q not in dictionary:
            while queue:
                node = queue.pop(0)
                if node.left:
                    dictionary[node.left] = node
                    queue.append(node.left)
                if node.right:
                    dictionary[node.right] = node
                    queue.append(node.right)
        visited = set()
        temp = p
        while temp:
            visited.add(temp)
            temp = dictionary[temp]
        temp = q
        while temp not in visited:
            temp = dictionary[temp]
        return temp
