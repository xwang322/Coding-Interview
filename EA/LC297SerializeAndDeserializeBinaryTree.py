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
            if not node:
                answer += ',null'
            else:
                answer += ',' + str(node.val)
                queue.append(node.left)
                queue.append(node.right)
        print answer
        return answer



    def deserialize(self, data):
        data = data.split(',')
        data.pop(0)
        if data[0] == 'null':
            return None
        else:
            root = TreeNode(int(data.pop(0)))
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                temp1 = data.pop(0)
                temp2 = data.pop(0)
                if temp1 == 'null':
                    node.left = None
                else:
                    node.left = TreeNode(int(temp1))
                    queue.append(node.left)
                if temp2 == 'null':
                    node.right = None
                else:
                    node.right = TreeNode(int(temp2))
                    queue.append(node.right)
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
