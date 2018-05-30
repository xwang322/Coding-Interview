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
        queue = [root]
        answer = ''
        while queue:
            node = queue.pop(0)
            if node:
                answer += ',' + str(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                answer += ',null'
        return answer


    def deserialize(self, data):
        data = data.split(',')
        if len(data) == 2 and data[1] == 'null':
            return None
        data.pop(0)
        root = TreeNode(int(data.pop(0)))
        node = root
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                str1 = data.pop(0)
                str2 = data.pop(0)
                if str1 != 'null':
                    node.left = TreeNode(int(str1))
                    queue.append(node.left)
                else:
                    node.left = None
                if str2 != 'null':
                    node.right = TreeNode(int(str2))
                    queue.append(node.right)
                else:
                    node.right = None
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
