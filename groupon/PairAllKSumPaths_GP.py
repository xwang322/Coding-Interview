/*
* Given a binary tree, find the path which nodes sum to a given value. The path can start from and end with any nodes
* 好像是一道CC150原题
**/
# temporary solution, use bottom up might be better
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def PairAllKSumPaths(root, k):
    if not root:
        return []
    answer = []
    nodelist = bfs(root)
    while nodelist:
        dfs(answer, nodelist.pop(0), k, [])
    return answer

def bfs(root):
    if not root:
        return
    answer = []
    queue = [root]
    while queue:
        element = queue.pop(0)
        answer.append(element)
        if element.left:
            queue.append(element.left)
        if element.right:
            queue.append(element.right)
    return answer


def dfs(answer, node, target, path):
    if not node:
        return
    if node and node.val + sum(path) == target:
        answer.append(path+[node.val])
    dfs(answer, node.left, target, path+[node.val])
    dfs(answer, node.right, target, path+[node.val])

root = TreeNode(1)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(1)
root.left.right.left = TreeNode(1)
root.right = TreeNode(-1)
root.right.left = TreeNode(4)
root.right.left.left = TreeNode(1)
root.right.left.right = TreeNode(2)
root.right.right = TreeNode(5)
root.right.right.right = TreeNode(2)
answer = PairAllKSumPaths(root, 5)
print answer
