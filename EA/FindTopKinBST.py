'''
第二题：就问问，没写代码。在binary search tree里面找topk。我感觉我答得不好，好像复杂度就是O(n)吧。按照inorder-traverse.
'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def findTopKinBST(root, k):
    if not root:
        return []
    answer = []
    stack = []
    i = 0
    while root or stack:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            answer.append(root.val)
            root = root.right
    return answer[:k] if len(answer) >= k else answer

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)
node9 = TreeNode(9)
node10 = TreeNode(10)
node6.left = node3
node6.right = node9
node3.left = node2
node3.right = node5
node2.left = node1
node5.left = node4
node9.left = node7
node9.right = node10
answer = findTopKinBST(node6, 12)
print answer
