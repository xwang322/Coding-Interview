'''
isBalancedTree 这个题和leetcode的不大一样，要求是看整个tree最短的和整个tree最长的path 差是否小于2.我的复杂度高了点，没被满意。
'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class IsBalancedTree(object):
    def __init__(self):
        self.node1 = TreeNode(7)
        self.node2 = TreeNode(4)
        self.node3 = TreeNode(9)
        self.node1.left = self.node2
        self.node1.right = self.node3
        self.node4 = TreeNode(3)
        self.node5 = TreeNode(5)
        self.node2.left = self.node4
        self.node2.right = self.node5
        self.node6 = TreeNode(8)
        self.node7 = TreeNode(10)
        self.node3.left = self.node6
        self.node3.right = self.node7
        self.node8 = TreeNode(2)
        self.node9 = TreeNode(6)
        self.node10 = TreeNode(1)
        self.node4.left = self.node8
        self.node5.right = self.node9
        self.node8.left = self.node10

    def maxDepth(self, root):
        if not root:
            return 0
        answer = self.dfs(root, 0)
        return answer

    def dfs(self, root, answer):
        if not root:
            return answer
        answer += 1
        return max(self.dfs(root.left, answer), self.dfs(root.right, answer))

    def minDepth(self, root):
        if not root:
            return 0
        elif not root.left:
            return self.minDepth(root.right) + 1
        elif not root.right:
            return self.minDepth(root.left) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

    def isBalanced(self):
        root = self.node1
        return self.maxDepth(root) - self.minDepth(root) <= 2

obj = IsBalancedTree()
print obj.isBalanced()
