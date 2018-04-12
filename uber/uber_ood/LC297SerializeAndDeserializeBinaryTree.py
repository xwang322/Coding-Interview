# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        if not root:
            return ',null'
        answer = ''
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if not node:
                answer += ',null'
            else:
                answer += ','+str(node.val)
                queue.append(node.left)
                queue.append(node.right)
        return answer


    def deserialize(self, data):
        data = data.split(',')
        data.pop(0) # at the beginning there is a ','
        value = data.pop(0)
        if value == 'null':
            root = None
        else:
            root = TreeNode(int(value))
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if node:
                left, right = data.pop(0), data.pop(0)
                if left != 'null':
                    node.left = TreeNode(int(left))
                else:
                    node.left = None
                if right != 'null':
                    node.right = TreeNode(int(right))
                else:
                    node.right = None
                queue.append(node.left)
                queue.append(node.right)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
