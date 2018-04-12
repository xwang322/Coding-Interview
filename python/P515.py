# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # bfs
    def largestValues(self, root):
        if not root:
            return []
        curr_list = [root]
        answer = []
        while curr_list:
            maxnumber = None
            next_level = []
            for each in curr_list:
                maxnumber = max(each.val, maxnumber)
                if each.left:
                    next_level.append(each.left)
                if each.right:
                    next_level.append(each.right)
            answer.append(maxnumber)
            curr_list = next_level
        return answer
        