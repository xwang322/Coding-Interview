# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        if not root:
            return []
        answer = []
        stack = []
        while root or stack:
            if root:
                answer.append(str(root.val))
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                root = root.right
        return ','.join(answer)

    def deserialize(self, data):
        if not data:
            return None
        data = map(int, data.split(','))
        stack = []
        root = TreeNode(data[0])
        node = root
        for n in data[1:]:
            if n < node.val:
                node.left = TreeNode(n)
                stack.append(node)
                node = node.left
            else:
                while stack and stack[-1].val < n:
                    node = stack.pop()
                node.right = TreeNode(n)
                node = node.right
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
