# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """
    def pathSum(self, root, sum):
        answer = []
        if not root:
            return answer
        curr_list = [root.val]
        self.dfs(root, root.val, curr_list, sum, answer)
        return answer
    
    
    def dfs(self, root, curr, curr_list, target, answer):
        if not root.left and not root.right:
            if curr == target:
                answer.append(curr_list)
        if root.left:
            self.dfs(root.left, curr+root.left.val, curr_list+[root.left.val], target, answer)
        if root.right:
            self.dfs(root.right, curr+root.right.val, curr_list+[root.right.val], target, answer)
    """
    def pathSum(self, root, s):
        if not root:
            return []
        answer = []
        stack= [(root, [root.val])]
        while stack:
            node, temp_sum = stack.pop()
            if not node.left and not node.right and sum(temp_sum) == s:
                answer.append(temp_sum)
            if node.left:
                stack.append((node.left, [node.left.val]+temp_sum))
            if node.right:
                stack.append((node.right, [node.right.val]+temp_sum))
        for each in answer:
            each.reverse()
        return answer