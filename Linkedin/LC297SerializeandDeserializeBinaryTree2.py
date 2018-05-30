# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        if not root:
            return '#$'
        stack = [root]
        answer = ''
        while stack:
            node = stack.pop()
            if node:
                answer += '#' + str(node.val)
                stack.append(node.right)
                stack.append(node.left)
            else:
                answer += '#$'
        return answer


    def deserialize(self, data):
        data = data.split('#')[1:]
        if data[0] == '$':
            return None
        root = TreeNode(int(data[0]))
        data = data[::-1]
        data.pop()
        stack = [root]
        node = root
        while data:
            value = data.pop()
            while data and value != '$':
                node.left = TreeNode(int(value))
                node = node.left
                stack.append(node)
                value = data.pop()
            while data and value == '$':
                node = stack.pop()
                value = data.pop()
            if data:
                node.right = TreeNode(int(value))
                node = node.right
                stack.append(node)
        return root



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
