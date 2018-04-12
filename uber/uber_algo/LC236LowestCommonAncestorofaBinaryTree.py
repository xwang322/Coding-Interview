# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None
        queue = [root]
        dictionary = {root: None}
        while p not in dictionary or q not in dictionary:
            element = queue.pop(0)
            if element.left:
                dictionary[element.left] = element
                queue.append(element.left)
            if element.right:
                dictionary[element.right] = element
                queue.append(element.right)
        temp = set()
        while p:
            temp.add(p)
            p = dictionary[p]
        while q not in temp:
            q = dictionary[q]
        return q
