'''
写一个多叉树的level traversal，自己定义和构造节点，然后写算法吧~用了BFS。然后他说如果用DFS呢，不许用递归，讲了一下思路就OK。
'''
# I am still writing binary tree, it is easy to expand to n-ary tree and most difficult is to use DFS without recursion and how to deal with list of list in Python when set up the list
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        if not root: return []
        stack = []
        answer = [[]]
        dictionary = {}
        height = -1
        while root or stack:
            if root:
                height += 1
                dictionary[root] = height
                if len(answer) < height+1:
                    answer.insert(height, [])
                answer[height].append(root.val)
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                height = dictionary.get(root)
                root = root.right
        return answer
